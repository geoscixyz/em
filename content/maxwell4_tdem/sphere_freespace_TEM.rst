.. _sphere_freespace:

Response from a Conducting and Permeable Sphere in Free-Space
-------------------------------------------------------------

Introduction
============

1. Introduce what were are doing

2. General flavour of obtaining time-domain responses from our frequency-dependent excitation factor

3. The impulse response and step-response for a purely conductive sphere (Wait, 1951; Wait and Spies, 1969)

4. Approximations of the time dependent decay for conductive and permeable objects (Becker et al., 'no date')

5. Dipole response in free space


Obtaining the Time-Domain Response of a Conducting and Permeable Sphere
=======================================================================

.. figure:: ./images/figGeometrySphere.png
	:align: center
        :scale: 50%
        :name: GeometrySphere

Consider a conductive and permeable sphere in a resistive media (Figure  ).
This sphere is excited by a time-dependent field :math:`h_0(t)`.
In the frequency domain, the induced magnetic dipole moment :math:`\vec m(t)` of the sphere was given by:

.. math::
	\vec m (\omega) = \frac{4\pi}{3}R^3 \chi (\omega) \vec H_0 (i \omega) 
	:label: DipoleMoment

where :math:`R` was the radius of the sphere, :math:`\chi (\omega)` was an excitation factor, and :math:`H_0 (i \omega)` was a harmonic inducing field.
Recall that our sphere is isotropic.
As a result, all excitation is parallel to the inducing field.

To obtain the time-dependent magnetic dipole moment of the sphere, we can apply an inverse Fourier transform to Eq. :eq:`DipoleMoment`:

.. math::
	m(t) = \frac{1}{2\pi} \int_{-\infty}^\infty m(\omega) e^{i\omega t} \, d\omega = \frac{4 \pi}{3} R^3 \Bigg [ \frac{1}{2\pi} \int_{-\infty}^\infty \chi(\omega) H_0 (i\omega) e^{i\omega t} \, d\omega \Bigg ]
	:label: mIFT

By taking the inverse Fourier transform of the product of two frequency-dependent functions, :math:`m(t)` can be expressed in terms of a convolution:

.. math::
	m(t) = \frac{4\pi}{3} R^3 \big [ \chi_\delta (t) \otimes h_0(t) \big ] 
	:label: mConvolutionDef
	
where :math:`\chi_\delta (t)` is defined as the excitation's impulse response and :math:`h_0 (t)` is a time-dependent inducing field.
The excitation's impulse response is defined as the inverse Fourier transform of :math:`\chi (\omega)`:

.. math::
	\chi_\delta (t) = \frac{1}{2\pi} \int_{-\infty}^\infty \chi (\omega) e^{i\omega t} \, d\omega
	:label: ImpulseIFT

The convolution :math:`\chi_\delta (t) \otimes h_0 (t)` is defined as:

.. math::
	\chi_\delta (t) \otimes h_0 (t) = \int_{-\infty}^\infty \chi_\delta (\tau) h_0 (t -\tau) d\tau = \int_{-\infty}^\infty \chi_\delta (t - \tau) h_0 (\tau) d\tau 
	:label: ConvolutionDef

As we will find out later, the time-domain response of the sphere is causal.
As a result, the convolution is frequently expressed as an integral from 0 to :math:`\infty`.
For many geophysical applications, we are interested in the response to step-off excitation.
In this case, the sphere is excited by an inducing field of the form:

.. math::
	h_0 (t) = h_0 \big [ 1 - u(t) \big ]
	:label: StepOff

where :math:`h_0` is the amplitude of the field before it is removed, and :math:`u(t)` is the unit step function.
According to Newmann (et al., 1996), the time-dependent magnetization at :math:`t>0` can be expressed using inverse sine and cosine transforms:

.. math::
	\begin{split}
	m(t) &= - \frac{4\pi}{3}R^3 \Bigg [ \frac{2}{\pi} \int_0^\infty \frac{Im [\chi(\omega)]}{\omega} \; cos(\omega t) \;d \omega \Bigg ] h_0 \\
	     &= m(0) - \frac{4\pi}{3}R^3 \Bigg [ \frac{2}{\pi} \int_0^\infty \frac{Re [\chi(\omega)]}{\omega} \; sin(\omega t) \; d \omega \Bigg ] h_0
	\end{split}
	:label: mSineCosine

where :math:`m(0)` represents some initial dipole moment at :math:`t=0`. For the rate of decay:

.. math::
	\begin{split}
	\frac{d \, m(t)}{d t} &= \frac{4\pi}{3}R^3 \Bigg [ \frac{2}{\pi} \int_0^\infty Im [\chi (\omega)] \; sin(\omega t) \;d \omega \Bigg ] h_0\\
					    &= - \frac{4\pi}{3}R^3 \Bigg [ \frac{2}{\pi} \int_0^\infty Re [\chi(\omega)]\; cos(\omega t) \; d \omega \Bigg ] h_0 
	\end{split}
	:label: dmdtSineCosine


Response from a Conducting Sphere in a Resistive Medium
=======================================================

Here we consider the time-dependent magnetization of a purely conductive sphere (:math:`\mu = \mu_0`) within a resistive medium (:math:`\sigma_b \ll \sigma`).
In this case, the frequency-dependent excitation of the sphere is defined by:

.. math::
	\chi (\omega) = \frac{3}{2} \Bigg [ 1 + \frac{3}{\alpha^2} - \frac{3 \, \textrm{coth} (\alpha)}{\alpha} \Bigg ]
	:label: ChiConductive

where, if electric displacement is neglected (i.e. :math:`\omega \varepsilon \ll \sigma`):

.. math::
	\alpha = \Big [ i \omega \mu_0 \sigma \Big ]^{1/2} R
	:label: alpha


Impulse Response
++++++++++++++++

To obtain the excitation factor's impulse response, Wait and Spies (1969) employed a change of variables on Eq. :eq:`ChiConductive` by replacing :math:`s=i\omega` and :math:`\beta=(\mu_0 \sigma)^{1/2} R`.
The hyperbolic cotanjent term was then re-expressed as an infinit series, thus:

.. math::
	\begin{align}
	\chi (s)&= \frac{3}{2} \Bigg [ 1 + \frac{3}{\beta^2 s} - \frac{3 \, \textrm{coth} (\beta s^{1/2} )}{\beta s^{1/2}} \Bigg ] \\
		&= \frac{3}{2} \Bigg [ 1 + \frac{3}{\beta^2 s} + \frac{3}{\beta s^{1/2}} \Bigg ( \frac{1 + e^{-2 \beta s^{1/2} } }{1 -  e^{-2 \beta s^{1/2}}} \Bigg ) \Bigg ] \\
		&= \frac{3}{2} \Bigg [ 1 + \frac{3}{\beta^2 s} - \frac{3}{\beta s^{1/2}} - \frac{6}{\beta} \sum_{n = 1}^\infty \frac{e^{-2n \beta s^{1/2}}}{s^{1/2}} \Bigg ]
	\end{align}
	:label: ChiChangeVar

This allowed them to obtain the excitation's impulse response using the inverse Laplace transform:

.. math::
	\chi_\delta (t) = \frac{1}{2 \pi i} \int_{c - i\infty}^{c + i\infty} \chi (s) e^{st} ds = \mathcal{L}^{-1} \big [ \chi (s) \big ]
	:label: LaplaceIFT

where :math:`c` is a small positive constant, chosen so that the contour path of integration lies within the convergence region of :math:`\chi (s)`.
By substituting Eq. :eq:`ChiChangeVar` into Eq. :eq:`LaplaceIFT`, a conductive sphere's impulse response can be expressed as:

.. math::
	\chi_\delta (t) = \frac{3}{2} \delta (t) + \frac{9}{2} \Bigg [ \frac{1}{\beta^2} - \frac{1}{\beta \sqrt{\pi t}} \Bigg ( 1 + 2 \sum_{n = 1}^\infty e^{-(n\beta)^2/t} \Bigg ) \Bigg ] u(t)
	:label: ImpulseConductive

where :math:`\delta(t)` is the Dirac delta function.
We can see that Eq. :eq:`ImpulseConductive` is zero for :math:`t<0`, implying it is causal.
Although the impulse response is written as an infinite series, exponential functions of the form :math:`e^{-an^2}` are negligible for sufficiently large :math:`n`.
Thus, only a finite number of terms are required to approximate the sphere's impulse response.


Step Response
++++++++++++++++

Consider the sphere's response to step-excitation.
In this case, the inducing field is of the form:

.. math::
	h_0 (t) = h_0 u(t)
	:label: StepOn

where :math:`h_0` is the amplitude of the field, and :math:`u(t)` is the unit step function.
Using Eqs. :eq:`ConvolutionDef`, :eq:`ImpulseConductive` and :eq:`StepOn` to solve Eq. :eq:`mConvolutionDef`:

.. math::
	m(t) = \frac{4\pi}{3}R^3 \Bigg [ \int_{-\infty}^{\infty} \chi_\delta (\tau) h_0 u(t-\tau) d\tau \Bigg ] = \frac{4\pi}{3}R^3 \Bigg [ \int_0^t \chi_\delta (\tau) d\tau \Bigg ] h_0
	:label: ConvolutionStep

The convolution is in Eq. :eq:`ConvolutionStep` only requires us to integrate the impulse response from 0 to :math:`t`.
By substituting Eq. :eq:`ChiConductive` into Eq :eq:`ConvolutionStep`, we can obtain the final expression presented in Wait and Spies (1969):

.. math::
	\int_0^t \chi_\delta (t) d\tau = \frac{9}{2} \Bigg [ \frac{1}{3} + \frac{t}{\beta^2} - \frac{2}{\beta} \sqrt{\dfrac{t}{\pi}} \Bigg ( 1 + 2 \sum_{n=1}^\infty e^{-(n\beta)^2/t} \Bigg ) - 2 \sum_{n=1}^\infty n \; \textrm{erfc}\Bigg ( \frac{n\beta}{\sqrt{t}} \Bigg ) \Bigg ] u(t)
	:label: IntImpulse0t

where :math:`\textrm{erfc}(z)` is the complimentary error function given by:

.. math::
	\textrm{erfc}(z) = \frac{2}{\sqrt{\pi}} \int_z^\infty e^{-t^2} dt
	:label: erfc
	
It should be noted that our expression differs from the one in Wait and Spies by a factor of :math:`3/2`.
This is because of how we chose to define :math:`\chi (\omega)`.
Although a rigorous proof will not be provided here, Eq. :eq:`IntImpulse0t` goes to 0 as :math:`t` goes to infinity.
Thus:

.. math::
	\int_0^\infty \chi_\delta (\tau) d\tau = 0
	:label: IntImpulseLimit
	
This is expected given that inductive responses decay to zero after sufficient time.
The response to step-off excitation may be obtained by implementing the appropriate waveform into Eq. :eq:`ConvolutionStep`.
This results in the following expression:

.. math::
	m(t) = \frac{4\pi}{3}R^3 \Bigg [ \int_{-\infty}^{\infty} \chi_\delta (\tau) h_0 \big [ 1 - u(t-\tau) \big ] d\tau \Bigg ] = - \; \frac{4\pi}{3}R^3 \Bigg [ \int_0^t \chi_\delta (\tau) d\tau \Bigg ] h_0

Therefore, the response to step-on and step-off excitation behave identically and have opposing sign.

Rate of Decay
+++++++++++++

dfasdf

.. math::
	\begin{align}
	\frac{d \, m(t)}{dt} &= \frac{4\pi}{3}R^3 \Bigg [ \int_{-\infty}^{\infty} \chi_\delta (\tau) \frac{d \, h_0 (t-\tau)}{dt} d\tau \Bigg ] \\
			     &= \frac{4\pi}{3}R^3 \Bigg [ - \; \int_{-\infty}^{\infty} \chi_\delta (\tau) \delta (t-\tau) d\tau \Bigg ] h_0 \\
			     &= - \; \frac{4\pi}{3}R^3 \, \chi_\delta (t) \, h_0
	\end{align}








Step-Off Response from a Conducting and Magnetically Permeable Sphere in a Resistive Medium
===========================================================================================













Dipole Response in Free-Space
=============================

Here, we present a model for predicting the anomalous frequency-domain response in free-space, from a conductive and permeable sphere, due to an inductive loop source.
In the previous section, analytic expressions were derived by considering a uniform inducing field about the sphere.
However, if the radius of the sphere is sufficiently smaller than its distance from an inductive source, this condition will hold approximately for small enough frequencies.
According to Ward and Hohmann (1988?), a distance larger than 5 times the average dimension of the object is required for a dipole source.
If the frequency-dependent dipole moment of a conductive and permeable sphere is known, the resulting free-space dipole field may be calculated using Eq. :eq:`DipoleField`, where :math:`\vec m (\omega)` is given by Eq. :eq:`DipoleMoment`.
The geometry of this problem can be seen in Fig. (\ref{}).
By decomposing the problem into separable cartesian components, Eq. :eq:`DipoleField` can be re-expressed as:

.. math::
	{\bf B}(\omega) = \frac{\mu_0}{4 \pi r^3} \Big [ 3 {\bf \hat r \otimes \hat r - I} \Big ] \cdot {\bf m} (\omega) = {\bf G} \, {\bf m} (\omega)
	:label: DipoleVacuumLin
	
where

.. math::
	{\bf B} (\omega) = \begin{bmatrix} B_x (\omega) \\ B_y(\omega) \\ B_z(\omega) \end{bmatrix}, \; \;
	{\bf m}(\omega) = \begin{bmatrix} m_x (\omega) \\ m_y(\omega) \\ m_z(\omega) \end{bmatrix} \; \; \textrm{and} \; \;
	{\bf I} = \begin{bmatrix} 1&0&0\\0&1&0\\0&0&1 \end{bmatrix}
	:label: DipoleOperator

The vector from :math:`P` to :math:`Q` is denoted by :math:`\vec r`, and has unit-direction :math:`{\bf \hat r}`.
For our formulation, we use :math:`{\bf \hat r \otimes \hat r}` to represent an outer-product.
We can see from Eq. :eq:`DipoleVacuumLin` that :math:`{\bf G}` is a :math:`3\times 3` linear operator, which depends solely on the geometry of the problem.
Because the magnetization factor for our sphere is a scalar quantity, it may be used to obtain each cartesian component of the induced dipole moment separately.
As a result, we may express :math:`{\bf m} (\omega)` as follows:

.. math::
	{\bf m} (\omega) = {\bf M \, H_0}
	:label: mDecomposition
	
where

.. math::
	{\bf M} = \Bigg ( \frac{4}{3} \pi R^3 \chi (\omega ) \Bigg ) {\bf I} \; \; \textrm{and} \; \;
	{\bf H_0} = \begin{bmatrix} H_x(\omega) \\ H_y (\omega) \\ H_z (\omega) \end{bmatrix}
	:label: Magnetization
	
By substituting Eq. :eq:`mDecomposition` into Eq. :eq:`DipoleVacuumLin`, the free-space dipole response can be expressed as:

.. math::
	{\bf B}(\omega) = {\bf G \, M \, H_0}
	:label: DipoleVacuumLinSys

.. figure::
	./images/figResponseVacuum.png
        :align: center
	:figwidth: 50%
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	