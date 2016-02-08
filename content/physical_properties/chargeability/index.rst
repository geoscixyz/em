.. _chargeability_index:

Chargeability
=============

The electrical conductivity of a material can depend upon frequency. In Ohm's Law, :math:`\vec{E} = \rho\vec{J}`, :math:`\rho` is a complex number. The underlying microscopic phenomonan accounting for this is complicated and depends upon the minerals, grain sizes, and surface-to-volume ratios and the abundance of clays. There is no simple mathematical formula that describes the relation between conductivity and frequency but one that has some practical use is the Cole-Cole model, which describes dispersive dielectric constant (CITE). Pelton XXX (CITE), modified this for resistivity which can be written as 

.. math::
    \rho(\omega) = \rho_0 \Big[1 - \eta \Big(1-\frac{1}{1+(\imath\omega\tau)^c}\Big) \Big],
    :label: colecole_pelton_res

where :math:`\rho_0` is resistance at zero frequency, :math:`\eta` is chargeability, :math:`\tau` (s) is a time constant, :math:`c` is a frequency dependency. :math:`\eta` is the "chargeability" (dimensionless :math:`0\le\eta<1`); :math:`\eta` is often related to the concentration of a chargeable mineral, for instance :math:`\eta` is related to the total percentage of sulfide minerals. :math:`\tau` is a time constant generally thought to be related to grain size; :math:`c` is a variable associated with distribution of grain size. Historically "chargeabilty" has been referred to as "over-voltage". The description arises from geophysial surveys in the 1950's and is illustrated in the following diagram:

.. figure:: ./figures/IPonoff.png
   :align: center
   :name: LogCond

   Overvoltage effects. (a) Input current. (b) Measured voltage.

Here :math:`V_\infty` and :math:`V_0` respecively indicate measured voltage at infinte and zero frequencies. The chargeability can be expressed as 

.. math::
    \eta = \frac{V_0-V_\infty}{V_0}

or 

.. math::
    \eta = \lim_{t \to 0} V_s(t),

where :math:`V_s (t)` is measured voltage at off-time.

.. todo:: Citations


**Contents**

 .. toctree::
    :maxdepth: 2

    chargeability_lab_setup_measurements
    chargeability_units_values
    chargeability_factors
    chargeability_mathematical_relationships

References: Rock and Mineral Properties: Keller SEG Vol 1 Electromagnetic Methods in Applied Geophysics

Knight and Enders: An introduction to Rock Physics Principles for near surface geophysics: Investigations in geophysics No13; SEG Near;-Surface Geophysics edited by Dwain Butler

Stan Ward: Resistivity ad Induced Polarization Methods (p147..)
Investigations in geophysics #5; Geotechical and environemental geophysics.
    


