.. _airborne_fdem_pratical_considerations:

Practical Considerations
========================

.. topic:: Purpose

  To remind people the practical aspects of airborne FDEM.

So far we have described the airborne FDEM survey on book. There can be
other important items that worth considering in practice.

Cultural noise
--------------

An airborne EM data set may contain signals from non-geologic object, for
example, power lines, pipes, etc. Some of them can act as active EM sources
transmitting interfering signals, while others may be surficial good
conductors. Measures have been taken by the system operator to minimize those
negative effect, but sometimes they can still be significant in the data. In a 
packaged airborne data set, there is usually a channel called 
"power line monioring" that can indicate the existence of power line in proximity.
Advanced modeling may be necessary to take them into account for
interpretation if they are difficult to suppress.


Recovery of true flight height
------------------------------

The flight height is usually derived from radar and/or laser altimeters.
Sometimes, non-geologic objects at surface like trees can lead to
miscalculation. If the EM system is operating in the inductive limit, there is
hope to recover the true flight height. When a loop-loop system is saturated,
the real part of the airborne FEM data asymptotes and the imaginary part
vanishes. So the data is no longer sensitive to the conductivity change caused
by geologic variation. The inductive-limit data may only change if the
conductivity varies within many orders of magnitude, like the contrast between
the earth and the air. Effectively, such data are direct measurement of the
distance from the coils to the surface.


