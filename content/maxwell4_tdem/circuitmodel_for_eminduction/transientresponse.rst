.. _transientresponse:

Transient responses
===================

Often time domain EM method utilize a transient primary field rather than an alternating (or sinusoidal) one. That is, the source varies stepwise in time (TDEM) than varies harmonically (FDEM). We consider the theoretical connections between two types of response.

A unit-step function (same as Heaviside step function) can be written in a spectral form:

.. math::
    u(t) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} U (\omega) e^{\imath \omega t}d \omega

where :math:`\omega` is angular frequency (rad/s) and :math:`U(\omega)` is the spectrum of :math:`u(t)` and is given by

.. math::
    U(\omega) = \int_{-\infty}^{\infty} u(t) e^{-\imath \omega t} d t \\
              = \int_{0}^{\infty} u(t) e^{-\imath \omega t} d t

Although the latter integral is divergent, it can be evaluated by introducing a damping facttor :math:`e^{-pt} \ (p>0)` and taking limit:

.. math::
    U(\omega) = \lim_{p \rightarrow 0} \int_{0}^{\infty} u(t) e^{-\imath \omega t} e^{-pt} d t = \frac{1}{\imath \omega}

If the Fourier transform of :math:`u(t)` is :math:`\frac{1}{\imath \omega}` then it is clear that the transformation of the secondary field :math:`h^s_{on}` produced by a step-on current: :math:`I u(t)` is related to the respones :math:`H^s (\omega) e^{\imath \omega t}` due to a sinusoidal current: :math:`I e^{\imath \omega t}` as follows:

.. math::
    h^s_{on} = \frac{1}{2 \pi} \int_{-\infty}^{\infty} \frac{H^s(\omega)}{\imath \omega}  e^{\imath \omega t} d \omega


Current
-------

Response function
-----------------

Induced EMF
-----------

