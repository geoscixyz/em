.. _harmonic_planewaves_homogeneous_phasevelocity:

Phase Velocity
==============

Phase velocity defines the speed at which waves oscillating at a particular frequency propagate. Like the :ref:`wavelength<harmonic_planewaves_homogeneous_wavelength>`, the phase velocity depends on the real component of the :ref:`wavenumber<harmonic_planewaves_homogeneous_wavenumber>` (:math:`\alpha`) and is given by:

.. math:: v_{ph} = \frac{\omega}{\alpha} = \left ( \frac{\mu \epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right )^{1/2} + 1 \right ] \right )^{-1/2}

Phase Velocity for Various Materials
------------------------------------

The table below shows phase velocity for certain rocks at various frequencies. This is meant to serve as a general guide, as rock types are classified by a range of physical properties values which can lead to order of magnitude differences in phase velocity.

+-----------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Type             |:math:`\sigma`     |:math:`\mu_r`|:math:`\epsilon_r`|:math:`v_{ph}` (1Hz) |:math:`v_{ph}` (1kHz) |:math:`v_{ph}` (1MHz) |:math:`v_{ph}` (1GHz) |
+=================+===================+=============+==================+=====================+======================+======================+======================+
|Air              | 0 S/m             | 1           | 1                | 299.8 m/us          | 299.8 m/us           | 299.8 m/us           | 299.8 m/us           |
+-----------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Sea Water        | 3.3 S/m           | 1           | 80               | 0.0017 m/us         | 0.055 m/us           | 1.7 m/us             | 32 m/us              |
+-----------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Igneous          |:math:`10^{-4}` S/m| 1           | 5                | 0.32 m/us           | 10 m/us              | 132 m/us             | 134 m/us             |
+-----------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Sedimentary (dry)|:math:`10^{-3}` S/m| 1           | 4                | 0.1 m/us            | 3.2 m/us             | 90 m/us              | 150 m/us             |
+-----------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Sedimentary (wet)|:math:`10^{-2}` S/m| 1           | 25               | 0.032 m/us          | 1 m/us               | 30 m/us              | 60 m/us              |
+-----------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Sulphide Skarn   |:math:`10^{2}` S/m | 1           | 5                | 0.00032 m/us        | 0.01 m/us            | 0.32 m/us            | 10 m/us              |
+-----------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Magnetite Skarn  |:math:`10^{2}` S/m | 2           | 5                | 0.00022 m/us        | 0.007 m/us           | 0.22 m/us            | 7 m/us               |
+-----------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+


Approximations
--------------

.. _harmonic_planewaves_homogeneous_phasevelocity_quasi:

Quasi-Static Approximation
^^^^^^^^^^^^^^^^^^^^^^^^^^

In the quasi-static regime (:math:`\epsilon\omega \ll \sigma`), the phase velocity simplifies to:

.. math:: v_{ph} = \sqrt{ \frac{2\omega}{\mu \sigma} }

Thus the phase velocity is faster to waves which oscillate at higher frequencies. EM waves also move slower in media that a conductive and highly permeable.

Wave Regime Approximation
^^^^^^^^^^^^^^^^^^^^^^^^^

In the wave regime ( :math:`\epsilon \omega \gg \sigma` ), the phase velocity simplifies to:

.. math:: v_{ph} = \frac{1}{\sqrt{\mu \epsilon}}
        :name: wn3

Thus at sufficiently high frequencies, waves at all frequencies propagate as the same speed. In free space, the previous equations simplifies to :math:`1/ \! \sqrt{\mu_0\epsilon_0} = 3\times 10^8` m/s, which is the speed of light.

Relating Wavelength and Phase Velocity
--------------------------------------

As we have shown, both the :ref:`wavelength<harmonic_planewaves_homogeneous_wavelength>` and phase velocity can be defined in terms of the real component of the :ref:`wavenumber<harmonic_planewaves_homogeneous_wavenumber>` (:math:`\alpha`). As a result, we can define a mathematical relationship when relates the wavelength and phase velocity at a given frequency. This relationship is given by:

.. math::
	\lambda = \frac{2\pi v_{ph}}{\omega} = \frac{v_{ph}}{f}

where :math:`f` is the frequency of oscillation in Hz. From this expression, we can see that EM waves which propagate faster through the Earth correspond to longer wavelengths.





