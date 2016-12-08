.. _electrical_conductivity_mathematical_relationships_Archie:

Archie's Law
============

Archie defined an empirical relationship which considers above factors
defining the conductivity of a sedimentary rock. Archie’s law can be written
as

.. math::
	\sigma = F^{-1} \sigma_w S_w^{n},
	:label: Archies_cond

where :math:`S_w` is the water saturation, :math:`\sigma_w` is the
conductivity of the brine, and :math:`F` is the formation factor. In
resistivity form, this can be written as

.. math::
	\rho = F \rho_w S_w^{-n},
	:label: Archies_resis

where :math:`\rho_w` is the resistivity of the brine. The formation factor is defined as

.. math::
	F = \frac{a}{\phi^m} = \frac{\sigma_w}{\sigma_o} = \frac{\rho_o}{\rho_w},
	:label: Archies_formationfactor


where :math:`\sigma_o` and :math:`\rho_o` are the conductivity and resistivity
of the rock filled with only brine (:math:`S_w=1`), respectively. Here m is
the cementation factor (usually in the range of 1.3<m<2.3), n is the
saturation exponent (usually close to 2), and a is tortuosity factor. The
cementation factor describes how much the pore network decreases the
conductivity (assuming rock itself is not conductive). The more consolidated
rock usually have the greater cementation factor, which is effectively related
to the pressure:

	- For slightly consolidated sandstones m=1.4
	- For consolidated sandstones m=1.7

Tortuosity factor describes the excess length of the equivalent electrolyte
path relative to the rock specimen length, hence the greater tortuosity makes
the greater porosity resulting in higher conductivity.

The resistivity index can be written as

.. math::
	RI = \frac{\rho}{\rho_w} = S_w^{-n},
	:label: Archies_RI

.. note::

	Archie’s law is purely empirical law intending to describe ion flow in
	clean and consolidated sands. Electrical conduction is assumed not to be
	present within the rock grains. Hence it may not work for a rock includes
	considerable amount of clay minerals because a clay or shale particle acts
	as a separate conducting path.
