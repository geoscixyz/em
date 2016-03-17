.. _magnetic_permeability_magnetism:

Magnetism in Rocks
==================


Magnetism is attributed to the movement of electrical charges.
Within a material, the motion and spin of individual electrons is responsible for generating a collection of magnetic moments :math:`\{{\bf m_i}\}`.
The total magnetic moment for the material :math:`{\bf m}`, is equal to the vector sum of all electron magnetic moments:

.. math::
	{\bf m} = \sum_i {\bf m_i}
	:label: Sum_Dipoles
	
Magnetization :math:`{\bf M}` is defined as the magnetic moment per unit volume:

.. math::
	{\bf M} = \frac{d {\bf m}}{d V}
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
	{\bf M} = \chi {\bf H}
	:label: Const_Rel_Mag

where :math:`\chi` is magnetic susceptibility of the rock, :math:`{\bf H}` is the magnetic field intensity, and :math:`{\bf M}` is the induced magnetization.
Because the majority of rocks are paramagnetic, they are almost always characterized by magnetic susceptibilities greater than 0.

According to the magnetic constitutive relationship (link), the relationship between magnetic susceptibiliy and magnetic permeability (link), and Eq. ():

.. math::
	{\bf B} = \mu {\bf H} = \mu_0 \big [1 +\chi \, ] {\bf H} = \mu_0 \big [ {\bf H + M} \big ]
	:label: Rel_BMH

where :math:`\mu_0 = 4\pi \times 10^{-7}` H/m is the permeability of free-space.
Eq. () implies that induced magnetization contributes towards the net magnetic flux density within the rock.
Furthermore, the nature of this contribution may be represented by the rock's magnetic permeability.











