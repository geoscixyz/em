.. _frequency_domain_planewave_sources_analytic_solution:

Analytic Solution
=================

.. topic:: Purpose

    We provide solutions of Plane wave equations in frquency domain for the homogeneous medium. And from the solutions, we extract meaningful physical principles: wavenumber, skin depth, phase velocity, and wave legnth of EM waves.


:ref:`Maxwell's equations in the frequency domain <frequency_domain_equations>`, without source terms, are:

.. math:: \boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  = 0

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  = 0

where :math:`k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}` is the complex wave number. These are vector Helmholtz equations and, in a homogeneous medium, they support plane wave solutions. For ease of discussions, assume the electric and magnetic fields lie in the x-y plane and the wave propagates perpendicular to that plane (in the z-direction).

With this geometry, the governing equations in the electric field is

.. math:: \frac{\partial^2 \mathbf{E}}{\partial z^2} + k^2 \mathbf{E} = 0,

where :math:`\mathbf{E} \equiv \mathbf{E}(z,\omega)`. This has a solution of the following form:

.. math:: \mathbf{E} = \mathbf{E}_0 e^{\pm ikz} = 0,
        :name: fd1

where :math:`\mathbf{E}_0` is the amplitude. Writing the wave number as :math:`k = k_R + ik_I` and substituting into Equation :eq:`fd1` yields:

.. math:: \mathbf{E} = \mathbf{E}_0 e^{\pm i(k_R +ik_I)z}.
        :name: fd2

This has two terms. The first, :math:`e^{\pm ik_Rz}`, is a complex sinusoidal. The second term, :math:`e^{\pm k_Iz}`, has a real exponent and this term shows how the amplitude vaires with :math:`z`. Equation :eq:`fd2` thus corresponds to a propagating harmonic wave that decays as it travels.

To add clarity, and keep with notation that is typically used, we do the following. First, we explicitly include the time dependence :math:`e^{i\omega t}`. Second, we write

.. math:: k = \alpha + i\beta
        :name: fd3

We have chosen to keep this notation for :math:`k` since it corresponds to that used in :cite:`ward1988`. The propagating harmonic wave in time is then written as

.. math:: \mathbf{e} (z,t) \equiv \mathbf{e} = \mathbf{e}_0^+ e^{-\beta z} e^{-i(\alpha z - \omega t)} + \mathbf{e}_0^- e^{-\beta z} e^{-i(\alpha z + \omega t)}.
        :name: fd4

We begin by considering the first part of this equation. The term :math:`e^{-i(\alpha z - \omega t)}` represents a wave travelling in the positive z-direction. The phase velocity of the wave is :math:`v_{phase} = \omega/\alpha`. The initial amplitude of the wave is :math:`\mathbf{e}_0^+` and the term :math:`e^{-\beta z}` indicates that the amplitude decreases exponentially with :math:`z`. Thus in homogeneous media, the electromagnetic fields can propagate as plane waves in which their amplitude exponentially decreases with distance. The second part in Equation :eq:`fd4` is understood in the same manner except that the wave is travelling in the opposite direction (negative z-direction) and the initial amplitude is :math:`\mathbf{e}_0^-`.

General solutions of the 1D Helmholtz equations generally require waves travelling in the positive and negative z-directions.

The magnetic field will also travel in the x-y plane but is perpendiculat to :math:`\mathbf{e}`.

.. We can investigate the plane wave propagation more fully by looking more closely at the mathematics and using an interactive app.

.. _frequency_domain_plane_wave_sources_wavenumber:

Wavenumber
----------

The wave number :math:`k` is:

.. math:: k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}.

Dividing :math:`k` into real and imaginary parts, and following :cite:`stratton1941,ward1988`, we have:

.. math:: k = \alpha + i \beta

.. math:: \alpha = \omega \left ( \frac{\mu \epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right )^{1/2} + 1 \right ] \right )^{1/2}

.. math:: \beta = \omega \left ( \frac{\mu\epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right)^{1/2} - 1 \right ] \right ) ^{1/2}
        :name: wn1

The wave travelling in the positive z-direction has the form:

.. math:: \mathbf{e} = \mathbf{e}_0^+ e^{-\beta z}e^{-i(\alpha z - \omega t)}.
        :name: wn2

The real and positive quantity :math:`\beta` controls how quickly the wave decays with :math:`z`. Effectively it quantifies the skin depth.

.. _frequency_domain_plane_wave_sources_skin_depth:

Skin Depth
----------

The skin depth :math:`\delta` is the distance the wave travels for its amplitude to have decayed by a factor of :math:`1/e`. Thus

.. math:: \delta = \frac{1}{\beta}.

:numref:`sd` illustrates the concept of skin depth.

.. figure:: images/skindepth.png
        :figwidth: 50%
        :align: right
        :name: sd

        Skindepth is defined as the depth at which the amplitude of the wave has been reduced by :math:`1/e`.

From Equation :eq:`wn1`, it is seen that :math:`\beta`, and hence :math:`\delta`, are dependent upon the ratios of physical properties and frequency.

.. _frequency_domain_plane_wave_sources_phase_velocity:

Phase Velocity
--------------

The complex sinusoidal term :math:`e^{-i(\alpha z - \omega t)}` in Equation :eq:`wn2` represents a travelling wave. The phase velocity is expressed as:

.. math:: v_{phase} = \frac{\omega}{\alpha}.

Note that the phase velocity is frequency dependent (i.e. dispersive) even if all of the physical properties: :math:`\sigma`, :math:`\epsilon`, and :math:`\mu` are real-valued.

.. _frequency_domain_plane_wave_sources_wavelength:

Wavelength
----------

Finally, the wavelength of the waves is given by:

.. math:: \lambda = \frac{v}{f} = \frac{\omega}{\alpha f} = \frac{2\pi}{\alpha}.

.. .. figure:: images/planewaveprop.PNG

..         :figwidth: 20%
..         :align: right
..         :name: pwp

..         A plane harmonic wave propagates into the earth.
