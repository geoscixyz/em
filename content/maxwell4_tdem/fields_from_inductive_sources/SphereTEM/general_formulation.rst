.. _SphereTEM_general_formulation:

General Formulation
-------------------

**Purpose**:  Here, we present analytic expressions according to Wait and Spies (1969).
These expressions can be used to predict the time-dependent dipole response from a conductive and magnetically permeable sphere in free-space. 
 
.. figure:: ./images/figSphereTEMfreespace.png
	:align: right
        :scale: 35%
        :name: SphereTEMfreespace2

        

**Problem Geometry**: Consider the illustration in Figure :numref:`SphereTEMfreespace2`.
Here, a sphere of radius :math:`R`, conductivity :math:`\sigma` and magnetic permeability :math:`\mu` is located in the vicinity of an inductive source transmitter :math:`Tx`.
The transmitter generates a time-dependent primary field :math:`h_0 (t)` which induces an excitation within the sphere.
The excitation induced within the sphere produces a secondary field which is then measured by a receiver coil :math:`Rx`.
Note that because we are in free-space, :math:`h_0 (t)` may be calculated using the Biot-Savart law.

**Dipole Response**: To approximate the sphere’s response, Wait and Spies (1969) considered the dipole response from a conductive and magnetically permeable sphere under the influence of a spatially uniform field (Fig. ()).
The geometry of this problem is illustrated in :numref:`SphereTEMfreespace2`.
For an inductive source, the inducing field may be considered spatially uniform about the sphere if 1) the radius of the sphere is much smaller than the wavelength of the inducing field, and 2) the distance between the transmitter and the sphere is sufficiently larger than the sphere's radius (typically :math:`> 10R`).
According to Wait and Spies (1969), the sphere's free-space dipole response :math:`{\bf h} (t)` can be expressed in terms of a time-dependent dipole moment :math:`{\bf m}(t)` such that:

.. figure:: ./images/figSphereTEMgeometry.png
	:align: right
        :scale: 35%
        :name: SphereTEMgeometry

.. math::
	{\bf h} (t) = \frac{1}{4\pi} \Bigg [\frac{3{\bf r} [ \, {\bf m}(t) \cdot {\bf r}\, ]}{r^5} - \frac{{\bf m}(t)}{r^3} \Bigg ]
	:label: eqDipoleResponseGen

where :math:`{\bf r}` is the vector distance between :math:`{\bf P}` and :math:`{\bf Q}`.
The induced magnetic dipole moment characterizing the sphere's excitation is given by the following convolution:

.. math::
	{\bf m}(t) = \frac{4\pi}{3}R^3 \chi (t) \otimes {\bf h_0} (t)
	:label: eqDipoleMomentGenDef

where :math:`\chi (t)` represents an impulse response for the sphere's induced dipole moment.
Here, the impulse response is defined as the inversion Fourier transform of the sphere's frequency-dependent excitation factor :math:`\chi (i \omega)` (link).
An explicit expression for :math:`\chi (t)` can be obtained from Becker??:

.. math::
	\chi (t) = - \frac{3}{2} \delta (t) + \frac{3}{2} \Bigg ( \frac{6 \mu_r}{\beta^2} \sum_{n=1}^\infty \frac{\xi_n^2 e^{-\xi_n^2 \, t/\beta^2}}{(\mu_r + 2)(\mu_r - 1) + \xi_n^2} \Bigg ) u(t)
	:label: eqImpulseResponseGenDef

where :math:`u(t)` is the unit-step function, :math:`\delta (t)` is the Dirac delta function, :math:`\mu_r = \mu/\mu_0` is the relative permeability of the sphere and:

.. math::
	\beta = \big ( \mu_0 \sigma \big )^{1/2} R
	:label: eqBetaGenDef
	
Coefficients :math:`\xi_n` within the sum are defined by:

.. math::
	\textrm{tan} \, \xi_n = \frac{(\mu_r - 1)\xi_n}{\mu_r - 1 + \xi_n^2}

From Wait and Spies (1969), coefficients :math:`\xi_n` are spaced roughly :math:`\pi` apart with:

.. math::
	n\pi \leq \xi_n \leq (n+1/2) \pi
	
	
The value of each coefficient may be found iteratively using very few iterations (< 10) according to:

.. math::
	\xi_n^{(k+1)} = n\pi + \textrm{tan}^{-1}\Bigg ( \frac{(\mu_r - 1) \xi_n^{(k)}}{\mu_r - 1 + (\xi_n^{(k)} )^2} \Bigg )



