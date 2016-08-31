.. _electrical_conductivity_effectsclay:

Effects of clay minerals
------------------------

In the classical petroleum engineering approach to sedimentary rocks, rock containing clay particle often called “dirty sands”. Since clay particle is substantially more conductive than the mineral grains, it could be a separate conducting path. Archie’s law usually working well for sedimentary rocks, and needs to be corrected. Fundamental cause of this abnormally high conductivity based upon the double layer of the absorbed cations as shown in :numref:`DoubleLayer`.

.. figure:: ../images/DoubleLayer.png
   :align: center
   :name: DoubleLayer

   Conceptual diagram of ions absorbed on clay particle.

The cations are required to balance the charge due to substitution within the crystal lattice, and to broken bonds. The finite size of the cations prevents the formation of a single layer. Rather, a “double layer” is created; it is composed of a “fixed layer” immediately adjacent to the clay surface and a “diffuse layer” which drops off in charge density exponentially with distance from the fixed layer. Different from the fixed layer, the diffuse layer is not fixed but free to move under an applied electric field. This double layer phenomenon is simply considered as cation selective membrane. And those cations captured by clay minerals, will be added to the normal ion concentration and thus increase the density of charge carriers. The net result is an increased “surface conductivity :cite:`ward1990`.

The impact of a disseminated clay on rock conductivity becomes increasingly important as the conductance through the pore decreases. Hydrothermal alteration changes feldspars to kaolinite, montmorillonite, and other clay minerals, particularly for siliceous rocks. In basics rocks, chlorite and serpentine may be produced. All of these alteration products exhibit high conductivity. As the concentration of of the electrolyte increases the relative contribution of the electrolyte conduction path to the clay conduction path increases.
The total conductivity :math:`\sigma` of a rock can be expressed as

.. math::
	\sigma = \sigma_n + \sigma_s,

where :math:`\sigma_n` is the normal rock conductivity and :math:`\sigma_s` is the surficial conductivity  of the clay. Assuming fully saturated rock (:math:`S_w=1`) and with Archie's law (:math:`\sigma = \frac{\sigma_e}{F}S_w^{n}`), we obtain :math:`\sigma_n = \frac{\sigma_e}{F}`. Then, we rewrite above equation as

	.. math::
		\sigma = \frac{\sigma_e}{F} + \sigma_s.

This clearly shows that as the concentration of the electrolyte increases the relative contribution of the electrolyte conduction path (:math:`\sigma_n`) to the clay conduction path (:math:`\sigma_s`) increases.

:cite:`waxman1968` give the expression for the resistivity of a clay-bearing rock

.. math::
	\rho = \frac{\rho_w F_t}{1+ \rho_w BQ},
	:label: Waxman&Smits

and effectively in conductivity form

.. math::
	\sigma = \frac{\sigma_w+BQ}{F_t},

where B is the factor related to the mobility of exchange cations on the pore water concentration, Q is the clay cation exchange capacity per unit volume, and :math:`F_t` is the formation factor at very high concentrations where the effects of clays can be neglected (the true formation factor). From Eq. :eq:`Waxman&Smits` an apparent formation factor can be written as

.. math::
	F_a = \frac{\rho_r}{\rho_w} = \frac{F_t}{1+\rho_w BQ}.
