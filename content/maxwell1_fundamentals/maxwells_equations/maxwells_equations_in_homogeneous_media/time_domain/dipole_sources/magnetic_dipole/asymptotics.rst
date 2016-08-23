.. _time_domain_magnetic_dipole_asymptotics:

Asymptotics
===========

.. topic:: Purpose

    Purpose here



Near-Field/Late-Times
---------------------

For fields which are very close to the electric dipole source, or at sufficiently late times:

.. math::
	\theta r = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2} r \ll 1
	:label: theta_nearfield_latetime


In this case, the exponential and complimentary error function can be approximated as follows:

.. math::
	e^{-\theta^2 r^2} \approx 1 - \theta^2 r^2 + O (\theta^4 r^4)
	:label: Taylor_expansion_exp
	
and

.. math::
	\textrm{erfc}(\theta r) \approx 1 - \frac{2}{\sqrt{\pi}} \theta r + \frac{1}{3 \sqrt{\pi}}\theta^3 r^3 + O (\theta^5 r^5)
	:label: erfc_approximation


By substituting the above expressions into the full analytic solutions for :math:`{\bf e_e}` and :math:`{\bf h_e}`, we can obtain near-field/late-time approximations.
In the case of the electric field:

.. math::
	{\bf e_e}(t) \approx \frac{2 m \theta^5}{\pi^{3/2} \sigma} \big ( -z \, \hat y + y \, \hat z \big )
	:label: e_nearfield_latetime

According to Eq. :eq:`e_nearfield_latetime`, the near-field/late-time electric field decays proportional to :math:`t^{-5/2}`.
For the magnetic field, the near-field/late-time approximation is given by:

.. math::
	{\bf h_e}(t) \approx \frac{m}{4\pi r^3} \Bigg [ \Bigg ( \frac{x^2}{r^2}\hat x + \frac{xy}{r^2}\hat y + \frac{xz}{r^2}\hat z \Bigg ) \Bigg ( 3 - \frac{1}{\sqrt{\pi}}\theta^3 r^3 \Bigg ) - \Bigg ( 1 + \frac{7}{3\sqrt{\pi}} \theta^3 r^3 \Bigg ) \hat x \Bigg ]
	:label: h_nearfield_latetime

According to Eq. :eq:`h_nearfield_latetime`, the near-field/late-time magnetic field is a sum of the DC magnetic field (link) and a time-dependent part which decays proportional to :math:`t^{-3/2}`.
The near-field/late-time approximation for the time-derivative of the magnetic field is given by:

.. math::
	\frac{\partial {\bf h_e}}{\partial t} \approx 
	:label: dhdt_nearfield_latetime

According to Eq. :eq:`dhdt_nearfield_latetime`, the time-derivative of the magnetic field has a single term which decays proportional to :math:`t^{-5/2}`.


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







