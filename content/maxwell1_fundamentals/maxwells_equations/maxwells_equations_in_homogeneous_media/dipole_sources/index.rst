.. _maxwells_equations_in_homogeneous_media_dipole_sources_index:

Maxwell's Equations for Dipole Sources
======================================

.. raw:: html
    :file: ../../../../../underconstruction.html


.. Purpose::

    In this section of EMgeosci, we present the concept of dipole sources and examine the fields they generate within homogeneous media.
    The intent of this material is to provide a fundamental understanding of the sources used in many geophysical applications.
    
    For each dipole source:
    
    	- Analytic expressions for the electric and magnetic fields are provided in both the frequency and time domains.
    	- Useful asymptotic expressions are provided for several cases.
    	- Numerical modeling tools are made available for investigating the dependency of the magnetic and electric fields on various parameters.



Dipole sources are fundamental electromagnetic sources which exist at a single point in space.
Although true dipole sources do not exist in nature, they do very well at approximating the electromagnetic sources used in many geophysical applications.
In geophysics, there are two types of dipole sources: electrical current dipole sources and magnetic dipole sources.

.. The electrical current dipole can be thought of as an infinitesimally short length of wire carrying an electrical current.
.. The magnetic dipole is generally interpreted as being a very small bar magnet (with both positive and negative poles) or a small loop of current which generates a magnetic field.




Something about "here are the free-space fields". The inclusion of physical properties and induction at higher frequencies will distort this field.



**Add images of the fields**


Both electrical current and magnetic dipoles can be represented as sources terms in Maxwell's equations.
For the electrical current dipole, the source term (:math:`\mathbf{J_e}`) represents an electrical current density (link?).
For the magnetic dipole, the source term (:math:`\mathbf{J_m}`) is described as a magnetic current density (link?).
By including electromagnetic source terms, Maxwell's equations in the frequency domain are given by:


.. math::
	\begin{split}
	\nabla \times \mathbf{E} + i \omega \mu \mathbf{H} &= \pm \, \mathbf{J_m}  \\
	\nabla \times \mathbf{H} - \sigma \mathbf{E} &= \pm \, \mathbf{J_e}
	\end{split}


where :math:`\pm` depends on a choice in sign convention.
Therefore, the right-hand side of Faraday's law (link?) becomes non-zero in the presence of a magnetic source.
And the right-hand side of Ampere's law (link?) becomes non-zero in the presence of an electrical current source.


**Contents**

For each dipole source, analytic expressions for the electric and magnetic fields are provided in both the frequency and time domains.
Useful asymptotic expressions are then provided for various cases.
Numerical modeling tools are also made available for investigating the dependency of the magnetic and electric fields on various parameters.
Quick links to subsequent content are given below.

.. toctree::
    :maxdepth: 2

    electric_dipole_frequency/index
    magnetic_dipole_frequency/index
    electric_dipole_time/index
    magnetic_dipole_time/index


