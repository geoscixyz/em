.. _sphere_freespace_FEM:

Response from a Conducting and Permeable Sphere in Free-Space
-------------------------------------------------------------

.. Introduction
.. ============

.. Frequency-domain responses from ore bodies and unexploded ordnance items are of great practical importance to geophysicists.
.. On a fundamental level, these responses can be understood by considering the excitation of a conductive and magnetically permeable sphere, under the influence of a harmonic inducing field.
.. Here, expressions derived by Wait (1951) are used to characterize the excitation of the sphere in terms of an induced dipole moment.
.. We examine how a target's dipole moment depends on its size and physical properties.
.. A simple model for predicing the sphere's dipole response in free-space is then presented.
.. For a sufficiently compact target, the free-space response represents a low-order approximation to the response of a conductive and permeable object within a resistive medium.


.. Plane Wave Excitation of a Conducting and Magnetically Permeable Sphere
.. =======================================================================

.. In this section, equations derived by Wait (1951) are used to describe the induced magnetic dipole moment of a conductive and permeable sphere, resulting from excitation by a uniform magnetic field (Figure ??).
.. According to Ward and Hohmann (1989), the frequency-domain wave equation within a homogeneous media can be expressed in terms of the magnetic Schelkunoff potential :math:`\vec F`:

.. .. figure:: ./images/figGeometrySphere.png
.. 	:align: right
..         :scale: 45%
..         :name: GeometrySphere

.. .. math::
.. 	\nabla^2 \vec F - \gamma^2 \vec F = 0
.. 	:label: Schelkunoff_Wave

.. For a propagation media with conductivity :math:`\sigma`, magnetic permeability :math:`\mu` and electric permittivity :math:`\varepsilon`, the wavenumber :math:`\gamma` can be expressed as follows:

.. .. math::
.. 	\gamma = \Big [ i \omega \mu \sigma - \omega^2 \mu \varepsilon \Big ]^{1/2}
.. 	:label: Wave_Number

.. By definition of the Schelkunoff potential, the electric field :math:`\vec E` may be obtained by substituting :math:`\vec F` into the following expression:

.. .. math::
.. 	\vec E = - \nabla \times \vec F
.. 	:label: EcurlF

.. And for the magnetic field :math:`\vec H`:

.. .. math::
.. 	\vec H = - \big (\sigma + i \omega \varepsilon \big ) \vec F + \frac{1}{i \omega \mu} \nabla \big ( \nabla  \cdot \vec F \big )
.. 	:label: SchelkunoffH

.. For his derivation, Wait (1951) began by considering the induced magnetic dipole moment resulting from an incident plane wave.
.. If the wavelength of the incident wave is sufficiently larger than the radius of the sphere (i.e. :math:`|\gamma_b |/2\pi \ll R`), then we may assume the magnetic field which induces the dipole moment is approximately uniform about the sphere.
.. For an inducing field of the form :math:`\vec H_0 (i\omega) = H_0 e^{i\omega t} \hat z`, symmetry of the problem implies that :math:`\vec E` only has components in :math:`\hat \phi`.
.. Therefore by Eq. :eq:`EcurlF`, it follows that our Schelkunoff potential will only have components in :math:`\hat z`.
.. The Schulkunoff potential may be obtained by considering seperate solutions inside and outside of the sphere:

.. .. math::
.. 	\vec F (\omega) = \begin{cases}
.. 	F_b e^{i \omega t} \hat z \; \; \textrm{  at  } \; \; r>R \\
.. 	\\
.. 	F_s e^{i \omega t} \hat z \; \; \textrm{  at  } \; \; r<R
.. 	\end{cases}
.. 	:label: SolnsInsideOutside


.. For our problem, boundary conditions on the sphere require that tanjential components of the magnetic field and normal components of the flux density must be continuous.
.. According to Wait (1951), these conditions are satisfied by the following:

.. .. math::
.. 	\textrm{At }r=R: \; \begin{cases}
.. 	\dfrac{1}{r} \dfrac{\partial F_b}{\partial r} - \gamma_b^2 F_b = \dfrac{1}{r} \dfrac{\partial F_s}{\partial r} - \gamma_s^2 F_s \\
.. 	  \\
.. 	\mu_b \Bigg ( \dfrac{\partial^2 F_b}{\partial r^2} - \gamma_b^2 F_b \Bigg ) = \mu_s \Bigg ( \dfrac{\partial^2 F_s}{\partial r^2} - \gamma_s^2 F_s \Bigg )
.. 	\end{cases}
.. 	:label: BoundaryConditions

.. To solve the boundary value problem, Wait (1951) expressed the Schelkunoff potentials, both inside and outside of the sphere, as a sum of spherical harmonic modes with coefficients :math:`a_n` and :math:`b_n`, respectively.
.. For the boundary conditions to be satisfied however, he found that coefficients :math:`a_n=b_n=0 \; \forall \; n>0`.
.. As a result, the solution to the Schelkunoff potentials inside and outside the sphere are defined by:

.. .. math::
.. 	F_b = - \frac{H_0 }{\sigma_b + i \omega \varepsilon_b} + i \omega \mu_b  \frac{e^{-\gamma_b r}}{r}a_0 H_0
.. 	:label: Foutside

.. and

.. .. math::
.. 	F_s = i \omega \mu_s \frac{sinh \big ( \gamma_s r \big )}{r} b_0 H_0
.. 	:label: Finside

.. To determine the solution outside of the sphere, Eqs. :eq:`Foutside` and :eq:`Finside` may be substituted into Eq. :eq:`BoundaryConditions`.
.. Through meticulous algebra, coefficient :math:`a_0` can be expressed as:

.. .. math::
.. 	a_0 \! =\! \frac{R^3}{2 e^{-\alpha_b}} \!\Bigg [ \! \frac{2\mu_s \big [ tanh(\alpha_s) - \alpha_s  \big ] + \mu_b \big [\alpha_s^2 \, tanh(\alpha_s) - \alpha_s + tanh(\alpha_s) \big ] }{\mu_s \big ( \alpha_b^2 +\alpha_b + 1 \big ) \big [ tanh(\alpha_s) - \alpha_s \big ] - \mu_b \big ( \alpha_b + 1 \big ) \big [ \alpha_s^2 \, tanh(\alpha_s) - \alpha_s + tanh(\alpha_s) \big ] } \! \Bigg ]
.. 	:label: a0

.. where

.. .. math::
.. 	\alpha_b = \gamma_b R = \Big [ i \omega \mu_b \sigma_b - \omega^2 \mu_b \varepsilon_b \Big ]^{1/2} R
.. 	:label: alpha_b

.. and

.. .. math::
.. 	\alpha_s = \gamma_s R = \Big [ i \omega \mu_s \sigma_s - \omega^2 \mu_s \varepsilon_s \Big ]^{1/2} R
.. 	:label: alpha_s

.. The total magnetic field outside the sphere, in response to an inducing field of the form :math:`\vec H_0 e^{i\omega t}`, may be obtained by substituting Eqs. :eq:`Foutside` and :eq:`a0` into Eq. :eq:`SchelkunoffH`.
.. Note that our derivation of :math:`a_0` did not require us to include the frequency-dependent term :math:`e^{i\omega t}` of the primary field.
.. Therefore, we may generalize our solution for any inducing field of the form :math:`\vec H_0 (i\omega )`.
.. For practical purposes, it is common to examine the dipole response of the sphere.
.. In this case, the dipole response :math:`\vec B (\omega)` at location :math:`Q` is:

.. .. math::
.. 	\vec B (\omega) =\frac{\mu_0}{4\pi} \Bigg [ \frac{3\vec r \; \big [ \vec m(\omega) \cdot \vec r \; \big ]}{r^5} - \frac{\vec m (\omega) }{r^3} \Bigg ]
.. 	:label: DipoleField

.. where :math:`\mu_0` is the permeability of free-space, :math:`\vec r` defines the spatial vector from :math:`P` to :math:`Q`, and :math:`\vec m (\omega)` is the frequency-dependent dipole moment induced by the primary field.
.. The dipole moment can be expressed as the product of the sphere's volume, the inducing field, and a magnetization factor :math:`\chi (\omega)`:

.. .. math::
.. 	\vec m (\omega) = 4 \pi a_0 \vec H_0 (i \omega) = \frac{4\pi}{3}R^3 \chi (\omega) \vec H_0 (i \omega)
.. 	:label: DipoleMoment

.. where

.. .. math::
.. 	\chi (\omega) \! =\! \frac{3}{2 e^{-\alpha_b}} \!\Bigg [ \! \frac{2\mu_s \big [ tanh(\alpha_s) - \alpha_s  \big ] + \mu_b \big [\alpha_s^2 \, tanh(\alpha_s) - \alpha_s + tanh(\alpha_s) \big ] }{\mu_s \big ( \alpha_b^2 +\alpha_b + 1 \big ) \big [ tanh(\alpha_s) - \alpha_s \big ] - \mu_b \big ( \alpha_b + 1 \big ) \big [ \alpha_s^2 \, tanh(\alpha_s) - \alpha_s + tanh(\alpha_s) \big ] } \! \Bigg ]
.. 	:label: ChiFull

.. If the sphere is located within a resistive medium, then :math:`\alpha_b \ll \alpha_s`, :math:`\mu_b = \mu_0`, and Eq. :eq:`ChiFull` will reduce to:

.. .. math::
.. 	\chi (\omega) = \frac{3}{2} \Bigg [ \! \frac{2\mu_s \big [ tanh(\alpha_s) - \alpha_s  \big ] + \mu_0 \big [\alpha_s^2 \, tanh(\alpha_s) - \alpha_s + tanh(\alpha_s) \big ] }{\mu_s  \big [ tanh(\alpha_s) - \alpha_s \big ] - \mu_0 [ \alpha_s^2 \, tanh(\alpha_s) - \alpha_s + tanh(\alpha_s) \big ] } \! \Bigg ]
.. 	:label: ChiApprox


.. .. figure::
.. 	./images/figChiOmega.png
.. 	:figwidth: 40%
.. 	:align: right

.. 	Magnetization factor for a sphere in free-space with :math:`\sigma_s` = 10 S/m, :math:`\mu_s` = 1.1 :math:`\mu_0` , :math:`\varepsilon_s` = :math:`\varepsilon_0`, and :math:`R` = 25 m.

.. .. figure::
.. 	./images/figChiKappa.png
.. 	:figwidth: 40%
.. 	:align: right

.. 	Magnetization facter at :math:`\omega` = 0 for increasing magnetic susceptibilities (red), compared to a linear trend with respect to :math:`\kappa` (black).

.. The magnetization factor for a sphere in free space, with :math:`\sigma_s` = 10 S/m, :math:`\mu_s` = 1.1 :math:`\mu_0` , :math:`\varepsilon_s` = :math:`\varepsilon_0` and :math:`R` = 25 m, can be seen in Figure (reference).
.. Near the resistive limit, :math:`\chi (\omega)` is positive, implying that excitation of the sphere is parallel to the inducing field.
.. Because the EM induction is negligible at sufficiently low frequencies, this case represents a purely magnetic response by the sphere.
.. Near the inductive limit, :math:`\chi(\omega)` is negative.
.. Therefore, inductive excitation of the sphere will oppose the inducing field.
.. For a conductive and permeable sphere in free-space, Eq. :eq:`ChiApprox` can be used to show that:

.. .. math::
.. 	\chi (\omega) = \begin{cases}
.. 	\dfrac{3 \big ( \mu_s - \mu_0 \big )}{ \big ( \mu_s + 2 \mu_0 \big ) } = \dfrac{3 \kappa }{3 + \kappa} & \textrm{ as } \omega \rightarrow 0 \\
.. 	\\
.. 	\dfrac{3}{2}  & \textrm{ as } \omega \rightarrow \infty
.. 	\end{cases}
.. 	:label: ChiLimits

.. where :math:`\kappa` is the magnetic susceptibility of the sphere, and :math:`\mu_s =\mu_0 \big [ 1 + \kappa \big ]`.
.. According to Eq. :eq:`ChiLimits`, the inductive limit of :math:`\chi (\omega)` is constant.
.. As a result, the dipole moment which characterizes the sphere in this case is proportional only to :math:`R^3`, and the strength of the inducing field.
.. For purely magnetic responses however, the magnetization factor ultimately depends on the magnetic susceptibility of the sphere.
.. For small magnetic susceptibilities (:math:`\kappa < 0.1`), the relationship between :math:`\kappa` and the resulting dipole moment is approximately linear.
.. For large values however, the effects of self-demagnetization within the sphere will result in a weaker magnetic dipole moment for the sphere.
.. As :math:`\kappa \rightarrow \infty`, Eq. :eq:`ChiLimits` can be used to show that :math:`\chi \rightarrow 3`.
.. The magnetization factor for :math:`\omega = 0`, denoted here as :math:`\chi (\kappa)`, is plotted in Figure (reference).

.. For a purely conductive object (i.e. :math:`\mu_s = \mu_0`), Eq. :eq:`ChiApprox` can be further simplified.
.. By neglecting electric displacement (i.e. :math:`\omega \varepsilon_s \ll \sigma_s`):

.. .. math::
.. 	\chi (\omega) = - \; \frac{3}{2} \Bigg [ 1 + \frac{3}{\alpha^2} - \frac{3 \, \textrm{coth}(\alpha)}{\alpha} \Bigg ]
.. 	:label: ChiConductive

.. where

.. .. math::
.. 	\alpha = \Big [ i \omega \mu_0 \sigma_s \Big ]^{1/2} R
.. 	:label: alpha_c

.. Eq. :eq:`ChiConductive` is commonly used to understand the excitation of a compact conductive object in a resistive medium.



.. Dipole Response in Free-Space
.. =============================

.. Here, we present a model for predicting the anomalous frequency-domain response in free-space, from a conductive and permeable sphere, due to an inductive loop source.
.. This scenario represents a low-order approximation for a conductive and magnetically permeable object within a resistive medium.
.. The geometry of this problem is shown in Figure ??.

.. .. figure::
.. 	./images/figResponseVacuum.png
..         :align: center
.. 	:figwidth: 50%

.. In the previous section, analytic expressions were derived by considering a uniform inducing field about the sphere.
.. However, if the radius of the sphere is sufficiently smaller than its distance from an inductive source, this condition will hold approximately for small enough frequencies.
.. According to Ward and Hohmann (1988?), a distance larger than 5 times the average dimension of the object is required for a dipole source.
.. If the frequency-dependent dipole moment of a conductive and permeable sphere is known, the resulting free-space dipole field may be calculated using Eq. :eq:`DipoleField`, where :math:`\vec m (\omega)` is given by Eq. :eq:`DipoleMoment`.
.. By decomposing the problem into separable cartesian components, Eq. :eq:`DipoleField` can be re-expressed as:

.. .. math::
.. 	{\bf B}(\omega) = \frac{\mu_0}{4 \pi r^3} \Big [ 3 {\bf \hat r \otimes \hat r - I} \Big ] \cdot {\bf m} (\omega) = {\bf G} \, {\bf m} (\omega)
.. 	:label: DipoleVacuumLin

.. where

.. .. math::
.. 	{\bf B} (\omega) = \begin{bmatrix} B_x (\omega) \\ B_y(\omega) \\ B_z(\omega) \end{bmatrix}, \; \;
.. 	{\bf m}(\omega) = \begin{bmatrix} m_x (\omega) \\ m_y(\omega) \\ m_z(\omega) \end{bmatrix} \; \; \textrm{and} \; \;
.. 	{\bf I} = \begin{bmatrix} 1&0&0\\0&1&0\\0&0&1 \end{bmatrix}
.. 	:label: DipoleOperator

.. The vector from :math:`P` to :math:`Q` is denoted by :math:`\vec r`, and has unit-direction :math:`{\bf \hat r}`.
.. For our formulation, we use :math:`{\bf \hat r \otimes \hat r}` to represent an outer-product.
.. We can see from Eq. :eq:`DipoleVacuumLin` that :math:`{\bf G}` is a :math:`3\times 3` linear operator, which depends solely on the geometry of the problem.
.. Because the magnetization factor for our sphere is a scalar quantity, it may be used to obtain each cartesian component of the induced dipole moment separately.
.. As a result, we may express :math:`{\bf m} (\omega)` as follows:

.. .. math::
.. 	{\bf m} (\omega) = {\bf M \, H_0}
.. 	:label: mDecomposition

.. where

.. .. math::
.. 	{\bf M} = \Bigg ( \frac{4}{3} \pi R^3 \chi (\omega ) \Bigg ) {\bf I} \; \; \textrm{and} \; \;
.. 	{\bf H_0} = \begin{bmatrix} H_x(\omega) \\ H_y (\omega) \\ H_z (\omega) \end{bmatrix}
.. 	:label: Magnetization

.. By substituting Eq. :eq:`mDecomposition` into Eq. :eq:`DipoleVacuumLin`, the free-space dipole response can be expressed as:

.. .. math::
.. 	{\bf B}(\omega) = {\bf G \, M \, H_0}
.. 	:label: DipoleVacuumLinSys
















..
