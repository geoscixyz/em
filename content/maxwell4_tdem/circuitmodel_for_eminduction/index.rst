.. _emi_tuotorial_index_TD:

Circuit Model for EM Induction
==============================

.. purpose::

    We expand EM response derived from the circuit model in :ref:`frequency
    domain <emi_tuotorial_index_FD>` to time domain.

The basic EM  survey is shown in :numref:`Concepts_3loops_TD`. The time
varying magnetic field (referred to as the primary field) in the Tx induces
currents in the conductor. Those currents produce a secondary field that can
be recorded at the receiver.

.. figure:: ../../maxwell3_fdem/circuitmodel_for_eminduction/images/Concepts_3loops.png
   :align: center
   :scale: 60%
   :name: Concepts_3loops_TD

   Conceptual diagrams for EM inductions. Top panel shows excitation of the
   conductor using induction, and botton panel shows corresponding 3-loops
   system.

From :ref:`faraday`, we establish the link between EMF (:math:`\mathcal{E}`,
voltage), and time varying flux (:math:`\Phi_b`). Below diagram illustrates
how EMF could be generated from time-varying flux (:math:`\mathcal{E}= -
\frac{d \Phi_b}{dt}  = \imath \omega \Phi_b`). The EMF (voltage) produces a
current in the loop.

.. figure:: ../../maxwell3_fdem/circuitmodel_for_eminduction/images/EMF.png
    :align: center
    :scale: 60%
    :name: EMF_TD

The circuit model is now understood as follows:

- Loop 1: is the transmitter (Tx). It has a time varying current (often a
  step-off current in time domain: :math:`I_1 (1-u(t))`) and hence produces a
  time varying field everywhere in space. Here :math:`u(t)` indicates
  Heaviside step function. **This is the main difference in time domain
  response compared to frequency domain using sinusoidal current.**

- Loop 2: represents the conductive body. The time varying flux generates
  currents in the conductor (:math:`I_2 (t)`). These time varying currents
  produce a time varying field everywhere in space.

- Loop 3: is the receiver (Rx). The measured EMF, :math:`\mathcal{E}^t` is

  .. math::
    \mathcal{E}^t = \mathcal{E}^p +\mathcal{E}^s

  where superscripts refer respectively  to the total, primary, and  secondary fields.

In time domain, primary and secondary voltage at the Loop due to step-off
current can be expressed as

.. math::
  \mathcal{E}^p = M_{13} I_1 \delta(t)

.. math::
  \mathcal{E}^s = \frac{M_{12}M_{23}}{L} \frac{I_1 u(t)}{\tau}  e^{-t / \tau}

Here, :math:`M_{ij}` is the mutual inductance between loops :math:`i` and
:math:`j`, :math:`L` is the self inductance of the target loop.

.. note::

    The terms in these equations do not separate quite as neatly as in the
    frequency domain (:math:`\mathcal{E}^s / \mathcal{E}^p = CQ`). All have
    dimensions, so scale is important in time domain.

Below shows secondary voltage with variable :math:`\tau` in Log-Log and Lin-
Log plot. In the Lin-Log plot, exponential decay will be straight line.

.. plot::

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.rcParams['font.size'] = 12
    # Time constant
    tau = [1e-1, 1e-1/5, 1e-1/10]
    fig = plt.figure(figsize=(10, 3))
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)
    axs = [ax1, ax2]
    color = ["k", "b", "r"]
    t = np.logspace(-3, 0, 61)
    for i in range(3):
        resp = 1./tau[i] * np.exp(-t/tau[i])
        ax1.loglog(t, resp, color[i], lw=3)
        ax2.semilogy(t, resp, color[i], lw=3)
    for ax in axs:
        ax.grid(True)
        ax.set_ylim(1e-2, 1e2)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Secondary voltage (V)")
    ax2.legend(("$\\tau=0.1$","$\\tau=0.05$", "$\\tau=0.01$"), loc=1)
    ax1.set_title("Log-Log scale")
    ax2.set_title("Lin-Log scale")
    plt.tight_layout()
    plt.show()

In the following pages we illustrate

.. - How to transform frequency domain response to time domain
.. - Convert frequency domain response to time domain
.. - Provide widgets to explore concepts

.. toctree::
    :maxdepth: 1

    transientresponse
    understanding_trasientEMresponse
    synthesis_FDEMandTDEMresponse




