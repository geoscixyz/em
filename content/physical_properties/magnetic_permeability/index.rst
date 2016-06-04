.. _magnetic_permeability_index:

Magnetic Permeability
=====================

Magnetic permeability is an important diagnostic physical property in geophysics.
In addition to compositional differences, rocks and other objects may be differentiated by their magnetic permeabilities.
In mineral exploration, contrasts in magnetic permeabilities between rock types can be exploited to recover subsurface geological structures.
Contrasts in magnetic permeability have also been used to locate unexploded ordnance items; as their casings are significantly more permeable than the medium in which they are buried.

Formal Definition
-----------------

When exposed to an applied magnetic field, the collection of individual magnetic dipole moments within most materials will attempt to reorient themselves along the direction of the field.
This generates an induced magnetization, which contributes towards the net magnetic flux density inside the material.
The degree in which the induced magnetization impacts the magnetic flux density depends on the material's magnetic permeability.

  .. figure:: ./images/figBvsHillustr.png
    :name: BvsHillustr
    :figwidth: 45%
    :align: right

    Magnetic flux density as a function of magnetic field intensity for various classifications of permeable rock types: diamagnetic, vacuum, paramagnetic, and ferromagnetic.

Magnetic permeability :math:`\mu` defines the ratio between the magnetic flux density :math:`{\bf B}` within a material, and the intensity of an applied magnetic field :math:`{\bf H}`; provided the fields are sufficiently weak:

.. math::
	{\bf B}(\omega) = \mu \, {\bf H}(\omega)
	:label: Const_Rel_Flux

In a vacuum, the relationship between :math:`{\bf B}` and :math:`{\bf H}` is given by the permeability of free-space :math:`\mu_0 = 4\pi \times 10^{-7}` T :math:`\!\cdot\!` m/A.
An illustration representing the magnetic flux density as a function of the applied field strength for various rock classifications is shown here.




Relative Permeability
---------------------

In addition to the magnetic permeability, magnetic properties are frequently represented using the relative permeability.
Relative permeability characterizes whether the induced magnetization increases or reduces the density of magnetic flux within a material.
The relative premeability :math:`\mu_r` is the ratio between the magnetic permeability of a material and the premeability of free-space:

.. math::
	\mu_r = \frac{\mu}{\mu_0}
	:label: Rel_Permeability

For the majority of rocks, induced magnetization is parallel to the applied field, thus adding to the density of magnetic flux.
These rocks are characterized by relative permeabilities :math:`\mu_r > 1`.
A relative permeability of :math:`\mu_r = 1` is used to characterize materials which are incapable of supporting induced magnetization.
In rare cases, a very small magnetization can be induced in rocks, which opposes the applied field, and reduces the density of magnetic flux.
These rocks are characterized by magnetic permeabili3810 characters, 495 words, 78 linesties :math:`\mu_r < 1`.
The partial alignment of magnetic dipole moments under an applied field, and the resulting magnetic flux densities in all three cases, are represented in the figure below.

.. figure:: ./images/figMagFluxDensity.png
	:align: center
        :scale: 70%

	Partial alignment of magnetic dipole moments under the influence of an applied magnetic field for various cases. (a) Paramagnetic (:math:`\mu_r > 1`).
	Magnetization is parallel to the applied field and increases the density of magnetic flux. (b) Non-permeable (:math:`\mu_r = 1`).
	Does not support induced magnetization. (c) Diamagnetic (:math:`\mu_r < 1`). Magnetization is weak and opposes the applied magnetic field, thus reducing the density of magnetic flux.



**Contents:**

 .. toctree::
    :maxdepth: 2

    magnetic_permeability_lab_measurements
    magnetic_permeability_units
    magnetic_permeability_values
    magnetic_permeability_magnetism
    magnetic_permeability_factors
    magnetic_permeability_frequency_dependent



References:

Rock and Mineral Properties: Keller SEG Vol 1 Electromagnetic Methods in Applied Geophysics

Griffiths, David J., "Introduction to Electrodynamics", 3rd Ed., Prentice Hall, 1999.
