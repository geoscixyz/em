.. _magnetic_permeability_definition:

What are Magnetic Permeability and Magnetic Susceptibility?
===========================================================


Magnetism is attributed to the movement of electrical charges.
Within a material, the motion and spin of individual electrons is responsible for generating a collection of magnetic moments :math:`\{\vec m_i \}`.
The total magnetic moment for the material :math:`\vec m`, is equal to the vector sum of all electron magnetic moments:

.. math::
	\vec m = \sum_i \vec m_i
	:label: Sum_Dipoles
	
Magnetization :math:`\vec M` is defined as the magnetic moment per unit volume:

.. math::
	\vec M = \frac{d \vec m}{d V}
	:label: Mag_Definition

The majority of rocks are paramagnetic.
In the absence of a magnetic field, magnetic moments within paramagnetic rocks are frequently disordered.
In this case, individual magnetic moments cancel out one another, resulting in a net magnetization of zero.
When exposed to a magnetic field, the magnetic moments within paramagnetic rocks experience a torque.
This torque attempts to align individual magnetic moments along the direction of the field.
As a result, the rock experiences a net magnetization parallel to the applied field.
This process is illustrated in Figure (needs reference).

.. figure:: ./figures/figMagDipoles.png
	:align: center
        :scale: 70%

Magnetic susceptibility is defined as the ratio between induced magnetization and the strength of an applied magnetic field.
Provided the magnetic field is not too strong, this relationship is linear:

.. math::
	\vec M = \chi \vec H
	:label: Const_Rel_Mag

where :math:`\chi` is magnetic susceptibility of the rock, :math:`\vec H` is the magnetic field intensity, and :math:`\vec M` is the induced magnetization.
Because the majority of rocks are paramagnetic, they are almost always characterized by magnetic susceptibilities greater than 0.

When a magnetic field is applied to a susceptible object, there is a corresponding change in magnetic flux through the object.
Magnetic permeability is defined as the ratio between the density of magnetic flux and the applied magnetic field intensity:

.. math::
	\vec B = \mu \vec H
	:label: Const_Rel_Flux

where :math:`\vec B` is the magnetic flux density, and :math:`\mu` is the material's magnetic permeability.
If the magnetization within the material is linear, then magnetic susceptibility and magnetic permeability are related by the following expression:

.. math::
	\mu = \mu_0 \big [ 1+ \chi \big ]
	:label: Rel_Mu_Chi

where :math:`\mu_0 = 4\pi \times 10^{-7}` H/m is the permeability of free-space.
Therefore, both :math:`\chi` and :math:`\mu` can be used as diagnostic magnetic properties for rocks.











