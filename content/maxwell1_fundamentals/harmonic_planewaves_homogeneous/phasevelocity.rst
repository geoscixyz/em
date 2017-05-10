.. _harmonic_planewaves_homogeneous_phasevelocity:

Phase Velocity
==============

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
