.. _chargeability_measured_voltage:

Measured voltage and chargeability
----------------------------------

By injecting suite of sinulsoidal currents to a rock specimen, we can measure complex voltage, covert to complex impedance using Ohm's law: :math:`V(\omega) = I(\omega)Z(\omega)`, which corresponds to :math:`\mathbf{E}(\omega) = \rho (\omega)\mathbf{J}(\omega)`. Here :math:`Z(\omega)` stands for complex impedance. For time domain measurement, we often put a half-duty cycle current. Measured voltage at on-time can be considered as a voltage due to the step-on current if the period is long enough to reach steady-state for the polarization charge build-up.

.. note::
	The greater time constant, :math:`\tau`, requires the longer period to reach steady-state for polarization charge build-up.

In time domain, measured voltage with the step-on current:

.. math::
	V_{on}(t) = \frac{1}{I_0}\mathcal{L}^{-1} [\frac{Z(s)}{s}],

where :math:`s=\imath\omega` is the Laplace transform variable, and the step-on current is :math:`I(s) = \frac{I_0}{s}`. Using initial and final value theorem we have

.. math::
	\lim_{t \to 0} \mathcal{L}^{-1} [\frac{Z(s)}{s}] = \lim_{s \to \infty} Z(s) = \rho_0(1-\eta).

Using the relationship between step-on and -off, we obtain intrinsic-chargeability, :math:`\eta` as

.. math::
	\lim_{t \to 0} \frac{V_s(t)}{V_0} = 1- \lim_{s \to \infty} \frac{Z(s)}{Z_0} = \frac{\rho_0 \eta}{\rho_0} = \eta.

The chargeability can also expressed as

.. math::
	\eta = \frac{V_0-V_{\infty}}{V_0}.

Although we cannot measure exact :math:`V_{\infty}` and :math:`V_0`, when :math:`c` = 0.5 and :math:`\tau` = 0.1, we can obtain a good estimate of the intrinsic-chargeability value. Recalling a common definition of pseudo-chargeability, M (msec):

.. math::
	M = 10^3\int_{t_1}^{t_2} \frac{V_s(t)}{V_0} dt.

By using a specific time window (:math:`t_1` = 800 msec :math:`t_2` = 1400 msec), we numerically evaluate :math:`\frac{V_s(t)}{V_0}` then evaluate integration from :math:`t_1` to :math:`t_2`.

.. figure:: ../../../examples/physical_properties/chargeability/colecole_resis.png
   :align: center
   :name: colecole_resis_V

Right panel of :numref:`colecole_resis_V` Cole-Cole resistivity response with the step-off current, which can be considered as :math:`1-\mathcal{L}^{-1} [\frac{Z(s)}{s}]`, and computed pseudo-chargeability value (M) is 49.487 msec, which is close to the used chargeability, :math:`\eta=0.5` if we multiply by factor of 10. Although computed 10xpseudo-chargeability with this window provides a good estiamte of the intrisinc chargeability; however this is only when :math:`c` = 0.5 and :math:`\tau` = 0.1. For instance, when :math:`\tau` =0.01, computed pseudo-chargeability is much less than the intrisinsic one as shown in Table 1 hence, what we usually consider as chargeability is different from the intrinsic chargeability, :math:`\eta`.

**Table 1:** Comparision of intrinsic- and 10xpseudo-chargeability values (msec). For the computation of pseudo-chargeability for the integration time window: 800-1400 msec, and compared for two different time constant values (0.1 and 0.01 s).

+---------------------------+-----------------------------------------------------+------------------------------------------------------+
|**Intrinsic-chargeability**|**10xPseudo-chargeability (msec;time constant=0.1s)**|**10xPseudo-chargeability (msec;time constant=0.01s)**|
+===========================+=====================================================+======================================================+
| 0.1                       |   9.897                                             |   3.215                                              |
+---------------------------+-----------------------------------------------------+------------------------------------------------------+
| 0.2                       |   19.795                                            |   6.502                                              |
+---------------------------+-----------------------------------------------------+------------------------------------------------------+
| 0.3                       |   29.692                                            |   9.753                                              |
+---------------------------+-----------------------------------------------------+------------------------------------------------------+

.. todo::

	Add a link for the widget
