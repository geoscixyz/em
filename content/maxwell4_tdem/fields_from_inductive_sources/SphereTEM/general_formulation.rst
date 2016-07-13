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

where :math:`\chi (t)` is the inverse Fourier transform of the sphere's excitation factor :math:`\chi (i\omega )` (link).
Thus:

.. math::
	\chi (t) = \frac{1}{2 \pi} \int_{-\infty}^\infty \chi (i\omega) e^{i\omega t} d\omega
	:label: eqImpulseResponseDef
	
An explicit expression for :math:`\chi (i\omega)` may be found in Wait (1951):

.. math::
	\chi (i \omega ) = \frac{3}{2} \Bigg [ \frac{2\mu [tanh (\alpha) - \alpha] + \mu_0 [\alpha^2 tanh(\alpha) - \alpha + tanh(\alpha)]}{\mu [tanh(\alpha) - \alpha] - \mu_0 [\alpha^2 tanh(\alpha) - \alpha tanh(\alpha)]} \Bigg ]
	:label: eqExcitationFactorTEM
	
where:

.. math::
	\alpha = \Big [ i\omega \mu \sigma \Big ]^{1/2} R
	:label: eqAlphaDef






