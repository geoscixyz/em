.. _frequency_domain_electric_dipole_index:

Harmonic Electrical Current Dipole
==================================


.. Purpose::

    Here, we provide a physical description of the harmonic electrical current dipole.
    This is used to develop a mathematical expression which can be used to replace the electrical source term in Maxwell's equations. 


The harmonic electrical current dipole source can be thought of as an infinitesimally short length of wire which carries a harmonic current.
In many cases, this type of source is referred to as the 'electric dipole source'; however a true electric dipole represents the polarization of electrical charges of opposite sign.

**Primary Current Density from a Finite Wire**


In order to develop a proper definition for the electrical current dipole, let us first consider the source current from a wire of finite length.
Assume the wire has length :math:`\Delta s` and carries a current :math:`I` which flows in the :math:`\hat x` direction along the wire.
Thus the source current density :math:`\mathbf{J (r)}` for the wire is given by:

.. math::
	\mathbf{J (r)} = \hat x I \Delta s \Bigg [ \frac{\textrm{u}\big (x + \frac{\Delta s}{2} \big ) - \textrm{u} \big ( x - \frac{\Delta s}{2} \big )}{\Delta s} \Bigg ] \delta (y) \delta (z)


.. figure:: images/E_source_finte_wire.png
		:align: right
		:figwidth: 50%
		:name: FiniteWire

        	Primary electrical current density due to a finite current-carrying wire.


where :math:`u(x)` is the unit step function and :math:`\delta (x)` is the Dirac delta function.
In Maxwell's equations, :math:`\mathbf{J (r)}` could be used to define an electrical source term.

As we can see from :numref:`FiniteWire`, the source generates a primary current density in the surrounding region.
Notice how the primary current density flows out one end of the wire and into the other.
Additionally, the current density is much larger near either end of the wire and decreases exponentially with distance.


**Defining the Electrical Current Dipole**

The electrical current dipole is defined by letting :math:`\Delta s \rightarrow ds`; making it a wire of infinitessimal length.
From the previous equation, the source current density for a harmonic electrical current dipole in the :math:`\hat x` direction is given by:

.. figure:: images/E_source_current_dipole.png
		:align: right
		:figwidth: 50%
		:name: CurrentDipole

        	Primary electrical current density due to an electrical current dipole.


.. math::
	\mathbf{J(r)} = \hat x I ds \delta (x) \delta (y) \delta (z)


By examining :numref:`CurrentDipole`, we see that the primary current density converges to a single point.
However, the primary current density still flows outwards from one side and into the other.


The strength of the electrical current dipole source is defined by a **dipole moment** (:math:`p`).
By definition from the previous equation, the dipole moment for an electrical current dipole has magnitude:

.. math::
	p = I ds
	

By considering an electrical current dipole oriented in an arbitrary direction, the source current becomes a vector (:math:`\mathbf{I}`).
Thus, the source current density for an electrical current dipole is given by:

.. math::
	\mathbf{J(r)} = \mathbf{I}ds \, \delta (x) \delta (y) \delta (z) = \mathbf{p} \, \delta (x) \delta (y) \delta (z)


where the dipole moment :math:`\mathbf{p}` has both magnitude and direction.






**Contents**

.. toctree::
    :maxdepth: 2

    analytic_solution
    asymptotics
    fields

