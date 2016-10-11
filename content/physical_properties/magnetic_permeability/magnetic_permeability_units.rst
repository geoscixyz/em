.. _magnetic_permeability_units:

Units
=====

Two sets of units may be used to represent the magnetic permeability: Teslas times meters per Ampere (T :math:`\! \cdot \!` m/A), and Henrys per meter (H/m):

.. math::
    \frac{H}{m} = \frac{T \cdot m}{A}
    :label: Units_Hm

The magnetic field intensity :math:`{\bf H}` is frequently given in Amperes per meter (A/m), whereas the magnetic flux density is given in Teslas (T).
Therefore, the first choice in units is defined by the :ref:`magnetic constitutive relationship <magnetic_permeability_index>`.
Henrys are used to represent a unit of magnetic inductance.
Therefore, the magnetic permeability also characterizes the magnetic inductance per unit length of a material.

More commonly, the magnetic properties of rocks are represented using the magnetic susceptibility :math:`\chi`.
Magnetic susceptibility represents the proportion of total magnetic flux density attributed to induced magnetization.
A physical description of the magnetic susceptibility is discussed :ref:`here <magnetic_permeability_magnetism>`.
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

