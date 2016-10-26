.. _frequency_domain_magnetic_dipole_asymptotics:

Asymptotic Approximations
=========================

.. purpose::

    Here, simplified expressions for the electric and magnetic fields are presented for several cases.
    By examining simplified expressions, we can more easily see how the fields depend on certain parameters. 



DC-Field Approximation
----------------------

The DC electric and magnetic fields from a magnetic dipole source can be obtained from the full analytic solutions by taking the limit as :math:`\omega \rightarrow 0`.
In this case, the wave-number :math:`k \rightarrow 0`.
For a magnetic dipole source :math:`M \hat x`, the DC magnetic field within a homogenous medium is given by:

.. math::
	\lim_{\omega \rightarrow 0} \mathbf{H}_m = \frac{m}{4 \pi r^3} \left[ \left(\frac{3x^2}{r^2} - 1 \right) \hat{x} + \frac{3xy}{r^2} \hat{y} + \frac{3xz}{r^2} \hat{z} \right]
	:label: eq_Mdip_Hdc

According to Eq. :eq:`eq_Mdip_Hdc`, the DC magnetic field depends solely on the observation location and the dipole moment. It is independent of any physical properties of the medium.
The source and the magnetic field are also completely in-phase.
Similarly, the corresponding DC electric field within the medium is given by:

.. math::
	\lim_{\omega \rightarrow 0} \mathbf{E}_m = 0
	:label: eq_Mdip_Edc

According to Eq. :eq:`eq_Mdip_Edc`, the DC electric field is null.


Near-Field Approximation
------------------------

For fields which are sufficiently close to the electric dipole source, we may assume that :math:`| kr | \ll 1`.
In this case, the exponential term in :math:`\mathbf{E}_m` and :math:`\mathbf{H}_m` can be approximated using Taylor expansion:

.. math::
	e^{-ikr} \approx 1 - ikr + O \left ( k^2 r^2 \right )
	:label: eq_exp_TaylorO2

The near-field approximation for :math:`\mathbf{H}_m` can be obtained by replacing the exponential term in the full analytic solution with the Taylor series approximation from Eq. :eq:`eq_exp_TaylorO2`.
Thus:

.. math::
	\mathbf{H}_m \approx \frac{m}{4 \pi r^3} \left ( 1 - ikr + O \left ( k^2 r^2 \right ) \right ) \left[ \left(\frac{x^2}{r^2} \hat{x} + \frac{xy}{r^2} \hat{y} + \frac{xz}{r^2} \hat{z} \right) \left(-k^2 r^2 + 3ikr +3 \right) + \left(k^2 r^2 - ikr -1 \right) \hat{x} \right]
	:label: eq_Mdip_Hnear1

Eq. :eq:`eq_Mdip_Hnear1` can be simplified by neglecting polynomial terms which are :math:`O(k^2 r^2)` or higher.

.. math::
	\mathbf{H}_m \approx \frac{m}{4 \pi r^3} \left[ \left(\frac{3x^2}{r^2} - 1 \right) \hat{x} + \frac{3xy}{r^2} \hat{y} + \frac{3xz}{r^2} \hat{z} \right] + O(k^2 r^2 )
	:label: eq_Mdip_Hnear2

According to Eq. :eq:`eq_Mdip_Hnear2`, the near magnetic field depends only on the observation location and the magnetic dipole moment.
Additionally, the source and the magnetic field are completely in-phase.

The near-field approximation for :math:`\mathbf{E}_m` can be obtained by replacing the exponential term in the full analytic solution with the Taylor series approximation from Eq. :eq:`eq_exp_TaylorO2`.
Thus:

.. math::
	\mathbf{E}_m \approx \frac{i \omega \mu m}{4 \pi r^2} \left( ikr + 1 \right ) \left ( 1 - ikr + O \left ( k^2 r^2 \right ) \right ) \left( -\frac{z}{r} \hat{y} + \frac{y}{r} \hat{z} \right)
	:label: eq_Mdip_Enear1

Eq. :eq:`eq_Mdip_Enear1` can be further simplified by neglecting polynomial terms which are :math:`O(k^2 r^2)` or higher.
Therefore, the electric field in close proximity to magnetic dipole moment :math:`\hat x I S` is approximately equal to:

.. math::
	\mathbf{E}_m \approx \frac{i \omega \mu m}{4 \pi r^2} \left( -\frac{z}{r} \hat{y} + \frac{y}{r} \hat{z} \right) + O(k^2 r^2 )
	:label: eq_Mdip_Enear2

According to Eq. :eq:`eq_Mdip_Enear2`, :math:`\mathbf{E}_m` does depend on the physical properties of the background medium.
Furthermore, Eq. :eq:`eq_Mdip_Enear2` indicates that :math:`\mathbf{E}_m` and :math:`\mathbf{H}_m` are out-of-phase.

Far-Field Approximation
-----------------------

For fields which are sufficient far away from the electric dipole source, we may assume that :math:`1 \ll | kr |`.
In this case, Taylor expansion may not be used to simplify exponential terms in full analytic solutions for the fields.
Expressions may still be simplified, however, by considering the largest order terms in each equation.

Let us first consider the far-field approximation of :math:`\mathbf{H}_m` within a uniform medium.
For off-axis locations (:math:`y,z \not \ll x`), only :math:`O (k^2r^2)` terms are needed to accurately approximate the electric field from an electric dipole source.
However, in the case where (:math:`y,z \ll x`), second order terms in the :math:`\hat x` direction cancel, and both the :math:`\hat y` and :math:`\hat z` are insignificant due to geometry.
Assuming we are in the quasi-static regime :math:`k^2 = - i \omega \mu \sigma`, the far field approximation of :math:`\mathbf{H}_m` is represented by the following two cases:

.. math::
	\mathbf{H}_m \approx
	\begin{cases}
	\dfrac{i \omega \mu \ sigma m}{4 \pi r} e^{-ikr} \Bigg [ \left ( \dfrac{x^2}{r^2} - 1 \right ) \hat x + \dfrac{xy}{r^2} \, \hat y + \dfrac{xz}{r^2} \, \hat z \Bigg ] \; \; &\textrm{for} \; \; y,z \not \ll x \\
	\; & \; \\
	\dfrac{ik m}{2 \pi x^2} e^{-ikx} \hat x &\textrm{for} \; \; y,z \ll x
	\end{cases}

Let us now consider the far-field approximation of :math:`\mathbf{E}_m` within a uniform medium.
Since :math:`1 \ll | kr |`, we can simplify the full analytic expression in the same manner and show that:

.. math::
	\mathbf{H}_e \approx \frac{-k \omega \mu m}{4\pi r} e^{-ikr} \left ( -\frac{z}{r}\hat y + \frac{y}{r}\hat z \right )




