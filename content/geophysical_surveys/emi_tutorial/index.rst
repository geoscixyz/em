.. _emi_tuotorial_index:

EM induction tutorial
=====================

The fundamental principles of electromagnetic (EM) induction can be understood with a simple geometry involving three elements each represented by a loop of conducting wire as shown in :numref:`Concepts_3loops`.

- Loop1: is the transmitter. It carries a current that produces an associated magnetic field. This magnetic field is called the primary field. For induction experiments the current in the transmitter varies with time and hence the magnetic field varies with time.

- Loop 2: represents a conductive body. The  time varying magnetic field generates an  Electromotive Force (EMF) and hence a current in the conductor. These are called secondary currents. The generate secondary magnetic fields.

- Loop 3: is the receiver: This measures magnetic field which consists of the sum of the primary and secondary fields.

.. figure:: ./figures/Concepts_3loops.png
   :align: center
   :scale: 60%
   :name: Concepts_3loops

   Conceptual diagrams for EM inductions. Top panel shows excitation of the conductor using induction, and botton panel shows corresponding 3-loops system.

.. note::
	Geophysical goal: remove the primary field from the measurements and interpret the data to find information about the buried conductor.

Goals for this tutorial:

	- Show how the above process can be explained in terms of and RL  electric circuits
	- Derive and  understand the  inductive response function
	- Introduce self- and mutual inductances
	- Illustrate the concept of “coupling”
	- Provide the final expression which encapsulated both coupling and induction responses.
	- Provide an interactive notebook in which the above goals can be crystallized. (350)

Contents:
---------

.. toctree::
    :maxdepth: 1

    induced_currents_body


