.. _time_domain_magnetic_dipole_analytic_solution:

Analytic Solution
=================

.. topic:: Purpose

    Here, analytic solutions for an magnetic dipole source are derived for a step-off respone.

**General Formulation**

For a magnetic source (:math:`{\bf \, j_m^s \,}`) within a homogeneous media, Maxwell's equations in the time-domain can be written as follows:

.. math::
	\nabla \times {\bf e_e} + \mu \frac{\partial}{\partial t} ({\bf h_e}) = -i \omega \mu {\bf j_m^s} 
	:label: Faraday_time_homogeneous

.. math::
	\nabla \times {\bf h_e} - (\sigma + i\omega \varepsilon ) {\bf e_e} = 0
	:label: Ampere_time_homogeneous

Provided the source term is represented by a time-dependent magnetic dipole source :math:`m(t)` in the :math:`\hat x` direction, :math:`{\bf j_m^s}` is given by:

.. math::
	{\bf j_m^s} = \hat x  \delta (x) \delta (y) \delta (z) m(t)
	:label: mag_dipole_source_time

For a magnetic dipole defined by current :math:`I (t)` and area :math:`a`:

.. math::
	m(t) = a \, I(t)
	:label: mag_dipole_moment_time
	

We are interested in the time-dependent electric and magnetic fields which arise due to a step-off excitation, also known as the transient response.
For a step-off excitation, the current describing the magnetic dipole is given by:

.. math::
	I(t) = I u(-t) = I \big [ 1 - u(t) \big ]
	:label: step_off_current

Here, we will avoid the unnecessary difficulty of deriving final expressions directly from Maxwell's equations. Instead, we will be using the approach shown in Ward and Hohmann.
For this approach, frequency-domain solutions previously derived for the harmonic magnetic dipole (link) are transformed into the time-domain via inverse Laplace transform.
The strategy for obtaining the step-off response is identical to that which was used in the case of the electric dipole (link).

**Frequency Domain to Time Domain**

For a causal system, the unit step-response (:math:`g_+`) at :math:`t \geq 0` is given by:

.. math::
	g_+(t) = \int_{-\infty}^\infty f(\tau) u(t - \tau) d\tau = \int_0^t f(\tau) d\tau \; \; \; \textrm{for} \; \; \; t\geq 0
	:label: causal_step

where :math:`f(t)` is the system's impulse response.
For most geophysical problems however, we are interested in the step-off response (:math:`g_-`).
The step-off response for a causal system may be given by:

.. math::
	g_-(t) = \int_{-\infty}^\infty f(\tau) \big [ 1 - u(t - \tau) \big ] d\tau = \int_0^\infty f(\tau) d\tau - \int_0^t f(\tau) d\tau = g_+ (\infty) - g_+(t) \; \; \; \textrm{for} \; \; \; t\geq 0
	:label: causal_step_off

where :math:`g_+ (\infty )` represents the step-response at :math:`t = \infty`.
Therefore, if the step-response is known for :math:`t \geq 0`, it can be used to obtain the step-off response at :math:`t \geq 0`.

According to Ward and Hohmann, the step-response can be obtained via the following inverse Laplace transform:

.. math::
	g_+(t) = L^{-1} \Bigg [ \frac{F(s)}{s} \Bigg ]
	:label: step_inverse_Laplace

where :math:`F(s)` is obtained by replacing :math:`s=i\omega` in the system's harmonic response function.
For the electric and magnetic fields arising from a harmonic magnetic dipole, these have already been derived (link).
For the electric field:

.. math::
	{\bf E_m}(i\omega ) = \frac{i\omega \mu m}{4\pi r^2} (ikr +1) e^{-ikr} \Bigg ( \frac{z}{r}\hat y - \frac{y}{r}\hat z  \Bigg )
	:label: E_harmonic_response

And for the magnetic field:

.. math::
	{\bf H_m}(i\omega ) = \frac{m}{4\pi r^3} e^{-ikr} \Bigg [ \Bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2} \hat z \Bigg ) \big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 -ikr -1 \big ) \hat x \Bigg ]
	:label: H_harmonic_response

where the wavenumber :math:`k` is given by:

.. math::
	k = \big ( \omega^2\mu\varepsilon - i \omega \mu \sigma \big )^{1/2}
	:label: wave_number



**Analytic Solution**


Let us consider the quasi-static transient response within the medium (i.e. :math:`|\omega\varepsilon \ll \sigma |`).
In this case, the wavenumber is given by:

.. math::
	k = \big (- i \omega \mu \sigma \big )^{1/2}
	:label: wave_number_quasi_static

If we substitute :math:`s = i\omega` in Eqs. :eq:`E_harmonic_response` and :eq:`H_harmonic_response` and divide by :math:`s` then:

.. math::
	\frac{{\bf E_m}(s)}{s} = s \Bigg [ \frac{\mu m}{4\pi r^3} \bigg ( \sqrt{\frac{ \mu \sigma}{s}} r + \frac{1}{s} \bigg ) e^{-\sqrt{s \mu \sigma r^2}} \big ( z \, \hat y - y\, \hat z  \big ) \Bigg ]
	:label: E_frac_inverse_Laplace

and:

.. math::
	\frac{{\bf H_e}(s)}{s} = \frac{m}{4\pi r^3} e^{-\sqrt{s\mu \sigma r^2}} \Bigg [ \Bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2} \hat z \Bigg ) \Bigg ( -\mu\sigma r^2 + 3 \sqrt{\frac{\mu \sigma}{s}}r + \frac{3}{s} \Bigg ) + \Bigg ( -\mu\sigma r^2 - \sqrt{\frac{\mu \sigma}{s}} r - \frac{1}{s} \Bigg ) \hat x \Bigg ]
	:label: H_frac_inverse_Laplace
	

To obtain the inverse Laplace transform of the previous two expressions, and thus the step-response, we can use the following three identities (Abramowitz and Stegun, 1964):

.. math::
	L^{-1} \Big [ s F(s) \Big ] = \frac{d}{dt} f(t)

.. math::
	L^{-1} \Big [ e^{-\alpha \sqrt{s}} \Big ] = \frac{\alpha}{2\sqrt{\pi t^3}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha > 0 \\
	:label: inverse_Laplace_identity_2

.. math::	
	L^{-1} \Bigg [ \frac{1}{\sqrt{s}} e^{-\alpha \sqrt{s}} \Bigg ] = \frac{1}{\sqrt{\pi t}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha \geq 0 \\
	:label: inverse_Laplace_identity_3

.. math::
	L^{-1} \Bigg [ \frac{1}{s} e^{-\alpha \sqrt{s}} \Bigg ] = \textrm{erfc}\Bigg ( \frac{\alpha}{2\sqrt{t}} \Bigg )\;\;\; \textrm{for} \; \; \; \alpha \geq 0
	:label: inverse_Laplace_identity_4


where erfc(x) is the complimentary error function.
Using the above identities, the step-response for the electric and magnetic fields can be determined according to Eq. :eq:`step_inverse_Laplace`.
For the electric field, the step-response is given by:

.. math::
	L^{-1}\Bigg [ \frac{{\bf E_m}(s)}{s} \Bigg ] = \frac{2 m \theta^5 }{\pi^{3/2} \sigma} e^{-\theta^2 r^2} \big ( -z \, \hat y + y \, \hat z \big )
	:label: e_step_response


And for the magnetic field:

.. math::
	\begin{split}
	L^{-1}\Bigg [ \frac{{\bf H_m}(s)}{s} \Bigg ] = \frac{m}{4\pi r^3} \Bigg [ \Bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2}\hat z \Bigg ) \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}} \theta^3 r^3 +& \frac{6}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} + 3\, \textrm{erfc} (\theta r) \Bigg ) \, ...  \\
	& - \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}} \theta^3 r^3 + \frac{2}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} +  \textrm{erfc} (\theta r) \Bigg ) \hat x \Bigg ]
	\end{split}
	:label: h_step_response

where

.. math::
	\theta = \Bigg ( \frac{\mu\sigma}{4t} \Bigg )^{1/2}
	:label: theta_quasi_static


Using the step-response, we can obtain the transient response according to Eq. :eq:`causal_step_off`.
For the electric field, the transient response is given by:

.. math::
	{\bf e_m}(t) = \frac{2 m \theta^5 }{\pi^{3/2} \sigma} e^{-\theta^2 r^2} \big ( -z \, \hat y + y \, \hat z \big )
	:label: e_step_off_response

And for the magnetic field

.. math::
	\begin{split}
	{\bf h_m}(t) = \frac{m}{4\pi r^3} \Bigg [ \Bigg ( \frac{x^2}{r^2} \hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2} \hat z \Bigg ) \Bigg ( 3 \, \textrm{erf}(\theta r) - \bigg ( \frac{4}{\sqrt{\pi}}\theta^3 r^3 + &\frac{6}{\sqrt{\pi}}\theta r \bigg ) e^{-\theta^2 r^2} \Bigg ) \; ... \\
	&-  \Bigg (\textrm{erf}(\theta r) - \bigg ( \frac{4}{\sqrt{\pi}}\theta^3 r^3 + \frac{2}{\sqrt{\pi}}\theta r \bigg ) e^{-\theta^2 r^2} \Bigg ) \hat x  \Bigg ]
	\end{split}
	:label: h_step_off_response


For geophysical applications, we generally measure the electromotive force induced within a receiver coil.
As a result, we are interested in the time-rate of decay of the magnetic field.
Taking the derivative of Eq. :eq:`h_step_off_response`, this is given by:

.. math::
	\frac{\partial{ \bf h_m}}{\partial t} = - \frac{4m \theta^5}{\pi^{3/2} \mu\sigma} e^{-\theta^2 r^2} \Bigg [ \Bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2} \hat y + \frac{xz}{r^2} \hat z \Bigg ) \theta^2 r^2  + \big (1 -\theta^2 r^2 \big ) \hat x \Bigg ]
	:label: dhdt_step_off_quasi_static
