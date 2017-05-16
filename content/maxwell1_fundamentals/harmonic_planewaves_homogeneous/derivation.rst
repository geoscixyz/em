.. _harmonic_planewaves_homogeneous_derivation:

Derivation
==========

General Solution for a Planewave
--------------------------------

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_freq_derivation

   Geometry of an EM planewave propagating downwards.

To obtain a solution for EM planewaves within a homogeneous medium, let us begin with the following vector Helmholtz equations for :math:`\mathbf{E}` and :math:`\mathbf{H}`:

.. math::
    \boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  &= 0\\
    \boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  &= 0
    :name: Helmholtz_full_analytic

where the complex :ref:`wavenumber<harmonic_planewaves_homogeneous_wavenumber>` is given by:

.. math::
    k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}
    :name: Helmholtz_complex_wavenumber

For simplicity, let us assume that the planewave propagates along the z-direction. According to Griffiths :cite:`griffiths1999` (pp. 378), the electric and magnetic fields supported by a planewave are transverse to the direction of propagation; thus the electric and magnetic fields lie in the xy-plane. In this case, the governing equation for the electric field simplifies to:

.. math::
    \frac{\partial^2 \mathbf{E}}{\partial z^2} + k^2 \mathbf{E} = 0
    :name: Helmholtz_1D_analytic

where :math:`\mathbf{E} \equiv \mathbf{E}(z,\omega)`; thus it does not depend on :math:`x` or :math:`y`. The previous equation has a general solution of the form:

.. math::
    \mathbf{E} = \mathbf{E}_0^- \, e^{i(kz-\omega t)} + \mathbf{E}_0^+ \, e^{-i(kz + \omega t)}
    :name: Helmholtz_1D_solution

where :math:`\mathbf{E}_0^-` and :math:`\mathbf{E}_0^+` are the vector amplitudes of down-going and up-going waves, respectively. The :math:`e^{-i\omega t}` in both terms controls the temporal phase. The complex wavenumber has both real and imaginary components. Thus it can be expressed as:

.. math::
    k = \alpha - i\beta
    :name: wavenumber_split

where :math:`\alpha \geq 0` and :math:`\beta \geq 0` depend on the frequency and physical properties of the media. Substituting Eq. :eq:`wavenumber_split` into Eq. :eq:`Helmholtz_1D_solution`, the solution to our wave equation for :math:`\mathbf{E}` becomes:

.. math::
    \mathbf{E} = \mathbf{E}_0^- \, e^{\beta z} e^{i(\alpha z -\omega t)} + \mathbf{E}_0^+ \, e^{-\beta z} e^{-i (\alpha z + \omega t)} 
    :name: Helmholtz_1D_components

For both the down-going and up-going waves, there are two important behaviours within the solution. The first term, which contains :math:`e^{\pm i \alpha z}`, controls the oscillatory behaviour (i.e. :ref:`wavelength<harmonic_planewaves_homogeneous_wavelength>`) and :ref:`velocity<harmonic_planewaves_homogeneous_phasevelocity>` of each wave. The second term, which contains :math:`e^{\pm \beta z}`, controls the decay behaviour (i.e. :ref:`attenuation<harmonic_planewaves_homogeneous_skindepth>`) of each wave. Notice that as :math:`z \rightarrow -\infty` for the down-going wave, its amplitude goes to zero. The same behaviour occurs for the up-going wave as :math:`z \rightarrow \infty`.

Using the same approach on the Helmholtz equation for :math:`\mathbf{H}`, the magnetic field has a general solution of the form:

.. math::
    \mathbf{H} &= \mathbf{H}_0^- \, e^{i(kz-\omega t)} + \mathbf{H}_0^+ \, e^{-i(kz+\omega t)}\\
    &= \mathbf{H}_0^- \, e^{\beta z} e^{i(\alpha z-\omega t)} + \mathbf{H}_0^+ \, e^{-\beta z} e^{-i (\alpha z+\omega t)}
    :name: Helmholtz_1D_h

.. note::

    Eq. :eq:`Helmholtz_1D_components` is still a general solution. To determine :math:`\mathbf{E}_0^-` and :math:`\mathbf{E}_0^+` explicitly, you must envoke a set of boundary conditions. For example, :math:`\mathbf{E}(z \rightarrow -\infty,\omega) = 0` and :math:`\mathbf{E}(z =0,\omega) = \mathbf{E}_0`. This would give you a solution :math:`\mathbf{E}(z,\omega) = \mathbf{E}_0 \, e^{\beta z} e^{ i(\alpha z-\omega t)}` (i.e. just the down-going wave). From this solution, :math:`\mathbf{H}(z,\omega)` can be determined using Faraday's law. You could also envoke boundary conditions to solve for :math:`\mathbf{H}` and use the Ampere-Maxwell law to obtain :math:`\mathbf{E}`.

.. _harmonic_planewaves_homogeneous_derivation_app:

Supporting Derivation for the App
---------------------------------

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_freq_derivation_2

   Downward propagating planewave modeled by the app.

The app simulates the downward propagation of an EM planewave. As we can see in :numref:`planewavedown_freq_derivation_2`, the planewave is polarized such that the electric lies along the x-direction and the magnetic field lies along the y-direction. Physically, we can think of this wave as being caused by a horizontal sheet of harmonic current :math:`\mathbf{I}(\omega) = I_x \, \textrm{cos} (\omega t) \mathbf{u_x}`, where :math:`\mathbf{u_x}` is the unit vector in the x-direction.

To solve for the electric field, we begin with the general solution from Eq. :eq:`Helmholtz_1D_components`:

.. math::
    \mathbf{E} (z,\omega) = \mathbf{E}_0^-  e^{ikz} + \mathbf{E}_0^+ e^{-ikz} 
    :name:

where :math:`\mathbf{E}_0^-` and :math:`\mathbf{E}_0^+` are the amplitudes of the down-going and up-going waves, respectively. Given that we are only modeling the downgoing wave and the corresponding electric field only has components in the x-direction, our solution takes the form:

.. _harmonic_planewaves_homogeneous_derivation_app_soln:

.. math::
    \mathbf{E} (z,\omega) = E_x (z,\omega) \, \mathbf{u_x} = E_{x,0}^{-} e^{ikz} \mathbf{u_x}
    :name:

where :math:`E_x` is a scalar function and :math:`E_{x,0}^{-}` is the scalar amplitude of the electric field. Using Faraday's law, we can confirm that the corresponding magnetic field only has components in the y-direction, where:

.. math::
    \frac{\partial E_x}{\partial z} + i \omega \mu H_y = 0
    :name:

Solving for the y-component of the magnetic field, we obtain:

.. math::
    H_y (z,\omega ) = H_{y,0}^- e^{ikz} = -\frac{k}{\omega \mu} E_{x,0}^- \, e^{ikz}
    :name:

Thus: 

.. math::
    \mathbf{H}(z,\omega) = H_y (z,\omega) \, \mathbf{u_y} = - \frac{k}{\omega \mu} E_{x,0}^- \, e^{ikz} \, \mathbf{u_y}

where :math:`\mathbf{u_y}` is the unit vector in the y-direction.


