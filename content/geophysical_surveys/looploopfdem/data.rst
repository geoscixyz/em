.. _looploopfdem_data:

Data
====

Loop-loop EM systems like the Airborne Resolve (TODO:link), measure the
voltage generated in a loop which has a time-varying magnetic flux through it, according to :ref:`faraday`. 
In the case of a frequency domain survey, this is a harmonic signal. 

A harmonic current is used to generate a time-harmonic magnetic field
(:numref:`looploopEMbasics`). This induces secondary currents in the subsurface,
which intern produce secondary magnetic fields. Both the primary and secondary
magnetic fields reach the receiver. The time-varying magnetic flux through the
receiver loop induces currents which act to oppose the change in flux. The voltage in the receiver loop is what we use to define a datum. 

 .. figure:: http://gpg.geosci.xyz/en/latest/_images/Hp_Hs_schematic.jpg
    :align: center
    :scale: 80%
    :name: looploopEMbasics


    A time varying current ( \\(I_0 \\cos \\omega t\\)) generates a primary magnetic field \\(\\mathbf{H_p} \\cos \\omega t\\) which induces secondary currents in the subsurface and intern, creates secondary magnetic fields (\\(\\mathbf{H_s} \\cos(\\omega t + \\psi)\\)). Both the primary and secondary fields reach the receiver. Image adapted from the GPG_. TODO: cc - by 4.0? or re-create? 

.. _GPG: http://gpg.geosci.xyz/en/latest/content/electromagnetics/responses_from_a_conductor_in_free_space.html

The voltage in the receiver loop is measured as a function of time, defining a
time-series. This is converted to a time-derivative of magnetic flux density (\\(\\frac{\\partial \\mathbf{b}}{\\partial t}\\)) through :ref:`faraday`. 

To obtain a datum defined in the frequency domain, a Fourier transform of
these must be taken. To accomplish this, the time-series is segmented into
windows, in the case of the Resolve system, 10Hz or 0.1s windows, and a
discrete Fourier transform of the data in this window is taken to provide a
single complex number defining the harmonic at the transmitter frequency. This can be done in real-time. [1]_ 

Noise: Spheric Pulses (from lightning) -> narrow bandwidth, strong peaks (considered acceptable when < 10 spheric pulses at a given frequency per 100 samples continuously). Monitored separately. [1]_

Filters: spheric rejection median & Hanning filter

Question: do they take a single value at the fixed frequency, or average in a frequency-window? 

TODO: In-Flight Calibration, bucking coils

TODO: Thibaut's notebook / images

.. [1] Slattery, S.R. and Andriashek, L.D. (2012): Overview of airborne-electromagnetic and -magnetic geophysical survey data collection using the RESOLVE® and GEOTEM® surveys near Red Deer,central Alberta; Energy Resources Conservation Board, ERCB/AGS Open File Report 2012-07, 246 p. Available at: http://www.ags.gov.ab.ca/publications/OFR/PDF/OFR_2012_07.PDF
