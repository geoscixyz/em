.. _physical_properties_index:

Physical Properties
===================

.. purpose::

    Generate a resource that has a commpilation of values for physical
    properties as a function of rock type, mineral composition and saturating
    fluids. Background about how the laboratory measurements are made and the
    connection with constitutive relationships are presented. Each section
    will begin with examples for where the particular physical property has
    been diagnostic.



In geophysics, we characterize materials by their physical properties. The
relevant  properties for electromagnetics are:

- :ref:`electrical_conductivity_index`: :math:`\sigma` (or its reciprocal, resistivity, :math:`\rho`)
- :ref:`magnetic_permeability_index`, :math:`\mu`
- :ref:`dielectric_permittivity_index`, :math:`\varepsilon`

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

The constitutive relations, along with :ref:`Maxwell's equations <quick_guide_maxwell>`,  form a complete set of equations for electromagnetics.

In this section, we present basic material regarding the various physical properties. For each property, we provide:

- Examples to applications
- Constitutive relationship and laboratory experiment
- Useful tables
- Additional information
- References





**Contents:**

.. toctree::
    :maxdepth: 1

    electrical_conductivity/index
    magnetic_permeability/index
    dielectric_permittivity/index



