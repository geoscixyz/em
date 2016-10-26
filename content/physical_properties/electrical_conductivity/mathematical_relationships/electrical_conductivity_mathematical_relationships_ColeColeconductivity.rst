.. _electrical_conductivity_mathematical_relationships_ColeColeconductivity:

Cole Cole Conductivity
======================

Because resistivity is the inverse of conductivity (:math:`\sigma = 1 /
\rho`), we could have conductivity form of Cole-Cole model as well. Depending
on situations either resistivity or conductivity form can be advantageous,
hence we consider a conductivity form:

.. math::
    \sigma(\omega) = \sigma_{\infty}\Big(1-\frac{\eta}{1+(1-\eta)(\imath\omega\tau)^c} \Big),
    :label: colecole_pelton_sig

where :math:`\sigma_{\infty}` is conductivity at infinite frequency,
:math:`\eta` is chargeability, :math:`\tau` (s) is a time constant, :math:`c`
is a frequency dependency.

.. note::

    In a resistivity form we use resistivity at zero frequency, :math:`\rho_0
    = 1/\sigma_0`, to express Cole-Cole model. However, in conductivity form
    we use conductivity at infinite frequency, :math:`\sigma_{\infty}`.
    Conductivity at zero freuency can be expressed as :math:`\sigma_{0} =
    \sigma_{\infty}(1-\eta)`

.. todo::
	Add when useful to use conductivity form
