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