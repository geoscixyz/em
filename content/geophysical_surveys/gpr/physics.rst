.. _gpr_physics:

.. purpose::
	
	Here we discuss the physical principles in which GPR is founded.


Physics
=======

	- Basic Explanation
	- Some properties of radiowaves signals
	- 2D simulation for a layer model and a sphere model

.. figure:: images/GPR_schematic_example.jpg
    :align: right
    :figwidth: 55%
    :name: fig_physics_GPR_schematic

    Basic diagram for a GPR survey.

The basic conceptual understanding of GPR is shown in :numref:`fig_survey_GPR_schematic`. During GPR surveys, a source antenna (Tx) is used to send a pulse of radiowaves (10 MHz to 2.6 GHz) into the ground. As the radiowaves propagate through the Earth, they are distorted as a result of the Earth’s electromagnetic properties. At boundaries where the subsurface electromagnetic properties change abruptly, radiowave signals undergo transmission, reflection and/or refraction. Sensors (Rx) measure the amplitudes and travel times of radiowave signals that have been distorted by the Earth. This information is then used to image discrete targets and physical boundaries.

Properties of Radiowave Signals
-------------------------------

Having a-priori knowledge of radiowave properties within the Earth 

Propagation Velocity
********************

Radiowaves propagate through different materials at different speeds.
The velocity of the radiowaves depends on the physical properties of the medium.
In general, the velocity of radiowaves through a homogeneous material is given by:

.. math::
    V = \sqrt{\frac{2}{\mu \varepsilon}} \Bigg [ \Bigg ( 1 + \bigg ( \frac{\sigma}{\omega \varepsilon} \bigg )^2 \, \Bigg )^{1/2} \; + 1 \; \Bigg ]^{-1/2}

This equation can be used to show that the radiowave velocity is largest in free-space (i.e. when :math:`\sigma = 0`, :math:`\mu = \mu_0` and :math:`\varepsilon = \varepsilon_0`).
Therefore, electromagnetic waves in matter travel slower than the speed of light (c = 3.00 :math:`\times 10^8` m/s).

GPR signals are characterized as being high-frequency.
Thus in many cases (and for this course), it is safe to assume that :math:`\sigma \ll \omega \varepsilon`; especially if the Earth is resistive.
This is known as the **wave regime approximation**.
Using the approximation, and assuming the Earth is non-permeable (:math:`\mu = \mu_0`), the velocity of radiowaves can be simplified to:

.. math::
    V \approx \frac{1}{\sqrt{\mu_0 \varepsilon}} = \frac{c}{\sqrt{\varepsilon_r}}

where :math:`\mu_r` is the relative permeability and :math:`\varepsilon_r` is the relative permittivity.

Normal Transmission and Reflection
**********************************


Skin Depth
**********




Example: Layered Earth
----------------------





Example: Buried Conductor
-------------------------









