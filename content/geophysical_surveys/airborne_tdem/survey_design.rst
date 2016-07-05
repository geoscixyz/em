.. _airborne_tdem_survey_design:

Survey Design
=============

Choosing the instrument and the survey parameters and layout is usually referred to as "survey design". In most cases, the first step in a geophysical survey is to match the system parameters to the geologic task using rules of thumbs or emprical criteria. 

Applicability of ATEM
---------------------

ATEM is mostly suitable for large survey areas with focus on greater depth compared to AFEM. It can quickly deployed, giving a quick overview of the regional conductivity distribution and also vertical reoslution. The ATEM's recording system (towed frame) is usually larger than its counterpart in a freq-domain system, in which a compact tube is used to house all of the coils. So it is generally more costly than AFEM, but still cheaper than surface surveys if measured by line-km. Mineral or petroluem exploration is the main area of application for ATEM. It can also be an alternative to AFEM at shallow depth if a low moment ATEM is used.

Footprint
---------

In an AEM survey/system, a concept "footprint" is usually used to quantify the size of the underground volume that a system is sensitive to. Footprint can be evaluated using different formulations, but it mostly depends on the base frequency and the conductivity. A low base frequency allows longer off-time for the measurement of signals from the depth, resulting in a larger footprint. A more resistive terrain also creates a larger footprint. A higher flight height may also increase the footprint. A first-order estimate of footprint can be from "difussion distance", which considers the delay time (time after the transmitter current is turned off) and the conductivity.

Survey parameters
-----------------

The configuration of the coil in a ATEM system are usually fixed. There are three key parameters geophysicist need to consider in the survey design: dipole moment, base frequency and line spacing. Dipole moment and base frequency are usually tied together. A high moment current used for deep penetration is difficult to turn off rapidly, so it requires a low base frequency. A low moment has a short turn-off time, which is ideal for near-surface imaging, and requires a high base frequency. For a 3D survey, it is important to ensure the line spacing is at least equal or smaller than the footprint, so no "gap" is left between lines. At the locations where higher quality of data is desired, there may be densified survey lines. The line spacing is usually a trade-off between the cost and resolution. Another consideration is the sounding spacing. For a towed system, the in-line spacing is adjustable by the flight speed and sampling rates, and can easily achieve high density soundings. A fixed-wing system usually flies much faster, resulting in a larger in-line spacing and lower lateral resolution.

Flight height can be another parameter. Generally a lower flight height is preferred as it provides better resolution for the near surface structure using a smaller footprint. But some practical conditions may limit the lowest possible flight height, for example, trees, infrastructure, severe topography, aircraft safety, etc. A helicopter ATEM system can fly the frame as low as tens of meters, whereas a fixed-wing system must be above hundred meters for safety reasons.


Acquisition
-----------

Differential GPS (Global Positioning System) units are used to collect the location of the helicopter and the frame during the flight. Location data is also collected with a base station so post-survey correction to, for example, clock error and satellite orbit are possible.

There are two ways to terminate the actual flight height. The radar altimeter sends radio waves that reflect from the ground back to the helicopter, and times the travel time the conclude the distance. This type of altimeter is usually located in the helicopter, because it has long range. The laser altimeter uses a laser instead of radio waves. It is more sensitive with lower range than the radar, so it is often located in the bird. It doesn’t work over water. The altitude is measured several times in a second.

The inertia measurement unit (IMU) is used to record the position of the frame. It records g-force and angular rate of the frame using accelerometers and gyroscopes.



Field Notes
***********

.. Due dilegence

On-flight camera can be used to record the video or still picture of the scene during acquisition. This information may be a good reference for interpreters if cultural noise, like power lines, is present in the data. Field notes may also be recored by the surface crew for weather conditions, etc.



