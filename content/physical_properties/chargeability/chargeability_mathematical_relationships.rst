.. _chargeability_mathematical_relationships:

Some mathematical relationships
===============================

To explain chargeability, we used "over-voltage" effects due to the polarization build-up under the external electric field. This often called induced polarization phenomenon, and can be mathematically formulated using a complex conductivity or resistivity model in frequency domain. This will include more IP parameters than the chargeability and we will explore those through a simple complex conductivity model.

Complex conductivity or resistivity
-----------------------------------

The electrical conductivity of a material can depend upon frequency. In Ohm's Law, :math:`\mathbf{J} = \sigma\mathbf{E}`, :math:`\sigma` is a complex number. 
There is no simple mathematical formula that describes the relation between conductivity and frequency but one that has some practical use is the Cole-Cole model, which describes dispersive dielectric constant (CITE). Pelton XXX (CITE), modified this for resistivity which can be written as 

.. math::
    \rho(\omega) = \rho_0 \Big[1 - \eta \Big(1-\frac{1}{1+(\imath\omega\tau)^c}\Big) \Big],
    :label: colecole_pelton_res

where :math:`\rho_0` is resistivity at zero frequency, :math:`\eta` is chargeability, :math:`\tau` (s) is a time constant, :math:`c` is a frequency dependency. :math:`\eta` is the "chargeability" (dimensionless :math:`0\le\eta<1`); :math:`\eta` is often related to the concentration of a chargeable mineral, for instance :math:`\eta` is related to the total percentage of sulfide minerals. :math:`\tau` is a time constant generally thought to be related to grain size; :math:`c` is a variable associated with distribution of grain size. In a conductivity form, this can be written as

.. math::
    \sigma(\omega) = \sigma_{\infty}\Big(1-\frac{\eta}{1+(1-\eta)(\imath\omega\tau)^c} \Big),
    :label: colecole_pelton_sig

where :math:`\sigma_{\infty}` is conductivity at infinite frequency. 

Left panel of :numref:`colecole_resis` shows Cole-Cole resistivity with parameters: :math:`\eta=0.5`, :math:`\tau=0.1` s, :math:`c=0.5`, :math:`\sigma_{\infty}=1` S/m. 

.. figure:: ../../../examples/physical_properties/chargeability/colecole_resis.png
   :align: center
   :name: colecole_resis

   Cole-Cole resistivity response. Left and right panels show frequency and time domain responses. Time domain response assumed step-off current waveform. M indicates pseudo-chargeability computed within the window for Newmont's standard (800-1400 msec).

.. _chargeability_mathematical_relationships_measured_voltage:

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

By using the Nemont's standard (:math:`t_1` = 800 msec :math:`t_2` = 1400 msec), we numerically evaluate :math:`\frac{V_s(t)}{V_0}` then evaluate integration from :math:`t_1` to :math:`t_2`. Right panel of :numref:`colecole_resis` Cole-Cole resistivity response with the step-off current, which can be considered as :math:`1-\mathcal{L}^{-1} [\frac{Z(s)}{s}]`, and computed pseudo-chargeability value (M) with the Nemont's standard is 49.487 msec, which is close to the used chargeability, :math:`\eta=0.5`. Although computed pseudo-chargeability with the Newmont's standard provides a good estiamte; however this is only when :math:`c` = 0.5 and :math:`\tau` = 0.1. For instance, when :math:`\tau` =0.01, computed pseudo-chargeability is much less than the intrisinsic one as shown in Table 1. 

**Table 1:** Comparision of intrinsic- and pseudo-chargeability values. For the computation of pseudo-chargeability, Newmont's standard is used (time window: 800-1400 msec) and compared for two different time constant values (0.1 and 0.01 s). 

+---------------------------+---------------------------------------------------+----------------------------------------------------+
|**Intrinsic-chargeability**| **Pseudo-chargeability (msec;time constant=0.1s)**| **Pseudo-chargeability (msec;time constant=0.01s)**|
+===========================+===================================================+====================================================+
| 0.1                       | 9.897                                             | 3.215                                              |
+---------------------------+---------------------------------------------------+----------------------------------------------------+
| 0.2                       | 19.795                                            | 6.502                                              |
+---------------------------+---------------------------------------------------+----------------------------------------------------+
| 0.3                       | 29.692                                            | 9.753                                              |
+---------------------------+---------------------------------------------------+----------------------------------------------------+

.. todo::

	Add a link for the widget

.. Time constant, :math:`\tau`
.. ---------------------------


.. Frequency dependency, :math:`c`
.. -------------------------------
