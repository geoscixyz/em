.. _harmonic_planewaves_homogeneous_questions:

Questions
=========


Skin Depth
----------

A plane wave :ref:`attenuates<harmonic_planewaves_homogeneous_skindepth>` as it propagates into the Earth. Use the default frequency of 10 Hz and conductivity :math:`\sigma` = 1 S/m for the initial simulation. 

	- Plot the amplitude versus depth and estimate the skin depth.
	- Evaluate the skin depth using the :ref:`formula provided<harmonic_planewaves_homogeneous_skindepth_formula_quasi>`. How do these values compare?
	- How does the skin depth change if f = 100 Hz and :math:`\sigma` = 0.1 S/m is used? 
	- How does the skin depth change f = 1 and :math:`\sigma` = 1 S/m is used?

Real and Imaginary Components
-----------------------------

As the plane wave propagates into the Earth there is both a real (in-phase) and an imaginary (quadrature or out-of-phase) component. By default, the App shows these signals at time t = 0 (e.g. :math:`e^{\pm i\omega t}` = 1). Thus at the surface (z = 0) the :math:`E_x` field is purely real and the :math:`H_y` field has equal real and imaginary parts. Why is this true? (hint: examine final solution for :math:`H_y` :ref:`here<harmonic_planewaves_homogeneous_derivation_app_soln>`).

	- Consider a depth z = 100 m. Evaluate the real and imaginary components of :math:`E_x` and :math:`H_y` at that point for f = 10 Hz and :math:`\sigma` = 1 S/m using the :ref:`analytic solution<harmonic_planewaves_homogeneous_derivation_app_soln>`; assume an initial amplitude of 1. Compare these values with those obtained using the app.
	- Use the real and imaginary values for :math:`E_x` from the app to calculate the amplitude at z = 100 m. Use the :ref:`attenuation formula<harmonic_planewaves_homogeneous_attenuation_formula>` to compute the theoretical amplitude at that depth; assume an initial amplitude :math:`A_0` = 1.
	- Compute the phase between real and imaginary components of :math:`E_x` at z = 100 m. How does your number compare with that directly provided by the app? Notice that the phase curve exhibits some strange behavior. Does this seem physically real and what is happening?


Wavelength
----------

There are a number of plots from which you can estimate the wavelength of the EM fields

	- Which one seems the most precise? Why?
	- Use the app to visually estimate the wavelength from both :math:`E_x` and :math:`H_y` for f = 10 Hz and :math:`\sigma` = 1 S/m. Are both values the same or different, and does this make sense? Use :ref:`this formula<harmonic_planewaves_homogeneous_wavelength_formula>` to calculate the wavelength and compare to the values obtained from the app.
	- What happens to the wavelength if you set f = 100 Hz?


Phase Velocity
--------------

The App provides a snapshot of the waves in the earth at time t = 0 (e.g. :math:`e^{\pm i\omega t}` = 1). As time progresses the waves propagate downward. If you follow an individual peak, trough, or zero crossing (try the log scale!) with time you can estimate the phase velocity. Do this by adjusting the time slider.

	- Pick a reference point at two times (say 0.02 and 0.04 seconds) and estimate the phase velocity. Compare your result with the theoretical result given by :ref:`this equation<harmonic_planewaves_homogeneous_phasevelocity_quasi>`.


Impedance and Phase
-------------------

The :ref:`wave impedance<harmonic_planewaves_homogeneous_impedancephase>` :math:`Z_{xy}=E_x/H_y` is a complex number and it is viewable in the App along with the :math:`E_x` and :math:`H_y` fields. Using the wave impedance, we can compute the :ref:`phase lag<harmonic_planewaves_homogeneous_impedancephase>` between :math:`E_x` and :math:`H_y`. The fields vary with depth and with time but by definition, the impedance and phase do not.

	- Use the app to compute the wave impedance. Now calculate the wave impedance with :ref:`this equation<harmonic_planewaves_homogeneous_impedancephase>`. How do the values compare?
	- Use the app to determine the phase. Now calculate the phase with :ref:`this equation<harmonic_planewaves_homogeneous_impedancephase>`. How do the values compare?
	- Adjust the time slider. Does the impedance or phase change?


Apparent Resistivity
--------------------

Impedances can be converted to :ref:`apparent resistivities<harmonic_planewaves_homogeneous_apparentresistivity>`.

	- Use your impedance values from the previous exercise and :ref:`this equation<harmonic_planewaves_homogeneous_apparentresisitivity>` to compute the apparent resistivity. How does this value compare to the resistivity entered into the app? (*Note that it doesn’t matter at what depth the measurements were obtained*).  

Polarization Ellipses
---------------------

We need clear objectives and questions
Semi-axes of the ellipse - 







