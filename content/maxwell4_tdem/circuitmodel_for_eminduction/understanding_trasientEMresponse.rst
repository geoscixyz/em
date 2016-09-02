.. _understanding_trasientEMresponse:

Understanding the Transient EM response
=======================================

.. topic:: Purpose

    We provide expressions for trasient responses of the circuit model, compare them with harmonic responses, and understand their decay features.

For the harmonic response, we used normalized EMF or magnetic field:

.. math::
      \frac{H_3^s }{H_3^p} = \frac{\mathcal{E}_3^s }{\mathcal{E}_3^p}
      = - \frac{M_{12}M_{23}}{M_{13}L} \Big[\frac{\alpha^2 + \imath \alpha}{1+\alpha^2}\Big]

which was reduced to

.. math::
      \frac{H_3^s }{H_3^p} = \frac{\mathcal{E}_3^s }{\mathcal{E}_3^p} = C Q (\alpha)

where :math:`C` and :math:`Q` are coupling coefficient and response function, respectively. We did not consider effect of :math:`C`, but focus on :math:`Q` because it determines time behaviour in trasient response.

However, for the transient response this neat normalziation does not work, because of some complicated time function in :math:`\mathcal{E}_3^s` and :math:`\mathcal{E}_3^p` (assuming step-on current waveform):

.. math::
  \mathcal{E}^p_{on} = - M_{13} I_1 \delta(t)

.. math::
  \mathcal{E}^s_{on} = - \frac{M_{12}M_{23}}{L} \frac{I_1 u(t)}{\tau}  e^{-t / \tau}

All terms in above EMFs have dimensions hence scale is much more important for the trasient response compared to the harmonic one. In following, we work through time domain expressions for the current, response function, and EMF.

Currrent at the target loop
---------------------------

Current in the target loop for harmoninc case is

.. math::
  I_2 e^{\imath \omega t}
  =  - \frac{\imath \omega \tau}{ 1 + \imath \omega \tau} \frac{M_{12}I_1}{L} e^{\imath \omega t} \\

Corresponding step-on resposne, :math:`i_{2 \ on}` will be

.. math::
    i_{2 \ on} = \mathcal{F}^{-1}[\frac{I_2(\omega)}{\imath \omega}] = - \frac{M_{12}I_1}{L} e^{- t/\tau}, \ t>0

Using the relationship shown in :ref:`Transient response <transientresponse>`, we can obtain step-off response, :math:`i_{2 \ off}`:

.. math::
    i_{2 \ off} = i_{2 \ on}(\infty) - i_{2 \ on}(t) = \frac{M_{12}I_1}{L} e^{- t/\tau}, \ t>0

Only sign is different between :math:`i_{2 \ on}` and :math:`i_{2 \ off}`.

Impulse response, :math:`i_2(t)` can be simply obtained by taking time derivative to :math:`i_{2 \ on}`:

.. math::
    i_2(t) = \frac{\partial i_{2 \ on}} {\partial t} =  \frac{M_{12}I_1}{L} \frac{1}{\tau} e^{- t/\tau}, \ t>0

Response function
-----------------

Response function, :math:`Q` for the harmonic case is:

.. math::
    Q(\omega) = \frac{\imath \omega \tau}{1+\omega\tau}

Similarly, for step-on, -off, impulse responses can be written as

.. math::
    q_{on}(t) = e^{-t/\tau}, \ t>0

.. math::
    q_{off}(t) = -e^{-t/\tau}, \ t>0

and

.. math::
    q(t) = -\frac{1}{\tau} e^{-t/\tau}, \ t>0

Induced EMF at the Rx loop
--------------------------

For the harmonic case, primary and secondary EMFs at the receiver loop are:

.. math::
    \mathcal{E}^p (\omega) = - \imath \omega M_{13} I_1 e^{\imath \omega t}

.. math::
    \mathcal{E}^s (\omega) = - \imath \omega M_{23} I_2 e^{\imath \omega t} =
    \imath \omega \frac{M_{12}M_{23} I_1}{L} \Big[\frac{\imath \omega \tau}{ 1 + \imath \omega \tau} \Big] e^{\imath \omega t}

Similarly then step-on responses can be derived as

.. math::
  \mathcal{E}^p_{on}(t) = -M_{13} I_1 \delta(t)

.. math::
  \mathcal{E}^s_{on}(t) = \frac{M_{12}M_{23}}{L} \frac{I_1}{\tau}  e^{-t / \tau}, \ t>0

Step-off responses are:

.. math::
  \mathcal{E}^p_{off}(t) = M_{13} I_1 \delta(t)

.. math::
  \mathcal{E}^s_{off}(t) = -\frac{M_{12}M_{23}}{L} \frac{I_1}{\tau}  e^{-t / \tau}, \ t>0

.. note::
    Both primary EMFs: :math:`\mathcal{E}^p_{on}` and :math:`\mathcal{E}^p_{off}` are zero when :math:`t>0`. Therefore, after zero time, we only measure seconary EMF.

We do not consider impulse response for EMF because it is not well-defined.

