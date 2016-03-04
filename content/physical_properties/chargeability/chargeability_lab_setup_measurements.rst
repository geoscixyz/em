.. _chargeability_lab_setup_measurements:

Lab Setup and Measurements
==========================

To measure chargeability, we use similar set-up for conductivity measurement shown in :numref:`DCcircuit` except for the input current waveform. Rather than DC, we put half-duty rectangular waveform as shown in :numref:`ACcircuit`. If a rock specimen is chargeable then measured voltage will show overvoltage effect.

Based upon the definition of the chargeability (:math:`\eta=\frac{V_0-V_\infty}{V_0}`), where :math:`V_\infty` and :math:`V_0` are correspondingly measured voltage at zero and inifite frequency, we cannot measure correct chargeability.

.. figure:: ./figures/ACcircuit.png
   :align: center
   :name: ACcircuit

   Figure An AC circuit.

A simple and often used system on the field is GDD's `SCIP Tester <http://www.gddinstrumentation.com/index.php/scip-tester>`_.

.. figure:: ./figures/conductivity_chargeability_measurement.jpg
   :align: center
   :name: conductivity_chargeability_measurement

   Figure GDD SCIP tester.

Measured voltage can be stacked and we could obtain half-period voltage as shown in :numref:`DCIPcurve_lab`. We alterantively define pseudo-chargeability (M) as

.. math::
	M = \int_{t_1}^{t_2} \frac{V_s(t)}{V_0} dt

where :math:`t_1` and :math:`t_2` are arbitrary times. The unit of pseudo-chargeability is ms.

.. figure:: ../../../examples/physical_properties/electrical_conductivity/DCIPcurve.png
   :align: center
   :scale: 50%
   :name: DCIPcurve_lab

   Figure Measured time domain IP curve.
