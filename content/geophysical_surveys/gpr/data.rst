.. _gpr_csem_data:

Data
====

Measured Response
-----------------

During GPR surveys, a source antenna (Tx) is used to send a pulse of radiowaves (10 MHz to 2.6 GHz) into the ground. As the radiowaves propagate through the Earth, they are distorted as a result of the Earth’s electromagnetic properties. At boundaries where the subsurface electromagnetic properties change abruptly, radiowave signals undergo transmission, reflection and/or refraction. Distorted radiowave signals are then measured by the receiver antenna (Rx).

The receiver antenna acts as a transducer and converts incoming radiowave signals into electrical current. Like the primary current within the transmitter antenna, the current induced within the receiver antenna is also a wavelet. The 



Processing
----------

Gain Correction
***************

.. figure:: images/GPR_gain_time_function.png
	:align: right
	:figwidth: 40%
	
	Example gain function which corrects for a loss in signal strength at later times.


Signals measured at earlier times are much stronger than signals which are measured at later times.
This may be due to scattering, attenuation, geometric spreading or reflection/transmission events.
As a result, it may not be easy to distinguish important features in the data at later times.
To account for this, the raw data :math:`d_{raw}(t)` for each reading is multiplied by a gain function :math:`g(t)` as follows:

.. math::
	d(t) = g(t) \times d_{raw}(t)


where :math:`d(t)` is the data represented in the radargram.
The gain function itself is a positive function which increases in magnitude as a function of time.
Thus a larger gain is applied to raw data at later times.
An example of the gain function is shown on the right.
As we can see, the gain function increases in value exponentially to account for the exponential loss in return signal strength over time.
However, the gain function is generally bounded by a maximum value.

.. figure:: images/GPR_gain_signal.png
	:align: center
	:figwidth: 100%
	
	(Left) Single trace before gain correction. (Right) Single trace after gain correction.


The strength of returning signals is also much weaker at distances further away from the source.
Because of this, gain corrections may be applied based on Tx-Rx distance.
This is not necessary for common offset surveys, but may be important in common midpoint or transillumination surveys.


Stacking
********

GPR signals travel at velocities close to the speed of light (c = :math:`3.00 \times 10^8` m/s).
As a result, the total travel times for GPR signals are on the order of 100s of nanoseconds.
Because of this, it is easy to repeat the same GPR shot many times over a short interval.

Stacking describes the process of averaging a set of repeated GPR shots in order to reduce noise and improve interpretation.
Essentially, stacking acts as a way of improving the signal to noise ratio for GPR data collected at a certain location.
An example of this is demonstrated below.
As we can see, the more readings we stack, the clearer we see coherent GPR signals.


.. figure:: images/GPR_stacking_times.png
	:align: center
	:figwidth: 100%
	
	Example of how averaging multiple traces from the same Tx-Rx pair can improve the signal to noise ratio. This results in an improved image of the returning signal.





Smoothing
*********

Smoothing is another technique used to improve the interpretation of field collected GPR data.
In GPR systems, the data sampling rate is such that the returning wavelet signals should be reasonably smooth and visible.
Random noise on the other hand is completely incoherent.
When smoothing is applied to the data, it has the effect of reducing the amplitude of incoherent noise while retaining naturally smooth signals in the data.
One example of smoothing techniques is the moving average (shown below).
We can see that as more data points in time are used for the average, the more easily recognizable the wavelet signal is.



.. figure:: images/GPR_averaging_times.png
	:align: center
	:figwidth: 100%
	
	Example of smoothing a trace by using a moving average.





Visualization
-------------













