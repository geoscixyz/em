.. _airborne_fdem_data:

Data
====

.. topic:: Purpose

    - essential information for working with and interpreting the data - we want
      to mathematically model the data: what are they?

.. todo::

    - resshuffel below content: some of this belongs in transmitters and receivers
    - topics for this page:
        - getting from what is measured to the "data" we interpret (delivered data)
        - what are we working with - total field? or secondary field? (analytic or measured - how are they actually measuring it - don't need details, )
            - units : ppm of primary field? field units?
        - moments of tx, rx : are normalizations applied to the data?
        - visualizing the data : soundings, plan / map view, real and imaginary parts


.. todo::

    **blend in the following text, some may go in interpretation**

    Here we make distinction bewteen "raw data" and "delivered data". Raw data are
    usually direct dump from the instruments, and may contain repeated
    measurements at the same location. For EM, the raw data are generally in the
    form of time series at a certain sampling rate. Then the raw data are
    processed by stacking, averaging, transforming, filtering, etc. The delivered
    data are usually in a reduced format of smaller size and higher signal noise
    ratio. In our website, we interpret "delivered data".


.. todo::

    **bring in the following text: some may fit in interpretation**

    The primary goal of processing the raw data is to prepare the delivered data.
    The procedures usually involve considerations on the instrumentation and field
    operation. Examples are de-noising, leveling, smoothing, filtering, stacking,
    spatial and temporal corrections, convolution/deconvolution, transfer function
    estimation, etc. The readers are suggest to refer to the survey report or the
    field crew for more information.

    For delivered data, data processing is a step to examine and edit the data so
    it can be reliably interpreted in the next step. There are several major
    reasons why processing is necessary:

    - Quality control. Data without quality or uncertainty assessment mean nothing. So it is important to know the overall quality of a data set. A data set may be deemed not suitable for interpretation if the noise level is too high. For most data sets, preliminary QC is carried out during acquisition. So the delivered data can still show useful signals in decent quality. But we still have to identify the "bad data".
    - Uncertainty analysis. Uncertainty is a quantitative way of assessing the data quality. Data with greater noise may be assigned larger uncertainty. Most inversion programs need this information to decide how well the inversion wants to fit a particular datum.
    - Data preparation. A data set can be difficult to interpret because of its size and noise. For example, the numerical modeling time is roughly proportional to the number of measurements in an airborne survey that has significant data redundancy. So it may be desired to down-sample the data set without losing information. And high-frequency noise associated with non-geologic objects can be effectively removed by low-pass filtering and other smoothing methods.
    - Model parameterization. Any interpretation is based on models. By processing the data, we may choose more proper models (conductivity only? 1D/2D/3D? Cell/layer size?). For example, negative transients in a central loop TEM survey indicate the existance of induced polarization. So we know at some places a real and time-independent conductivity model is not enough to explain the data. Another example is the variation of data in space may indicate the scale of EM induction, which helps the design of discretization for numerical modeling.



Loop-loop EM systems like the Airborne Resolve (TODO:link), measure the
voltage generated in a loop which has a time-varying magnetic flux through it, according to :ref:`faraday`.
In the case of a frequency domain survey, this is a harmonic signal.

A harmonic current is used to generate a time-harmonic magnetic field
(:numref:`looploopEMbasics`). This induces secondary currents in the
subsurface, which intern produce secondary magnetic fields. Both the primary
and secondary magnetic fields reach the receiver. The time-varying magnetic
flux through the receiver loop induces currents which act to oppose the change
in flux. The voltage in the receiver loop is what we use to define a datum.

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
single complex number defining the harmonic at the transmitter frequency. This
can be done in real-time. :cite:`slattery2012`

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



Data visualization
-------------------
Data visualization is a useful tool in the following:

- Understanding the underlying physics.
- Data quality control.
- Qualitative interpretation.
- Quality control for advanced interpretation, e.g. predicted data in inversion.

Every datum point in an airborne EM survey can be specified using three
parameters: the horizontal sounding location (easting and northing) and the
time(t)/frequency(f). Using easting and northing as x and y respectively and
time/frequency as z, a 3D data volume can be formed. So there are three ways
of plotting data for airbrone EM survey:

- Map: contouring a particular time/freq as a function of the horizontal location. Slice the data volume horizontally. Spotting interesting area.
- Profile: plotting all or select time/freq along a flight line as a function of one horizontal dimension. Slice the data volume vertically. Compare time/freq along a transverse.
- Sounding: plotting data at a particular location as a function of time/freq. Drill the data volume vertically.


