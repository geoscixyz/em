.. _time_domain_magnetic_dipole_vector_potential:

Vector Potential
================

.. purpose::

    Here, we present an analytic expression for the transient vector potential corresponding to a magnetic dipole within a homogeneous media.
    Once again, expressions are derived for the quasi-static regime.


The vector potential for a time-dependent magnetic dipole has a simple mathematical representation yet it contains complete information about the electric and magnetic fields.
In order to obtain an explicit expression for the quasi-static (:math:`|\omega \varepsilon | \ll \sigma`) vector potential, we apply the approach from the :ref:`previous page<frequency_domain_magnetic_dipole_analytic_solution>`.

For a harmonic magnetic dipole in the :math:`\hat x` direction, and with moment amplitude :math:`m`, the :ref:`harmonic vector potential<frequency_domain_magnetic_dipole_vector_potential>` is given by:

.. math::
	{\bf F} = \frac{i\omega \mu m}{4\pi r} e^{-ikr} \hat x
	:label: harmonic_vector_potential

where

.. math::
	k = \big ( - i \omega \mu \sigma \big )^{1/2}
	:label: wave_number_quasi-static


By substituting :math:`s = i\omega` and dividing by :math:`s`:

.. math::
	\frac{{\bf F}(s)}{s} = \frac{\mu m}{4 \pi r} e^{- \sqrt{s \mu\sigma r^2}} \hat x
	:label: vector_potential_Laplace


Because the signal is causal, the step-response at :math:`t>0` can be derived by taking the inverse Laplace transform of the previous expression.
An explicit expression for the inverse Laplace transform can be obtained using the following identity (Abramowitz and Stegun, 1964):


.. math::
	L^{-1} \Big [ e^{-\alpha \sqrt{s}} \Big ] = \frac{\alpha}{2\sqrt{\pi t^3}} e^{-\alpha^2/4t} \; \; \; \textrm{for} \; \; \; t > 0
	:label: Laplace_identity_4


Using this identity, the step-response for the vector potential is given by:

.. math::
	L^{-1} \Bigg [ \frac{{\bf F}(s)}{s} \Bigg ] = \frac{m\theta^3}{\pi^{3/2} \sigma} e^{-\theta^2 r^2} \hat x
	:label: vector_potential_step


where:

.. math::
	\theta = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2}
	:label: theta_vector_potential


As we already showed on the :ref:`previous page<frequency_domain_magnetic_dipole_analytic_solution>`, the step-response for a causal system can be used directly to obtain the transient or step-off response.
Thus, the transient vector potential for a magnetic dipole within a homogeneous media is given by:


.. math::
	{\bf f}(t) = -\frac{m \theta^3}{\pi^{3/2} \sigma} e^{-\theta^2 r^2} \hat x
	:label: vector_potential_step_off









