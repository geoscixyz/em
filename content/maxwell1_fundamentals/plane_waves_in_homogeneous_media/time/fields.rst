.. _time_domain_plane_wave_sources_fields:

Fields
======

.. purpose::

    Within the quasi-static approximation, we provide explicit expressions for both eletric and magnetic fields for plane EM wave equations with an impulse electric field, and understands different features of electric and magnetic fields propagation in time.

.. figure:: ../images/planewavedown.png
   :align: center
   :scale: 60%

   Setup diagram of plane EM wave propagation heading downward (negaitve :math:`z`).

As shown in :numref:`planewavedown`, the same setup is considered to :ref:`frequency_domain_plane_wave_sources_fields`. However, in :ref:`time_domain_plane_wave_sources_analytic_solution` to solve the plane EM wave equations, we let known impulse electric field as an initial condition, and obtained full expression for the electric field. Here we limit our attention to quasi-static regime where displacement currents are ignored (:math:`\epsilon \frac{\partial \mathbf{e}}{\partial t} << \sigma \mathbf{e}`).

EM fields
^^^^^^^^^

Time domain magnetic for the given setup can be simply derived by transforming frequency domain magnetic field to time. Here we are going to use inverse Laplace transform. Frequency domain magnetic field obtained in :ref:`frequency_domain_plane_wave_sources_fields` can be rewritten as

.. math::
    H_y = -\frac{i k}{i\omega \mu} E_x = -\frac{i k}{i\omega \mu} E_{0 \ x}^- e^{ikz},
    :label: fd_Hy

where :math:`E_x = E_{0 \ x}^- e^{ikz}`, and here :math:`k = \sqrt{-i\omega\mu\sigma}` due to quai-static approximation. To evaluate transformation, use inverse laplace transform pair from :cite:`ward1988`:

.. math::
    \mathcal{L}^{-1}[\frac{ik}{s}e^{-ikr}]
    = \frac{2}{\pi^{1/2}} \theta e^{-\theta^2r^2},

where :math:`\text{erfc}` is the complementary error function, :math:`s=i\omega` and :math:`\theta=\sqrt{\frac{\mu\sigma}{4t}}`.

In Laplace domain by substituting :math:`s=i\omega`, and :math:`z=-r` Eq. :eq:`fd_Hy` can be rewritten as

.. math::
    H_y = - \frac{E_{0 \ x}^-}{\mu } \frac{ikr}{s} e^{-ikr},
    :label: ld_Hy

Evaluating inverse Laplace transform of this yields:

.. math::
    h_y(t) = \mathcal{L}^{-1}[H_y(s)]
    = - \frac{E_{0 \ x}^-}{\mu} \frac{2}{\pi^{1/2}} \theta e^{-\theta^2r^2},
    :label: hy_impulse_quasistatic

which can be rewritttenas

.. math::
    h_y(t) = - E_{0 \ x}^- \frac{2}{\pi^{1/2} \mu} \theta e^{-\theta^2z^2},

.. math::
    e_x(t) = -E_{0 \ x}^- \frac{(\mu\sigma)^{1/2}z}{2 \pi^{1/2}t^{3/2}} e^{-\mu\sigma z^2 / (4t)}
    = -E_{0 \ x}^- \frac{z}{ \pi^{1/2}t} \theta e^{-\theta^2z^2}.
    :label: ex_impulse_quasistatic

:numref:`Ward1988Fig1_2withhy` a and b shows both :math:`e_x` and :math:`h_y` as a function of time and depth, respectively.

.. figure:: ../images/Ward1988Fig1_2withhy.png
   :align: center
   :scale: 40%
   :name: Ward1988Fig1_2withhy

   Electric and magnetic field as a function of time 100 m from a 1D impulse in the field in a 0.01 S/m whole space (a). Electric and magnetic field at t = 0.03 ms as a function of distance (Modifed from :cite:`ward1988`) (b). Black and red lines differentiate electric and magnetic field.

.. todo::

    What physical meaning can we infer from magnetic field?

.. Dummy
.. .. math::
..     \mathcal{L}^{-1}[\frac{1}{s}e^{-ikr}] = \text{erfc} (\theta r)
