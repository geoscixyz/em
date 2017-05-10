.. _harmonic_planewaves_homogeneous_attenuation:

Attenuation
===========

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



