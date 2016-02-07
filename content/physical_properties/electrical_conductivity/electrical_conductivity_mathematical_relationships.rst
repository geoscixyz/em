.. _electrical_conductivity_mathematical_relationships:

Some mathematical relationships
===============================

.. todo:: Citations

.. _ionic_conductivity: 

Ionic conductivity
------------------

Conduction in surface rocks is mostly electrolytic, taking place in the connected pore spaces, along grain boundaries and in fractures, but negligibly through the mineral grains or silicate framework (CITES). For this case, the charge carrier is mostly ions dissolved in an electrolyte, so we often call this as ionic conductivity. Ionic conductivity of a rock is ranging from :math:`10^{3}`-:math:`10^{-5}` S/m. Porous media such as rocks at the earth’s surface that we are usually dealing with can be considered to solid semi-conductor. 

Ionic conductivity is resulting from the ordered movement of ions in an electrolyte under the application of an external electric field. Without an external electric field, the ions move randomly as a result of thermal agitation and collisions with other ions and atoms. Because both cations (+) and anions (-) are present in an electrolyte, the conductivity can be expressed as 

	.. math::

		\sigma = e(n^+\mu_m^+ + n^-\mu_m^-), 

where :math:`n` is the number of charge carriers, :math:`e` is the charge carried, and :math:`\mu_m` is the mobility of the carriers. Here superscripts + and - stand for cation and anion. 

Archie (CITE) defined an empirical relationship which considers above factors defining the conductivity of a sedimentary rock. Archie’s law can be written as 

	.. math::
		\sigma = F^{-1} \sigma_w S_w^{n},
		:label: Archies_cond

where :math:`S_w` is the water saturation, :math:`\sigma_w` is the conductivity of the brine, and :math:`F` is the formation factor. In resistivity form, this can be written as 

	.. math::
		\rho = F \rho_w S_w^{-n},
		:label: Archies_resis

where :math:`\rho_w` is the resistivity of the brine. The formation factor is defined as 

	.. math::
		F = \frac{a}{\phi^m} = \frac{\sigma_w}{\sigma_o} = \frac{\rho_o}{\rho_w}, 


where :math:`\sigma_o` and :math:`\rho_o` are the conductivity and resistivity of the rock filled with only brine (:math:`S_w=1`), respectively. Here m is the cementation factor (usually in the range of 1.3<m<2.3), n is the saturation exponent (usually close to 2), and a is tortuosity factor. 
The cementation factor describes how much the pore network decreases the conductivity (assuming rock itself is not conductive). The more consolidated rock usually have the greater cementation factor, which is effectively related to the pressure:

	- For slightly consolidated sandstones m=1.4
	- For consolidated sandstones m=1.7

Tortuosity factor describes the excess length of the equivalent electrolyte path relative to the rock specimen length, hence the greater tortuosity makes the greater porosity resulting in higher conductivity. 

The resistivity index can be written as 

	.. math::

		RI = \frac{\rho}{\rho_w} = S_w^{-n}, 

.. note::
	Archie’s law is purely empirical law intending to describe ion flow in clean and consolidated sands. Electrical conduction is assumed not to be present within the rock grains. Hence it may not work for a rock includes considerable amount of clay minerals because a clay or shale particle acts as a separate conducting path. 


.. _effects_of_clays: 

Effects of clay minerals
------------------------

In the classical petroleum engineering approach to sedimentary rocks, rock containing clay particle often called “dirty sands”. Since clay particle is substantially more conductive than the mineral grains, it could be a separate conducting path. Archie’s law usually working well for sedimentary rocks, and needs to be corrected. Fundamental cause of this abnormally high conductivity based upon the double layer of the absorbed cations as shown in :numref:`DoubleLayer`. 

.. figure:: ../../../examples/physical_properties/electrical_conductivity/DoubleLayer.png
   :align: center
   :name: DoubleLayer

   Conceptual diagram of ions absorbed on clay particle. 

The cations are required to balance the charge due to substitution within the crystal lattice, and to broken bonds. The finite size of the cations prevents the formation of a single layer. Rather, a “double layer” is created; it is composed of a “fixed layer” immediately adjacent to the clay surface and a “diffuse layer” which drops off in charge density exponentially with distance from the fixed layer. Different from the fixed layer, the diffuse layer is not fixed but free to move under an applied electric field. This double layer phenomenon is simply considered as cation selective membrane. And those cations captured by clay minerals, will be added to the normal ion concentration and thus increase the density of charge carriers. The net result is an increased “surface conductivity” (CITE).  

The impact of a disseminated clay on rock conductivity becomes increasingly important as the conductance through the pore decreases. Hydrothermal alteration changes feldspars to kaolinite, montmorillonite, and other clay minerals, particularly for siliceous rocks. In basics rocks, chlorite and serpentine may be produced. All of these alteration products exhibit high conductivity. As the concentration of of the electrolyte increases the relative contribution of the electrolyte conduction path to the clay conduction path increases. 
The total conductivity :math:`\sigma` of a rock can be expressed as 

	.. math::
		\sigma = \sigma_n + \sigma_s,

where :math:`\sigma_n` is the normal rock conductivity and :math:`\sigma_s` is the surficial conductivity  of the clay (CITE). Assuming fully saturated rock (:math:`S_w=1`) and substituting :math:`\sigma_w` to :math:`\sigma_e` (conductivity of the electrolyte) from Eq. :eq:`Archies_cond`, :math:`\sigma_n = \frac{\sigma_e}{F}`, we rewrite above equation as 

	.. math::
		\sigma = \frac{\sigma_e}{F} + \sigma_s. 

This clearly shows that as the concentration of the electrolyte increases the relative contribution of the electrolyte conduction path (:math:`\sigma_n`) to the clay conduction path (:math:`\sigma_s`) increases. 

Waxman and Smits (1968) (CITE) give the expression for the resistivity of a clay-bearing rock

	.. math::
		\rho = \frac{\rho_w F_t}{1+ \rho_w BQ}, 
		:label: Waxman&Smits

and effectively in conductivity form

	.. math::

		\sigma = \frac{\sigma_w+BQ}{F_t}, 

where B is the factor related to the mobility of exchange cations on the pore water concentration, Q is the clay cation exchange capacity per unit volume, and :math:`F_t` is the formation factor at very high concentrations where the effects of clays can be neglected (the true formation factor). From Eq. :eq:`Waxman&Smits` an apparent formation factor can be written as 

	.. math::

		F_a = \frac{\rho_r}{\rho_w} = \frac{F_t}{1+\rho_w BQ}. 