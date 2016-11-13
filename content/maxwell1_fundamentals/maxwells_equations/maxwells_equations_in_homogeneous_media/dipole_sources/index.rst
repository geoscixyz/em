.. _maxwells_equations_in_homogeneous_media_dipole_sources_index:

Maxwell's Equations for Dipole Sources
======================================

.. raw:: html
    :file: ../../../../../underconstruction.html


.. Purpose::

    In this section of EMgeosci, we will learn about dipole sources and the fields they generate in homogeneous media.
    For each dipole source:
    
    	- A physical model is supplied and used to formulate the corresponding source term in Maxwell's equations.
    	- Analytic expressions for the electric field, magnetic field and vector potential are then provided in both the frequency and time domains.
    	- Asymptotic expressions are provided for several cases.
    	- Numerical modeling tools are made available for investigating the dependency of the magnetic and electric fields on various parameters.



Dipole sources are fundamental electromagnetic sources which exist at a single point in space.
Although true dipole sources do not exist in nature, they do very well at approximating the electromagnetic sources used for many geophysical applications.
In geophysics, there are two types of dipole sources: electrical current dipole sources and magnetic dipole sources.

In matter, the electrical current dipole (:math:`\mathbf{p}`) generates a primary current density in the surrounding region; current does not flow in free-space.
This is illustrated in :numref:`DipolesFig` (left).
A magnetic dipole, on the other hand, generates a primary magnetic field in the surrounding region.
This is illustrated in :numref:`DipolesFig` (right).
Notice how the field lines converge at a single point in space for either source.


.. figure:: images/dipoles.png
		:align: center
		:figwidth: 100%
		:name: DipolesFig
		
		(Left) Electrical current dipole ( :math:`\mathbf{p}`) oriented in the :math:`\hat x` direction and the primary current density ( :math:`\mathbf{J}`) it produces. (Right) Magnetic dipole ( :math:`\mathbf{m}`) oriented in the :math:`\hat y` direction and the primary magnetic field ( :math:`\mathbf{H}`) it produces.


Both electrical current dipoles and magnetic dipoles can be represented as source terms in Maxwell's equations.
For the electrical current dipole, the source term (:math:`\mathbf{J_e}`) represents an electrical current density.
For the magnetic dipole, the source results from a magnetization (:math:`\mathbf{M}`).
However, the magetic source term (:math:`\mathbf{J_m} = - i\omega \mu \mathbf{M}`) is generally represented by a magnetic current density.
Physical descriptions of the electric and magnetic current densities were provided along with the :ref:`Ampere-Maxwell equation<ampere_maxwell>`.

In the presence of electromagnetic sources, Maxwell's equations in the frequency domain are given by:


.. math::
	\begin{split}
	\nabla \times \mathbf{E} + i \omega \mu \mathbf{H} &= \pm \, \mathbf{J_m}  \\
	\nabla \times \mathbf{H} - \sigma \mathbf{E} &= \pm \, \mathbf{J_e}
	\end{split}


where :math:`\pm` depends on a choice in sign convention.
Equivalent time-domain expressions can be obtained via inverse Fourier or inverse Laplace transform.

Ultimately, the right-hand side of :ref:`Faraday's law <faraday_differential_frequency>` becomes non-zero in the presence of a magnetic source.
And the right-hand side of the :ref:`Ampere-Maxwell law <ampere_maxwell_differential_frequency>` becomes non-zero in the presence of an electrical current source.


**Contents**

For each dipole source, we begin by presenting a physical model.
Analytic and asymptotic expressions along with numerical modeling tools are then provided for a harmonic dipole source.
A similar treatment is then provided for a transient dipole source.
Quick links to subsequent content are given below.


**Electrical Current Dipole**

.. toctree::
    :maxdepth: 2

    electric_dipole_definition/index
    electric_dipole_frequency/index
    electric_dipole_time/index


**Magnetic Dipole**

.. toctree::
    :maxdepth: 2
    
    magnetic_dipole_definition/index
    magnetic_dipole_frequency/index
    magnetic_dipole_time/index


