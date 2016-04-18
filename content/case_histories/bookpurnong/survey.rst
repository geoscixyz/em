.. _bookpurnong_survey:

Survey
======

Loop-loop system
----------------

DC resistivity can measure the ground conductivity (see Case History > Mt. Isa), but it requires direct connection between the instrument and the earth through cables and electrodes. Here we consider another type of measurement that relies on the inductive coupling between the instrument and the ground, a mechanism more suitable for portable or towed systems. Because it uses a loop as the transmitter and another loop as the receiver, it is often referred to as "loop-loop" system. 

In a loop-loop survey, the transmitter loop carries a time-varying current, which generates a time-varying primary magnetic field everywhere in a whole space. According to Faraday's law and Lenz's law, this changing magnetic field can induce a time-varying secondary current in the ground to resist the change of magnetic field. Then this secondary current can generate a time-varying secondary magnetic field that induced an electromotive force in the receiver loop. The capability of generating the induced current is determined by the ground conductivity. Generally speaking, more conductive ground tends to be more responsive. 

Airborne EM
-----------

Because loop-loop system does not require direct contact with the ground, it is ideal to be installed on an airborne platform. An airborne EM system usually have a multi-turned transmitter loop on a towed bird or frame (helicopter) or mounted around the nose-wingtip-tail (fixed wing). The actual size of the loops can vary based on the purpose of the survey. 

Frequency domain system
-----------------------

If the current waveform in the transmitter loop is sinusoidal at a certain frequency, this system is said to operate in frequency domain. For this case, the received waveform is also sinusoidal at the same frequency, but likely with altered magnitude and a phase shift. It is convenient to decompose the receiver waveform to two orthogonal sinusoidal components: one entirely in-phase (real) and the other entirely out-of-phase (imaginary or quadrature). A loop-loop system in frequency domain can be understood with a demonstrative 3-loop model, please read the tutorial (link). You may find the following concepts useful. Click the links to learn more in Geophysical Surveys.

* Skin depth
* Footprint of a system
* Separation of source and receiver
* Resistive and conductive limits
* Scaling with induction number
* Height above the surface
* Loop coupling
* Data representation

.. figure:: ./images/booky-resolve.jpg
    :align: left
    :scale: 80% 
    :name: booky-resolve
    
The figure above shows the frequency-domain loop-loop system used at Bookpurnong. The commercial name of the system is RESOLVE, operated by Fugro Airborne (now CGG). It operates five pairs of horizontal co-planar (HCP) loop-loop configurations at 382, 1822, 7970, 35920 and 130100 Hz, and one pair of vertical co-axial loop-loop configuration at 3258 Hz. The measured secondary magnetic field (Hs) is represented as the ratio to the primary field (Hp) in part per million.

Time domain system
------------------

If the transmitter current waveform is not sinusoid, it is said to operate in time domain. Usually the time-domain transmitter waveform is designed as an abrupt pulse or step off (on-time) followed by a no-current quiet peroid (off-time). The turn-off of the primary field excites the secondary current and field in the ground. The receiver loop measures the time-decaying transient at a number of time channels during the off-time when the primary field is absent. In theory, a time-domain system is equivelant to the convolution of the transmitter waveform with the inverse Fourier transform of a multi-frequency frequency-domain system. Early time channels are roughly equal to higher frequencies. Unlike a frequency-domain system, the time-domain data read real values of the actual field. Direct measurement of the magnetic field (B in Tesla) is possible, but people usually measure the time derivatives of the magnetic field (dB/dt in volt) for logistic reasons. You may find the following concepts useful. Click the links to learn more in Geophysical Surveys.

* Diffusion distance and "smoke ring"
* Frequency to time transform: DFT, digital filtering
* Transmitter dipole moment
* Data normalization

.. figure:: ./images/booky-skytem.jpg
    :align: left
    :scale: 80% 
    :name: booky-skytem

The figure above shows the time-domain loop-loop system used at Bookpurnong. The commercial name of the system is SkyTEM, operated by SkyTEM Surveys ApS, Danmark. Its transmitter is a large loop and its two receiver loops are mounted at the rear of the frame, in orthogonal orientations measuring dB/dt in z (vertical) and x (in-line horizontal) directions. The final data are normalized as if the dipole moments of the transmitter and the receiver are both unity. One special feature of SkyTEM is its capability of operating in dual-mode - transmitting a high moment pulse and a low moment pulse sequentially. A high moment pulse has greater penetrating depth, but is difficult to cut off clearly in electronics, causing unaccepted bias in the early times. A low moment does not see very deep, but has cleaner early time channels. The high moment is 113000 NIA at 25 Hz and the low moment is 12560 NIA at 222.22 Hz at Bookpurnong. 


Survey design
-------------

Choosing the instrument and the survey parameters and layout is usually referred to as "survey design". In most cases, a geophysical survey is designed using rules of thumbs or emprical criteria. In an EM survey, the most important goal in the survey design is to match the scale of investigation to the scale of the target, using the concept of skin depth or diffusion distance. At Bookpurnong, the background conductivity is about 1 S/m, and we are interested in the subsurface from 0 to about 50 m depth. The skin depths of the RESOLVE frequencies range from about 1 to 25 m. The diffusion distances of the SkyTEM time channels range 4 to 120 m. So the interested volume of the Earth should be reasonablly sensed by the two systems. 

Another consideration is the sounding spacing. For a towed system, the in-line spacing is adjustable by the flight speed and sampling rates, and can easily achieve high density soundings. The cross-line spacing is usually a trade-oof between the cost and resolution. At Bookpurnong, RESOLVE and SkyTEM fly in a 100 m cross-line spacing (Figure), so any single location can be at least sensed by two SkyTEM lines.

.. figure:: ./images/booky-coverage.jpg
    :align: left
    :scale: 80% 
    :name: booky-coverage
    
    
