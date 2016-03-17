.. _magnetic_permeability_units:

Units
=====

The magnetic field intensity :math:`{\bf H}` is frequently given in Amp\`{e}res per meter (A/m), whereas the magnetic flux density is given in Teslas (T).
By the magnetic constitutive relationship (link), the magnetic permeability of a material is represented in units of T :math:`\! \cdot \!` m/A.
Where Henrys (H) are used to represent a unit of magnetic inductance, the magnetic permeability can also be given in H/m:

.. math::
	\frac{H}{m} = \frac{T \cdot m}{A} 
	:label: Units_Hm

Therefore, the magnetic permeability characterizes the magnetic inductance per unit length of a material.
More commonly, the magnetic properties of rocks are represented using the magnetic susceptibility :math:`\chi`.
Magnetic susceptibility represents the proportion of total magnetic flux density attributed to induced magnetization.
A physical description of the magnetic susceptibility is discussed here (link).
Magnetic susceptibility is related to the magnetic permeability by the following equation:

.. math::
	\mu = \mu_0 \big [ 1 + \chi \, \big ]
	:label: susc_to_perm

where :math:`\mu_0 = 4\pi \times 10^{-7}` T :math:`\! \cdot \!` m/A is the permeability of free-space.
The correct SI units for magnetic susceptibility are (A/m)/(A/m).
However, it is commonly expressed as a unitless quantity.
Magnetic susceptibilities are occasionally given in CGS units.
The conversion between SI and CGS units is given by:

.. math::
	\chi^{(SI)} = 4\pi \chi^{(CGS)}
	:label: SI_to_CGS
	