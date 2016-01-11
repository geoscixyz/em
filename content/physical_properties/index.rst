.. _physical_properties_index:

Physical Properties
===================

In geophysics we characterize materials by their physical properties. The relevant  properties for electromagnetics are:
-electrical conductivity sigma (or its reciprocal, resistivity)
-chargeability (a parameter that characterizes how electrical conductivity depends upon frequency)
-magnetic permeabilty 
-electrical permittivity

A physical property quantifies how a rock responds to a particular input and it therefore connects a forcing field to a resulting flux. Typically the laboratory experiments are carried out in the frequency domain and the resultant distributive relationships are given by:
J(w)= sigma E(w)  (Ohm's Law)
B(w)= mu H(w)
D(w)= epsilon E(w)

Physical properties can be tensors, for example   J=Sigma E where Sigma is a 3x3 tensor. Or the properties can be dispersive, that is, frequency dependent. If expressions of the constitutive relations in time are needed then application of the Fourier transform yields
j(t)=sigma(t) conv e(t)
b(t)=mu(t) conv h(t)
d(t)=epsilon(t) conv e(t)

The constitutive relations, along with Maxwell's equations,  form a complete set of equations for electromagnetic. 

In this section we present basic material regarding the various physical properties. For each property we provide:
-laboratory experiment
-Useful tables
-Additional information 
-References 



**Contents:**

.. toctree::
    :maxdepth: 1

    physical_properties_electrical_conductivity
    physical_properties_chargeability
    physical_properties_magnetic_permeability
    physical_properties_electrical_permittivity

