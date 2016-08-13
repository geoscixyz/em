.. _airborne_tdem_index:

Airborne TDEM
=============

.. figure:: ./images/atem_cover.jpg
   :align: center
   :scale: 80%
   :name: atem_cover

.. Source: Jean M. Legault, 2015, Airborne Electromagnetic Systems – State of the Art and Future Directions, CSEG RECORDER, VOL. 40, No. 06.

Motivation
----------

DC resistivity can measure the ground conductivity, but it requires direct
connection between the instrument and the earth through cables and electrodes.
An airborne EM survey considers another type of measurement that relies on the
inductive coupling between the instrument and the ground, a mechanism more
suitable for portable or towed systems. Because it uses a loop as the
transmitter and another loop as the receiver, it is sometimes referred to as
"loop-loop" system.

Basic idea
----------

As presented in airborne FDEM, a loop-loop system can operate at multiple
frequencies to gain depth resolution in the earth. A single-frequency time-
harmonic coil is easy to create electronically, but such a system can only
sample discrete frequencies. Also the multi-coil arrangement in an AFEM system
limits the dipole moment of the transmitter loop, so its depth of penetration
is relatively shallow. A loop-loop system in time domain can overcome those
drawbacks by transmitting a current in a waveform with abrupt change that
spreads over a wide and continuous range of spectrum. By adjusting the
transmitter moment, an ATEM system can effectively explore from near surface
to great depth. As a result of better electronic techniques, ATEM has gained
popularity over the last decade, and is an industrtial standard in many
applications.

Examples
--------

Airborne EM is ideal for surveying a large area, so it has been used in
geological mapping and regional assessment for groundwater, mineral/petroleum
exploration and geothermal resource. An important feature of ATEM is that its
transmitter moment can vary from a relatively small loop towed by a helicopter
to a large loop mounted on a fixed-wing airplane. This makes it suitable for a
variety of geoscientific applications from environmetal to deep exploration.
On this website, we use ATEM in two case histories:

- Bookpurnong: groundwater salinization evaluation
- Tli Kwi Cho: kimberlite exploration


.. toctree::
    :maxdepth: 1

    physics
    survey
    data
    interpretation
    survey_design
    practical_considerations

.. todo::

    * Diffusion distance and "smoke ring"
    * Frequency to time transform: DFT, digital filtering
    * Transmitter dipole moment
    * Data normalization


    If the transmitter current waveform is not sinusoid, it is said to operate in
    time domain. Usually the time-domain transmitter waveform is designed as an
    abrupt pulse or step off (on-time) followed by a no-current quiet peroid (off-
    time). The turn-off of the primary field excites the secondary current and
    field in the ground. The receiver loop measures the time-decaying transient at
    a number of time channels during the off-time when the primary field is
    absent. In theory, a time-domain system is equivelant to the convolution of
    the transmitter waveform with the inverse Fourier transform of a multi-
    frequency frequency-domain system. Early time channels are roughly equal to
    higher frequencies. Unlike a frequency-domain system, the time-domain data
    read real values of the actual field. Direct measurement of the magnetic field
    (B in Tesla) is possible, but people usually measure the time derivatives of
    the magnetic field (dB/dt in volt) for logistic reasons. You may find the
    following concepts useful. Click the links to learn more in Geophysical
    Surveys.
