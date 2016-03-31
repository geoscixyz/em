.. _chargeability_units:

Units
=====

By definition of the intrinsic chargeability, :math:`\eta = \frac{V_0-V_\infty}{V_0}`, the unit will be V/V (Dimensionless); :math:`\eta` will be bounded to :math:`[0,1)`. The chargeability can be considered as net voltage difference from inifinte to zero frequency normalized by voltage at zero frequency, :math:`V_0`. As shown in below diagram, when the current switched-on in the on-time, polarization charges start to build up (:math:`V_0`) then at a late time it asymptotes to steatdy-state (:math:`V_0`). After the current is switched-off built polarization charge is decaying and asymptotes to zero.

.. figure:: ./figures/DCIPcurve.png
   :align: center
   :scale: 50%
   :name: DCIPcurve

   Time curve for DC-IP data.

Since we cannot measure exact value of :math:`V_{\infty}` and :math:`V_0`, we often alternatively measure voltage at off-time, :math:`V_s(t)` then integrate in certain range of time to obtain pseudo-chargeability, :math:`M`:

.. math::
	M = \int_{t_1}^{t_2} \frac{V_s(t)}{V_0} dt,

where :math:`t_1` and :math:`t_2` are arbitraty times used for integration. The unit of this pseudo-chareability (M) is often ms.

.. note::
	Depending on the used time window, measured pseudo-chargeability can under- or over-estiamte intrinsic chargeabiility. For instance, if discharging happens within really short time window and our integration time window is on much later time, then the integrated pseudo-charegability could be significantly underestimated. We will treat this later in :ref:`chargeability_measured_voltage`

There can be different types of the pseudo-chargeability:

.. math::
	M = (t_2-t_1)\int_{t_1}^{t_2} \frac{V_s(t)}{V_0} dt,

and its unit is mV/V.

