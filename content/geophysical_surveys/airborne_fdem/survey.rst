.. _airborne_fdem_survey:

Survey
======

.. topic:: Purpose

    to provide an overview of the basic airborne FDEM setup and commonly used instrumentation.

Basic Survey Setup
------------------

.. include:: transmitters_and_receivers.rst




Applicability of AFEM
---------------------

Choosing the instrument and the survey parameters and layout is usually
referred to as "survey design". In most cases, the first step in a geophysical
survey is to match the system parameters to the geologic task using rules of
thumbs or empirical criteria.

AFEM is mostly suitable for large survey areas with focus from the surface to
the shallow depth. It can quickly deployed, giving a quick overview of the
regional conductivity distribution. The recording system (towed bird) is
usually smaller than a time-domain system, in which a large and rigid frame is
used to mount the transmitter loop. So it is generally the least costly
geophysical EM solution measured by line-km. Hydrological, environmental and
engineering applications are the main area AFEM is used. It can also be useful
for mineral or petroleum exploration at shallow depth.

Footprint
---------

In an AEM survey/system, a concept "footprint" is usually used to quantify the
size of the underground volume that a system is sensitive to. Footprint can be
evaluated using different formulations, but it mostly depends on the frequency
and the conductivity. Higher frequency and higher conductivity can result in a
smaller footprint. A lower flight height may also reduce the footprint. A
first-order estimate of footprint can be from "skin depth", which considers
the frequency and the conductivity.


Survey parameters
-----------------

The operating frequencies, separations and orientations of the coils in a AFEM
system are usually fixed. The only variable geophysicist need to consider in
the survey design is the line spacing. For a 3D survey, it is important to
ensure the line spacing is at least equal or smaller than the footprint, so no
"gap" is left between lines. At the locations where higher quality of data is
desired, survey lines may be dense. The line spacing is usually a
trade-off between the cost and resolution.

Another consideration is the sounding spacing. For a towed system, the in-line
spacing is adjustable by the flight speed and sampling rates, and can easily
achieve high density soundings.

Flight height can be another parameter. Generally a lower flight height is
preferred as it provides better resolution for the near surface structure
using a smaller footprint. But some practical conditions may limit the lowest
possible flight height, for example, trees, infrastructure, severe topography,
aircraft safety, etc.



Acquisition
-----------

Differential GPS (Global Positioning System) units are used to collect the
location of the helicopter and the bird during the flight. Location data is
also collected with a base station so post-survey correction to, for example,
clock error and satellite orbit are possible.

There are two ways to terminate the actual flight height. The radar altimeter
sends radio waves that reflect from the ground back to the helicopter, and
times the travel time the conclude the distance. This type of altimeter is
usually located in the helicopter, because it has long range. The laser
altimeter uses a laser instead of radio waves. It is more sensitive with lower
range than the radar, so it is often located in the bird. It doesn’t work over
water. The altitude is measured several times in a second.

The inertia measurement unit (IMU) is used to record the position of the bird.
It records g-force and angular rate of the bird using accelerometers and
gyroscopes.




Field Notes
^^^^^^^^^^^

.. Due dilegence

On-flight camera can be used to record the video or still picture of the scene
during acquisition. This information may be a good reference for interpreters
if cultural noise, like power lines, is present in the data. Field notes may
also be recored by the surface crew for weather conditions, etc.


Instrumentation
---------------

.. include:: systems.rst
