.. _airborne_tdem_data:

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

 .. figure:: ../images/Hp_Hs_schematic.jpg
    :align: center
    :scale: 80%
    :name: looploopEMbasics


    A time varying current ( :math:`I_0 \cos \omega t`) generates a primary magnetic field :math:`\mathbf{H_p} \cos \omega t` which induces secondary currents in the subsurface and intern, creates secondary magnetic fields (:math:`\mathbf{H_s} \cos(\omega t + \psi)`). Both the primary and secondary fields reach the receiver. Image adapted from the GPG_. TODO: cc - by 4.0? or re-create?

.. _GPG: http://gpg.geosci.xyz/en/latest/content/electromagnetics/responses_from_a_conductor_in_free_space.html

The voltage in the receiver loop is measured as a function of time, defining a
time-series. This is converted to a time-derivative of magnetic flux density (:math:`\frac{\partial \mathbf{b}}{\partial t}`) through :ref:`faraday`.

To obtain a datum defined in the frequency domain, a Fourier transform of
these must be taken. To accomplish this, the time-series is segmented into
windows, in the case of the Resolve system, 10Hz or 0.1s windows, and a
discrete Fourier transform of the data in this window is taken to provide a
single complex number defining the harmonic at the transmitter frequency. This can be done in real-time. :cite:`slattery2012`

Noise: Spheric Pulses (from lightning) -> narrow bandwidth, strong peaks
(considered acceptable when < 10 spheric pulses at a given frequency per 100
samples continuously). Monitored separately. :cite:`slattery2012`

Filters: spheric rejection median & Hanning filter

Question: do they take a single value at the fixed frequency, or average in a frequency-window?


GPS (Global Positioning System) units are used to collect the location of the helicopter
and the bird during the flight. Location data is also collected with a base station so
post-survey correction to, for example, clock error and satellite orbit are possible.

There are two ways to terminate the actual flight height. The radar altimeter
sends radio waves that reflect from the ground back to the helicopter, and times
the travel time the conclude the distance. This type of altimeter is usually located
in the helicopter, because it has long range. The laser altimeter uses a laser
instead of radio waves. It is more sensitive with lower range than the radar, so
it is often located in the bird.  It doesn’t work over water. The altitude is
measured several times in a second.

The inertia measurement unit (IMU) is used to record the position of the bird.
It records g-force and angular rate of the bird using accelerometers and gyroscopes.


TODO: In-Flight Calibration, bucking coils

TODO: Thibaut's notebook / images

