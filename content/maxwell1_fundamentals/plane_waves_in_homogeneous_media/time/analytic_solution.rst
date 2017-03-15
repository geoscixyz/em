.. _time_domain_plane_wave_sources_analytic_solution:

Analytic Solution (Time Domain)
===============================

.. purpose::

    Here, we provide analytic solutions for the lossy wave equation for plane waves within a homogeneous medium. From the solutions, we extract and discuss meaningful physical principles such as: peak time, peak distance and peak velocity.

.. figure:: ../images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_time

   Geometry of an EM plane wave propagating downwards.

To characterize EM waves within a homogeneous medium, let us begin with the following vector wave equations for :math:`\mathbf{e}` and :math:`\mathbf{h}`:

.. math:: 
    \boldsymbol{\nabla}^2 \mathbf{e} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} &= 0\\
    \boldsymbol{\nabla}^2 \mathbf{h} - \mu\epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{h}}{\partial t} &= 0
    :name: Wave_full_analytic

For simplicity, let us assume that the electric and magnetic fields lie in the xy-plane and that the wave propagates perpendicular to that plane (in the z-direction); see :numref:`planewavedown_time`. With this geometry, the governing equation for the electric field simplifies to:

.. math::
    \frac{\partial^2 \mathbf{e}}{\partial z^2} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} = 0

In order to provide initial conditions for the PDE, let the electric field be caused an impulse such that our initial conditions are given by:

.. math::
  \mathbf{e}(t=0)=\mathbf{E}_0\delta(t)
  :name: e_impulse

where :math:`\delta(t)` is a Dirac-Delta function at :math:`t=0`. Instead of solving the time-depend PDE directly, we will apply the inverse Fourier transform to analytic solutions derived in the :ref:`frequency domain<frequency_domain_plane_wave_sources_analytic_solution>`:

.. math::
    \mathbf{E} =  \mathbf{E}_0^- e^{ikz} + \mathbf{E}_0^+ e^{-ikz}
    :name: e_frequency_analytic

where the :math:`e^{-i\omega t}` term is being supressed. The time domain solution for an impulse excitation can be expressed as:

.. math:: \mathbf{e}(t) = \mathcal{F}^{-1}[\mathbf{E}(\omega)]

where :math:`\mathcal{F}[\cdot]` is the Fourier transform. Modified from :cite:`ward1988`, the corresponding time domain solution for the wave equation is:

.. math::
    \mathbf{e}(t) =& \mathbf{E}_0^- \Bigg ( e^{a(z/c)} \delta \bigg ( t+\frac{z}{c} \bigg ) -\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t+\frac{z}{c} \bigg ) \Bigg ) \\
    &+ \mathbf{E}_0^+ \Bigg ( e^{-a(z/c)} \delta \bigg ( t-\frac{z}{c} \bigg ) +\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t-\frac{z}{c} \bigg ) \Bigg )
    :name: e_wave_analytic_sol

where

- :math:`u(t)` is the heaviside step function

- :math:`I_1(x)` is the modified Bessel function of the first kind

- :math:`a=\dfrac{\sigma}{2\epsilon}`

- :math:`c=\dfrac{1}{\sqrt{\mu\epsilon}}`

Both the up-going and down-going waves have two terms. The first term, containing the Dirac delta function, is the wave term. The second term is the diffusion term. Constants :math:`a` and :math:`c` control both the wave and diffusion properties of the plane wave. Note that the sign of :math:`z` is negative, hence the electric field decays according to :math:`e^{a(z/c)}`.

By the same approach, the solution for the down-going magnetic field is given by:

.. math::
    \mathbf{h}(t) =& \mathbf{H}_0^- \Bigg ( e^{a(z/c)} \delta \bigg ( t+\frac{z}{c} \bigg ) -\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t+\frac{z}{c} \bigg ) \Bigg )\\
    &+ \mathbf{H}_0^+ \Bigg ( e^{-a(z/c)} \delta \bigg ( t-\frac{z}{c} \bigg ) +\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t-\frac{z}{c} \bigg ) \Bigg )
    :name: h_wave_analytic_sol

Note that Eq. :eq:`e_wave_analytic_sol` and Eq. :eq:`h_wave_analytic_sol` have the exact same form.

.. note::

    Eq. :eq:`e_wave_analytic_sol` is still a general solution, as only initial conditions have been applied. To determine :math:`\mathbf{e}_0^-` and :math:`\mathbf{e}_0^+`, you must envoke a set of boundary conditions. For example, :math:`\mathbf{e}(z \rightarrow -\infty,t) = 0` in addition to :math:`\mathbf{e}(t=0) = \mathbf{e}_0 \delta (t)`. From this solution, :math:`\mathbf{h}(t)` can be determined using Faraday's law. You could also envoke boundary conditions to solve for :math:`\mathbf{h}` and use the Ampere-Maxwell law to obtain :math:`\mathbf{e}`.

.. _time_domain_plane_wave_sources_fundamental_physics:

Fundamental physics
-------------------

EM wave propagation in the time domain can be described using the following parameters: peak time, peak distance and peak velocity. These properties are discussed below by considering the electric field of a downward propagating EM wave. Recall that there are two important regimes for EM wave propagation:

- :math:`\epsilon \omega \ll \sigma` : "Quasi-static" regime
- :math:`\epsilon \omega \gg \sigma` : "Wave" regime

In both cases, we will show how parameters describing wave propagation are simplified.

**Quasi-Static Solution:**

In the quasi-static regime, the solution for the electric field can be simplified to:

.. math::
    \mathbf{e}(t) = - \mathbf{E}_0^- \frac{(\mu\sigma)^{1/2}z}{2 \pi^{1/2}t^{3/2}} e^{-\mu\sigma z^2 / (4t)}
    :label: e_impulse_quasistatic

The electric field as a function of time and depth is shown in :numref:`Ward1988Fig1_2` (a) and (b), respectively. Both peak time and peak depth can be recognized intuitively in this figure. Below, we derive peak time, depth and velocity in the quasi-static case from Eq. :eq:`e_impulse_quasistatic`.

.. figure:: ../images/Ward1988Fig1_2.png
   :align: center
   :scale: 40%
   :name: Ward1988Fig1_2

   Electric field as a function of time 100 m from a 1D impulse in the field in a 0.01 S/m whole space (a). Electric field at t = 0.03 ms as a function of distance (Modifed from :cite:`ward1988`) (b).

**Wave Regime Solution:**

In the wave regime, the solution for the electric field can be reduced to:

.. math::
    \mathbf{e}(t) = \mathbf{E}_0^- \delta \bigg ( t+\frac{z}{c} \bigg )

In this case, the wave propagates with velocity :math:`c = 1/\!\sqrt{\mu\epsilon}` and does not diffuse at it propagates.

.. _time_domain_planewave_sources_peaktime:

Peak Time
^^^^^^^^^

The peak time is the time at which the maximum signal amplitude is observed at a particular location. The peak time observed in :numref:`Ward1988Fig1_2` (a) can be dervied by setting the time derivative of Eq. :eq:`e_impulse_quasistatic` to zero:

.. math::
    t_{max} = \frac{\mu\sigma z^2}{6}
    :label: tmax

For an impulse excitation, the peak time is proportional to the square of the distance traveled.

.. _time_domain_planewave_sources_diffusiondistance:

Peak Depth (Diffusion Distance)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At a particular time, the distance at which the signal amplitude is largest is the peak depth. The peak depth observed in :numref:`Ward1988Fig1_2` (b) can be dervied by setting the depth derivative of Eq. :eq:`e_impulse_quasistatic` to zero:

.. math::
    z_{max} = \sqrt{\frac{2 t}{\mu\sigma}} \approx 1260 \sqrt{\frac{ t}{\sigma}}.
    :label: zmax

This quantity is frequently referred to as the **diffusion distance**. It acts as a time domain equivalent for the :ref:`skin depth<frequency_domain_plane_wave_sources_skindepth>`.

.. _time_domain_planewave_sources_peakvelocity:

Peak Velocity
^^^^^^^^^^^^^

As the EM wave propagates, the peak depth moves as a function of time. The velocity at which the peak moves is called the peak velocity. By by taking time derivative of Eq. :eq:`zmax`, the peak velocity is given by:

.. math::
    v_{max} = \frac{d z_{max}}{dt} = \frac{1}{\sqrt{2\mu\sigma t}}

