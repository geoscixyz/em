.. _time_domain_electric_dipole_vector_potential:

Vector Potential
================

.. topic:: Purpose

    Here, we present an analytic expression for the transient vector potential corresponding to an electric dipole within a homogeneous media.
    Final expressions are derived in the quasi-static regime. 


The vector potential for a time-dependent electric dipole has a simple mathematical representation yet it contains complete information about the electric and magnetic fields.
In order to obtain an analytic expression for vector potential in the quasi-static (:math:`|\omega \varepsilon | \ll \sigma`), we apply the method shown on the :ref:`previous page<time_domain_electric_dipole_analytic_solution>`.

For an electric current dipole in the :math:`\hat x` direction, and with moment :math:`Ids`, the :ref:`harmonic vector potential<frequency_domain_electric_dipole_vector_potential>` is given by:

.. math::
	{\bf A} = \frac{Ids}{4\pi r}e^{-ikr} \hat x
	:label: harmonic_vector_potential

where

.. math::
	k = \big ( - i \omega \mu \sigma \big )^{1/2}
	:label: wave_number_quasi-static


By substituting :math:`s = i\omega` and dividing by :math:`s`:

.. math::
	\frac{{\bf A}(s)}{s} = \frac{Ids}{4 \pi r} \frac{e^{- \sqrt{s \mu\sigma r^2}}}{s} \hat x
	:label: vector_potential_Laplace


Because the signal is causal, the step-response at :math:`t \geq 0` can be derived by taking the inverse Laplace transform of the previous expression.
As we already showed on the :ref:`previous page<time_domain_electric_dipole_analytic_solution>`, the step-response for a causal system can be used to determine the transient or step-off response at :math:`t \geq 0` .
The inverse Laplace transform can be obtained trivially by using the following identity (Abramowitz and Stegun, 1964):


.. math::
	L^{-1} \Bigg [ \frac{e^{-\alpha \sqrt{s}}}{s} \Bigg ] = \textrm{erfc} \Bigg ( \frac{\alpha}{2 \sqrt{t}} \Bigg ) \; \; \; \textrm{for} \; \; \; \alpha \geq 0
	:label: Laplace_identity_4
	

Thus, the step response for the vector potential at :math:`t \geq 0` is given by:


.. math::
	L^{-1} \Bigg [ \frac{{\bf A}(s)}{s} \Bigg ] = \frac{Ids}{4 \pi r} \textrm{erfc} (\theta r) \hat x
	:label: vector_potential_step


where:

.. math::
	\theta = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2}
	:label: theta_vector_potential


Ultimately by the same method as before, the transient vector potential is given by:

.. math::
	{\bf a}(t) = \frac{Ids}{4 \pi r} \textrm{erf} (\theta r) \hat x
	:label: vector_potential_step_off
 








