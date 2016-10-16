.. _airborne_fdem_index:

Airborne FDEM
=============

.. purpose::

   To illustrate the fundamentals of an airborne frequency domain EM survey,
   provide a vision for how it is applied in the field, and demonstrate
   potential uses.

.. figure:: ./images/afem_cover.jpg
   :align: right
   :figwidth: 30%
   :name: afem_cover

   RESOLVE system (courtesy CGG).

DC resistivity can measure the ground conductivity, but it requires direct
connection between the instrument and the earth through cables and electrodes.
An airborne EM survey considers another type of measurement that relies on the
inductive coupling between the instrument and the ground, a mechanism more
suitable for portable or towed systems. Because it uses a loop as the
transmitter and another loop as the receiver, it is sometimes referred to as a
"loop-loop" system.

In such a survey, the transmitter loop carries a time harmonic current at a certain frequency, which
generates a time harmonic primary magnetic field everywhere in a whole space.
According to Faraday's law and Lenz's law, this changing magnetic field can
induce a time harmonic secondary current in the ground to resist the change of
magnetic field. Then this secondary current can generate a time harmonic
secondary magnetic field that induced an electromotive force in the receiver
loop. The capability of generating the induced current is determined by the
ground conductivity, and possibly the magnetic permeability. Generally
speaking, more conductive ground tends to be more responsive.

Mounting transmitter and receiver on an aircraft, an airborne system can quickly probe the
earth's conductivity over large areas, so it has been used in
geological mapping and regional assessment for groundwater, mineral/petroleum
exploration and geothermal resource. Compared to ground-based surveys,
airborne EM may have higher level of noise due to the instability of the
platform, which limits its depth penetration.


**Contents**

.. toctree::
   :maxdepth: 1

   physics
   survey
   data
   interpretation
   survey_design
   practical_considerations


**Related Case Histories**

- :ref:`Bookpurnong <bookpurnong_index>`: groundwater salinization evaluation

- Tli Kwi Cho: kimberlite exploration
