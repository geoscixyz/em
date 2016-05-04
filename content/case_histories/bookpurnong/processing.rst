.. _bookpurnong_processing:

Processing
==========


Processing of Frequency domain data
-----------------------------------

The RESOLVE data, viewed along the profiles, is mostly smooth, so the high-
frequency random noise is likely to be suppressed at the contractor's end. But
we are still able to identify some outliers with suspecious negative values.
We have therefore removed them.

.. figure:: ./images/booky-resolveqc.jpg
    :align: left
    :scale: 80%
    :name: booky-resolveqc

Other considerations:

(1) The real part of the two highest frequencies are really close. This suggests the system is in the inductive limit, and the data at the highest frequency may be just a measure of sensor height, instead of the ground conductivity. See how the high frequency data can be used to correct the flight height on a separate page.

(2) The uncertainty assigned to this data set is 5% plus 10 ppm.


Processing of Time domain data
------------------------------

The SkyTEM data are in reasonable quality. There are noticeable irregular data
called "channel jumping", and noise that contaminates the late time channels.

.. figure:: ./images/booky-skytemqc.jpg
    :align: left
    :scale: 80%
    :name: booky-skytemqc

Some automated procedures can be used to screen the data:

(1) Use the first and second order derivative of a decay curve to detect unrealistic decay.

(2) Identify outliers using the first order derivative.

(3) Remove the data outside of the feasible range.

Other considerations:

(1) Bookpurnong is conductive, so induction takes longer time to dissipate. If the base frequency is not low enough (i.e. off time not long enough) the measured data may be affected by the previous cycle. See discussion on a separation page.

(2) Like the frequency domain system, the earliest time channel may be used to correct the bird's flight height.

(3) Uncertainty = 10% + 1E-13.
