.. _maxwells_equations_in_homogeneous_media_dipole_sources_index:

Maxwell's Equations for Dipole Sources
======================================

.. raw:: html
    :file: ../../../../../underconstruction.html


.. topic:: Purpose

    In this section of EMgeosci, we present the concept of dipole sources and examine the fields they generate within homogeneous media.
    The intent of this material is to provide a fundamental understanding of the sources used in many geophysical applications.
    For each dipole source, analytic expressions for the electric and magnetic fields are provided in both the frequency and time domains.
    Numerical modeling tools are also made available for investigating the dependency of the magnetic and electric fields on various parameters.


Dipole sources are fundamental electromagnetic sources which exist at a single point in space.
In geophysics, there are generally two types of dipole sources: electrical current dipole sources and magnetic dipole sources.
Although true dipole sources do not exist in nature, they do very well at approximating the electromagnetic sources used in many geophysical applications.
On this page, we will focus on defining the term dipole source and show how dipole sources can be represented within Maxwell's equations.


.. math::
	\begin{split}
	\nabla \times \mathbf{E} + i \omega \mu \mathbf{H} &= \pm \, \mathbf{J_m}  \\
	\nabla \times \mathbf{H} - \sigma \mathbf{E} &= \pm \, \mathbf{J_e}
	\end{split}










**Organization of sections here**





**Contents**

.. toctree::
    :maxdepth: 2

    electric_dipole_frequency/index
    magnetic_dipole_frequency/index
    electric_dipole_time/index
    magnetic_dipole_time/index


