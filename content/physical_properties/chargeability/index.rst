.. _chargeability_index:

Chargeability
=============

Earth material can be polarizable under the external electric field, which makes additional polarization charge build-up. Chargeability indicates a rock's capability to build polarization charge build-up under the external electric field. The underlying microscopic phenomonan accounting for this is complicated and depends upon the minerals, grain sizes, and surface-to-volume ratios and the abundance of clays. Historically "chargeabilty" has been referred to as "over-voltage". The description arises from geophysial surveys in the 1950's and is illustrated in the following diagram:

.. figure:: ./figures/IPonoff.png
   :align: center
   :name: IPonoff

   Overvoltage effects. (a) Input current. (b) Measured voltage.

Here :math:`V_\infty` and :math:`V_0` respecively indicate measured voltage at infinte and zero frequencies. The chargeability can be expressed as

.. math::
    \eta = \frac{V_0-V_\infty}{V_0}

or

.. math::
    \eta = \lim_{t \to 0} V_s(t),
    :label: pseudo_chargeability_int

where :math:`V_s (t)` is measured voltage at off-time.

Geophysical application, which uses chargeability called induced polarization (IP) technique. Mineral exploration for sulfides (disseminated and massive) is unquestionably
the most common application of IP because those types of ore minerals are
often chargeable.There are also applications in hydrogeology. For example,
mapping salt water intrusions in aquifers that include clayey layers may be
difficult using resistivity alone. However, the increased chargeability
associated with clay may help differentiate between zones with more saline
water and clay, both of which have low resistivity. In addition, there is a
growing interest in the possibility of using chargeability to aid in the
detection and delineation of contaminants in the ground. There has also been
some effort to apply IP to oil and gas exploration.

**Contents**

 .. toctree::
    :maxdepth: 2

    chargeability_units
    chargeability_factors
    chargeability_complex_conductivity
    chargeability_measured_voltage


.. References: Rock and Mineral Properties: Keller SEG Vol 1 Electromagnetic Methods in Applied Geophysics

.. Knight and Enders: An introduction to Rock Physics Principles for near surface geophysics: Investigations in geophysics No13; SEG Near;-Surface Geophysics edited by Dwain Butler




