.. _plane_waves_in_homogeneous_media_downward_solution:

Solving for a Down-Going Plane Wave
===================================

To obtain analytic solutions for the setup in :numref:`planewavedown_freq_index`, we begin by solving the Helmholtz equations in the frequency domain. Time domain solutions are obtained by taking the inverse Fourier or inverse Laplace transform.

For EM plane waves, the Helmholtz equations for :math:`\mathbf{E}` and :math:`\mathbf{H}` are given by:

.. math::
    \boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  = 0
    :label: fd_helmholtz_e

.. math::
    \boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  = 0
    :label: fd_helmholtz_h

where :math:`k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}` is the complex wave number. In order to solve the above differential equations, boundary conditions are required. The first set of boundary conditions states that :math:`\mathbf{H}(z=\infty) = 0` and :math:`\mathbf{E}(z=\infty) = 0`. For solving Eqs. :eq:`fd_helmholtz_e` and Eq. :eq:`fd_helmholtz_h`, we have two choices for the second boundary condition: 1) :math:`\mathbf{E}(z=0) = \mathbf{E}_0` or 2) :math:`\mathbf{H}(z=0) = \mathbf{H}_0`.

**Option 1:**

Let us consider solving the Helmholtz equations where :math:`\mathbf{E}(z=0) = \mathbf{E}_0`. In this case, the solution for the electric field is given by:

.. math::
    \mathbf{E} = \mathbf{E}_0 e^{i(kz -\omega t)}

Using :ref:`Faraday's Law<faraday>`, the corresponding magnetic field is given by:

.. math::
    \mathbf{H} = -\frac{1}{i \omega \mu} \nabla \times \big ( \mathbf{E}_0 e^{i(kz-\omega t)} \big )

Note that the previous expression is in fact a solution to :eq:`fd_helmholtz_h`.

The solution in the time domain can be obtained using the inverse Fourier transform: :math:`\mathbf{e}(t) = \mathcal{F}^{-1}[\mathbf{E}(\omega)]`, which solves the equivalent differential equation in time:

.. math::

    \boldsymbol{\nabla}^2 \mathbf{e} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t}    = 0,

with the initial condition:

.. math::
    \mathbf{e}(t=0)=\delta(t)\mathbf{E}_0, \ \text{when} \ z=0,

    \mathbf{e}(t=0)=0, \ \text{when} \ z\neq 0.

**Option 2:**

If boundary condition 2) is used in to solve Eq. :eq:`fd_helmholtz_h`, then the magnetic field has a solution:

.. math::
    \mathbf{H} = \mathbf{H}_0 e^{i(kz - \omega t)}

Using the :ref:`Ampere-Maxwell equation<ampere_maxwell>`, the corresponding electric field is given by:

.. math::
    \mathbf{E} = \frac{1}{\sigma + i\omega\epsilon} \nabla \times \big ( \mathbf{H_0}e^{i(kz - \omega t)} \big )

Note that the previous expression is in fact a solution to :eq:`fd_helmholtz_e`.

The solution in the time domain can be obtained using the inverse Fourier transform: :math:`\mathbf{h}(t) = \mathcal{F}^{-1}[\mathbf{H}(\omega)]`, which solves the equivalent differential equation in time:

.. math::

    \boldsymbol{\nabla}^2 \mathbf{h} - \mu\epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{h}}{\partial t}    = 0,

with the initial condition:

.. math::
    \mathbf{h}(t=0)=\delta(t)\mathbf{H}_0, \ \text{when} \ z=0,

    \mathbf{h}(t=0)=0, \ \text{when} \ z\neq 0.

.. note::
    Although solutions to the Helmholtz equation contain terms of the form :math:`e^{-i\omega t}`, these terms are often suppressed for more concise notation.

**Summary:**

Solutions to the Helmholtz equations, and the wave equations, can be obtained two ways. Either we solve for the electric field and use it to obtain the magnetic field, or visa versa. In the following material, we will solve the scenario illustrated in :numref:`planewavedown_freq_index` by using our first choice in boundary conditions; which solves for the electric field and uses it to obtain the magnetic field.

In following sections, we derive analytic expressions for the plane wave EM fields in both frequency and time domain. Important physical behaviours of each solution are discussed (Analytic Solution section) along with the relationship between EM fields (Fields section). Finally, using numerical apps, we simulate plane EM fields, and visualize them (Simulation section).

.. _plane_waves_in_homogeneous_media_index_Poynting:

Poynting Vector
---------------

The Poynting vector (:math:`\mathbf{S}`) defines the directional energy flux density of an electromagnetic field. The Poynting vector is useful from a qualitative standpoint because it can be used to relate the electric field, magnetic field and propagation direction of EM waves. This quantity is given by the following equation:

.. math::
    \mathbf{S} = \mathbf{E \times H}
    :name:

Thus if an EM wave at a certain time and location were to support an electric field in the positive x-direction and a magnetic field in the negative y-direction, we could deduce that the EM wave is propagating downward.



