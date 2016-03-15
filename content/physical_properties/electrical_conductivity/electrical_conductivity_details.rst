.. _electrical_conductivity_detials:

Additional information
======================

Factors that affect electrical conductivity
===========================================

Electric and Ionic conductions
------------------------------

Electrical conductivity is the movement of electrical charge from on location to another, and two important charge carriers are electrons and ions, which will define the conductivity of a rock. Considering this, we express conductivity as

.. math::
	\sigma = n e \mu_e,

where :math:`n` is the number of charge carriers, :math:`e` is charge carried by each charge carrier, and :math:`\mu_e` is the mobility of carriers. Hence, the conductivity of a rock can be determined by its capability to move charges by charge carriers: electrons and ions. This classifies two main different types: a) Electric and b) Ionic conductions.

Both conductions are related to random motion of particles affected by an applied electric field. However, how charge moves in conduction processes are quite different. The charge carrier for the electric conduction is electron, which will define conductivity of most metals such as iron and copper. The random motion of valence electrons (a measure of its combining power with other atoms) among the atom is ordered by the application of an external electric field. The electrons then travel with a drift velocity through solid.

For the ionic conduction, the charge carrier is ion. Considering most of surface rocks are saturated by some fluids (water, oil and gas, ... etc), conduction in surface rock is mostly electrolytic, taking place in the connected pore spaces, along grain boundaries and in fractures, but negligibly through the mineral grains or silicate framework :cite:`ward1990`.


What makes a rock conductivity?
-------------------------------

Here are common factors determine conductivity of a rock:

	- Metallic particles
	- Electrolyte in the pore of a rock with large number of ions
	- Temperature
	- Pressure
	- Porosity
	- Rock texture
	- Clay materials

If a rock includes metallic particles, obviously that rock will be conductive (electric conduction).

Each ion is able to only a certain quantity of charge, it indicates that the more ions in an solution and faster they move, the greater charge will be carried which result in greater conductivity of a rock. Hence, the solution with the greater number of ions will have higher conductivity. Accordingly, a rock which includes saline water within its pores will have larger conductivity when the salinity of the water is higher than when it is lower.

An increase in temperature will increase the mobility of ions in the solution resulting in an increase of the conductivity. Based upon that temperature increase and salinity decrease with depth, conductivity should increase with depth. However, the effect of pressure should be considered to understand conductivity of the earth with depth as we shall explore later.

Most minerals forming rocks are nonconductive. However, the porosity and pore distribution of a rock specimen will have effect on determining conductivity. In addition, clay minerals in a rock can be a separate conducting path from electrolyte conduction, which will increase the conductivity of a rock.

.. _ionic_conductivity:

Ionic conductivity
------------------

Conduction in surface rocks is mostly electrolytic, taking place in the connected pore spaces, along grain boundaries and in fractures, but negligibly through the mineral grains or silicate framework :cite:`ward1990`. For this case, the charge carrier is mostly ions dissolved in an electrolyte, so we often call this as ionic conductivity. Ionic conductivity of a rock is ranging from :math:`10^{3}`-:math:`10^{-5}` S/m. Porous media such as rocks at the earth’s surface that we are usually dealing with can be considered to solid semi-conductor.

Ionic conductivity is resulting from the ordered movement of ions in an electrolyte under the application of an external electric field. Without an external electric field, the ions move randomly as a result of thermal agitation and collisions with other ions and atoms. Because both cations (+) and anions (-) are present in an electrolyte, the conductivity can be expressed as

	.. math::

		\sigma = e(n^+\mu_m^+ + n^-\mu_m^-),

where :math:`n` is the number of charge carriers, :math:`e` is the charge carried, and :math:`\mu_m` is the mobility of the carriers. Here superscripts + and - stand for cation and anion.

Archie defined an empirical relationship which considers above factors defining the conductivity of a sedimentary rock (). Archie’s law can be written as

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

The cations are required to balance the charge due to substitution within the crystal lattice, and to broken bonds. The finite size of the cations prevents the formation of a single layer. Rather, a “double layer” is created; it is composed of a “fixed layer” immediately adjacent to the clay surface and a “diffuse layer” which drops off in charge density exponentially with distance from the fixed layer. Different from the fixed layer, the diffuse layer is not fixed but free to move under an applied electric field. This double layer phenomenon is simply considered as cation selective membrane. And those cations captured by clay minerals, will be added to the normal ion concentration and thus increase the density of charge carriers. The net result is an increased “surface conductivity” :cite:`ward1990`.

The impact of a disseminated clay on rock conductivity becomes increasingly important as the conductance through the pore decreases. Hydrothermal alteration changes feldspars to kaolinite, montmorillonite, and other clay minerals, particularly for siliceous rocks. In basics rocks, chlorite and serpentine may be produced. All of these alteration products exhibit high conductivity. As the concentration of of the electrolyte increases the relative contribution of the electrolyte conduction path to the clay conduction path increases.
The total conductivity :math:`\sigma` of a rock can be expressed as

	.. math::
		\sigma = \sigma_n + \sigma_s,

where :math:`\sigma_n` is the normal rock conductivity and :math:`\sigma_s` is the surficial conductivity  of the clay. Assuming fully saturated rock (:math:`S_w=1`) and substituting :math:`\sigma_w` to :math:`\sigma_e` (conductivity of the electrolyte) from Eq. :eq:`Archies_cond`, :math:`\sigma_n = \frac{\sigma_e}{F}`, we rewrite above equation as

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
