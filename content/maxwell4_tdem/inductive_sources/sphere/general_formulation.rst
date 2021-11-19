.. _SphereTEM_general_formulation:

General Formulation
===================

.. Purpose::

	Here, we present analytic expressions according to Wait and Spies (:cite:`WaitSpies1969`).
	These expressions can be used to predict the time-dependent dipole response from a conductive and magnetically permeable sphere in free-space. 
 

.. sidebar:: Problem Geometry

    .. figure:: ./images/figSphereTEMfreespaceb.png
        :align: right
        :figwidth: 100%
        :name: SphereTEMfreespace2

        Problem geometry for a conductive and magnetically permeable sphere in free-space.

    .. figure:: ./images/figSphereTEMgeometry.png
        :align: right
        :figwidth: 100%
        :name: SphereTEMgeometry
    
    	Dipolar response :math:`\mathbf{h} (t)` (purple) from a conductive and magnetically permeable sphere, under the influence of a spatially uniform field :math:`h_0 (t)` (red). The induced dipole moment (blue) is represented by :math:`\mathbf{m} (t)`.


Consider the illustration in :numref:`SphereTEMfreespace2`.
Here, a sphere of radius :math:`R`, conductivity :math:`\sigma` and magnetic permeability :math:`\mu` is located in the vicinity of an inductive source transmitter (:math:`Tx`).
The transmitter generates a time-dependent primary field :math:`\mathbf{h_0} (t)` which induces an excitation within the sphere.
The excitation induced within the sphere produces a secondary field :math:`\mathbf{h_s} (t)` which is then measured by a receiver coil (:math:`Rx`).
Note that because we are in free-space, :math:`\mathbf{h_0} (t)` may be calculated using the :ref:`Biot-Savart law<biot_savart>`.

To approximate the sphere's response, Wait and Spies (:cite:`WaitSpies1969`) considered the dipole response from a conductive and magnetically permeable sphere under the influence of a spatially uniform field.
The geometry of this problem is illustrated in :numref:`SphereTEMfreespace2`.
The transmitter's primary field may be considered spatially uniform about the sphere if 1) the radius of the sphere is much smaller than the wavelength of the inducing field, and 2) the distance between the transmitter and the sphere is sufficiently larger than the sphere's radius (typically :math:`> 10R`).
According to Wait and Spies (:cite:`WaitSpies1969`), the sphere's free-space dipole response :math:`{\bf h} (t)` can be expressed in terms of a time-dependent dipole moment :math:`{\bf m}(t)` such that:

.. math::
	{\bf h} (t) = \frac{1}{4\pi} \Bigg [\frac{3{\bf r} [ \, {\bf m}(t) \cdot {\bf r}\, ]}{r^5} - \frac{{\bf m}(t)}{r^3} \Bigg ]
	:label: eqDipoleResponseGen

where :math:`{\bf r}` is the vector distance between :math:`{\bf P}` and :math:`{\bf Q}`.
The induced magnetic dipole moment for the sphere's excitation is given by the following convolution:

.. math::
	{\bf m}(t) = \frac{4\pi}{3}R^3 \chi (t) \otimes {\bf h_0} (t)
	:label: eqDipoleMomentGenDef

where :math:`\chi (t)` represents an impulse response for the sphere's induced dipole moment.
The impulse response is defined as the inverse Fourier transform of the sphere's frequency-dependent :ref:`excitation factor<sphereFEM_excitation_factor>` :math:`\chi (i \omega)`.
An explicit expression for :math:`\chi (t)` can be obtained from Wait and Spies (:cite:`WaitSpies1969`):

.. math::
	\chi (t) = - \frac{3}{2} \delta (t) + \frac{3}{2} \Bigg ( \frac{6 \mu_r}{\beta^2} \sum_{n=1}^\infty \frac{\xi_n^2 e^{-\xi_n^2 \, t/\beta^2}}{(\mu_r + 2)(\mu_r - 1) + \xi_n^2} \Bigg ) u(t)
	:label: eqImpulseResponseGenDef

where :math:`u(t)` is the unit-step function, :math:`\delta (t)` is the Dirac delta function, :math:`\mu_r = \mu/\mu_0` is the relative permeability of the sphere and:

.. math::
	\beta = \big ( \mu \sigma \big )^{1/2} R
	:label: eqBetaGenDef
	
Coefficients :math:`\xi_n` within the sum are defined by:

.. math::
	\textrm{tan} \, \xi_n = \frac{(\mu_r - 1)\xi_n}{\mu_r - 1 + \xi_n^2}
	:label: eqCoefLaw

These coefficients are spaced roughly :math:`\pi` apart with:

.. math::
	n\pi \leq \xi_n \leq (n+1/2) \pi
	:label: eqCoefSeparation
	
In practice, the value of each coefficient may be found iteratively using very few iterations (< 10) according to:

.. math::
	\xi_n^{(k+1)} = n\pi + \textrm{tan}^{-1}\Bigg ( \frac{(\mu_r - 1) \xi_n^{(k)}}{\mu_r - 1 + (\xi_n^{(k)} )^2} \Bigg )
        :label: eqCoefIteration


Therefore, we can predict the sphere's dipole response by performing the following operations.
First, the impulse response defined in Eq. :eq:`eqImpulseResponseGenDef` is determined for a particular sphere.
Although it is expressed as an infinite sum, only a finite number of terms are needed; as the contribution of each term decays with respect to :math:`n`.
The :math:`\xi_n` coefficients used to approximate the sum are determined individually using Eq. :eq:`eqCoefIteration`, with an initial value according to :eq:`eqCoefSeparation`.
For a particular inducing field :math:`h_0(t)`, the convolution in Eq. :eq:`eqDipoleMomentGenDef` is evaluated numerically for a set of times.
After a numerical approximation for the magnetic dipole moment is obtained, the time-dependent response at a particular location is predicted according to Eq. :eq:`eqDipoleResponseGen`.

.. figure:: ./images/figMagnetizationTEMexample.png
    :align: right
    :figwidth: 40%
    :name: SphereTEMexample

    Transient dipole moment at :math:`t>0` for a sphere of radius :math:`R` = 10 m, conductivity :math:`\sigma` = 10 S/m and relative permeability :math:`\mu_r` = 6. 

As an example, let us consider a sphere of radius :math:`R=10` m, conductivity :math:`\sigma = 10` S/m and relative permeability :math:`\mu_r=6`.
The sphere has been subjected to a static inducing field with magnitude :math:`h_0=1` A/m since :math:`t = -\infty`.
At :math:`t=0` s, the field is removed; which induces a time-dependent excitation within the sphere.
This particular excitation defines the sphere's transient or "step-off" response.
The magnetic dipole moment which characterizes the sphere at :math:`t>0` is shown in :numref:`SphereTEMexample`.

The sphere's step-off response depends on the dimensions and physical properties of the sphere.
These dependencies are discussed in the :ref:`following section<SphereTEM_transient_response>` for permeable and non-permeable spheres.


