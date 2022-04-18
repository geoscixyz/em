.. _harmonic_planewaves_homogeneous_skindepth:

Attenuation and Skin Depth
==========================

.. figure:: images/skindepth.png
        :figwidth: 50%
        :align: right
        :name: sd

        Skindepth is defined as the depth at which the amplitude of the wave has been reduced by :math:`1/e`.

Attenuation
-----------

Attenuation defines the rate of amplitude loss an EM wave experiences at it propagates (:numref:`sd`). The attenuation of an EM wave is defined by the parameter :math:`\beta`. For a downgoing planewave, the attenuation formula is given by:

.. _harmonic_planewaves_homogeneous_attenuation_formula:

.. math::
	A(z) = A_0 e^{-\beta z}

where absolute :math:`A` is the amplitude, :math:`A_0` is the absolute amplitude at :math:`z` = 0 m and:

.. math::
	\beta = \omega \left ( \frac{\mu\epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right)^{1/2} - 1 \right ] \right ) ^{1/2} \geq 0

Skin Depth
----------

Skin depth defines the distance a wave must travel before its amplitude has decayed by a factor of :math:`1/e`. The skin depth is the reciprocal of the decay constant :math:`\beta`. Thus:

.. _harmonic_planewaves_homogeneous_skindepth_formula:

.. math:: \delta = \frac{1}{\beta} = \frac{1}{\omega} \left ( \frac{\mu\epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right)^{1/2} - 1 \right ] \right ) ^{1/2}

Since :math:`\beta` depends on the frequency and the physical properties of the media, so does the skin depth. For a general case, the skin depth can be considered a fairly complicated function. However, approxmations exist in the quasi-static and wave regimes.

Skin Depth for Various Materials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below shows skin depths for certain rocks at various frequencies. This is meant to serve as a general guide, as rock types are classified by a range of physical properties values which can lead to order of magnitude differences in skin depth.

+-----------------+-------------------+-------------+------------------+--------------------+---------------------+---------------------+---------------------+
|Type             |:math:`\sigma`     |:math:`\mu_r`|:math:`\epsilon_r`|:math:`\delta` (1Hz)|:math:`\delta` (1kHz)|:math:`\delta` (1MHz)|:math:`\delta` (1GHz)|
+=================+===================+=============+==================+====================+=====================+=====================+=====================+
|Air              | 0 S/m             | 1           | 1                |:math:`\infty`      | :math:`\infty`      |:math:`\infty`       |:math:`\infty`       |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+---------------------+---------------------+
|Sea Water        | 3.3 S/m           | 1           | 80               | 277 m              | 8.76 m              | 0.277 m             | 0.015 m             |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+---------------------+---------------------+
|Igneous          |:math:`10^{-4}` S/m| 1           | 5                | 50,300 m           | 1,590 m             | 121 m               | 119 m               |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+---------------------+---------------------+
|Sedimentary (dry)|:math:`10^{-3}` S/m| 1           | 4                | 15,900 m           | 500 m               | 18 m                | 11 m                |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+---------------------+---------------------+
|Sedimentary (wet)|:math:`10^{-2}` S/m| 1           | 25               | 5,000 m            | 160 m               | 5.4 m               | 2.6 m               |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+---------------------+---------------------+
|Sulphide Skarn   |:math:`10^{2}` S/m | 1           | 5                | 50 m               | 1.6 m               | 0.05 m              | 0.002 m             |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+---------------------+---------------------+
|Magnetite Skarn  |:math:`10^{2}` S/m | 2           | 5                | 36 m               | 1.1 m               | 0.04 m              | 0.001 m             |
+-----------------+-------------------+-------------+------------------+--------------------+---------------------+---------------------+---------------------+


Approximations
^^^^^^^^^^^^^^

.. _harmonic_planewaves_homogeneous_skindepth_formula_quasi:

**Quasi-Static Approximation**

In the quasi-static regime (:math:`\epsilon\omega \ll \sigma`), the skin depth is approximately equal to:

.. math:: \delta = \frac{1}{\beta} = \sqrt{\frac{2}{\omega \mu \sigma}}.

Assuming the Earth is non-magnetic (:math:`\mu = \mu_0 = 4\pi \times 10^{-7}` H/m) and replacing :math:`\omega=2\pi f`, a simpler form of the skin depth is given by:

.. math:: \delta \approx 503 \sqrt{\frac{1}{f \sigma}} = 503 \sqrt{\frac{\rho}{f}}.

where :math:`\rho = 1/\sigma` is the resistivity. Thus from the previous two equations, we see that the skin depth decreases as the conductivity :math:`\sigma`, magnetic permeability :math:`\mu` and frequency :math:`\omega` increase. In most cases however, the magnetic properties are negligible as :math:`\mu \sim \mu_0`. 

**Wave-Regime Approximation**

In the wave regime (:math:`\epsilon\omega \gg \sigma`), the skin depth is approximately equal to:

.. math:: \delta = \frac{1}{\beta} = \frac{2}{\sigma} \sqrt{\frac{\epsilon}{\mu}}

Assuming the Earth is non-magnetic (:math:`\mu = \mu_0 = 4\pi \times 10^{-7}` H/m) and by using the :ref:`relative permittivity<dielectric_permittivity_index>` :math:`\epsilon_r = \epsilon/\epsilon_0`, a simpler form of the skin depth is given by:

.. math:: \delta \approx 0.0053 \frac{\sqrt{\epsilon_r}}{\sigma}

Thus from the previous two equations, we see that the skin depth decreases proportional :math:`\sqrt{\epsilon_r}/\sigma`; provided the magnetic properties are negligible (:math:`\mu \sim \mu_0`). The below shows skin depths for some representative rocks and frequencies in the wave regime. To see how physical properties and frequencies affect skin depth, check out the app.





