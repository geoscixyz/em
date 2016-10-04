.. _frequency_domain_electric_dipole_index:

Harmonic Electrical Current Dipole
==================================


.. topic:: Purpose

    Here, we provide a physical description for the harmonic electrical current dipole.
    This is used to develop a mathematical expression which can be used to replace the electrical source term in Maxwell's equations. 


The harmonic electrical current dipole source can be thought of as an infinitesimally short length of wire which carries a harmonic current.
This should not be confused with the more classic definition of an electric dipole which describes the polarization of opposing electrical charges.

The strength of the electric dipole source is defined by its dipole moment (:math:`\mathbf{p}`).
Where :math:`\mathbf{I}` is the vector amplitude of the current within a length of wire :math:`ds`, the dipole moment for a harmonic electric dipole source is given by:

.. math::
	\mathbf{p} = \mathbf{I} \, ds


Let us now examine the source current which results from a harmonic electric dipole source.
For a source current of magnitude :math:`I` which lies in the :math:`\hat x` direction along a wire segment of length :math:`\Delta s`, the source current density is given by:

.. math::
	\mathbf{J (r)} = \hat x I \Delta s \Bigg [ \frac{\textrm{u}\big (x + \frac{\Delta s}{2} \big ) - \textrm{u} \big ( x - \frac{\Delta s}{2} \big )}{\Delta s} \Bigg ] \delta (y) \delta (z)


where :math:`u(x)` is the unit step function and :math:`\delta (x)` is the Dirac delta function.
By letting :math:`\Delta s \rightarrow ds`, the source current density for a harmonic electric dipole in the :math:`\hat x` direction is given by:

.. math::
	\mathbf{J(r)} = \hat x I ds \delta (x) \delta (y) \delta (z)


By analogy of the previous equation, the source current density for a harmonic electric dipole in any direction can be expressed as:

.. math::
	\mathbf{J(r)} = \mathbf{I}ds \, \delta (x) \delta (y) \delta (z) = \mathbf{p} \, \delta (x) \delta (y) \delta (z)



**Needs Image** with some description.




**Contents**

.. toctree::
    :maxdepth: 2

    analytic_solution
    asymptotics
    fields

