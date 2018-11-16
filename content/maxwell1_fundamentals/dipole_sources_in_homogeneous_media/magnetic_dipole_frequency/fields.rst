.. _frequency_domain_magnetic_dipole_fields:

Visualization of the Electromagnetic Fields
===========================================

.. Purpose::

    Here, we provide numerical modeling tools for visualizing the electric field, magnetic field and current density caused by a magnetic dipole source.
    A set of questions about the fields and their dependency on various parameters are then presented as a learning exercise.
    By completing this exercise, you will become comfortable with the numerical modeling tools provided and gain a fundamental understanding of the fields which are caused by a harmonic magnetic dipole.


**Link to the app**

Research Questions
------------------

Here, a set of questions about the fields and their dependency on various parameters are presented as a learning exercise.
The user is encouraged to answer these questions in order, as we begin with simple cases and move to cases with more challenging physics.
The user is also encouraged to use analytic and asymptotic expressions as a reference when completing the exercise.
 

**DC (Static) Case:**

For the DC case, ensure that the frequency is set to 0 Hz. When answering the following questions, examine the x, y and z components of the electric field, magnetic field and current density. The vector plot is recommended.

	- In this case, is there a non-zero electric field and/or current density?
	- Does the magnetic field have any radial components?
	- Does the magnetic field have any quadrature (imaginary) components?
	- Do any aspects of the magnetic field change when you alter the physical properties of the medium?
	- Do your observations make sense when considering the :ref:`DC approximation<frequency_domain_magnetic_dipole_asymptotics_DC>`?

**Near-Field Approximation:**

Now set the conductivity of the background to 1 S/m and set the frequency to 1 Hz. According to our asymptotic approximations, the :ref:`near-field<frequency_domain_magnetic_dipole_asymptotics_near>` (:math:`| kr | \ll 1`) the magnetic field should behave like the DC case and the electric field should have only quadrature (imaginary) components.

	- Examine the electric and magnetic fields. Do your observations compare well to what your would expect?
	- Increase the frequency by a factor of 10. Does the strength of the magnetic field change? Does the strength of the electric field change? Does this make sense when considering the near-field approximations?
	- Are the induced electric fields rotational about the dipole?

Now slowly increase the frequency by factors of 10. When you reach 1000 Hz, notice that at sufficient distance from the dipole, the near-field approximation is no longer valid. However near the dipole source, the fields more or less behave like DC fields.

	- At what distance is the near-field approximation no longer valid at 1000 Hz? Use this value to confirm that :math:`| kr | \ll 1`.

**The Inductive Response:**

According to :ref:`Faraday's law<faraday>`, the effects of EM induction increase as frequency increases. Set the conductivity to 0.1 S/m and choose a point (x,y,z) = (40m, 0m, 0m). Examine the x,y and z components of the electric and magnetic fields.

	- At what frequency do the effects of EM induction become significant?
	- Now increase the background conductivity to 1 S/m and examine the same location. At what frequency do the effects of EM induction become significant?
	- Now choose a location closer to the dipole source (x,y,z) = (10m, 0m, 0m). At what frequency do the effects of EM induction become significant compared to the primary field?

**Magnetic Permeability and Dielectric Permittivity**

Set the log-conductivity to 0.01 S/m.

	- Try increasing the relative permeability (:math:`\mu_r`). Do you notice any significant changes in the shape and amplitude of the electric and magnetic fields?
	- Now try increasing the relative permittivity (:math:`\varepsilon_r`). When you do this at low frequencies, do you notice any significant changes in the shape and amplitude of the electric and magnetic fields? How about when you do this at high frequencies?






