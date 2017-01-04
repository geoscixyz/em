.. _frequency_domain_plane_wave_sources_analytic_solution:

Analytic Solution
=================

.. purpose::

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

.. math:: \mathbf{e} (z,t) \equiv \mathbf{e} = \mathbf{e}_0^+ e^{-\beta z} e^{-i(\alpha z - \omega t)} + \mathbf{e}_0^- e^{\beta z} e^{i(\alpha z + \omega t)}.
    :name: fd4

We begin by considering the first part of this equation. The term :math:`e^{-i(\alpha z - \omega t)}` represents a wave travelling in the positive z-direction. The phase velocity of the wave is :math:`v_{phase} = \omega/\alpha`. The initial amplitude of the wave is :math:`\mathbf{e}_0^+` and the term :math:`e^{-\beta z}` indicates that the amplitude decreases exponentially with :math:`z`. Thus in homogeneous media, the electromagnetic fields can propagate as plane waves in which their amplitude exponentially decreases with distance. The second part in Equation :eq:`fd4` is understood in the same manner except that the wave is travelling in the opposite direction (negative z-direction) and the initial amplitude is :math:`\mathbf{e}_0^-`.

General solutions of the 1D Helmholtz equations generally require waves travelling in the positive and negative z-directions.

The magnetic field will also travel in the x-y plane but is perpendiculat to :math:`\mathbf{e}`. Similarly, solution of the magnetic field can be written as

.. math:: \mathbf{h} (z,t) \equiv \mathbf{h} = \mathbf{h}_0^+ e^{-\beta z} e^{-i(\alpha z - \omega t)} + \mathbf{h}_0^- e^{\beta z} e^{i(\alpha z + \omega t)}.
    :name: fd5

.. We can investigate the plane wave propagation more fully by looking more closely at the mathematics and using an interactive app.
.. ..todo :: add app




.. _frequency_domain_plane_wave_sources_fundamental_physics:

Fundamental physics
-------------------

EM wave propagation can be described by some parameters including: wavenumber, skin depth, phase velocity, and wave length. In addition, two important regimes of the EM wave propagation can be made depending upon the relative amplitude between :math:`\epsilon \omega` and :math:`\sigma`:

- :math:`\epsilon \omega \ll \sigma` : "Quasi-static" approximation
- :math:`\epsilon \omega \gg \sigma` : "Wave" approximation

Those two regimes are fundamental bases of geophysical applications using EM. EM induction, and GPR are correspondingly based upon "Quasi-static", and "Wave" approximation. In each regime, EM wave propagtaion shows distinctively different physical behavior. Thus, by working through imporant concepts on EM wave propagation: wave number, skin depth, phase velocity, and wave length, we understand different features of the EM wave propagation in each regime.

.. _frequency_domain_plane_wave_sources_wavenumber:

Wavenumber
^^^^^^^^^^

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

Wavenumber with each approximation can be:

- Quasi-static regime: :math:`k = \sqrt{- i \mu \sigma \omega}`
- Wave regime: :math:`k = \sqrt{\mu \epsilon \omega^2} = \omega \sqrt{\mu \epsilon}`

Note that in quasi-static regime, :math:`k` is complex-valued, but in wave regime it is real-valued.

Similarly, :math:`\alpha` and :math:`\beta` in each regime can be:

- Quasi-static regime:

.. math::
    \alpha = \beta = \left ( \frac{\omega \mu \sigma}{2} \right ) ^{1/2}
    :name: wn4

- Wave regime:

.. math::
    \alpha = k = \omega \sqrt{\mu \epsilon}, \ \beta = 0
    :name: wn5

In wave regime, :math:`\beta` is zero hence the wave does not decay with :math:`z`.

.. _frequency_domain_plane_wave_sources_skindepth:

Skin Depth
^^^^^^^^^^

The skin depth :math:`\delta` is the distance the wave travels for its amplitude to have decayed by a factor of :math:`1/e`. Thus

.. math:: \delta = \frac{1}{\beta}.

:numref:`sd` illustrates the concept of skin depth.

.. figure:: ../images/skindepth.png
        :figwidth: 50%
        :align: right
        :name: sd

        Skindepth is defined as the depth at which the amplitude of the wave has been reduced by :math:`1/e`.

From Equation :eq:`wn1`, it is seen that :math:`\beta`, and hence :math:`\delta`, are dependent upon the ratios of physical properties and frequency. For a general case skin depth can be considered as fairly complicated function. However, in quasi-static regime, :math:`\beta` can be simplified and the skin depth can be simplified as

.. math:: \delta = \frac{1}{\beta} = \sqrt{\frac{2}{\omega \mu \sigma}}.

Assuming permeability of free space, :math:`\mu_0 = 4\pi \times 10^{-7}` H/m, and writing :math:`\omega=2\pi f`, we obtain the following useful equation for :math:`\delta` in meters:

.. math:: \delta \approx 503 \sqrt{\frac{1}{f \sigma}} = 503 \sqrt{\frac{\rho}{f}}.

For problems involving high frequencies, for example GPR surveys, or very early time transient EM problems, the displacement current may be important (:math:`\epsilon \omega \simeq \sigma`). Then Equation :eq:`wn1` needs to be invoked.

To see how physical properties and frequencies affect skin depth, check out

.. todo:: NEED Seogi's APP LINK

The following table shows skin depths for some representative rocks and frequencies:

+---------------------+----------------+------------------+----------+------------+--------------+
|                     | Resistivity    | Conductivity     | f = 1 Hz | f = 100 Hz | f = 1,000 Hz |
|                     | :math:`\rho`   | :math:`\sigma`   |          |            |              |
+---------------------+----------------+------------------+----------+------------+--------------+
| Magmatic rocks      | 10,000         | 0.0001           | 50,000 m | 5,000 m    | 1,581 m      |
+---------------------+----------------+------------------+----------+------------+--------------+
| Metamorphic rocks,  |                |                  | 15,811 m | 1,581 m    | 500 m        |
| limestone           | 1,000          | 0.001            |          |            |              |
+---------------------+----------------+------------------+----------+------------+--------------+
| Sediments           | 100            | 0.01             | 5,000 m  | 500 m      | 158 m        |
+---------------------+----------------+------------------+----------+------------+--------------+
| Sea water           | 0.3            | 3.3              | 274 m    | 27 m       | 9 m          |
+---------------------+----------------+------------------+----------+------------+--------------+
| Suphides, graphite  | 0.01           | 100              | 50 m     | 5 m        | 2 m          |
+---------------------+----------------+------------------+----------+------------+--------------+

.. _frequency_domain_plane_wave_sources_phasevelocity:

Phase Velocity
^^^^^^^^^^^^^^

The complex sinusoidal term :math:`e^{-i(\alpha z - \omega t)}` in Equation :eq:`wn2` represents a travelling wave. The phase velocity is expressed as:

.. math:: v_{phase} = \frac{\omega}{\alpha}.

In quasi-static regime, :math:`\alpha` is given by Equation :eq:`wn4` and the plane wave velocity becomes

.. math:: v_{phase} = \sqrt{ \frac{2\omega}{\mu \sigma} },

so velocity increases with frequency but they travel more slowly in conductive permeable media. The velocity of the EM wave will be different at different frequency, and this often called "dispersive".

Alternatively, in wave regime ( :math:`\epsilon \omega \gg \sigma` ), from :eq:`wn5`, we obtain

.. math:: v_{phase} = \frac{1}{\sqrt{\mu \epsilon}}.
        :name: wn3

In free space, Equation :eq:`wn3` equates to :math:`3\times 10^8` m/s, which is the speed of light. Different from quasi-static case, the phase velocity is independent on frequency.

.. _frequency_domain_plane_wave_sources_wavelength:

Wavelength
^^^^^^^^^^

.. figure:: ../images/planewaveprop.PNG
        :figwidth: 20%
        :align: right
        :name: pwp

        A plane harmonic wave propagates into the earth.

Finally, the wavelength of the waves is given by:

.. math:: \lambda = \frac{v}{f} = \frac{\omega}{\alpha f} = \frac{2\pi}{\alpha}.

In quasi-static regime, wavelength is dispersive, that is wavelength varies with frequency, but in wave regime it is independent on frequency. For instance, in free space, :math:`\lambda = \frac{3\times10^8}{f}`. In a conducting medium, if the quasi-static approximation is valid, then :math:`\alpha = \beta = 1/\delta` and so :math:`\lambda = 2\pi \delta`.

Thus even though the waves have a sinusoidal description inside the earth, they have lost most of their amplitude by the time they have propagated one wavelength into the earth. The above elements are illustrated in :numref:`pwp` where a plane harmonic wave in free space propagates into the earth.

