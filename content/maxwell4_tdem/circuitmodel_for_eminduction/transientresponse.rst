.. _transientresponse:

Transient responses
===================

.. purpose::

    Understand relationship between transient (TDEM) and harmonic (FDEM)
    responses. Differentiate standard types of transient responses: a) step-on,
    b) impulse, and c) step-off.

.. plot::

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.rcParams['font.size'] = 12
    tau = [1e-1, 1e-1/5, 1e-1/10]
    fig = plt.figure(figsize=(10, 3))
    ax1 = plt.subplot(131)
    ax2 = plt.subplot(132)
    ax3 = plt.subplot(133)
    axs = [ax1, ax2, ax3]

    t = np.linspace(-0.2, 1, 300)
    oncurrent = np.ones_like(t)
    oncurrent[t<0.] = 0.

    offcurrent = np.zeros_like(t)
    offcurrent[t<0.] = 1.

    omega = 5*np.pi*2
    current_FD = np.cos(t*omega)

    ax1.plot(t, oncurrent, "k", lw=3)
    ax2.plot(t, offcurrent, "k", lw=3)
    ax3.arrow(0, 0, 0, 0.9, width=0.003, facecolor="k")

    for ax in axs:
        ax.plot(t, np.zeros_like(t), "k:", lw=1)
        ax.plot(np.zeros_like(t), np.linspace(-0.2, 1.2, t.size), "k:", lw=1)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Current (A)")
        ax.set_ylim(-.2, 1.2)

    ax1.set_title("Step-on current")
    ax2.set_title("Step-off current")
    ax3.set_title("Impulse current")
    plt.tight_layout()
    plt.show()

Step-on response
----------------

Often time domain EM method utilize a transient primary field rather than an
alternating (or sinusoidal) one. That is, the source varies stepwise in time
(TDEM) than varies harmonically (FDEM). We consider the theoretical
connections between two types of response.

A unit-step function (same as Heaviside step function) can be written in a
spectral form:

.. math::
    u(t) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} U (\omega) e^{\imath \omega t}d \omega

where :math:`\omega` is angular frequency (rad/s) and :math:`U(\omega)` is the
spectrum of :math:`u(t)` and is given by

.. math::
    U(\omega) = \int_{-\infty}^{\infty} u(t) e^{-\imath \omega t} d t \\
              = \int_{0}^{\infty} u(t) e^{-\imath \omega t} d t

Although the latter integral is divergent, it can be evaluated by introducing
a damping facttor :math:`e^{-pt} \ (p>0)` and taking limit:

.. math::
    U(\omega) = \lim_{p \rightarrow 0} \int_{0}^{\infty} u(t) e^{-\imath \omega t} e^{-pt} d t = \frac{1}{\imath \omega}

If the Fourier transform of :math:`u(t)` is :math:`\frac{1}{\imath \omega}`
then it is clear that the transformation of the secondary field
:math:`h^s_{on}` produced by a step-on current: :math:`I u(t)` is related to
the response :math:`H^s (\omega) e^{\imath \omega t}` due to a sinusoidal
current: :math:`I e^{\imath \omega t}` as follows:

.. math::
    h^s_{on}(t) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} \frac{H^s(\omega)}{\imath \omega}  e^{\imath \omega t} d \omega
    :label: stepon

From :eq:`stepon`, computing transient response, :math:`h^s_{on}` is possible
with full spectrum of harmonic response, :math:`H^s(\omega)`. Conversely, we
know from the Fourier theorem:

.. math::
    \frac{1}{\imath \omega} H^s(\omega) = \int_{-\infty}^{\infty} h^s_{on}(t) u(t) e^{-\imath \omega t} d t

and thus

.. math::
    H^s(\omega) = \imath \omega \int_{0}^{\infty} h^s_{on}(t) e^{-\imath \omega t} d t

Therefore, the harmonic response is computable if the transient response
:math:`h^s_{on}(t)` is known for :math:`t>0`.

Impulse response
----------------

Impulse response indicates that we put Dirac-Delta function as a current,
which corresponds steady-state source in frequency domain (:math:`Ie^{\imath
\omega t}`). Note that Fourier transform of :math:`Ie^{\imath \omega t}` is
:math:`I\delta(t)`, where :math:`\delta(t)` is Dirac-Delta function.

From step-on response :math:`h^s_{on}(t)`, we can simply obtain impulse
response :math:`h^s(t)`

.. math::
    h^s(t) = \frac{\partial h^s_{on}(t)}{\partial t}

or it can be defined with Fourier transform

.. math::
    h^s(t) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} H^s(\omega)  e^{\imath \omega t} d \omega

Conversely, from the impulse response, step-on response can be defined as

.. math::
    h^s_{on}(t) = \int_{0}^t h^s(\tau) d \tau

Step-off response
-----------------

For practical applications, common current waveform is closer to step-off
rather than step-on. Step-off waveform can be defined as

.. math::
    u(-t) = 1-u(t)

Then step-off response :math:`h^s_{off}(t)` can be

.. math::
    h^s_{off}(t) = \int_{0}^{\infty} h^s(\tau) d \tau - \int_{0}^t h^s(\tau) d \tau \\
                 = h^s_{on}(\infty) - h^s_{on}(t), \ \ t > 0

Thus the derivative of :math:`h^s_{off}(t)` with respect to time is
:math:`-h^s(t)`, which is the negative of the impulse response. In the
following section, we discuss transient responses from the circuit model.
