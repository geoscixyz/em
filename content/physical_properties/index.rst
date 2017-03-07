.. _physical_properties_index:

Physical Properties
===================

.. purpose::

    To generate a resource that has a compilation of values for physical
    properties as a function of rock type, mineral composition and saturating
    fluids. Background about how the laboratory measurements are made and the
    connection with constitutive relationships are presented. Each section
    will begin with examples for where the particular physical property has
    been diagnostic.

A physical property quantifies how a rock responds to a particular physical input. In electromagnetic geophysics, the relevant physical properties are:

- :ref:`electrical_conductivity_index`: :math:`\sigma` (or its reciprocal, resistivity, :math:`\rho`)
- :ref:`magnetic_permeability_index`, :math:`\mu`
- :ref:`dielectric_permittivity_index`, :math:`\varepsilon`

Electromagnetic physical properties are defined using a set of constitutive relationships. Each constitutive relationship characterizes the resulting flux due to a causative forcing field. In most cases, laboratory measurements are performed in the frequency domain, but they can be performed in the time domain. If the physical properties are non-dispersive, the relationship between the field and the corresponding flux is independent of frequency. Thus the constitutive relationships are given by:

- :math:`\mathbf{J}(\omega)= \sigma \mathbf{E}(\omega)`  (Ohm's Law)
- :math:`\mathbf{B}(\omega)= \mu \mathbf{H}(\omega)`
- :math:`\mathbf{D}(\omega)= \varepsilon \mathbf{E}(\omega)`

By taking the inverse Fourier transform, the corresponding time domain relationships are given by:

- :math:`\mathbf{j}(t)= \sigma \mathbf{e}(t)`  (Ohm's Law)
- :math:`\mathbf{b}(t)= \mu \mathbf{g}(t)`
- :math:`\mathbf{d}(t)= \varepsilon \mathbf{e}(t)`

**Dispersion**

Dispersion implies that a given physical property is frequency-dependent. Electrical conductivity, magnetic permeability and dielectric permittivity all exhibit dispersive properties under various conditions. For dispersive physical properties, the constitutive relationships are given by:

- :math:`\mathbf{J}(\omega)= \sigma (\omega) \mathbf{E}(\omega)`  (Ohm's Law)
- :math:`\mathbf{B}(\omega)= \mu (\omega) \mathbf{H}(\omega)`
- :math:`\mathbf{D}(\omega)= \varepsilon (\omega) \mathbf{E}(\omega)`

Once again, the time domain equivalent for the constitutive relationships can be obtained by taking the inverse Fourier transform. If the physical properties are dispersive, the relationship between each field and its corresponding flux becomes a convolution:

- :math:`\mathbf{j}(t)=\sigma(t) \ast \mathbf{e}(t)`
- :math:`\mathbf{b}(t)=\mu(t) \ast \mathbf{h}(t)`
- :math:`\mathbf{d}(t)=\varepsilon(t) \ast \mathbf{e}(t)`

**Anisotropy**

Anisotropy means that the physical response of a rock to an applied field is not the same in all directions. In this case, each field and is corresponding flux is related by a 3X3 tensor:

- :math:`\mathbf{J}= \Sigma \mathbf{E}`
- :math:`\mathbf{B}= \Gamma \mathbf{H}`
- :math:`\mathbf{D}= \Upsilon \mathbf{E}`

where

.. math::
    \Sigma = \begin{bmatrix} \sigma_{xx} & \sigma_{xy} & \sigma_{xz} \\ \sigma_{yx} & \sigma_{yy} & \sigma_{yz} \\ \sigma_{zx} & \sigma_{zy} & \sigma_{zz} \end{bmatrix} , \; \;
    \Gamma = \begin{bmatrix} \mu_{xx} & \mu_{xy} & \mu_{xz} \\ \mu_{yx} & \mu_{yy} & \mu_{yz} \\ \mu_{zx} & \mu_{zy} & \mu_{zz} \end{bmatrix} \; \; \textrm{and} \; \;
    \Upsilon = \begin{bmatrix} \varepsilon_{xx} & \varepsilon_{xy} & \varepsilon_{xz} \\ \varepsilon_{yx} & \varepsilon_{yy} & \varepsilon_{yz} \\ \varepsilon_{zx} & \varepsilon_{zy} & \varepsilon_{zz} \end{bmatrix} , \; \;

The constitutive relations, along with :ref:`Maxwell's equations <quick_guide_maxwell>`,  form a complete set of equations for electromagnetics. In this section, we present basic material regarding the various physical properties. For each property, we provide:

- the constitutive relationship, a physical descriptions and its relevance to electromagnetic geoscience
- a description of common laboratory measurement techniques
- tables containing a typical range of values
- a list of factor which control the physical property value
- references

**Contents:**

.. toctree::
    :maxdepth: 1

    electrical_conductivity/index
    magnetic_permeability/index
    dielectric_permittivity/index



