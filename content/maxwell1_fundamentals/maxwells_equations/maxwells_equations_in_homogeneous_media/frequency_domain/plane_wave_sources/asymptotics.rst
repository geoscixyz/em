.. _frequency_domain_planewave_sources_asymptotics:

Asymptotic Solution
===================

.. topic:: Purpose

    With some assumptions, full plane EM wave solutions can be simplified. Different types of EM geophysical methods fundamentally based upon different assumptions (e.g. DC, GPR, and EM induction methods). Here we recognize those assumptions and with them revisit concepts of wavenumber, skin depth, phase velocity, and wave length.

We consider three canonical situations where:

- :math:`\omega \approx 0`: "DC" approximation
- :math:`\epsilon \omega \ll \sigma` : "Quasi-static" approximation
- :math:`\epsilon \omega \gg \sigma` : "Wave" approximation

Those three regimes are fundamental bases of geophysical applications using EM. DC resistivity, EM induction, and GPR are correspondingly based upon "DC", "Quasi-static", and "Wave" approximation. In each regime, EM wave propagtaion shows distinctively different physical behavior. Thus, by revisiting imporant concepts on EM wave propagation: wave number, skin depth, phase velocity, and wave length, we understand different features of the EM propagation in each regime.

Skin depth
----------

For many geophysical surveys, we have :math:`\epsilon \omega \ll \sigma` and :math:`k` is well-approximated as:

.. math:: k = \sqrt{-i\omega \mu \sigma}.

So

.. math:: \alpha = \beta = \left ( \frac{\omega \mu \sigma}{2} \right ) ^{1/2}.
        :name: wn4

Thus the skin depth becomes:

.. math:: \delta = \frac{1}{\beta} = \sqrt{\frac{2}{\omega \mu \sigma}}.

Assuming permeability of free space, :math:`\mu_0 = 4\pi \times 10^{-7}` H/m, and writing :math:`\omega=2\pi f`, we obtain the following useful equation for :math:`\delta` in meters:

.. math:: \delta \approx 503 \sqrt{\frac{1}{f \sigma}} = 503 \sqrt{\frac{\rho}{f}}.

For problems involving high frequencies, for example GPR surveys, or very early time transient EM problems, the displacement current may be important. Then Equation :eq:`wn1` needs to be invoked.

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


Phase Velocity
--------------

For situations where displacement currents are negligible, :math:`\alpha` is given by Equation :eq:`wn4` and the plane wave velocity becomes

.. math:: v_{phase} = \sqrt{ \frac{2\omega}{\mu \sigma} },

so velocity increases with frequency but they travel more slowly in conductive permeable media. Alternatively, in materials where the conductivity is zero, then:

.. math:: k = \alpha = \sqrt{\mu \epsilon \omega^2}

and

.. math:: v_{phase} = \frac{1}{\sqrt{\mu \epsilon}}.
        :name: wn3

In free space, Equation :eq:`wn3` equates to :math:`3\times 10^8` m/s, which is the speed of light.


Wave length
-----------

In free space, :math:`\lambda = \frac{3\times10^8}{f}`. In a conducting medium, if the quasistatice approximation is valid, then :math:`\alpha = \beta = 1/\delta` and so :math:`\lambda = 2\pi \delta`.

Thus even though the waves have a sinusoidal description inside the earth, they have lost most of their amplitude by the time they have propagated one wavelength into the earth. The above elements are illustrated in :numref:`pwp` where a plane harmonic wave in free space propagates into the earth.



