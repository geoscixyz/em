.. _time_domain_electric_dipole_analytic_solution:

Analytic Solution
=================

.. topic:: Purpose

    Here, analytic solutions for an electric dipole source are derived for a step-off respone.



For an electrical current source (:math:`{\bf j_e^s}`), Maxwell's equations in the time-domain can be written as follows:

.. math::
	\begin{align}
	\nabla \times {\bf e_e} &+ \frac{\partial}{\partial t} (\mu {\bf h_e}) = 0\\
	\nabla \times {\bf h_e} &- (\sigma + i\omega \varepsilon ) {\bf e_e} = {\bf j_e^s}
	\end{align}

For a time-dependent electric dipole source in the :math:`\hat x` direction, with current :math:`I (t)` and length :math:`ds`, :math:`{\bf j_e^s}` is given by:

.. math::
	{\bf j_e^s} = \hat x  \delta (x) \delta (y) \delta (z)I(t) ds


We are interested in the time-dependent electric and magnetic fields which arise due to a step-off excitation, also known as the transient response.
For a step-off excitation, the current describing the electric dipole is given by:

.. math::
	I(t) = I u(-t) = I \big [ 1 - u(t) \big ]

Here, we will avoid the unnecessary difficulty of deriving final expression from Maxwell's equations by using the approach shown in Ward and Hohmann.
For this approach, frequency-domain solutions previously derived for a harmonic electric dipole are transformed into the time-domain via inverse Laplace transform.



**Frequency Domain to Time Domain**

For a causal system, the step-response (:math:`g_+`) at :math:`t \geq 0` is given by:

.. math::
	g_+(t) = \int_{-\infty}^\infty f(\tau) u(t - \tau) d\tau = \int_0^t f(\tau) d\tau \; \; \; \textrm{for} \; \; \; t\geq 0


where :math:`f(t)` is the system's impulse response.
For most geophysical problems, we are interested in the response once a long-standing field is removed.
This is known as the step-off or transient response (:math:`g_-`).
The transient response for a causal system may be given by:

.. math::
	g_-(t) = \int_{-\infty}^\infty f(\tau) \big [ 1 - u(t - \tau) \big ] d\tau = \int_0^\infty f(\tau) d\tau - \int_0^t f(\tau) d\tau = g_+ (\infty) - g_+(t) \; \; \; \textrm{for} \; \; \; t\geq 0

where :math:`g_+ (\infty )` represents the step-response at :math:`t = \infty`.
Therefore, if the step-response is known, it can be used to obtain the step-off response at :math:`t \geq 0`.





.. math::
	{\bf E_e} = \frac{Ids}{4\pi (\sigma + i\omega \varepsilon )r^3} e^{-ikr} \Bigg [ \bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2} \hat z \Bigg ) \big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 -ikr -1 \big ) \hat x \Bigg ]



.. math::
	{\bf H_e} = \frac{Ids}{4\pi r^2} (ikr +1) e^{-ikr} \Bigg ( - \frac{z}{r}\hat y + \frac{y}{r}\hat z  \Bigg )




**Quasi-Static Case**


Let us consider the quasi-static response within the medium (i.e. :math:`|\omega\varepsilon \ll \sigma |`).
In this case, the electric field from a harmonic electric dipole source is given by:

.. math::
	{\bf E_e} = \frac{Ids}{4\pi \sigma r^3} e^{-ikr} \Bigg [ \bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2} \hat z \Bigg ) \big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 -ikr -1 \big ) \hat x \Bigg ],


and the magnetic field is given by:

.. math::
	{\bf H_e} = \frac{Ids}{4\pi r^2} (ikr +1) e^{-ikr} \Bigg ( - \frac{z}{r}\hat y + \frac{y}{r}\hat z  \Bigg ),


where the wavenumber is given by:

.. math::
	k \approx \big ( -i\omega \mu \sigma \big )^{1/2}


Before performing the inverse Laplace transform which provides the step-response can by obtained by replacing :math:`s = i\omega` and divi

.. math::
	\frac{{\bf E_e}(s)}{s} = \frac{Ids}{4\pi \sigma r^3} e^{-ikr} \Bigg [ \bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2} \hat z \Bigg ) \big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 -ikr -1 \big ) \hat x \Bigg ]



.. math::
	\frac{{\bf H_e}(s)}{s} = \frac{Ids}{4\pi r^2} (ikr +1) e^{-ikr} \Bigg ( - \frac{z}{r}\hat y + \frac{y}{r}\hat z  \Bigg )









.. math::
	\theta = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2}





.. math::
	\begin{align}
	L^{-1} \Bigg ( \frac{}{} \Bigg ) &= \\
	L^{-1} \Bigg (  \Bigg ) &=  \\
	L^{-1} \Bigg (  \Bigg ) &=
	\end{align}




