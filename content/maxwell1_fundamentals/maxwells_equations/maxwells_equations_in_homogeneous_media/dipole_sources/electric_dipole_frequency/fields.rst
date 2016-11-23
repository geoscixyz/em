.. _frequency_domain_electric_dipole_fields:

Visualization of the Electromagnetic Fields
===========================================

.. Purpose::

    Here, we provide numerical modeling tools for visualizing the electric field, magnetic field and current density caused by an electrical current dipole source.
    A set of questions about the fields and their dependency on various parameters are then presented as a learning exercise.
    By completing this exercise, you will become comfortable with the numerical modeling tools provided and gain a fundamental understanding of the fields which are caused by a harmonic electrical current dipole.



Introduction
------------

Here, we will show you how to use the widget and walk you through some research questions.



**Simple instructions on how to open it and get it running**

Within the jupyter notebook, there are 3 tools:


.. figure:: images/E_source_widget_geometry.png
		:align: right
		:figwidth: 50%
		:name: widget_geometry

		Visualization of problem geometry in 3D.


**Step 1: Choosing Geometric Parameters**

These toggles allow the user to adjust the problem geometry and visualize it in 3D.
Relative to the source dipole, the user may specify observation locations on a profile line or comprising a plane.
An example of the problem geometry is shown on the right.


**Step 2: Visualizing the Fields**

These toggles allow the user to change physical parameters relevant to the problem and visualize different components of the electric field, magnetic field and current density.
As any of the physical parameters or plotting parameters are changed, the fields are automatically plotted on the profile line and plane defined in Step 1.
An example of the fields on a profile line and on a plane is shown below.


.. figure:: images/E_source_plane_example.png
		:align: center
		:figwidth: 100%
		:name: field_example

		Visualization of the fields. (Left panel) Vector plot of :math:`E_x` at locations on a plane. (Right panel) In-phase component of :math:`E_x` along a profile line.


Research Questions
------------------

Here, a set of questions about the fields and their dependency on various parameters are presented as a learning exercise.
The user is encouraged to answer these questions in order, as we begin with simple cases and move to cases with more challenging physics.
The user is also encouraged to use analytic and asymptotic expressions as a reference when completing the exercise.
 

**DC (static) Case:**

For the DC case, ensure that the frequency is set to 0 Hz. When answering the following questions, examine the x, y and z components of the electric field, magnetic field and current density.

	- Do the electric field, magnetic field or current density have a quadrature (imaginary) components?
	- Does the magnetic field have any components along the orientation of the dipole?
	- When you alter the conductivity (:math:`\sigma`), does the shape of the electric or magnetic field change? Does the magnitude change?
	- When you alter the conductivity (:math:`\sigma`), does anything about the current density change? (note that :math:`\mathbf{J = \sigma E}`)
	- Do your observations make sense when considering the :ref:`DC approximation<frequency_domain_electric_dipole_asymptotics_DC>`?


*Could add 1 image each for the DC electric field and magnetic field on a plane*

**Near-Field Approximation:**

Now set the log-conductivity of the background to 0 and leave the frequency at 0 Hz. According to our asymptotic approximations, the :ref:`near-field<frequency_domain_electric_dipole_asymptotics_near>` should behave like the :ref:`DC field<frequency_domain_electric_dipole_asymptotics_DC>`.



*Images showing DC field, lower frequency and higher frequency fields (Choose E or H). They should demonstrate the distance at which the near-field is valid.*


**The Inductive Response:**



*Show real and imaginary components at low, medium and high frequency. Should contain vector lines to show direction information.*

**Magnetic Permeability and Dielectric Permittivity**

Set the log-conductivity to .


	- Try increasing the relative permeability (:math:`\mu_r`). Do you notice any significant changes in the shape and amplitude of the electric and magnetic fields?
	- Now try increasing the relative permittivity (:math:`\varepsilon_r`). When you do this at low frequencies, do you notice any significant changes in the shape and amplitude of the electric and magnetic fields? How about when you do this at high frequencies?


**Hypothetical Scenario 1:**

*I put this here in case we wanted to make a hypthetical scenario where these equations could be used to solve a practical problem.*




