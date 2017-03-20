.. _frequency_domain_plane_wave_sources_analytic_solution:

Analytic Solution (Frequency Domain)
====================================

.. purpose::

    Here, we provide analytic solutions for the Helmholtz equation for plane waves within a homogeneous medium. From the solutions, we extract and discuss meaningful physical principles such as: :ref:`wavenumber<frequency_domain_plane_wave_sources_wavenumber>`, :ref:`skin depth<frequency_domain_plane_wave_sources_skindepth>`, :ref:`phase velocity<frequency_domain_plane_wave_sources_phasevelocity>`, and :ref:`wavelength<frequency_domain_plane_wave_sources_wavelength>`.


.. figure:: ../images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_frequency

   Geometry of an EM plane wave propagating downwards.

To characterize EM waves within a homogeneous medium, let us begin with the following vector Helmholtz equations for :math:`\mathbf{E}` and :math:`\mathbf{H}`:

.. math::
    \boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  &= 0\\
    \boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  &= 0
    :name: Helmholtz_full_analytic

where the complex :ref:`wavenumber<frequency_domain_plane_wave_sources_wavenumber>` is given by:

.. math::
    k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}
    :name: Helmholtz_complex_wavenumber

For simplicity, let us assume that the electric and magnetic fields lie in the xy-plane and that the wave propagates perpendicular to that plane (in the z-direction); see :numref:`planewavedown_frequency`. With this geometry, the governing equation for the electric field simplifies to:

.. math::
    \frac{\partial^2 \mathbf{E}}{\partial z^2} + k^2 \mathbf{E} = 0
    :name: Helmholtz_1D_analytic

where :math:`\mathbf{E} \equiv \mathbf{E}(z,\omega)`; thus it does not depend on :math:`x` or :math:`y`. The previous equation has a general solution of the form:

.. math::
    \mathbf{E} = \mathbf{E}_0^- \, e^{i(kz-\omega t)} + \mathbf{E}_0^+ \, e^{-i(kz + \omega t)}
    :name: Helmholtz_1D_solution

where :math:`\mathbf{E}_0^-` and :math:`\mathbf{E}_0^+` are the amplitudes of down-going and up-going waves, respectively. The :math:`e^{-i\omega t}` in both terms controls the temporal phase. The complex wavenumber has both real and imaginary components, thus it is commonly expressed as:

.. math::
    k = \alpha - i\beta
    :name: wavenumber_split

where :math:`\alpha` and :math:`\beta` depend on the frequency and physical properties of the media. Substituting Eq. :eq:`wavenumber_split` into Eq. :eq:`Helmholtz_1D_solution`, the solution to our wave equation for :math:`\mathbf{E}` becomes:

.. math::
    \mathbf{E} = \mathbf{E}_0^- \, e^{\beta z} e^{i(\alpha z -\omega t)} + \mathbf{E}_0^+ \, e^{-\beta z} e^{-i (\alpha z + \omega t)} 
    :name: Helmholtz_1D_components

For both the down-going and up-going waves, there are two important behaviours within the solution. The first term, which contains :math:`e^{\pm i \alpha z}`, controls the oscillatory behaviour of each wave. The second term, which contains :math:`e^{\pm \beta z}`, controls the decay behaviour of each wave. Notice that as :math:`z \rightarrow -\infty` for the down-going wave, its amplitude goes to zero. The same behaviour occurs for the up-going wave as :math:`z \rightarrow \infty`.

Using the same approach, the magnetic field has a general solution of the form:

.. math::
    \mathbf{H} &= \mathbf{H}_0^- \, e^{i(kz-\omega t)} + \mathbf{H}_0^+ \, e^{-i(kz+\omega t)}\\
    &= \mathbf{H}_0^- \, e^{\beta z} e^{i(\alpha z-\omega t)} + \mathbf{H}_0^+ \, e^{-\beta z} e^{-i (\alpha z+\omega t)}
    :name: Helmholtz_1D_h

.. note::

    Eq. :eq:`Helmholtz_1D_components` is still a general solution. To determine :math:`\mathbf{E}_0^-` and :math:`\mathbf{E}_0^+`, you must envoke a set of boundary conditions. For example, :math:`\mathbf{E}(z \rightarrow -\infty,\omega) = 0` and :math:`\mathbf{E}(z =0,\omega) = \mathbf{E}_0`. This would give you a solution :math:`\mathbf{E}(z,\omega) = \mathbf{E}_0 \, e^{\beta z} e^{ i(\alpha z-\omega t)}` (i.e. just the down-going wave). From this solution, :math:`\mathbf{H}(z,\omega)` can be determined using Faraday's law. You could also envoke boundary conditions to solve for :math:`\mathbf{H}` and use the Ampere-Maxwell law to obtain :math:`\mathbf{E}`.

.. _frequency_domain_plane_wave_sources_fundamental_physics:

Fundamental physics
-------------------

EM wave propagation can be described using the following parameters: wavenumber, skin depth, phase velocity, and wave length. These properties are discussed below. In addition, two important regimes exist for EM wave propagation. These regimes depend on the relative magnitudes of :math:`\epsilon \omega` and :math:`\sigma`, where:

- :math:`\epsilon \omega \ll \sigma` : "Quasi-static" regime
- :math:`\epsilon \omega \gg \sigma` : "Wave" regime

These two regimes are fundamental bases of geophysical applications using EM. EM induction, and GPR are correspondingly based upon "Quasi-static", and "Wave" approximation. In each regime, EM wave propagtaion shows distinctively different physical behavior. Thus, by working through imporant concepts on EM wave propagation: wave number, skin depth, phase velocity, and wave length, we understand different features of the EM wave propagation in each regime.

.. _frequency_domain_plane_wave_sources_wavenumber:

Wavenumber
^^^^^^^^^^

The wavenumber characterizes all properties of electromagnetic waves described by the Helmholtz equation. Recall that the wave number :math:`k` is given by:

.. math:: k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}.

and that it may be decomposed into real and imaginary components such that:

.. math:: k = \alpha - i \beta

According to :cite:`stratton1941,ward1988`, :math:`\alpha` and :math:`\beta` depend on the frequency and the physics properties of the media, where:

.. math:: \alpha = \omega \left ( \frac{\mu \epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right )^{1/2} + 1 \right ] \right )^{1/2} \geq 0

.. math:: \beta = \omega \left ( \frac{\mu\epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right)^{1/2} - 1 \right ] \right ) ^{1/2} \geq 0

Let us now examine a wave travelling in the negative z-direction with the following form:

.. math::
    \mathbf{E} = \mathbf{E}_0^- \, e^{\beta z}e^{i(\alpha z-\omega t)}
    :name: E_downgoing

As we already discussed during our derivation, :math:`\beta` controls the rate of decay with respect to :math:`z`. And :math:`\alpha` controls the oscillatory behaviour.



**Quasi-Static Regime:**

In the quasi-static regime (:math:`\epsilon\omega \ll \sigma`), the wavenumber simplifies to:

.. math::
    k \approx \sqrt{- i \mu \sigma \omega}

where it can be shown that:

.. math::
    \alpha = \beta = \left ( \frac{\omega \mu \sigma}{2} \right ) ^{1/2}

In this case, the waves oscillate and decay as they propagate.

**Wave Regime:**

In the wave regime (:math:`\epsilon\omega \gg \sigma`), the wavenumber simplifies to:

.. math::
    k \approx \alpha = \sqrt{\mu \epsilon \omega^2} = \omega \sqrt{\mu \epsilon}

and

.. math::
    \beta \approx \frac{\sigma}{2} \sqrt{\frac{\mu}{\epsilon}} \sim 0

For a perfect wave equation, :math:`\beta = 0` and the waves do not decay in amplitude as they propagate. In geophysical problems (:ref:`ground-penetrating radar<gpr_index>` for example), signals still experience amplitude loss as they propagate through the Earth.


.. _frequency_domain_plane_wave_sources_skindepth:

Attenuation and Skin Depth
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../images/skindepth.png
        :figwidth: 50%
        :align: right
        :name: sd

        Skindepth is defined as the depth at which the amplitude of the wave has been reduced by :math:`1/e`.

**Attenuation** defines the rate of amplitude loss an EM wave experiences at it propagates. The attenuation of an EM wave depends on the parameter :math:`\beta`. The **skin depth** :math:`\delta` defines the distance a wave must travel before its amplitude has decayed by a factor of :math:`1/e`. This is illustrated in :numref:`sd`. As it turns out, the skin depth is the reciprocal of the decay constant :math:`\beta`. Thus:

.. math:: \delta = \frac{1}{\beta}.

Since :math:`\beta` depends on the frequency and the physical properties of the media, so does the skin depth. For a general case, the skin depth can be considered a fairly complicated function. However, approxmations exist in the quasi-static and wave regimes.

**Quasi-static**

In the quasi-static regime (:math:`\epsilon\omega \ll \sigma`), the skin depth is approximately equal to:

.. math:: \delta = \frac{1}{\beta} = \sqrt{\frac{2}{\omega \mu \sigma}}.

Assuming the Earth is non-magnetic (:math:`\mu = \mu_0 = 4\pi \times 10^{-7}` H/m) and replacing :math:`\omega=2\pi f`, a simpler form of the skin depth is given by:

.. math:: \delta \approx 503 \sqrt{\frac{1}{f \sigma}} = 503 \sqrt{\frac{\rho}{f}}.

where :math:`\rho = 1/\sigma` is the resistivity. Thus from the previous two equations, we see that the skin depth decreases as the conductivity :math:`\sigma`, magnetic permeability :math:`\mu` and frequency :math:`\omega` increase. In most cases however, the magnetic properties are negligible as :math:`\mu \sim \mu_0`. 

**Wave Regime:**

In the wave regime (:math:`\epsilon\omega \gg \sigma`), the skin depth is approximately equal to:

.. math:: \delta = \frac{1}{\beta} = \frac{2}{\sigma} \sqrt{\frac{\epsilon}{\mu}}

Assuming the Earth is non-magnetic (:math:`\mu = \mu_0 = 4\pi \times 10^{-7}` H/m) and by using the :ref:`relative permittivity<dielectric_permittivity_index>` :math:`\epsilon_r = \epsilon/\epsilon_0`, a simpler form of the skin depth is given by:

.. math:: \delta \approx 0.0053 \frac{\sqrt{\epsilon_r}}{\sigma}

Thus from the previous two equations, we see that the skin depth decreases proportional :math:`\sqrt{\epsilon_r}/\sigma`; provided the magnetic properties are negligible (:math:`\mu \sim \mu_0`). The below shows skin depths for some representative rocks and frequencies in the wave regime. To see how physical properties and frequencies affect skin depth, check out the app.

The table below shows skin depths for certain rocks at various frequencies. This is meant to serve as a general guide, as rock types are classified by a range of physical properties values.

+-----------------+-------------------+-------------+------------------+--------------------+---------------------+----------------------+---------------------+
|Type             |:math:`\sigma`     |:math:`\mu_r`|:math:`\epsilon_r`|:math:`\delta` (1Hz)|:math:`\delta` (1kHz)|:math:`\delta` (10kHz)|:math:`\delta` (1GHz)|
+=================+===================+=============+==================+====================+=====================+======================+=====================+
|Air              | 0 S/m             | 1           | 1                |:math:`\infty`      | :math:`\infty`      |:math:`\infty`        |:math:`\infty`       |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+----------------------+---------------------+
|Sea Water        | 3.3 S/m           | 1           | 80               |31 m                |  1 m                | 0.3 m                | 0.001 m             |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+----------------------+---------------------+
|Igneous          |:math:`10^{-4}` S/m| 1           | 5                |22,500 m            |710 m                | 225 m                | 17 m                |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+----------------------+---------------------+
|Sedimentary (dry)|:math:`10^{-4}` S/m| 1           | 4                |25,200 m            |800 m                | 250 m                | 17 m                |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+----------------------+---------------------+
|Sedimentary (wet)|:math:`10^{-2}` S/m| 1           | 25               |1,000 m             |32 m                 | 10m                  | 0.17 m              |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+----------------------+---------------------+
|Sulphide Skarn   |:math:`10^{2}` S/m | 1           | 5                |22.5 m              | 0.7 m               | 0.23 m               | 0.0007 m            |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+----------------------+---------------------+
|Magnetite Skarn  |:math:`10^{2}` S/m | 2           | 5                |22.5 m              | 0.7 m               | 0.23 m               | 0.0007 m            |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+----------------------+---------------------+






.. _frequency_domain_plane_wave_sources_phasevelocity:

Phase Velocity
^^^^^^^^^^^^^^

Phase velocity defines the speed at which waves oscillating at a particular frequency propagate. Where the complex sinusoidal term :math:`e^{i(\alpha z - \omega t)}` in Eq. :eq:`E_downgoing` represents a travelling wave, the corresponding phase velocity is given by:

.. math:: v_{phase} = \frac{\omega}{\alpha}

**Quasi-Static Regime:**

In quasi-static regime (:math:`\epsilon\omega \ll \sigma`), the phase velocity simplifies to:

.. math:: v_{phase} = \sqrt{ \frac{2\omega}{\mu \sigma} }

Thus the phase velocity is faster to waves which oscillate at higher frequencies. EM waves also move slower in media that a conductive and highly permeable.

**Wave Regime:**

In the wave regime ( :math:`\epsilon \omega \gg \sigma` ), the phase velocity simplifies to:

.. math:: v_{phase} = \frac{1}{\sqrt{\mu \epsilon}}
        :name: wn3

Thus at sufficiently high frequencies, waves at all frequencies propagate as the same speed. In free space, the previous equations simplifies to :math:`1/ \! \sqrt{\mu_0\epsilon_0} = 3\times 10^8` m/s, which is the speed of light.

.. _frequency_domain_plane_wave_sources_wavelength:

Wavelength
^^^^^^^^^^

.. figure:: ../images/planewaveprop.PNG
        :figwidth: 20%
        :align: right
        :name: pwp

        A plane harmonic wave propagates into the earth.

Wavelength refers to the physical distance a wave travels during a single oscillation. For EM waves, the wavelength is given by:

.. math:: \lambda = \frac{2\pi}{\alpha} = \frac{2\pi v}{\omega} = \frac{v}{f} 

As we can see, higher frequency waves correspond to shorter wavelengths.

**Quasi-Static:**

In quasi-static regime (:math:`\epsilon\omega \ll \sigma`), the wavelength simplifies to:

.. math:: \lambda = \sqrt{ \frac{2}{\omega \mu \sigma} }

Notice that in this case, the wavelength is actually equal to the skin depth.

**Wave Regime:**

In the wave regime ( :math:`\epsilon \omega \gg \sigma` ), the wavelength simplifies to:

.. math:: \lambda = \frac{1}{\omega \sqrt{\mu \epsilon}}

