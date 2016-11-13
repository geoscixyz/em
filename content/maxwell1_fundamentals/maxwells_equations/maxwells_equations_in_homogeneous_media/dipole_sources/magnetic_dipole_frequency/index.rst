.. _frequency_domain_magnetic_dipole_index:

Harmonic Magnetic Dipole
========================

.. Purpose::

    Here, we provide a physical description of the harmonic magnetic dipole.
    This is used to develop a mathematical expression which can be used to replace the magnetic source term in Maxwell's equations.



The harmonic magnetic dipole can be thought of as an infinitessimally small loop which carries a harmonic current.
The strength of the source is therefore defined by a harmonic dipole moment :math:`\mathbf{m}(\omega)`.
For a harmonic magnetic dipole defined by vector surface area :math:`\mathbf{S}` and harmonic current :math:`I(\omega) = I e^{i\omega t}`, the dipole moment is given by:


.. figure:: images/H_source_magnetic_dipole.png
		:align: right
		:figwidth: 50%
		:name: MagDipole
		
		Physical representation of the magnetic dipole source where :math:`\mathbf{m}` = 1 Am :math:`\!^2`.


.. math::
	\mathbf{m} (\omega) = \mathbf{m} \, e^{i\omega t} = I \mathbf{S} \, e^{i\omega t}
	

where :math:`\mathbf{m} = I \mathbf{S}` is the vector amplitude of the dipole moment.
When formulating Maxwell's equations in the frequency domain, :math:`e^{i\omega t}` is generally suppressed.
As a result, the source term for the harmonic magnetic dipole is given by:


.. math::
	\mathbf{J_m (r)} = -I\mathbf{S} \, \delta (x) \delta (y) \delta (z)


where :math:`\delta (x)` is the Dirac delta function.
By including the source term, Maxwell's equations in the frequency domain are given by:


.. math::
	\begin{split}
	\nabla \times \mathbf{E} &+ i \omega \mu \mathbf{H} = - I \mathbf{S} \, \delta(x) \delta(y) \delta(z)  \\
	&\nabla \times \mathbf{H} - \sigma \mathbf{E} = 0
	\end{split}



The source is responsible for generating a primary magnetic field in the surrounding region (:numref:`ElecDipole`).
According to :ref:`Faraday's law<faraday_differential_frequency>`, the harmonic nature of the primary magnetic field generates rotational electric fields.
In matter, this leads to an induced current density which produces secondary magnetic fields according to the :ref:`Ampere-Maxwell equation<ampere_maxwell_differential_frequency>`.
In the following section, we solve Maxwell's equations for a harmonic magnetic dipole source and provide analytic expressions for the electric and magnetic fields within a homogeneous medium.






**Contents**

.. toctree::
    :maxdepth: 2

    analytic_solution
    asymptotics
    fields
