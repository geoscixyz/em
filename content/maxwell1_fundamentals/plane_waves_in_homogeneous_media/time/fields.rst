.. _time_domain_plane_wave_sources_fields:

Fields
======

.. purpose::

    Within the quasi-static regime, we provide explicit expressions for the electric and magnetic fields supported by plane waves. Relationships between the electric and magnetic fields are discussed.

.. figure:: ../images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewave_down_fields_time

   Setup diagram of plane EM wave propagation heading downward (negaitve :math:`z`).

When deriving :ref:`analytic solutions<time_domain_plane_wave_sources_analytic_solution>`, we considered a downward propgating plane wave caused by an impulse :math:`\mathbf{e} (t=0)=\mathbf{E}_0 \delta (t)` (:numref:`planewave_down_fields_time`). This lead to set a complicated expressions for both the electric and magnetic fields. For simplicity, we will consider only the quasi-static solution (:math:`\omega\epsilon \ll \sigma`). For a down-going wave, the solution is given by:

.. math::
    \mathbf{e}(t) = -\mathbf{E}_0^- \frac{(\mu\sigma)^{1/2}z}{2 \pi^{1/2} t^{3/2}} e^{-\mu\sigma z^2 / (4t)}

According to the setup in :numref:`planewave_down_fields_time`, the impulse only generates components for the electric field in the x-direction. As a result, the electric field as a function of time can be simplified to:

.. math::
    \mathbf{e}(t) = e_x(t) \mathbf{u_x} = -E_{x,0}^- \frac{(\mu\sigma)^{1/2}z}{2 \pi^{1/2} t^{3/2}} e^{-\mu\sigma z^2 / (4t)} \mathbf{u_x}

where :math:`\mathbf{u_x}` is the unit vector in the x-direction. Using Faraday’s law, we find that the corresponding magnetic field only has components in the y-direction. This can be described by the following ODE:

.. math::
    \frac{\partial e_x}{\partial z} + \mu \frac{\partial h_y}{\partial t}= 0

To obtain a quasi-static solution for the magnetic field, it is best to take the :ref:`frequency domain solution<frequency_domain_plane_wave_sources_analytic_solution>` and apply the inverse Laplace transform:

.. math::
    \mathcal{L}^{-1}[H_y (z,\omega)] = \mathcal{L}^{-1} \Bigg [ - \frac{ik}{i\omega \mu} E_{x,0}^- \, e^{ikz} \Bigg ] = \mathcal{L}^{-1} \Bigg [ \sqrt{ \dfrac{\sigma}{\mu s}} E_{x,0}^- \, e^{- \sqrt{\mu\sigma s} z} \Bigg ]

where :math:`k = \sqrt{-i\omega\mu\sigma}` and we replace :math:`s = i\omega`. If we use the following identity (Abramowitz and Stegun, 1964):

.. math::
    \mathcal{L}_{-1} = \Bigg [ \frac{1}{\sqrt{s}} e^{-\alpha \sqrt{s}} \Bigg ] = \frac{1}{\sqrt{\pi t}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \;\;\; \alpha \geq 0

the quasi-static solution for the magnetic field is given by:

.. math::
    \mathbf{h}(t) = h_y(t) \mathbf{u_y} =  E_{x,0}^- \sqrt{\dfrac{\sigma}{\pi\mu t}}\, e^{-\mu\sigma z^2/4t} \, \mathbf{u_y}

where :math:`\mathbf{u_y}` is the unit vector in the y-direction.




.. EM fields
.. ^^^^^^^^^

.. Time domain magnetic for the given setup can be simply derived by transforming frequency domain magnetic field to time. Here we are going to use inverse Laplace transform. Frequency domain magnetic field obtained in :ref:`frequency_domain_plane_wave_sources_fields` can be rewritten as

.. .. math::
..     H_y = -\frac{i k}{i\omega \mu} E_x = -\frac{i k}{i\omega \mu} E_{0 \ x}^- e^{ikz},
..     :label: fd_Hy

.. where :math:`E_x = E_{0 \ x}^- e^{ikz}`, and here :math:`k = \sqrt{-i\omega\mu\sigma}` due to quai-static approximation. To evaluate transformation, use inverse laplace transform pair from :cite:`ward1988`:

.. .. math::
..     \mathcal{L}^{-1}[\frac{ik}{s}e^{-ikr}]
..     = \frac{2}{\pi^{1/2}} \theta e^{-\theta^2r^2},

.. where :math:`\text{erfc}` is the complementary error function, :math:`s=i\omega` and :math:`\theta=\sqrt{\frac{\mu\sigma}{4t}}`.

.. In Laplace domain by substituting :math:`s=i\omega`, and :math:`z=-r` Eq. :eq:`fd_Hy` can be rewritten as

.. .. math::
..     H_y = - \frac{E_{0 \ x}^-}{\mu } \frac{ikr}{s} e^{-ikr},
..     :label: ld_Hy

.. Evaluating inverse Laplace transform of this yields:

.. .. math::
..     h_y(t) = \mathcal{L}^{-1}[H_y(s)]
..     = - \frac{E_{0 \ x}^-}{\mu} \frac{2}{\pi^{1/2}} \theta e^{-\theta^2r^2},
..     :label: hy_impulse_quasistatic

.. which can be rewritttenas

.. .. math::
..     h_y(t) = - E_{0 \ x}^- \frac{2}{\pi^{1/2} \mu} \theta e^{-\theta^2z^2},

.. .. math::
..     e_x(t) = -E_{0 \ x}^- \frac{(\mu\sigma)^{1/2}z}{2 \pi^{1/2}t^{3/2}} e^{-\mu\sigma z^2 / (4t)}
..     = -E_{0 \ x}^- \frac{z}{ \pi^{1/2}t} \theta e^{-\theta^2z^2}.
..     :label: ex_impulse_quasistatic

.. :numref:`Ward1988Fig1_2withhy` a and b shows both :math:`e_x` and :math:`h_y` as a function of time and depth, respectively.


.. figure:: ../images/EHtime.gif
   :align: right
   :figwidth: 50%
   :name: planewave_fields_time_1D

   Electric and magnetic fields from a down-going EM wave resulting from initial conditions :math:`\mathbf{e}(t) = E_0 \delta (t) \, \mathbf{u_x}`.

Examining the Fields
^^^^^^^^^^^^^^^^^^^^

In :numref:`planewave_fields_time_1D`, we show the electric and magnetic fields from the down-going wave illustrated in :numref:`planewave_down_fields_time`. The square-root of the amplitude is being plotted so that characteristics of the wave are more easily visible over all times. Note that the electric field is in the positive x-direction and the magnetic field is in the negative y-dirction. We can verify that the EM is propagating downward by computing the :ref:`Poynting vector<plane_waves_in_homogeneous_media_index_Poynting>`.

Examining :numref:`planewave_fields_time_1D`, we can see both the wave and diffusive behaviours of the signal. We can also see the time-dependency of the peak distance; i.e. the peak velocity. The peak distance (:math:`z_{max}`) increases proportional to :math:`t^{1/2}` whereas the peak velocity (:math:`v_{max}`) is proprtional to :math:`t^{-1/2}`.




