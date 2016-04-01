.. _dipole_response

Dipole Response in Free-Space
-----------------------------

Here, expressions from Wait (1951) are used to characterize the dipole response from a conductive and magnetically permeable sphere in free-space.

.. figure:: ./images/figFreeSpaceSphere.png
        :align: right
        :figwidth: 40%
        :name: FreeSpaceSphere

        Problem geometry for a conductive and magnetically permeable sphere in free-space.

Consider the problem geometry illustrated in Figure (??), wherein a sphere of radius :math:`R`, conductivity :math:`\sigma`, magnetic permeability :math:`\mu` and electric permittivity :math:`\varepsilon` is located in the vicinity of an inductive source transmitter (Tx).
The transmitter generates a harmonic primary field :math:`{\bf H_0} (i\omega)`, which induces an excitation within the sphere.
Because we are in free-space, :math:`{\bf H_0} (i\omega)` may be calculated using the Biot-Savart law (link).
The excitation induced within the sphere, produces a secondary field :math:`{\bf H_s} (i\omega)` which is then measured by a receiver coil (Rx).


.. figure:: ./images/figDipoleField.png
        :align: right
        :figwidth: 40%
        :name: DipoleField
        
        Response from a conductive and magnetically permeable sphere, under the influence of a uniform, harmonic inducing field :math:`{\bf H_0} (i\omega)`. The induced dipole moment is represented by :math:`{\bf m} (i\omega)` and the resulting dipole response is represented by :math:`{\bf H} (i\omega)`.

Wait (1951) considered the dipole response from a conductive and magnetically permeable sphere, under the influence of a uniform, harmonic field (Figure ??).
For a magnetic dipole moment :math:`{\bf m} (i\omega)`, the dipole field :math:`{\bf H} (i\omega)` is given by:

.. math::
	{\bf H} (i \omega) =\frac{1}{4\pi} \Bigg [ \frac{3 {\bf r} \; \big [ {\bf m}(i \omega) \cdot {\bf r} \; \big ]}{r^5} - \frac{{\bf m} (i \omega) }{r^3} \Bigg ] 

where :math:`{\bf r}` is the vector distance between :math:`P` and :math:`Q`.
For practical problems, the inducing field may be considered approximately uniform about the sphere if 1) the radius of the sphere is much smaller than the wavelength of the inducing field , and 2) the distance between the transmitter and the sphere is sufficiently larger than the sphere's radius (typically :math:`> 10R` ).
If these conditions are satisfied, the magnetic dipole moment characterizing the sphere's excitation is given by:

.. math::
	{\bf m} (i \omega) = \frac{4\pi}{3}R^3 \chi (i \omega) \, {\bf H_0} (i \omega)

where :math:`\chi (i\omega)` is defined as the sphere's excitation factor.
The nature of the sphere's frequency-domain response is represented by the excitation factor.
An explicit expression for the excitation factor is given by (Wait, 1951):

.. math::
	\chi (i \omega) = \frac{3}{2} \Bigg [ \! \frac{2\mu \big [ tanh(\alpha) - \alpha  \big ] + \mu_0 \big [\alpha^2 \, tanh(\alpha) - \alpha + tanh(\alpha) \big ] }{\mu  \big [ tanh(\alpha) - \alpha \big ] - \mu_0 [ \alpha^2 \, tanh(\alpha) - \alpha + tanh(\alpha) \big ] } \! \Bigg ]

where

.. figure:: ./images/figChiOmega.png
        :align: right
        :figwidth: 40%
        :name: ExcitationEx

.. math::
	\alpha = \Big [ i \omega \mu \sigma - \omega^2 \mu \varepsilon \Big ]^{1/2} R,

:math:`\mu_0 = 4\pi \times 10^{-7}` H/m is the permeability of free-space, and :math:`\varepsilon`.
The excitation factor for a sphere with physical properties :math:`R`, :math:`\sigma`, :math:`\mu` and :math:`\varepsilon` is shown in Figure ??.























