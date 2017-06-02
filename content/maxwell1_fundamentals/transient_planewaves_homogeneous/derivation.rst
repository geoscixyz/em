.. _transient_planewaves_homogeneous_derivation:

Derivation
==========

General Solution for a Planewave
--------------------------------

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_time_derive

   Geometry of an EM plane wave propagating downwards.

To obtain a solution for EM planewaves within a homogeneous medium, let us begin with the following vector wave equations for :math:`\mathbf{e}` and :math:`\mathbf{h}`:

.. math:: 
    \boldsymbol{\nabla}^2 \mathbf{e} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} &= 0\\
    \boldsymbol{\nabla}^2 \mathbf{h} - \mu\epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{h}}{\partial t} &= 0
    :name: Wave_full_analytic

For simplicity, let us assume that the planewave propagates along the z-direction. According to Griffiths :cite:`griffiths1999` (pp. 378), the electric and magnetic fields supported by a planewave are transverse to the direction of propagation; thus the electric and magnetic fields lie in the xy-plane. In this case, the governing equation for the electric field simplifies to:

.. math::
    \frac{\partial^2 \mathbf{e}}{\partial z^2} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} = 0

where :math:`\mathbf{e} \equiv \mathbf{e}(z,t)`; thus it does not depend on x or y. In order to provide initial conditions for the PDE, let the electric field be caused an impulse such that our initial conditions are given by:

.. math::
  \mathbf{e}(t=0)=\mathbf{E}_0\delta(t)
  :name: e_impulse

where :math:`\delta(t)` is a Dirac-Delta function at :math:`t=0`. Instead of solving the time-depend PDE directly, we will apply the inverse Laplace transform to analytic solutions derived in the :ref:`frequency-domain<harmonic_planewaves_homogeneous_derivation>`:

.. math::
    \mathbf{E} =  \mathbf{E}_0^- e^{ikz} + \mathbf{E}_0^+ e^{-ikz}
    :name: e_frequency_analytic

where :math:`E_0^-` and :math:`E_0^+` are the vector amplitudes of down-going and up-going waves, respectively. Note that the harmonic term :math:`e^{-i\omega t}` term is being supressed. The time domain solution for an impulse excitation can be expressed as:

.. math::
	\mathbf{e}(t) = \mathcal{F}^{-1}[\mathbf{E}(\omega)]

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

Both the up-going and down-going waves have two terms. The first term, containing the Dirac delta function, is the wave term. The second term is the diffusion term. Constants :math:`a` and :math:`c` control both the wave and diffusion properties of the plane wave.

In the case that the EM wave were caused by an impulse corresponding to initial conditions :math:`\mathbf{h}(t=0) = \mathbf{H_0}\delta (t)`, the general solution for the magnetic field would be given by:

.. math::
    \mathbf{h}(t) =& \mathbf{H}_0^- \Bigg ( e^{a(z/c)} \delta \bigg ( t+\frac{z}{c} \bigg ) -\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t+\frac{z}{c} \bigg ) \Bigg )\\
    &+ \mathbf{H}_0^+ \Bigg ( e^{-a(z/c)} \delta \bigg ( t-\frac{z}{c} \bigg ) +\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t-\frac{z}{c} \bigg ) \Bigg )
    :name: h_wave_analytic_sol

Note that Eq. :eq:`e_wave_analytic_sol` and Eq. :eq:`h_wave_analytic_sol` have the exact same form.

.. note::

    Eqs. :eq:`e_wave_analytic_sol` and :eq:`h_wave_analytic_sol` are still general solutions, as only initial conditions have been applied. To determine :math:`\mathbf{E}_0^-` and :math:`\mathbf{E}_0^+` or :math:`\mathbf{H}_0^-` and :math:`\mathbf{H}_0^+`, you must envoke a set of boundary conditions. For example, :math:`\mathbf{e}(z \rightarrow -\infty,t) = 0` in addition to :math:`\mathbf{e}(t=0) = \mathbf{E}_0 \delta (t)` results in a downward propagating electric field.

.. _transient_planewaves_homogeneous_derivation_app:

Supporting Derivation for the App
---------------------------------

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_time_derive_app

   Setup diagram of plane EM wave propagation heading downward (negaitve :math:`z`).

The app simulates the downward propagation of an EM planewave due to an impulse current. As we can see in :numref:`planewavedown_time_derive_app`, the planewave is polarized such that the electric lies along the x-direction and the magnetic field lies along the y-direction. Physically, we can think of this wave as being caused by a horizontal impulse current :math:`\mathbf{I}(t) = I_0 \delta (t) \mathbf{u_x}`, where :math:`\mathbf{u_x}` is the unit vector in the x-direction.

For the app, we only consider the quasi-static approximation of Eq. :eq:`e_wave_analytic_sol`. This can be obtained by taking the inverse Laplace transform of the :ref:`corresponding harmonic solution<harmonic_planewaves_homogeneous_derivation_app_soln>` such that :math:`k = \sqrt{-i\omega\mu\sigma}`, i.e:

.. math::
    \mathbf{E} (z,\omega) = E_x (z,\omega) \, \mathbf{u_x} = E_{x,0}^{-} e^{i\sqrt{-i\omega\mu\sigma}z} \mathbf{u_x}
    :name:

where :math:`E_x` is a scalar function and :math:`E_{x,0}^{-}` is the scalar amplitude of the electric field. If we replace :math:`s=i\omega`, the inverse Laplace transform of :math:`E_x (z,w)` becomes:

.. math::
    \mathcal{L}^{-1}[E_x (z,\omega)] = \mathcal{L}^{-1} \Bigg [ E_{x,0}^- \, e^{- \sqrt{\mu\sigma s} z} \Bigg ]
    :name:

If we use the following identity (Abramowitz and Stegun, 1964):

.. math::
    \mathcal{L}^{-1} \Bigg [ e^{-\alpha \sqrt{s}} \Bigg ] = \frac{\alpha}{2 \pi^{1/2} t^{3/2}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \;\;\; \alpha \geq 0


the quasi-static solution for the electric field at :math:`t>0` is given by:

.. math::
	\mathbf{e}(t) = e_x(t) \mathbf{u_x} = E_{x,0}^- \frac{\big (\mu\sigma)^{1/2} z}{2\pi^{1/2} t^{3/2}} \, e^{-\mu\sigma z^2/4t} \, \mathbf{u_x}
	:name:

Similarly, the solution for the magnetic field can be obtained by taking inverse Laplace transform of the :ref:`corresponding harmonic solution<harmonic_planewaves_homogeneous_derivation_app_soln>` such that :math:`k = \sqrt{-i\omega\mu\sigma}`.

.. math::
    \mathcal{L}^{-1}[H_y (z,\omega)] = \mathcal{L}^{-1} \Bigg [ - \frac{ik}{i\omega \mu} E_{x,0}^- \, e^{ikz} \Bigg ] = \mathcal{L}^{-1} \Bigg [ - \sqrt{ \dfrac{\sigma}{\mu s}} E_{x,0}^- \, e^{- \sqrt{\mu\sigma s} z} \Bigg ]

where :math:`k = \sqrt{-i\omega\mu\sigma}`, we replace :math:`s = i\omega` and we let :math:`\sqrt{-1} = -i`. If we use the following identity (Abramowitz and Stegun, 1964):

.. math::
    \mathcal{L}^{-1} \Bigg [ \frac{1}{\sqrt{s}} e^{-\alpha \sqrt{s}} \Bigg ] = \frac{1}{\sqrt{\pi t}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \;\;\; \alpha \geq 0

the quasi-static solution for the magnetic field is given by:

.. math::
    \mathbf{h}(t) = h_y(t) \mathbf{u_y} =  -E_{x,0}^- \sqrt{\dfrac{\sigma}{\pi\mu t}}\, e^{-\mu\sigma z^2/4t} \, \mathbf{u_y}

where :math:`\mathbf{u_y}` is the unit vector in the y-direction.



