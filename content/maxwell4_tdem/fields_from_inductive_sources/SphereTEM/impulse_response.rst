.. _SphereTEM_impulse_response:

Impulse Response
----------------

**Purpose**: The sphere's time-dependent response to an arbitrary excitation is represented by its impulse response.
Here, analytic expressions for the sphere's impulse response are presented for a permeable and a non-permeable sphere.
Some aspects regarding the sphere's response to an arbitrary excitation are discussed.

Introduction
============

According to our :ref:`general formulation<SphereTEM_general_formulation>`, the induced dipole moment :math:`m(t)` characterizing the sphere is defined by a convolution:

.. math::
	m(t) = \Bigg ( \frac{4\pi}{3} R^3 \Bigg ) \int_{-\infty}^\infty \chi (\tau) h_0 (t-\tau )d\tau
	:label: eqDipoleMomentConvStepOff
	
where :math:`R` is the sphere's radius, :math:`\chi (t)` represents the sphere's impulse response and :math:`h_0 (t)` represents the inducing field.
By definition, :math:`\chi (t)` is defined as the inverse Fourier transform of the sphere's frequency-dependent excitation factor (link) (Wait, 1951):

.. math::
	\chi (t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \chi (i \omega) e^{i\omega t} d\omega
        :label: eqInverseFourierGenDef

Wait and Spies (1969) derived the impulse response according to Eq. :eq:`eqInverseFourierGenDef`.
In this section, only analytic results are presented.
However, we do provide derivations of the sphere's impulse response in the :ref:`following section<SphereTEM_analytic_derivation>`.



Conductive Sphere
=================

For a conductive and non-permeable (:math:`\mu = \mu_0`) sphere, the impulse response is given by (Wait and Spies, 1969):

.. math::
	\chi (t) = - \; \frac{3}{2} \delta (t) - \frac{9}{2} \Bigg [ \frac{1}{\beta^2} - \frac{1}{\beta \sqrt{\pi t}} \Bigg ( 1 + 2 \sum_{n = 1}^\infty e^{-(n\beta)^2/t} \Bigg ) \Bigg ] u(t)
	:label: eqImpulseConductive

where :math:`\delta (t)` is the Dirac delta function, :math:`u(t)` is the unit-step function and:

.. math::
	\beta = (\mu_0 \sigma )^{1/2} R
	



Conductive and Permeable Sphere
===============================

Here, we present the impulse response for a conductive and  magnetically permeable sphere.


.. math::
	\chi_\delta (t) = - \, \frac{3}{2} \delta (t) + \, \frac{3}{2} \Bigg ( \frac{6 \mu_r}{\beta^2} \sum_{n=1}^\infty \frac{ \xi_n^2 \, e^{-\xi_n^2 t/\beta^2}}{(\mu_r + 2)(\mu_r - 1)+\xi_n^2} \Bigg ) u(t)
	:label: eqImpulseConductivePermeable

where:

.. math::
	\beta = (\mu_0 \sigma )^{1/2} R
	
	
Coefficients :math:`\xi_n` within the sum are defined by:

.. math::
	\textrm{tan} \, \xi_n = \frac{(\mu_r - 1)\xi_n}{\mu_r - 1 + \xi_n^2}

From Wait and Spies (1969), coefficients :math:`\xi_n` are spaced roughly :math:`\pi` apart with:

.. math::
	n\pi \leq \xi_n \leq (n+1/2) \pi
	
	
The value of each coefficient may be found iteratively using very few iterations (< 10) according to:

.. math::
	\xi_n^{(k+1)} = n\pi + \textrm{tan}^{-1}\Bigg ( \frac{(\mu_r - 1) \xi_n^{(k)}}{\mu_r - 1 + (\xi_n^{(k)} )^2} \Bigg )



