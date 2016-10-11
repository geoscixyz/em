.. _airborne_fdem_survey:

Survey
======

.. topic:: Purpose

    To provide an overview of the basic airborne FDEM system configuration and
    commonly used instrumentation.

Basic Survey Setup
------------------

.. include:: transmitters_and_receivers.rst


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

On-flight camera can be used to record the video or still picture of the scene
during acquisition. This information may be a good reference for interpreters
if cultural noise, like power lines, is present in the data. Field notes may
also be recored by the surface crew for weather conditions, etc.


Instrumentation
---------------

.. include:: systems.rst
