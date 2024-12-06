.. _electrostatic_sphere:

Conducting sphere in a uniform electric field
=============================================

A sphere in a whole-space provides a simple geometry to examine a variety of
questions and can provide powerful physical insights into a variety of
problems. Here we examine the case of a conducting sphere in a uniform
electrostatic field. This scenario gives us a setting to examine aspects of
the DC resistivity experiment, including the behavior of electric potentials,
electric fields, current density and the build up of charges at interfaces.
This work follows the derivation in :cite:`ward1988` and is supported by apps developed in a `binder`_.

.. _binder: https://mybinder.org/v2/gh/geoscixyz/em_apps/master?filepath=%2Fnotebooks%2FDC_Sphere_Constant_E.ipynb

 .. image:: http://mybinder.org/badge.svg
    :target: https://mybinder.org/v2/gh/geoscixyz/em_apps/master?filepath=%2Fnotebooks%2FDC_Sphere_Constant_E.ipynb
    :align: center

Setup
-----

The problem setup is shown in the figure below, where we have

- a uniform electric field oriented in the :math:`x`-direction: :math:`\mathbf{E_0} = E_0 \mathbf{\hat{x}}`
- a whole-space background with conductivity :math:`\sigma_0`
- a sphere with radius :math:`R` and conductivity :math:`\sigma_1`
- the origin of coordinate system coincides with the center of the sphere


.. plot::

    from matplotlib import patches

    R = 50  # Define the radius of the sphere

    fig, ax = plt.subplots(1,1, figsize = (6,6))

    circle = patches.Circle([0,0],radius=R, alpha=0.4, color='blue', linewidth=1.5)
    ax.add_patch(circle)
    ax.arrow(0., 0., np.sqrt(2.)*R/2., np.sqrt(2.)*R/2., head_width=0., head_length=0.)

    for y in np.linspace(-2 * R, 2 * R, 10):
        ax.arrow(-2*R, y, 0.3*R, 0.0, head_width=5., head_length=2., color='k')

    ax.text(-1., -np.sqrt(R)/2.-10., '$\sigma_1$')
    ax.text(-0.05, -R-10, '$\sigma_0$')
    ax.text(0.5*np.cos(np.pi/6)*R, 0.5*np.sin(np.pi/6)*R, 'R')
    ax.text(-1.8*R, 1.3*R, '$\mathbf{E_0} = E_0 \mathbf{\hat{x}}$ V/m')

    ax.set_facecolor([0.4, 0.7, 0.4, 0.3])
    ax.set_xlim([-2 * R, 2 * R])
    ax.set_ylim([-2 * R, 2 * R])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.show()



Governing Equations
-------------------

The governing equation for DC resistivity problem can be obtained from
:ref:`Maxwell's equations <maxwell1_fundamentals_index>`. We start by
considering the zero-frequency case, in which case, Maxwell's equations are

.. math::
    \nabla \times \mathbf{e} = 0
    :label: Faraday_DC

.. math::
    \nabla \times \mathbf{h} = \mathbf{j}
    :label: Ampere_DC

Knowing that the curl of the gradient of any scalar potential is always zero,
according to :eq:`Faraday_DC`, we can define a scalar potential so that the
primary electric field is the gradient of a potential. For convenience, we
define it to be the negative gradient of the potential, :math:`V`

.. math::
    \mathbf{e} = -\nabla V
    :label: DC_Potential

To define the potential at a point :math:`p` from an electric field requires integration

.. math::
    V = -\int_{ref}^p \mathbf{e} \cdot \mathbf{dl}
    :label: V_from_e

The choice of reference point :math:`ref` is arbitrary, but it is often
convenient to consider the reference point to be infinitely far away, so
:math:`ref = \infty`. In this case, the electric potential at :math:`p` is
equivalent to the amount of work done to bring a positive charge from
infinity to the point :math:`p`.


Potentials
----------

Assuming an x-directed uniform electric field and zero potential at infinity,
the integration from :eq:`V_from_e` gives


.. math::
    V_p = - E_0 x = -E_0 r \cos\theta
    :label: Primary_Potential


.. plot::

    from matplotlib import patches
    from geoana.em.static import ElectrostaticSphere

    sig0 = 10.**-3.         # conductivity of the whole-space in S/m
    sig1 = 10.**-1.         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m

    sphere = ElectrostaticSphere(R, sig1, sig0, E0) # create the sphere object

    n = 50             #level of discretization
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    X, Y = np.meshgrid(xr, yr)
    Z = np.zeros_like(X)

    potentials = sphere.potential((X, Y, Z), field='primary')

    fig, ax = plt.subplots(1,1, figsize = (8,6))
    im = ax.pcolor(X, Y, potentials, shading='auto')
    cb = plt.colorbar(im)
    cb.set_label(label='Potential ($V$)')
    ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

    ax.set_title('Primary Potential')
    ax.set_ylabel('Y coordinate ($m$)')
    ax.set_xlabel('X coordinate ($m$)')
    ax.set_aspect('equal')

The total potential outside the sphere :math:`(r > R)` is

.. math::
    V_1 = -E_0 \big(1 - \frac{R^3}{r^3}\frac{\sigma_1 - \sigma_0}{\sigma_1 + 2\sigma_0} \big) r \cos\theta
    :label: totalP_outside

and inside the sphere :math:`(r < R)`

.. math::
    V_2 = -E_0 \frac{3\sigma_0}{\sigma_1+2\sigma_0}r \cos\theta
    :label: totalP_inside


.. plot::

    from matplotlib import patches
    from geoana.em.static import ElectrostaticSphere

    sig0 = 10.**-3.          # conductivity of the whole-space in S/m
    sig1 = 10.**-1.         # conductivity of the sphere in S/m
    sig2 = 10.**-5.         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m

    sphere1 = ElectrostaticSphere(R, sig1, sig0, E0) # create the sphere object
    sphere2 = ElectrostaticSphere(R, sig2, sig0, E0) # create the sphere object

    n = 50             #level of discretization
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    X, Y = np.meshgrid(xr, yr)
    Z = np.zeros_like(X)

    Vt1, Vp1, Vs1 = sphere1.potential((X, Y, Z), field='all')
    Vt2, Vp2, Vs2 = sphere2.potential((X, Y, Z), field='all')

    fig, axs = plt.subplots(2,2,figsize=(18,12))
    for ax, V, title in zip(
        axs.flatten(),
        [Vt1, Vt2, Vs1, Vs2],
        [
            'Conductive Sphere: \n Total Potential',
            'Resistive Sphere: \n Total Potential',
            'Conductive Sphere: \n Secondary Potential',
            'Resistive Sphere: \n Secondary Potential',
        ]
    ):
        im = ax.pcolor(X, Y, V, shading='auto')
        cb = plt.colorbar(im, ax=ax)
        cb.set_label(label='Potential ($V$)')
        ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

        ax.set_title(title)
        ax.set_ylabel('Y coordinate ($m$)')
        ax.set_xlabel('X coordinate ($m$)')
        ax.set_aspect('equal')

    plt.tight_layout()
    plt.show()

.. _dc_e_field:

Electric Field
--------------

When an external electric field crosses conductivity discontinuities within heterogeneous media,
it leads to charge buildup on the interface, which immediately gives
rise to a secondary electric field governed by Gauss's Law, to oppose the change of the primary field.
Considering that the electric field is defined as the negative gradient of the potential,
according to :eq:`totalP_outside` and :eq:`totalP_inside`, the electric field at any point (x,y,z) is

.. math::
    E_1 = E_0\mathbf{\hat{x}} + E_0\frac{\sigma_1-\sigma_0}{\sigma_1+2\sigma_0}\frac{R^3}{r^5}\big[(2x^2 - y^2 - z^2)\mathbf{\hat{x}} + (3xy)\mathbf{\hat{y}} + (3xz)\mathbf{\hat{z}}\big] \; (r > R)
    :label: eField_outside

.. math::
    E_2 = E_0\frac{3\sigma_0}{\sigma_1+2\sigma_0}\mathbf{\hat{x}} \; (r < R)
    :label: eField_inside

.. plot::

    from matplotlib import patches
    from geoana.em.static import ElectrostaticSphere

    sig0 = 10.**-3.          # conductivity of the whole-space in S/m
    sig1 = 10.**-1.         # conductivity of the sphere in S/m
    sig2 = 10.**-5.         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m

    sphere1 = ElectrostaticSphere(R, sig1, sig0, E0) # create the sphere object
    sphere2 = ElectrostaticSphere(R, sig2, sig0, E0) # create the sphere object

    n = 50             #level of discretization
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    X, Y = np.meshgrid(xr, yr)
    Z = np.zeros_like(X)

    Et1, Ep1, Es1 = sphere1.electric_field((X, Y, Z), field='all')
    Et2, Ep2, Es2 = sphere2.electric_field((X, Y, Z), field='all')

    fig, axs = plt.subplots(2,2,figsize=(18,12))
    Es = [Et1, Et2, Es1, Es2]
    titles = [
        'Conductive Sphere: \n Total Electric Field',
        'Resistive Sphere: \n Total Electric Field',
        'Conductive Sphere: \n Secondary Electric Field',
        'Resistive Sphere: \n Secondary Electric Field',
    ]
    for ax, E, title in zip(axs.flatten(), Es, titles):
        E_amp = np.linalg.norm(E, axis=-1)
        im = ax.pcolor(X, Y, E_amp, shading='auto')
        cb = plt.colorbar(im, ax=ax)
        cb.set_label(label= 'Amplitude ($V/m$)')
        ax.streamplot(X, Y, E[..., 0], E[..., 1], color='gray', linewidth=2., density=0.75)
        ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

        ax.set_ylabel('Y coordinate ($m$)')
        ax.set_xlabel('X coordinate ($m$)')
        ax.set_aspect('equal')
        ax.set_title(title)

    plt.tight_layout()
    plt.show()

.. _current_density_J:

Current Density
---------------

The current density describes the magnitude of the electric current per unit cross-sectional area at a given point in space.
According to Ohm's law there is a linear relationship between the current density and the electric field at any location within the field:
:math:`\mathbf{J} = \sigma \mathbf{E}`. This can be directly used to compute both the total and the primary current densities.

Secondary Current
^^^^^^^^^^^^^^^^^

The secondary current density is defined as a difference between the total
current density, :math:`\mathbf{J_T} = \sigma \mathbf{E_T}` and the primary
current :math:`\mathbf{J_0} = \sigma_0 \mathbf{E_0}`

.. math::
    \mathbf{J_s} &= \mathbf{J_T} - \mathbf{J_0} \\
                 &= \sigma\mathbf{E_T} - \sigma_0 \mathbf{E_0} \\
                 &= (\sigma_0 + \Delta\sigma)(\mathbf{E_0} + \mathbf{E_s}) - \sigma_0 \mathbf{E_0} \\
                 &= \Delta\sigma\mathbf{E_0}  + \sigma \mathbf{E_s}
    :label: SecondaryCurrentDefinition


Outside the sphere, the secondary current :math:`\mathbf{J_s}` acts as a electric dipole, due to and in
accordance with the charge build-up at the interface (see Charge Accumulation below).

Inside a conductive sphere, :math:`\mathbf{J_T}` is bigger than :math:`\mathbf{J_{0}}`, but in the same time
:math:`\mathbf{E_0}` is bigger than :math:`\mathbf{E_{Total}}`.
The secondary current :math:`\mathbf{J_s}` is in the reverse direction compared to the  secondary electric
field :math:`\mathbf{E_s}`. The boundary condition, stating that the normal component of current density is
continuous, is then respected by the secondary current.

Inside a resistive sphere, :math:`\mathbf{J_T}` is smaller than :math:`\mathbf{J_{0}}` but in the same time
:math:`\mathbf{E_0}` is smaller than :math:`\mathbf{E_{Total}}`.
The secondary current :math:`\mathbf{J_s}` is again in the reverse direction compared to the  secondary
electric field :math:`\mathbf{E_s}` and the boundary condition for the normal component of current density
is respected.


.. need to reference the boundary condition page. Where is it?


This can seem counter-intuitive at first as, inside the sphere, the secondary current
go from the negative to the positive charges (see Charge Accumulation below).
However we can explain it by saying that the current inside the sphere is building
the charges and not the reverse.



.. plot::

    from matplotlib import patches
    from geoana.em.static import ElectrostaticSphere

    sig0 = 10.**-3.          # conductivity of the whole-space in S/m
    sig1 = 10.**-1.         # conductivity of the sphere in S/m
    sig2 = 10.**-5.         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m

    sphere1 = ElectrostaticSphere(R, sig1, sig0, E0) # create the sphere object
    sphere2 = ElectrostaticSphere(R, sig2, sig0, E0) # create the sphere object

    n = 50             #level of discretization
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    X, Y = np.meshgrid(xr, yr)
    Z = np.zeros_like(X)

    Jt1, Jp1, Js1 = sphere1.current_density((X, Y, Z), field='all')
    Jt2, Jp2, Js2 = sphere2.current_density((X, Y, Z), field='all')

    fig, axs = plt.subplots(2,2,figsize=(18,12))
    Js = [Jt1, Jt2, Js1, Js2]
    titles = [
        'Conductive Sphere: \n Total Current Density',
        'Resistive Sphere: \n Total Current Density',
        'Conductive Sphere: \n Secondary Current Density',
        'Resistive Sphere: \n Secondary Current Density',
    ]
    for ax, J, title in zip(axs.flatten(), Js, titles):
        J_amp = np.linalg.norm(J, axis=-1)
        im = ax.pcolor(X, Y, J_amp, shading='auto')
        cb = plt.colorbar(im, ax=ax)
        cb.set_label(label='Current Density ($A/m^2$)')
        ax.streamplot(X, Y, J[..., 0], J[..., 1], color='gray', linewidth=2., density=0.75)
        ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

        ax.set_ylabel('Y coordinate ($m$)')
        ax.set_xlabel('X coordinate ($m$)')
        ax.set_aspect('equal')
        ax.set_title(title)

    plt.tight_layout()
    plt.show()

.. _bound_charge_Q:

Charge Accumulation
-------------------


Conductivity discontinuities will lead to charge buildup at the boundaries of
these discontinuities.  According to :ref:`gauss_electric`, the electric
charge accumulated on the surface of the sphere can be quantified by

.. math::
    \int_V \boldsymbol{\nabla} \cdot \mathbf{e} \; \mathrm{d}V = \int_V \frac{\rho}{\varepsilon_0} \mathrm{d}V = Q
    :label: chargeAccumulationIntegral

Based on Gauss's theorem, surface charge density at the interface is given by

.. math::
    \mathbf{e}_1 \cdot \mathbf{n} - \mathbf{e}_2 \cdot \mathbf{n} = \frac{\rho_s}{\varepsilon_0}
    :label: chargeAccumualationInterface

According to :eq:`eField_outside` :eq:`eField_inside`, the charge quantities accumulated at the surface is

.. math::
    \oint_S \rho_s \mathrm{d}a = \varepsilon_0 \oint_S (\mathbf{e}_{1n} - \mathbf{e}_{2n}) = \varepsilon_0 \oint_S 3\mathbf{E_0} R^2 \frac{\sigma_1-\sigma_0}{\sigma_1 + 2\sigma_0}\cos\theta \sin\theta \mathrm{d}\phi\mathrm{d}\theta
    :label: totalCharge

The figure below shows surface charge density at the surface of sphere.

.. plot::

    from matplotlib import patches
    from geoana.em.static import ElectrostaticSphere

    sig0 = 10.**-3.          # conductivity of the whole-space in S/m
    sig1 = 10.**-1.         # conductivity of the sphere in S/m
    sig2 = 10.**-5.         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m

    sphere1 = ElectrostaticSphere(R, sig1, sig0, E0) # create the sphere object
    sphere2 = ElectrostaticSphere(R, sig2, sig0, E0) # create the sphere object

    n = 50             #level of discretization
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    X, Y = np.meshgrid(xr, yr)
    Z = np.zeros_like(X)

    q1 = sphere1.charge_density((X, Y, Z), dr=xr[1]-xr[0])
    q2 = sphere2.charge_density((X, Y, Z), dr=xr[1]-xr[0])

    fig, axs = plt.subplots(1,2,figsize=(18,6))
    qs = [q1, q2]
    titles = ['Conductive Sphere: \n Charge Accumulation', 'Resistive Sphere: \n Charge Accumulation']

    for ax, q, title in zip(axs, qs, titles):
        im = ax.pcolor(X, Y, q, shading='auto')
        cb1 = plt.colorbar(im, ax=ax)
        cb1.set_label(label= 'Charge Density ($C/m^2$)')
        ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

        ax.set_ylabel('Y coordinate ($m$)')
        ax.set_xlabel('X coordinate ($m$)')
        ax.set_title(title)
        ax.set_aspect('equal')

    plt.tight_layout()
    plt.show()


Data
----

During a DC survey, we measure the difference of potentials between two
electrodes, often along a profile.

Therefore, when we look at data (as in the bottom plot), we see that they will
depend upon the orientation of the survey line, as well as the spacing between electrodes.

We also notice that the differences measured inside the sphere are constant,
whereas outside the sphere, we observe variations in the potential differences
in the vicinity of the sphere that then approach a constant value as we move
away from the sphere.

For a conductive sphere, the potential differences measured in the area of
influence of the sphere are smaller than the background. This can be anticipated using Ohm's law.
The reverse is observed for a resistive sphere.

.. LJH: this statement needs a bit more explanation

.. plot::

    from matplotlib import patches
    from geoana.em.static import ElectrostaticSphere

    sig0 = 10.**-3.          # conductivity of the whole-space in S/m
    sig1 = 10.**-1.         # conductivity of the sphere in S/m
    sig2 = 10.**-5.         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m

    sphere1 = ElectrostaticSphere(R, sig1, sig0, E0) # create the sphere object
    sphere2 = ElectrostaticSphere(R, sig2, sig0, E0) # create the sphere object

    n = 31             #level of discretization
    xr = np.linspace(-100, 100, n) # X-axis dipole midpoints
    yr = xr.copy()      # Y-axis dipole midpoints
    X, Y = np.meshgrid(xr, yr)
    Z = np.zeros_like(X)

    Dx = np.linspace(-100, 100, n)
    Dy = np.linspace(-100, 100, n)
    Dz = np.zeros(n)
    electrode_spacing = 10

    Mx = Dx - 0.5 * electrode_spacing/np.sqrt(2)
    My = Dy - 0.5 * electrode_spacing/np.sqrt(2)
    Mz = Dz
    Nx = Dx + 0.5 * electrode_spacing/np.sqrt(2)
    Ny = Dy + 0.5 * electrode_spacing/np.sqrt(2)
    Nz = Dz

    fig = plt.figure(figsize=(20, 20))
    ax0 = plt.subplot2grid((20, 12), (0, 0), colspan=6, rowspan=6)
    ax1 = plt.subplot2grid((20, 12), (0, 6), colspan=6, rowspan=6)
    ax2 = plt.subplot2grid((20, 12), (8, 0), colspan=6, rowspan=6)
    ax3 = plt.subplot2grid((20, 12), (8, 6), colspan=6, rowspan=6)
    ax4 = plt.subplot2grid((20, 12), (16, 2), colspan=9, rowspan=4)

    for ax, color, sig_circ in zip([ax0, ax1], [[0.6, 0.1, 0.1], [0.1, 0.1, 0.6]], [sig1, sig2]):
        circle = patches.Circle([0,0],radius=R, alpha=0.4, color=color, linewidth=1.5)
        ax.add_patch(circle)
        ax.arrow(0., 0., np.sqrt(2.)*R/2., np.sqrt(2.)*R/2., head_width=0., head_length=0.)

        for y in np.linspace(-2 * R, 2 * R, 10):
            ax.arrow(-2*R, y, 0.3*R, 0.0, head_width=5., head_length=2., color='k')

        ax.text(0, -R/2., f'$\sigma_1$={sig_circ*1000:3.3f} mS/m')
        ax.text(0, -1.5*R, f'$\sigma_0$={sig0*1000:3.3f} mS/m')
        ax.text(0.5*np.cos(np.pi/6)*R, 0.5*np.sin(np.pi/6)*R, f'R={R:1.0f} m')
        ax.text(-1.8*R, 1.3*R, f'$\mathbf{{E_0}} = {E0:1.0f} \mathbf{{\hat{{x}}}}$ V/m')

        ax.set_facecolor([0.4, 0.7, 0.4, 0.3])
        ax.set_xlim([-2 * R, 2 * R])
        ax.set_ylim([-2 * R, 2 * R])
        ax.set_ylabel('Y coordinate ($m$)')
        ax.set_xlabel('X coordinate ($m$)')
        ax.set_aspect('equal')

    Vt1 = sphere1.potential((X, Y, Z), field='total')
    Vt2 = sphere2.potential((X, Y, Z), field='total')
    titles = [
            'Conductive Sphere: \n Total Potential',
            'Resistive Sphere: \n Total Potential',
        ]

    for ax, V, title in zip([ax2, ax3], [Vt1, Vt2], titles):
        im = ax.pcolor(X, Y, V, shading='auto')
        cb = plt.colorbar(im, ax=ax)
        cb.set_label(label='Potential ($V$)')
        ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

        ax.set_title(title)
        ax.set_ylabel('Y coordinate ($m$)')
        ax.set_xlabel('X coordinate ($m$)')
        ax.set_aspect('equal')

        ax.plot(Dx, Dy, color='gray')
        ax.scatter(Dx, Dx, color='black', label="Dipole Midpoint")
        ax.scatter(np.r_[Mx, Nx], np.r_[My, Ny], color='red', label="Electrodes")
        ax.legend(loc='best')

    VM1 = sphere1.potential((Mx, My, Mz), field='total')
    VN1 = sphere1.potential((Nx, Ny, Nz), field='total')

    VM2 = sphere2.potential((Mx, My, Mz), field='total')
    VN2 = sphere2.potential((Nx, Ny, Nz), field='total')

    #Plot the Data (from Configuration 0)
    ax4.plot(np.sqrt(2)*np.linspace(-100, 100, n), VM1-VN1,
             marker='o', color='red', linewidth=3., label='Left Model Response' )
    ax4.plot(np.sqrt(2)*np.linspace(-100, 100, n), VM2-VN2,
             marker='o', color='blue', linewidth=3., label='Right Model Response' )
    ax4.set_xlabel('Profile Distance ($m$)')
    ax4.set_ylabel('Potential Difference ($V$)')
    ax4.legend(loc='best')

    plt.show()


Building some Intuition for DC problem
--------------------------------------

In real life, we do not know the underground configuration. We only see the
data and we are trying to model the subsurface based on it. There are
several sets of parameters that can fit the data perfectly. Even in the simple
case presented here, where we know that the object is a sphere, whose response can be
calculated analytically, we find several configurations that can produce
the same data along the same profile.

Here is an example of two spheres generating the response along the chosen profile.
The only parameters that have changed are the radius and the conductivity of the sphere.

.. plot::

    from matplotlib import patches
    from geoana.em.static import ElectrostaticSphere

    sig0 = 10.**-3.          # conductivity of the whole-space in S/m
    sig1 = 10.**-1.         # conductivity of the sphere in S/m
    sig2 = 1.310344828 * 10**-3.
    R0   = 20.          # radius of the sphere in m
    R1   = 40.
    E0   = 1.           # inducing field strength in V/m

    sphere1 = ElectrostaticSphere(R0, sig1, sig0, E0) # create the sphere object
    sphere2 = ElectrostaticSphere(R1, sig2, sig0, E0) # create the sphere object

    n = 31             #level of discretization
    xr = np.linspace(-100, 100, n) # X-axis dipole midpoints
    yr = xr.copy()      # Y-axis dipole midpoints
    X, Y = np.meshgrid(xr, yr)
    Z = np.zeros_like(X)

    Dx = np.linspace(-100, 100, n)
    Dy = np.linspace(-100, 100, n)
    Dz = np.zeros(n)
    electrode_spacing = 10

    Mx = Dx - 0.5 * electrode_spacing/np.sqrt(2)
    My = Dy - 0.5 * electrode_spacing/np.sqrt(2)
    Mz = Dz
    Nx = Dx + 0.5 * electrode_spacing/np.sqrt(2)
    Ny = Dy + 0.5 * electrode_spacing/np.sqrt(2)
    Nz = Dz

    fig = plt.figure(figsize=(20, 20))
    ax0 = plt.subplot2grid((20, 12), (0, 0), colspan=6, rowspan=6)
    ax1 = plt.subplot2grid((20, 12), (0, 6), colspan=6, rowspan=6)
    ax2 = plt.subplot2grid((20, 12), (8, 0), colspan=6, rowspan=6)
    ax3 = plt.subplot2grid((20, 12), (8, 6), colspan=6, rowspan=6)
    ax4 = plt.subplot2grid((20, 12), (16, 2), colspan=9, rowspan=4)

    R = 50
    for ax, color, sig_circ, r in zip([ax0, ax1], [[0.6, 0.1, 0.1], [0.1, 0.1, 0.6]], [sig1, sig2], [R0, R1]):
        circle = patches.Circle([0,0],radius=r, alpha=0.4, color=color, linewidth=1.5)
        ax.add_patch(circle)
        ax.arrow(0., 0., np.sqrt(2.)*r/2., np.sqrt(2.)*r/2., head_width=0., head_length=0.)

        for y in np.linspace(-2 * R, 2 * R, 10):
            ax.arrow(-2*R, y, 0.3*R, 0.0, head_width=5., head_length=2., color='k')

        ax.text(0, -r/2., f'$\sigma_1$={sig_circ*1000:3.3f} mS/m')
        ax.text(0, -1.5*r, f'$\sigma_0$={sig0*1000:3.3f} mS/m')
        ax.text(0.5*np.cos(np.pi/6)*r, 0.5*np.sin(np.pi/6)*r, f'R={r:1.0f} m')
        ax.text(-1.8*R, 1.3*R, f'$\mathbf{{E_0}} = {E0:1.0f} \mathbf{{\hat{{x}}}}$ V/m')

        ax.set_facecolor([0.4, 0.7, 0.4, 0.3])
        ax.set_xlim([-2 * R, 2 * R])
        ax.set_ylim([-2 * R, 2 * R])
        ax.set_ylabel('Y coordinate ($m$)')
        ax.set_xlabel('X coordinate ($m$)')
        ax.set_aspect('equal')

    Vt1 = sphere1.potential((X, Y, Z), field='total')
    Vt2 = sphere2.potential((X, Y, Z), field='total')
    titles = [
            'Conductive Sphere: \n Total Potential',
            'Resistive Sphere: \n Total Potential',
        ]

    for ax, V, title, r in zip([ax2, ax3], [Vt1, Vt2], titles, [R0, R1]):
        im = ax.pcolor(X, Y, V, shading='auto')
        cb = plt.colorbar(im, ax=ax)
        cb.set_label(label='Potential ($V$)')
        ax.add_patch(patches.Circle([0,0], r, fill=False, linestyle='--'))

        ax.set_title(title)
        ax.set_ylabel('Y coordinate ($m$)')
        ax.set_xlabel('X coordinate ($m$)')
        ax.set_aspect('equal')

        ax.plot(Dx, Dy, color='gray')
        ax.scatter(Dx, Dx, color='black', label="Dipole Midpoint")
        ax.scatter(np.r_[Mx, Nx], np.r_[My, Ny], color='red', label="Electrodes")
        ax.legend(loc='best')

    VM1 = sphere1.potential((Mx, My, Mz), field='total')
    VN1 = sphere1.potential((Nx, Ny, Nz), field='total')

    VM2 = sphere2.potential((Mx, My, Mz), field='total')
    VN2 = sphere2.potential((Nx, Ny, Nz), field='total')

    #Plot the Data (from Configuration 0)
    ax4.plot(np.sqrt(2)*np.linspace(-100, 100, n), VM1-VN1,
             marker='o', color='red', linewidth=3., label='Left Model Response' )
    ax4.plot(np.sqrt(2)*np.linspace(-100, 100, n), VM2-VN2,
             marker='o', color='blue', linewidth=3., label='Right Model Response' )
    ax4.set_xlabel('Profile Distance ($m$)')
    ax4.set_ylabel('Potential Difference ($V$)')
    ax4.legend(loc='best')

    plt.show()
