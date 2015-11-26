.. _electrostatic_sphere:

Conducting sphere in a uniform electric field
=============================================

A sphere in a whole-space provides a simple geometry to examine a variety of
questions and can provide powerful physical insights into a variety of
problems. Here we examine the case of a conducting sphere in a uniform
electrostatic field. This scenario gives us a setting to examine aspects of
the DC resistivity experiment, including the behavior of electric potentials,
electric fields, current density and the build up of charges at interfaces.
This work follows the derivation in [1]_ and is supported by apps developed in
a `Jupyter Notebook`_.

.. _Jupyter Notebook: https://github.com/ubcgif/em/blob/AmpereMaxwell/examples/sphere/ElectrostaticSphere.ipynb

Setup
-----

The problem setup is shown in the figure below, where we have

- a uniform electric fields oriented in the \\(x\\)-direction: \\(\\mathbf{E_0} = E_0 \\mathbf{\\hat{x}}\\)
- a whole-space background with conductivity \\(\\sigma_0\\)
- a sphere with radius \\(R\\) and conductivity \\(\\sigma_1\\)
- the origin of coordinate coincides with the centre of the sphere


.. plot::

    from examples.sphere import *

    sig0 = 10.**-3.         # conductivity of the wholespace in S/m
    sig1 = 10.**-1.         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition

    fig, ax = plt.subplots(1,1, figsize = (6,6))
    ax = get_Setup(XYZ,sig0,sig1,R,E0,ax)

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
define it to be the negative gradient of a potential, \\(V\\)

.. math::
	\mathbf{e} = -\nabla V
	:label: DC_Potential

To define the potential at a point \\(p\\) from an electric field requires an integration

.. math::
    V = -\int_{ref}^p \mathbf{e} \cdot \mathbf{dl}
    :label: V_from_e

The choice of reference point \\(ref\\) is arbitrary, but it is often
convenient to consider the reference point to be infinitely far away, so
\\(ref = \\infty\\). In this case, the electric potential at \\(p\\) is
equivalent to the amount of work done by to bring a positive charge from
infinity to the point \\(p\\).


Potentials 
----------

Assuming an x-directed uniform electric field and zero potential at infinity,
the integration from :eq:`V_from_e` gives

.. math::
	V_p = - E_0 x = -E_0 r \cos\theta
	:label: Primary_Potential

.. plot::

    from examples.sphere import *

    sig0 = 10.**-3.         # conductivity of the wholespace in S/m
    sig1 = 10.**-1.         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition

    fig, ax = plt.subplots(1,1, figsize = (6,6))
    ax = Plot_Primary_Potential(XYZ,sig0,sig1,R,E0,ax)

The total potential outside the sphere \\(r > R\\) is

.. math::
	V_1 = -E_0 \big(1 - \frac{R^3}{r^3}\frac{\sigma_1 - \sigma_0}{\sigma_1 + 2\sigma_0} \big) r \cos\theta
	:label: totalP_outside

and inside the sphere \\(r < R\\)

.. math::
	V_2 = -E_0 \frac{3\sigma_0}{\sigma_1+2\sigma_0}r \cos\theta
	:label: totalP_inside

Solution, discussion, explain some intuition, questions. 

.. plot::
    
    from examples.sphere import *

    sig0 = 10.**-3          # conductivity of the wholespace in S/m
    sig1 = 10.**-1         # conductivity of the sphere in S/m
    sig2 = 10.**-5         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition

    fig, ax = plt.subplots(2,2,figsize=(18,12))
    ax = mkvc(ax)
    ax[0] = Plot_Total_Potential(XYZ,sig0,sig1,R,E0,ax[0])
    ax[0].set_title('Conductive Sphere: Total Potential',fontsize=ftsize_title)
    ax[1] = Plot_Secondary_Potential(XYZ,sig0,sig1,R,E0,ax[1])
    ax[1].set_title('Conductive Sphere: Secondary Potential',fontsize=ftsize_title)
    ax[2] = Plot_Total_Potential(XYZ,sig0,sig2,R,E0,ax[2])
    ax[2].set_title('Resistive Sphere: Total Potential',fontsize=ftsize_title)
    ax[3] = Plot_Secondary_Potential(XYZ,sig0,sig2,R,E0,ax[3])
    ax[3].set_title('Resistive Sphere: Secondary Potential',fontsize=ftsize_title)
    


Electric Field
--------------

When an external electric field comes across conductivity discontinuities within heterogeneous media, 
it Leads to charge buildup at boundaries of these discontinuities, which immediately gives 
rise to a secondary electric field governed by Gauss’s Law to oppose the primary field. 
Considering the electric field is defined as the negative gradient of the potential, 
according to :eq:`totalP_outside` and :eq:`totalP_inside`, the electric field at any point (x,y,z) is

.. math::
    E_1 = E_0\mathbf{\hat{x}} + E_0\frac{\sigma_1-\sigma_0}{\sigma_1+2\sigma_0}\frac{R^3}{r^5}\big[(2x^2 - y^2 - z^2)\mathbf{\hat{x}} + (3xy)\mathbf{\hat{y}} + (3xz)\mathbf{\hat{z}}\big] \; (r > R)
    :label: eField_outside
    
.. math::
    E_2 = E_0\frac{3\sigma_0}{\sigma_1+2\sigma_0}\mathbf{\hat{x}} \; (r < R)
    :label: eField_inside
	
.. plot::
    
    from examples.sphere import *

    sig0 = 10.**-3          # conductivity of the wholespace in S/m
    sig1 = 10.**-1         # conductivity of the sphere in S/m
    sig2 = 10.**-5         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition
    ftsize_title = 18      #font size for titles

    fig, ax = plt.subplots(2,2,figsize=(18,12))
    ax = mkvc(ax)
    ax[0] = Plot_Total_ElectricField(XYZ,sig0,sig1,R,E0,ax[0])
    ax[0].set_title('Conductive Sphere: Total Electric Field',fontsize=ftsize_title)
    ax[1] = Plot_Secondary_ElectricField(XYZ,sig0,sig1,R,E0,ax[1])
    ax[1].set_title('Conductive Sphere: Secondary Electric Field',fontsize=ftsize_title)
    ax[2] = Plot_Total_ElectricField(XYZ,sig0,sig2,R,E0,ax[2])
    ax[2].set_title('Resistive Sphere: Total Electric Field',fontsize=ftsize_title)
    ax[3] = Plot_Secondary_ElectricField(XYZ,sig0,sig2,R,E0,ax[3])
    ax[3].set_title('Conductive Sphere: Secondary Electric Field',fontsize=ftsize_title)

Current Density
---------------

The current density describes the magnitude of the electric current per unit cross-sectional area at a given point in space. 
According to Ohm’s law there is a linear relationship between the current density and the electric field at any location within the field: 
\\(\\mathbf{J} = \\sigma \\mathbf{E}\\). This can be directly used to compute both the total and the primary current densities. 

Secondary Current
^^^^^^^^^^^^^^^^^

The secondary current density is defined as a difference between the total
current density and the primary current :eq:`Secondary_Current_Definition`.

.. math::
    \mathbf{J_s} = \mathbf{J_T} - \mathbf{J_P}
    :label: Secondary_Current_Definition

.. math::
    \mathbf{J_s} = \sigma_1 \mathbf{E_{Total}} - \sigma_0 \mathbf{E_0}
    :label: Secondary_Current

This leads to an important corollary:

.. math::
    \mathbf{J_s} \neq \sigma_1 \mathbf{E_s}
    :label: Secondary_Current_Corollary

As \\(\\mathbf{E_0}\\) is bigger than \\(\\mathbf{E_{Total}}\\) inside the
sphere, the seconday current density inside the sphere is in the reverse
direction compared to the secondary electric field.The boundary condition,
stating that the normal component of current density is continuous, is then
respected by the secondary current.

.. need to reference the boundary condition page. Where is it?

This can seem counter-intuitive as, inside the sphere, the secondary current
go from the negative to the positive charges (see Charge Accumulation below).
However we have to keep in mind that the current inside the sphere is building
the charges and not the reverse.


.. plot::
    
    from examples.sphere import *

    sig0 = 10.**-3          # conductivity of the wholespace in S/m
    sig1 = 10.**-1         # conductivity of the sphere in S/m
    sig2 = 10.**-5         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition

    fig, ax = plt.subplots(2,2,figsize=(18,12))
    ax = mkvc(ax)
    ax[0] = Plot_Total_Currents(XYZ,sig0,sig1,R,E0,ax[0])
    ax[0].set_title('Conductive Sphere: Total Current Density',fontsize=ftsize_title)
    ax[1] = Plot_Secondary_Currents(XYZ,sig0,sig1,R,E0,ax[1])
    ax[1].set_title('Conductive Sphere: Secondary Current Density',fontsize=ftsize_title)
    ax[2] = Plot_Total_Currents(XYZ,sig0,sig2,R,E0,ax[2])
    ax[2].set_title('Resistive Sphere: Total Current Density',fontsize=ftsize_title)
    ax[3] = Plot_Secondary_Currents(XYZ,sig0,sig2,R,E0,ax[3])
    ax[3].set_title('Resistive Sphere: Secondary Current Density',fontsize=ftsize_title)
    


Charge Accumulation
-------------------


Conductivity discontinuities will lead to charge buildup at the boundaries of
these discontinuities.  According to :ref:`gauss_electric`, the electric
charge accumulated on the surface of the sphere can be quantified by

.. math::
	\int_V \boldsymbol{\nabla} \cdot \mathbf{e} \; \mathrm{d}V = \int_V \frac{\rho}{\varepsilon_0} \mathrm{d}V = Q
	:label:

Based on Gauss's theorem, surface charge density at the interface is given by

.. math::
	\mathbf{e}_1 \cdot \mathbf{n} - \mathbf{e}_2 \cdot \mathbf{n} = \frac{\rho_s}{\varepsilon_0}
	:label:

According to :eq:`eField_outside` :eq:`eField_inside`, the charge quantities accumulated at the surface is

.. math::
	\oint_S \rho_s \mathrm{d}a = \varepsilon_0 \oint_S (\mathbf{e}_{1n} - \mathbf{e}_{2n}) = \varepsilon_0 \oint_S 3\mathbf{E_0} R^2 \frac{\sigma_1-\sigma_0}{\sigma_1 + 2\sigma_0}\cos\theta \sin\theta \mathrm{d}\phi\mathrm{d}\theta
	:label:

The figure below shows surface charge density at the surface of sphere.

.. plot::

    from examples.sphere import *

    sig0 = 10.**-3          # conductivity of the wholespace in S/m
    sig1 = 10.**-1         # conductivity of the sphere in S/m
    sig2 = 10.**-5         # conductivity of the sphere in S/m
    R    = 50.          # radius of the sphere in m
    E0   = 1.           # inducing field strength in V/m
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition

    fig, ax = plt.subplots(1,2,figsize=(18,6))
    ax = mkvc(ax)
    ax[0] = Plot_ChargesDensity(XYZ,sig0,sig1,R,E0,ax[0])
    ax[0].set_title('Conductive Sphere: Charge Accumulation',fontsize=ftsize_title)
    ax[1] = Plot_ChargesDensity(XYZ,sig0,sig2,R,E0,ax[1])
    ax[1].set_title('Resistive Sphere: Charge Accumulation',fontsize=ftsize_title)


Data
----

During a DC survey, we measure the difference of potentials between two
electrodes, often along a profile. 

Therefore, when we look at data (as in the bottom plot), we see that they will
depend upon the orientation depend of the orientation of the survey line, as well as the spacing between electrodes.

We also notice that the differences measured inside the sphere is constant,
whereas outside the sphere, we observe variations in the potential differences
in the vicinity of the sphere that then approach a constant value as we move
away from the sphere.

For a conductive sphere, the potential differences measured in the area of
influence of the sphere are smaller than the background. This can be anticipated using Ohm's law.
The reverse is observed for a resistive sphere.

.. LJH: this statement needs a bit more explination

.. plot::
    
    import matplotlib.pyplot as plt
    from examples.sphere import *

    sig0 = 10.          # conductivity of the wholespace
    sig1 = 100.         # conductivity of the sphere
    R    = 50.          # radius of the sphere
    E0   = 1.           # inducing field strength
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition
    PlotOpt = 'Total'

    xstart=-100.
    ystart=-100.
    xend=100.
    yend=100.
    nb_dipole=11
    electrode_spacing=20

    plot_PotentialDifferences(XYZ,R,sig0,sig1,E0,xstart,ystart,xend,yend,nb_dipole,electrode_spacing,PlotOpt)

Building some Intuition for DC problem
--------------------------------------

In real life, we do not know the underground configuration. We only see the
data and we are trying to model the underground based on it. There are
several sets of parameters that can fit perfectly the data. Even in the simple
case presented here, where we know that the object is a sphere, whose response can be
calculated analytically, we find several configurations that can produce
the same data along the same profile.

Here is an example of two spheres generating the response along the chosen profile. 
The only parameters that have changed are the radius and the conductivity of the sphere. 

.. plot::

    import matplotlib.pyplot as plt
    from examples.sphere import *

    sig0 = 10.         
    sig1 = 100.         
    sig2 = 13.10344828
    R0    = 10.          
    R1 = 20.
    E0   = 1.           
    n = 100             
    xr = np.linspace(-100, 100, n) 
    yr = xr.copy()      
    zr = np.r_[0]          
    XYZ = ndgrid(xr,yr,zr)
    xstart = -100.
    ystart = 50.
    xend = 100.
    yend = 50.
    nb_dipole = 11
    electrode_spacing = 20.
    PlotOpt = 'Total'
    
    inversion_uncertainty(XYZ,sig0,sig1,sig2,R0,R1,E0,xstart,ystart,xend,yend,nb_dipole,electrode_spacing,PlotOpt)



.. [1] Ward, S. H., & Hohmann, W. *Electromagnetic Theory for Geophysical Applications Applications.* In Electromagnetic methods in applied geophysics (1st ed., pp. 130–311). Society of Exploration Geophysicists. 1988.
