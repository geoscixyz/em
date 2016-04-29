.. _airborne_tdem_index:

Airborne FDEM
=============

- Intro:
	- brief overview of the experiment
	- applications
	- links to case-histories


.. toctree::
    :maxdepth: 1

    governing_equations
    example
    transmitters
    receivers
    systems
    survey_design
    data
    interpretation
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
