.. _reflection_and_refraction_index:

Plane Waves at Interfaces
=========================

.. purpose::

    Here, we provide theory for describing the behaviour of plane waves as they reach physical property interfaces. Reflection, refraction and transmission are discussed.


.. figure:: images/LayeredEarth.gif
   :align: right
   :figwidth: 35%
   :name: reflections_example_index

   Reflection, refraction and transmission of a ground penetrating radar signal.

**Introduction**

When EM waves reach an interface characterized by an abrupt change in physical properties, portions of the signal undergo reflection, refraction and transmission. In :numref:`reflections_example_index`, we show these behaviours for a :ref:`ground penetrating radar<gpr_index>` signal. A fundamental understanding of reflection, refraction and transmission can be obtained by considering plane waves. Here, we provide theory which describes the behaviour of plane waves as they interact with physical property interfaces. Numerical modeling apps are provided to simulate these behaviours.

**Organization**

The content within this portion is organized into 3 parts:

	- :ref:`Reflection and Snell's Law<Snells_law>`: Defines the relationship between the propagation directions of incident, reflected and refracted EM waves.
	- :ref:`Fresnel Equations<Fresnel_equations>`: Defines the relationships between the propagation directions and amplitudes of incident, reflected, refracted and transmitted EM waves.
	- N-Layer Earth: After characterizing the behaviours of plane waves at a single interface, we extend the theory to a layered Earth model.

**Contents**

.. toctree::
    :maxdepth: 2

    Snells_law
    Fresnel_equations
    totalrefl_and_brewsterangl
    impedance_layeredearth

