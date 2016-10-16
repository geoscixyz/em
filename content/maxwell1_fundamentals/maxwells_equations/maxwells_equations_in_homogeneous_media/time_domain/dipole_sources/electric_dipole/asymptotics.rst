.. _time_domain_electric_dipole_asymptotics:

Asymptotics
===========

.. purpose::

    Here, we present near-field/late-time approximations for the transient electric and magnetic fields.



Near-Field/Late-Times
---------------------

For fields which are very close to the electric dipole source, or at sufficiently late times:

.. math::
	\theta r = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2} r \ll 1
	:label: theta_nearfield_latetime


In this case, the exponential and error functions can be approximated using Taylor expansion. Thus:

.. math::
	e^{-\theta^2 r^2} = 1 - \theta^2 r^2 + \frac{1}{2}\theta^4 r^4 + \; ...
	:label: Taylor_expansion_exp

and

.. math::
	\textrm{erf}(\theta r) =  \frac{2}{\sqrt{\pi}} \theta r - \frac{2}{3 \sqrt{\pi}}\theta^3 r^3 + \frac{1}{5\sqrt{\pi}} \theta^5 r^5 + \;...
	:label: erfc_approximation


By substituting the above Taylor expansions into the :ref:`full analytic solutions<time_domain_electric_dipole_analytic_solution>` for :math:`{\bf e_e}` and :math:`{\bf h_e}`, we can obtain near-field/late-time approximations.
In the case of the electric field:

.. math::
	{\bf e_e}(t) \approx \frac{ Ids}{15 \pi^{3/2} \sigma r^3} \Bigg [ 6 \,\theta^5 r^5 \Bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2}\hat z \Bigg )   + \Big ( 10 \,\theta^3 r^3 + 3 \,\theta^5 r^5 \Big ) \hat x \Bigg ]
	:label: e_nearfield_latetime

According to Eq. :eq:`e_nearfield_latetime`, :math:`\hat y` and :math:`\hat z` components of the near-field/late-time electric field decay proportional to :math:`t^{-5/2}`.
However, :math:`\theta^3 r^3` terms for the :math:`\hat x` component do not cancel.
Therefore, the :math:`\hat x` component of the electric field decays proportional to :math:`t^{-3/2}` at sufficiently late times.
For the magnetic field, the near-field/late-time approximation is given by:

.. math::
	{\bf h_e}(t) \approx \frac{\theta^3 Ids}{3\pi^{3/2}} \big (-z \, \hat y + y \, \hat z \big )
	:label: h_nearfield_latetime

According to Eq. :eq:`h_nearfield_latetime`, the near-field/late-time electric field decays proportional to :math:`t^{-3/2}`.
Taking the derivative of Eq. :eq:`h_nearfield_latetime`, near-field/late-time approximation for the time-derivative of the magnetic field is given by:

.. math::
	\frac{\partial {\bf h_e}}{\partial t} \approx \frac{2 \theta^5 Ids}{\mu \sigma \pi^{3/2}} \big ( z \, \hat y - y \, \hat  z \big )
	:label: dhdt_nearfield_latetime

According to Eq. :eq:`dhdt_nearfield_latetime`, the time-derivative of the magnetic field decays proportional to :math:`t^{-5/2}`.


Far-Field
---------

**Everything goes to zero so there is no asymptotic for this**



For fields which are far from the electric dipole source, or at sufficiently early times:

.. math::
	\theta r = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2} r \gg 1
	:label: theta_farfield

In this case, the exponential and complimentary error function can be approximated as follows:

.. math::
	e^{-\theta^2 r^2} \approx 0
	:label: exp_approximation

and

.. math::
	\textrm{erfc}(\theta r) \approx 0
	:label: erfc_approximation_2
















