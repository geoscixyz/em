.. _physical_properties_index:

Physical Properties
===================

In geophysics we characterize materials by their physical properties. The
relevant  properties for electromagnetics are:

 - electrical conductivity, :math:`\sigma` (or its reciprocal, resistivity, :math:`\rho`)
 - chargeability (a parameter that characterizes how electrical conductivity depends upon frequency)
 - magnetic permeability, :math:`\mu`
 - electrical permittivity, :math:`\varepsilon`

A physical property quantifies how a rock responds to a particular input and
it therefore connects a forcing field to a resulting flux. Typically the
laboratory experiments are carried out in the frequency domain and the
resultant distributive relationships are given by: 

 - :math:`\mathbf{J}(\omega)= \sigma \mathbf{E}(\omega)`  (Ohm's Law) 
 - :math:`\mathbf{B}(\omega)= \mu \mathbf{H}(\omega)` 
 - :math:`\mathbf{D}(\omega)= \varepsilon \mathbf{E}(\omega)`

Physical properties can be tensors, for example :math:`J=\Sigma E` where
:math:`\Sigma` is a 3x3 tensor. Or the properties can be dispersive, that is,
frequency dependent. If expressions of the constitutive relations in time are
needed then application of the Fourier transform yields

 - :math:`\mathbf{j}(t)=\sigma(t) \ast \mathbf{e}(t)`
 - :math:`\mathbf{b}(t)=\mu(t) \ast \mathbf{h}(t)`
 - :math:`\mathbf{d}(t)=\varepsilon(t) \ast \mathbf{e}(t)`

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

