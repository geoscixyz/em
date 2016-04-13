.. _physical_properties_index:

Physical Properties
===================


..ToDo::
	Iconic image: ? Geologic volume with an outlined prism; Then a connecting image of a lab setup and a list of the four physical properties that we are interested in.


**Purpose**
Physical properties form the connecting link between geophysics and the geologic or engineering problems that are to be solved. Here we compile values for these physical properties as a function of rock type, mineral composition and saturating fluids. Background about how the laboratory measurements are made and the connection with constitutive relationships are presented. Each section begins with examples for where the particular physical property has been diagnostic.



Overview
--------

..ToDo::
	An example figure for each of the physial properties below. These will be reused in the opening pages for each property. (possible candidates? including a transmitter/receiver; a geologic map or volumetric model with asought structure)
	Conductivity: ? photo of airborne EM system with saltwater intrusion
	Chargeability: ? ip survey system overtop a porphyry target. ()
	Magnetic susceptibility: airborne magnetometer flying over a geology map with a buried deposit
	Electrical permittivity: gpr system trying to detect metal pipes

In geophysics we characterize materials by their physical properties. For these to be useful in problem solving, the physical property of the target body or sought geologic structure must be significantly different the background host material. The relevant properties for electromagnetics are:

 - :ref:`electrical_conductivity_index`: :math:`\sigma` (or its reciprocal, resistivity, :math:`\rho`)
 - :ref:`magnetic_permeability_index`: :math:`\mu`
 - :ref:`electrical_permittivity_index`, :math:`\varepsilon`

A physical property quantifies how a rock responds to a particular input and
it therefore connects a forcing field to a resulting flux. Typically the
laboratory experiments are carried out in the frequency domain and the
resultant constitutive relationships are given by:

 - :math:`\mathbf{J}(\omega)= \sigma \mathbf{E}(\omega)`  where `mathbf{J}` is the electric current density and `mathbf{E}` is the electric field. This relationship is known as Ohm's Law.
 - :math:`\mathbf{B}(\omega)= \mu \mathbf{H}(\omega)` where `mathbf{B}` is the magnetic flux density and `mathbf{H}` is the magnetic field intensity.
 - :math:`\mathbf{D}(\omega)= \varepsilon \mathbf{E}(\omega)` where `mathbf{D}` is the electric displacement and `mathbf{E}` is the electric field.

Physical properties can be tensors, for example :math:`J=\Sigma E` where
:math:`\Sigma` is a 3x3 tensor. Or the properties can be dispersive, that is,
frequency dependent. If expressions of the constitutive relations in time are
needed then application of the Fourier transform yields

 - :math:`\mathbf{j}(t)=\sigma(t) \ast \mathbf{e}(t)`
 - :math:`\mathbf{b}(t)=\mu(t) \ast \mathbf{h}(t)`
 - :math:`\mathbf{d}(t)=\varepsilon(t) \ast \mathbf{e}(t)`

The constitutive relations, along with Maxwell's equations,  form a complete set of equations for electromagnetics.

In this section we present basic material regarding the various physical properties. For each property we provide:

- examples {links} to applications
- constitutive relationship and laboratory experiment
- Useful tables
- Additional information
- References





**Contents:**

.. toctree::
    :maxdepth: 1

    electrical_conductivity/index
    magnetic_permeability/index
    electrical_permittivity/index
    constitutive_relations/index





