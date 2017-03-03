.. _definition_electric_dipole_index:

Defining the Electrical Current Dipole
======================================


.. Purpose::

    Here, we provide a physical description of the electrical current dipole.
    This is used to develop a mathematical expression which can be used to replace the electrical source term in Maxwell's equations. 


**General Definition**


.. figure:: images/E_source_current_dipole.png
		:align: right
		:figwidth: 50%
		:name: ElecDipole

        	Physical representation of the electrical current dipole source where :math:`\mathbf{p}` = 1 Am.



The electrical current dipole can be thought of as an infinitesimally short length of wire which carries a current.
The strength of the source is defined by its dipole moment (:math:`\mathbf{p}`).
This leads to an electrical source term of the form:

.. math::
	\mathbf{J_e^s} = \mathbf{p} \delta (x) \delta (y) \delta (z)
	:name: eq_Je_def


where :math:`\delta (x)` is the Dirac delta function.
The source is responsible for generating a primary current density (:math:`\mathbf{J}`) in the surrounding region; secondary electric and magnetic fields are discussed later.
This is illustrated in :numref:`ElecDipole`.
In many cases, the term 'electric dipole source' is used instead.
However, a true electric dipole represents the polarization of electrical charges of opposite sign.


**Wire Model for an Electrical Current Dipole**


In order to develop a more detailed definition for the electrical current dipole, let us first consider the source current from a wire of finite length.
Assume the wire has length :math:`\Delta s` and carries a current :math:`I` which flows in the :math:`\hat x` direction along the wire.
The source current density :math:`\mathbf{J_e^s}` for the wire segment is given by:

.. math::
	\mathbf{J_e^s} = \hat x I \Delta s \Bigg [ \frac{\textrm{u}\big (x + \frac{\Delta s}{2} \big ) - \textrm{u} \big ( x - \frac{\Delta s}{2} \big )}{\Delta s} \Bigg ] \delta (y) \delta (z)
	:name: eq_Je_wire



where :math:`u(x)` is the unit step function.
In Maxwell's equations, :math:`\mathbf{J_e (r)}` defines the electrical source term and has units A/m :math:`\!^2`.

As we can see in :numref:`FiniteWire`, the source generates a primary current density (:math:`\mathbf{J}`) in the surrounding region.
Notice how the current flows out one end of the wire and into the other (:numref:`FiniteWire` left).
However, when the wire segment is much smaller than the scale of observation (:math:`\Delta s \ll r`), then it appears as though the current density converges to a single point; see :numref:`FiniteWire` (right).
The purpose of the electrical current dipole is to approximate a finite wire segment when observation scales are much larger than the wire's length. 
The electrical current dipole accomplishes this by defining a source term which exists at a single point in space.



.. figure:: images/E_source_finte_wire.png
		:align: center
		:figwidth: 100%
		:name: FiniteWire

        	Electrical current density due to a finite current-carrying wire. Long wire (left). Short wire (right). For both wires, the current was adjusted so that :math:`I\Delta s` = 1 Am.





The electrical current dipole source is defined by letting :math:`\Delta s \rightarrow ds` in the previous equation; making it a wire of infinitessimal length.
As a result, the source current density for a harmonic electrical current dipole in the :math:`\hat x` direction is given by:

.. figure:: images/E_source_current_dipole.png
		:align: right
		:figwidth: 50%
		:name: CurrentDipole

        	Primary electrical current density due to an electrical current dipole with :math:`\mathbf{p}` = 1 Am.


.. math::
	\mathbf{J_e^s} = \hat x I ds \delta (x) \delta (y) \delta (z)
	:name: eq_Je_xdip


Examining :numref:`CurrentDipole`, we see that the current density in the surrounding region converges to a single point; just like in :numref:`FiniteWire` (right).
However like a finite wire segment, the current still flows outwards from one side of the source and into the other.


If we consider an electrical current dipole oriented in an arbitrary direction, the source current becomes a vector :math:`\mathbf{I}`.
Thus, the source current density for an electrical current dipole is given by:

.. math::
	\mathbf{J_e^s} = \mathbf{I}ds \, \delta (x) \delta (y) \delta (z)
	:name: eq_Je_xdipI




The strength of the electrical current dipole source is defined by its dipole moment (:math:`\mathbf{p}`).
As we can see from the previous equation, the source term depends on the product :math:`\mathbf{I} ds`.
Thus the dipole moment for an electrical current dipole source is given by:

.. math::
	\mathbf{p} = \mathbf{I}ds
	:name: eq_Je_p_def
	

where


.. math::
	\mathbf{J_e^s} = \mathbf{p} \, \delta (x) \delta (y) \delta (z)
	:name: eq_Je_rdip


From our definition of the electrical current dipole, :math:`\mathbf{p}` has units Am, each of the Dirac delta functions carry units m :math:`\!^{-1}`, and thus :math:`\mathbf{J_e^s}` has units A/m :math:`\!^2`.





