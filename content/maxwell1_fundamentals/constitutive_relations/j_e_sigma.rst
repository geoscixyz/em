.. _j_e_sigma:

Ohm's Law
========================

Ohm's law is one of the three constitutive equations used in conjunction with Maxwell's equations. It is not a formal law as it describes the relationship between the current density :math:`\mathbf{J}`, which is defined as the electrical current through a cross-sectional area, and the electric field :math:`\mathbf{E}` for some materials, but not all. The law was originally published in 1827 by Georg Ohm in his book entitled "The galvanic circuit investigated mathematically" and was accepted widely by the 1850's. It is written in the frequency-domain as:

.. include:: ../../equation_bank/ohms_law_freq.rst

where :math:`\sigma` is the electrical conductivity, which is defined as the amount of resistance a material has to an electric current. The equation states that in order to generate a certain current density, the electric field must be increased as the electrical conductivity increases. Conductivity (or its inverse, resistivity :math:`\rho`) is a tensor as both the current density and the electric field are vectors with components in three orthogonal directions in Cartesian coordinates. For isotropic materials, this tensor simplifies to a scalar value as the conductivity does not vary with direction.

The electric field and the current density are complex numbers in the frequency-domain. The equation can also be written in the time-domain:

.. include:: ../../equation_bank/ohms_law_time.rst

where :math:`\mathbf{j}` is the current density and :math:`\mathbf{e}` is the electric field. Both quantities are real numbers.

Conductivity is expressed in units of siemens per meter [:math:`S/m`] and 1 siemens [:math:`S`] equates to the reciprocal of 1 ohm [:math:`\Omega^{-1}`], which in turn is equal to 1 amperes per volt [:math:`A/V`]:

  .. math::
     \left [ \frac{S}{m} \right ] = [\Omega^{-1}] = \left [ \frac{A}{V m} \right ]

The electric field has units of volts per meter [:math:`V/m`]. The units of current density then become:

  .. math::
     \mathbf{J} = \left [ \frac{A}{V m} \frac{V}{m}\right ] = \left [ \frac{A}{m^2} \right ]
        
These units agree with the definition of current density.

Further reading...
^^^^^^^^^^^^^^^^^^

Reynolds, J. M., 1998, An Introduction to Applied and Environmental Geophysis: Wiley.

Ward, S. H., and G. W. Hohmann, 1988, Ch. 4, in Electromagnetic Methods in Applied Geophysics: Society of Exploration Geophysicists, Vol. 1, 131-311.

West, G. F., and J. C. McNae, 1991, Ch. 1, in Physics of the Electromagnetic Induction Exploration Method: Society of Exploration Geophysicists, Vol. 2, 5-46.



