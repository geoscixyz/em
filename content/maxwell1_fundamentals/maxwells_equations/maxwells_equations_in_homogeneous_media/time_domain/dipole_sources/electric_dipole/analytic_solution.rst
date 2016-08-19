.. _time_domain_electric_dipole_analytic_solution:

Analytic Solution
=================

.. topic:: Purpose

    Here, analytic solutions for an electric dipole source are derived for a step-off respone.

**General Formulation**

For an electrical current source (:math:`{\bf j_e^s}`), Maxwell's equations in the time-domain can be written as follows:

.. math::
	\begin{align}
	\nabla \times {\bf e_e} &+ \frac{\partial}{\partial t} (\mu {\bf h_e}) = 0\\
	\nabla \times {\bf h_e} &- (\sigma + i\omega \varepsilon ) {\bf e_e} = {\bf j_e^s}
	\end{align}

For a time-dependent electric dipole source in the :math:`\hat x` direction, with current :math:`I (t)` and length :math:`ds`, :math:`{\bf j_e^s}` is given by:

.. math::
	{\bf j_e^s} = \hat x  \delta (x) \delta (y) \delta (z)I(t) ds


where :math:`I(t)` is the time-dependent current for the electric dipole and :math:`ds` represents its length.
We are interested in the time-dependent electric and magnetic fields which arise due to a step-off excitation, also known as the transient response.
For a step-off excitation, the current describing the electric dipole is given by:

.. math::
	I(t) = I u(-t) = I \big [ 1 - u(t) \big ]

Here, we will avoid the unnecessary difficulty of deriving final expressions directly from Maxwell's equations by using the approach shown in Ward and Hohmann.
For this approach, frequency-domain solutions previously derived for the harmonic electric dipole (link) are transformed into the time-domain via inverse Laplace transform.



**Frequency Domain to Time Domain**

For a causal system, the unit step-response (:math:`g_+`) at :math:`t \geq 0` is given by:

.. math::
	g_+(t) = \int_{-\infty}^\infty f(\tau) u(t - \tau) d\tau = \int_0^t f(\tau) d\tau \; \; \; \textrm{for} \; \; \; t\geq 0


where :math:`f(t)` is the system's impulse response.
For most geophysical problems however, we are interested in the step-off response (:math:`g_-`).
The step-off response for a causal system may be given by:

.. math::
	g_-(t) = \int_{-\infty}^\infty f(\tau) \big [ 1 - u(t - \tau) \big ] d\tau = \int_0^\infty f(\tau) d\tau - \int_0^t f(\tau) d\tau = g_+ (\infty) - g_+(t) \; \; \; \textrm{for} \; \; \; t\geq 0

where :math:`g_+ (\infty )` represents the step-response at :math:`t = \infty`.
Therefore, if the step-response is known for :math:`t \geq 0`, it can be used to obtain the step-off response at :math:`t \geq 0`.

According to Ward and Hohmann, the step-response can be obtained via the following inverse Laplace transform:

.. math::
	g_+(t) = L^{-1} \Bigg [ \frac{F(s)}{s} \Bigg ]


where :math:`F(s)` is obtained by replacing :math:`s=i\omega` in the system's harmonic response function.
For the electric and magnetic fields arising from a harmonic electric dipole, these have already been derived (link).
For the electric field:

.. math::
	{\bf E_e}(i\omega ) = \frac{Ids}{4\pi (\sigma + i\omega \varepsilon )r^3} e^{-ikr} \Bigg [ \bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2} \hat z \Bigg ) \big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 -ikr -1 \big ) \hat x \Bigg ]


And for the magnetic field:

.. math::
	{\bf H_e}(i\omega ) = \frac{Ids}{4\pi r^2} (ikr +1) e^{-ikr} \Bigg ( - \frac{z}{r}\hat y + \frac{y}{r}\hat z  \Bigg )


where the wavenumber :math:`k` is given by:

.. math::
	k = \big ( \omega^2\mu\varepsilon - i \omega \mu \sigma \big )^{1/2}




**Quasi-Static Case**


Let us consider the quasi-static transient response within the medium (i.e. :math:`|\omega\varepsilon \ll \sigma |`).
In this case, the wavenumber is given by:

.. math::
	k = \big (- i \omega \mu \sigma \big )^{1/2}


If we substitute :math:`s = i\omega` in Eqs. () and (), then:

.. math::
	\frac{{\bf E_e}(s)}{s} = \frac{Ids}{4\pi \sigma r^3} e^{- \sqrt{s\mu\sigma r^2 } } \Bigg [ \bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2} \hat z \bigg ) \bigg ( \mu\sigma r^2 + 3 \sqrt{\dfrac{\mu \sigma}{s} } r + \frac{3}{s} \bigg ) - \bigg ( \mu\sigma r^2 + \sqrt{\frac{\mu\sigma}{s}r} + \frac{1}{s} \bigg ) \hat x \Bigg ],


and:

.. math::
	\frac{{\bf H_e}(s)}{s} = \frac{Ids}{4\pi r^2} e^{- \sqrt{s\mu\sigma r^2 } } \bigg ( \sqrt{\frac{\mu\sigma}{s}r} + \frac{1}{s} \bigg )  \bigg ( - \frac{z}{r}\hat y + \frac{y}{r}\hat z  \bigg ),


To obtain the inverse Laplace transform of the previous two expressions, and thus the step-response, we can use the following three identities (Abramowitz and Stegun, 1964):

.. math::
	\begin{align}
	L^{-1} \Big [ e^{-\alpha \sqrt{s}} \Big ] &= \frac{\alpha}{2\sqrt{\pi t^3}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha > 0 \\
	L^{-1} \Bigg [ \frac{1}{\sqrt{s}} e^{-\alpha \sqrt{s}} \Bigg ] &= \frac{1}{\sqrt{\pi t}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha \geq 0 \\
	L^{-1} \Bigg [ \frac{1}{s} e^{-\alpha \sqrt{s}} \Bigg ] &= \textrm{erfc}\Bigg ( \frac{\alpha}{2\sqrt{t}} \Bigg )\;\;\; \textrm{for} \; \; \; \alpha \geq 0
	\end{align}


where erfc(x) is the complimentary error function.
By using these identities to obtain the step-response, results given by Eq. () can be used to obtain the step-off response for the electric and magnetic fields.
For the electric field, the step-off response is given by:

.. math::
	\begin{split}
	{\bf e_e}(t) = \frac{Ids}{4\pi \sigma r^3} \Bigg [ \Bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2}\hat z \Bigg ) \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}}\theta^3 r^3 & + \frac{6}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} + 3 \, \textrm{erfc}(\theta r) \Bigg ) ... \\
	&- \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}} \theta^3 r^3 + \frac{2}{\sqrt{\theta r}} \theta r \bigg ) e^{-\theta^2 r^2} + \textrm{erfc}(\theta r) \Bigg ) \hat x \Bigg ]
	\end{split}

where

.. math::
	\theta = \Bigg ( \frac{\mu\sigma}{4t} \Bigg )^{1/2}
	


For the magnetic field, the resulting step-off response is given by:

.. math::
	{\bf h_e}(t) = \frac{Ids}{4 \pi r^2} \bigg ( \frac{2}{\sqrt{\pi}} \theta r \, e^{-\theta^2 r^2} + \textrm{erfc}(\theta r) \bigg ) \bigg ( - \frac{z}{r}\hat y - \frac{y}{r}\hat z  \bigg )
	

For geophysical applications, we generally measure the electromotive force induced within a receiver coil.
As a result, we are interested in the time-rate of decay of the magnetic field.
Taking the derivative of Eq. (), this is given by:

.. math::
	\frac{\partial{ \bf h_e}}{\partial t} = \frac{\theta^3 r Ids}{2 \pi^{3/2} t} e^{-\theta^2 r^2} \bigg ( - \frac{z}{r}\hat y - \frac{y}{r}\hat z  \bigg )
	