.. _airborne_tdem_pratical_considerations:

Practical Considerations
========================

So far we have described the theory of airborne TDEM survey. There can be other important items that worth considering in practice.

Cultural noise
--------------

An airborne EM data set may contain signals from non-geologic object, for example, power lines, pipes, etc. Some of them can act as active EM sources transmitting interfering signals, while others may be surficial good conductors. Measures have been taken by the system operator to minimize those negative effect, but sometimes they can still be significant in the data. Advanced modeling may be necessary to take them into account for interpretation.


Recovery of true flight height
------------------------------

The flight height is usually derived from radar and/or laser altimeters. Sometimes, non-geologic objects at surface like trees can lead to miscalculation. If the EM system is operating in the inductive limit (very high frequency for AFEM or very early time for ATEM), there is hope to recover the true flight height. When a loop-loop system is measuring ATEM data that are early enough, the data is no longer sensitive to the conductivity change caused by geologic variation. The inductive-limit data may only change if the conductivity varies within many orders of magnitude, like the contrast between the earth and the air. Effectively, such data are direct measurement of the distance from the coils to the surface. 

Multi-moment system
-------------------

The transmitter dipole moment is a trade-off between resolution and penetration. A smaller moment can turn off the current quickly, resulting in more high-frequency-components in the data, but the signals from depth may be too weak for the receiver to effectively make a measurement. A larger moment magnifies the energy sent to underground, elevating the received signals above the noise, but such high moment would need a longer ramp for the current turn-off, limiting the richness of high-freq contents. In order to obtain information at both surface and depth, some systems have developed a hybrid current waveform that alternates high and low moments sequentially in a single flight. 

