.. _frequency_domain_electric_dipole_index:

Harmonic Electrical Current Dipole
==================================


.. Purpose::

    In the frequency domain, we consider harmonic electric and magnetic fields.
    Here, we provide a physical description of the harmonic electrical current dipole.
    This is used to develop a mathematical expression which can be used to replace the electrical source term in Maxwell's equations. 



**General Definition**


.. figure:: images/E_source_current_dipole.png
		:align: right
		:figwidth: 50%
		:name: CurrentWire

        	Physical representation of the harmonic electrical current dipole source where :math:`\mathbf{p}` = 1 Am.



The harmonic electrical current dipole can be thought of as an infinitesimally short length of wire which carries a harmonic current.
The strength of the source is therefore defined by a harmonic dipole moment :math:`\mathbf{p}(\omega)`.
For a harmonic current dipole defined by length :math:`ds` and harmonic current :math:`\mathbf{I} (\omega) = \mathbf{I}e^{i\omega t}`, the dipole moment is given by:



.. math::
	\mathbf{p}(\omega) = \mathbf{p} \, e^{i\omega t} = \mathbf{I} ds \, e^{i\omega t}
	:name: p_harmonic_def


where :math:`\mathbf{p} = \mathbf{I}ds` is the vector amplitude of the dipole moment.
When formulating Maxwell's equations in the frequency domain, :math:`e^{i\omega t}` is generally suppressed.
As a result, the source term for the harmonic electrical current dipole is given by:


.. math::
	\mathbf{J_e^s} = \mathbf{I}ds \, \delta (x) \delta (y) \delta (z)
	:name: Je_harmonic_def


where :math:`\delta (x)` is the Dirac delta function.
By including the source term, Maxwell's equations in the frequency domain are given by:


.. math::
	\begin{split}
	&\nabla \times \mathbf{E_e} + i \omega \mu \mathbf{H_e} = 0  \\
	\nabla \times \mathbf{H_e} - & (\sigma  + i\omega \varepsilon ) \mathbf{E_e} = \mathbf{I}ds \, \delta(x) \delta(y) \delta(z)
	\end{split}
	:name: p_Maxwells_harmonic



where subscripts :math:`_e` remind us that we are considering an electric source.
The source current is responsible for generating a primary current density (and thus an electric field) in the surrounding region (:numref:`ElecDipole`).
However, the :ref:`Ampere-Maxwell equation<ampere_maxwell_differential_frequency>` states that harmonic electric fields as well as free currents generate magnetic fields.
In addition, the harmonic nature of the magnetic fields should produce secondary electric fields according to :ref:`Faraday's law<faraday_differential_frequency>`.


**Organization**

In the following section, we solve Maxwell's equations for a harmonic electrical current dipole source and provide analytic expressions for the electric and magnetic fields within a homogeneous medium.
Asymptotic expressions are then provided for several cases.
Numerical modeling tools are made available for investigating the dependency of the electric and magnetic fields on various parameters.


.. toctree::
    :maxdepth: 2

    analytic_solution
    asymptotics
    fields

