.. _waves_freq_domain:

Wave equations in the frequency domain
======================================

To get the frequency-domain wave equations, we use the Fourier transform using an :math:`e^{i\omega t}` time dependence. If we look at the derivative of :math:`e^{i\omega t}` with respect to time, we see that it is :math:`i\omega e^{i\omega t}`. Thus, we can easily convert the :ref:`time-domain wave equations <wave_equations_time_domain>` to the frequency-domain by replacing :math:`\partial/\partial t` with :math:`i \omega` and  :math:`\partial^2/\partial t^2` with :math:`-\omega^2`. The frequency-domain equations are then expressed as:

.. math::  \boldsymbol{\nabla}^2 \mathbf{E} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{E}  = 0
        :name: hme8

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{H}  = 0
        :name: hmh8

Equations :eq:`hme8` and :eq:`hmh8` can be be written in a simpler form:

.. math:: \boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  = 0

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  = 0

where :math:`k` is the :ref:`wave number <wave_number>`. These equations are referred to as the vector Helmholtz equations. In a homogeneous medium, they support plane wave solutions. The electric and magnetic fields lie in a (x, y) plane and the wave propagates perpendicular to the plane (in the z-direction), as shown in FIGURE ???.

With this geometry, the governing equation for the electric field in 1D is:

.. math:: \frac{\partial^2 \mathbf{E}}{\partial z^2} + k^2 \mathbf{E},

where :math:`\mathbf{E} \equiv \mathbf{E}(z,\omega)`. This has a solution as following:

.. math:: \mathbf{E} = \mathbf{E}_0 e^{\pm ikz},
        :name: fd1

where :math:`k = (\mu \epsilon \omega - i\mu\sigma\omega)^2` is the complex :ref:`wave number <wave_number>` and :math:`\mathbf{E}_0` is the amplitude. Writing the wave number as :math:`k = k_R + ik_I` and substituting into Equation :eq:`fd1` yields:

.. math:: \mathbf{E} = \mathbf{E}_0 e^{\pm i(k_R +ik_I)z},

which has two terms. The first, :math:`e^{\pm ik_Rz}` is a complex exponential while the second term, :math:`e^{\pm k_Iz}` is a real exponential and shows how the amplitude varies with :math:`z`. Together they define a propagating harmonic wave that decays as it travels!

To add clarity, and keep with notation that is typically used, we do the following:

(i). Explicitly include the time dependence :math:`e^{i\omega t}`

(ii). Write :math:`k = \alpha + i\beta` :cite:`ward1988`

Then we can write the propagating harmonic wave as following:

.. math:: \mathbf{e} (z,t) \equiv \mathbf{e} = \mathbf{e}_0^+ e^{-\beta z} e^{-i(\alpha z - \omega t)} + \mathbf{e}_0^- e^{-\beta z} e^{-i(\alpha z + \omega t)}.
        :name: fd2

Consider the first part of this equation. The term :math:`e^{-i(\alpha z - \omega t)}` represents a wave travelling in the positive z-direction. The phase velocity of the wave is :math:`v_{phase} = \omega/\alpha`. The initial amplitude of the wave is :math:`\mathbf{e}_0` and the term :math:`e^{-\beta z}` indicates that the amplitude decreases exponentially with depth.

Thus in homogeneous media, the electromagnetic fields can propagate as plane waves in which their amplitude exponentially decreases with distance. The second part in Equation :eq:`fd2` is understood in the same manner except that the wave is travelling in the opposite direction (negative z-direction).

Remark: For problems involving a layered earth, the decomposition in Equation :eq:`fd2` refers to downward and upward propagating plane waves.

Remark: The above analysis has concentrated upon the electric field but identical statements hold for the magnetic field. That is:

.. math:: \mathbf{h} (z,t) \equiv \mathbf{h} = \mathbf{h}_0^+ e^{-\beta z} e^{-i(\alpha z - \omega t)} + \mathbf{h}_0^- e^{-\beta z} e^{-i(\alpha z + \omega t)}.

