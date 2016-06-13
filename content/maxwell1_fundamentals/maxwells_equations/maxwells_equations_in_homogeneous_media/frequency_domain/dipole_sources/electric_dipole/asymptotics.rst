.. _frequency_domain_electric_dipole_asymptotics:

Asymptotics
===========

.. topic:: Purpose

    Purpose here


DC-Field Approximation
----------------------

The DC electric and DC magnetic fields from an electric dipole source can be obtained from Eqs. :eq:`E_Cartesian` and :eq:`H_Cartesian` by taking the limit as :math:`\omega \rightarrow 0`.
In this case, the wave-number :math:`k \rightarrow 0` according to Eqs. :eq:`Helmholtz_A`.
For an electric dipole source :math:`\hat x I ds`, the DC electric field within a homogenous medium is given by:

.. math::
	\lim_{\omega \rightarrow 0} \mathbf{E}_e = \frac{I ds}{4 \pi \sigma  r^3} \left[ \left(\frac{3x^2}{r^2} - 1 \right) \hat{x} + \frac{3xy}{r^2} \hat{y} + \frac{3xz}{r^2} \hat{z} \right]
	:label: eq_Edip_Edc

According to Eq. :eq:`eq_Edip_Edc`, the DC electric field depends solely on the observation location and the conductivity of the medium.
The source and the electric field are also completely in-phase.
Similarly, the corresponding DC magnetic field within the medium is given by:

.. math::
	\lim_{\omega \rightarrow 0} \mathbf{H}_e = \frac{I ds}{4 \pi r^2} \left( -\frac{z}{r} \hat{y} + \frac{y}{r} \hat{z} \right)
	:label: eq_Edip_Hdc

According to Eq. :eq:`eq_Edip_Hdc`, the DC magnetic field is independent of any physical properties.
In addition, the DC electric and magnetic fields are in-phase with one another.


Near-Field Approximation
------------------------

For fields which are sufficiently close to the electric dipole source, we may assume that :math:`| kr | \ll 1`.
In this case, the exponential term in :math:`\mathbf{E}_e` and :math:`\mathbf{H}_e` can be approximated using Taylor expansion:

.. math::
	e^{-ikr} \approx 1 - ikr + O \left ( k^2 r^2 \right )
	:label: eq_exp_TaylorO2

The near-field approximation for :math:`\mathbf{E}_e` can be obtained by replacing the exponential term in Eq. :eq:`E_cartesian` with the Taylor series approximation from Eq. :eq:`eq_exp_TaylorO2`.
Thus:

.. math::
	\mathbf{E}_e \approx \frac{I ds}{4 \pi (\sigma + i \omega \varepsilon) r^3} \left ( 1 - ikr + O \left ( k^2 r^2 \right ) \right ) \left[ \left(\frac{x^2}{r^2} \hat{x} + \frac{xy}{r^2} \hat{y} + \frac{xz}{r^2} \hat{z} \right) \left(-k^2 r^2 + 3ikr +3 \right) + \left(k^2 r^2 - ikr -1 \right) \hat{x} \right]
	:label: eq_Edip_Enear1

To simplify Eq. :eq:`eq_Edip_Enear1`, we can simply neglect polynomial terms which are :math:`O(k^2 r^2)` or higher. 
Assuming we are in the quasi-static regime (:math:`i\omega\varepsilon \ll \sigma`), the electric field in close proximity to an electric dipole moment :math:`\hat x I ds` is given by:

.. math::
	\mathbf{E}_e \approx \frac{I ds}{4 \pi \sigma r^3} \left[ \left(\frac{3x^2}{r^2} - 1 \right) \hat{x} + \frac{3xy}{r^2} \hat{y} + \frac{3xz}{r^2} \hat{z} \right] + O(k^2 r^2 )
	:label: eq_Edip_Enear2

According to Eq. :eq:`eq_Edip_Enear2`, the near electric field depends only on the observation location and the conductivity of the medium.
Additionally, the source and the electric field are completely in-phase.

The near-field approximation for :math:`\mathbf{H}_e` can be obtained by replacing the exponential term in Eq. :eq:`H_cartesian` with the Taylor series approximation from Eq. :eq:`eq_exp_TaylorO2`.
Thus:

.. math::
	\mathbf{H}_e \approx \frac{I ds}{4 \pi r^2} \left( ikr + 1 \right) \left ( 1 - ikr + O \left ( k^2 r^2 \right ) \right ) \left( -\frac{z}{r} \hat{y} + \frac{y}{r} \hat{z} \right) 
	:label: eq_Edip_Hnear1

Eq. :eq:`eq_Edip_Hnear1` can be further simplified by neglecting polynomial terms which are :math:`O(k^2 r^2)` or higher. 
Therefore, the magnetic field in close proximity to electric dipole moment :math:`\hat x I ds` is approximately equal to:

.. math::
	\mathbf{H}_e \approx \frac{I ds}{4 \pi r^2} \left( -\frac{z}{r} \hat{y} + \frac{y}{r} \hat{z} \right) + O(k^2 r^2 )
	:label: eq_Edip_Hnear2

According to Eq. :eq:`eq_Edip_Hnear2`, :math:`\mathbf{H}_e` does not depend on the physical properties of the background medium.
Furthermore, Eq. :eq:`eq_Edip_Hnear2` indicates that :math:`\mathbf{E}_e` and :math:`\mathbf{H}_e` are in-phase.

Far-Field Approximation
-----------------------

For fields which are sufficient far away from the electric dipole source, we may assume that :math:`1 \ll | kr |`.
In this case, Taylor expansion may not be used to simplify the exponential term in Eqs. :eq:`E_Cartesian` and :eq:`H_Cartesian`.
Expressions may still be simplified, however, by considering the largest order terms in each equation. 

Let us first consider the far-field approximation of :math:`\mathbf{E}_e` within a uniform medium.
For off-axis locations (:math:`y,z \not \ll x`), only :math:`O (k^2r^2)` terms in Eq. :eq:`E_cartesian` are needed to accurately approximate the electric field from an electric dipole source.
However, in the case where (:math:`y,z \ll x`), second order terms in the :math:`\hat x` direction cancel, and both the :math:`\hat y` and :math:`\hat z` are insignificant due to geometry.
Assuming we are in the quasi-static regime (:math:`i\omega\varepsilon \ll \sigma`), and given that :math:`k^2 = \omega^2 \mu \varepsilon - i \omega \mu \sigma`, the far field approximation of :math:`\mathbf{E}_e` is represented by the following two cases:

.. math::
	\mathbf{E}_e \approx
	\begin{cases}
	\dfrac{i\omega \mu I ds}{4 \pi r} e^{-ikr} \Bigg [ \left ( \dfrac{x^2}{r^2} - 1 \right ) \hat x + \dfrac{xy}{r^2} \, \hat y + \dfrac{xz}{r^2} \, \hat z \Bigg ] \; \; &\textrm{for} \; \; y,z \not \ll x \\
	\; & \; \\
	\dfrac{ik Ids}{2\pi \sigma x^2} e^{-ikx} \hat x &\textrm{for} \; \; y,z \ll x
	\end{cases}

Let us now consider the far-field approximation of :math:`\mathbf{H}_e` within a uniform medium.
Since :math:`1 \ll | kr |`, Eq. :eq:`H_cartesian` can be used to show that:

.. math::
	\mathbf{H}_e \approx \frac{ik I ds}{4\pi r} e^{-ikr} \left ( -\frac{z}{r}\hat y + \frac{y}{r}\hat z \right )




