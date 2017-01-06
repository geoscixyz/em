.. _gpr_interpretation:


.. purpose::
	
	Here, some basic interpretation techniques for GPR data are discussed. As we will show, the responses from particular structures result in diagnostic signatures within radargram data.

Interpretation
==============

Zero-Offset Surveys: Buried Compact Objects
-------------------------------------------

Below we see the geometry for a zero-offset survey and the corresponding radargram.
We will show how the geometry of the problem and the radargram can be used to resolve the locations of pipes and blocky objects.


.. figure:: images/GPR_compact_objects.png
	:align: center
	:figwidth: 100%

        (Left) Problem geometry showing a buried pipe and a block. (Right) Corresponding radargram for the problem geometry.


In GPR, a **thin pipe** will act as a point reflector.
According to the geometry of the problem, the total travel time of the GPR signal as it reflects off the pipe is given by:

.. math::
	t_p = \frac{2 L_2}{V} = \frac{2 \sqrt{ (x - x_p)^2 + d^2}}{V}


where :math:`V` is the propagation velocity (light gray region) and :math:`d` is the depth to the pipe.
As we can see in the radargram, the arrival times for a compact object form a hyperbola.
When we are directly above the pipe (:math:`x = x_p`), the total travel time is smallest and equal to:

.. math::
	t_p (x_p) = \frac{2 d}{V}


For the **block**, things are a little more complicated.
Above the face of the block (:math:`x_L` = 6 m to :math:`x_R` = 16 m), the signal measured by the receiver reflects directly.
However, the return signal at locations outside the margins of the block occur on the points.
As a result, the total travel time for reflected signals off the block are given by:

.. math::
	t_b = \begin{cases} \dfrac{2 \sqrt{(x-x_L)^2 + h^2}}{V} \;\;\; &\textrm{for} \;\;\; x < x_L \\
	\dfrac{2h}{V} \;\;\; &\textrm{for} \;\;\; x_L \leq x \leq x_R \\
	\dfrac{2 \sqrt{(x-x_R)^2 + h^2}}{V} \;\;\; &\textrm{for} \;\;\; x > x_R \end{cases}

where :math:`h` is the depth to the top of the block.
As we can see from the previous equation, we expect to see a flat feature the block's radargram signature.
Then on either size of the block, the radargram signature resembles one-half of a hyperbola.

**Resolving Buried Objects: Method 1**

In order to locate buried objects, we first need to use the radargram to obtain a velocity for the medium.
Let us begin by considering the pipe.
Notice that at large offset distances from the horizontal location of the pipe (i.e. when :math:`x - x_p \gg d`), the travel time for the pipe becomes:

.. math::
	t_p = \frac{2 L_2}{V} \approx \frac{2 }{V} \Bigg ( (x - x_p) + \frac{1}{2} d \Bigg ) \;\;\; \textrm{for} \;\;\; \Delta x_2 \gg d


Therefore, each end of the hyperbolic signature has a slope :math:`m = \pm 2/V` (red dashed lines).
The slope on the radargram can ultimately be used as a crude approximation for the medium velocity.
Once the medium velocity has been obtained, the depth to the object can be calculated using the minimum travel time.
The minimum travel time for the pipe (blue dashed line) is given by:

.. math::
	t_0 = \frac{2d}{V}
	

Notice that for the block the travel time also shows a slope of :math:`m = \pm 2/V` as we move far enough away.
As a result, we can approximate the medium velocity using the block's radargram signature then use its minimum travel time to get the depth.


**Resolving Buried Objects: Method 2**

Notice that the offset distance must be sufficiently large in order to obtain the medium velocity.
If the offset distance is insufficient, we must use a different method for determining the medium velocity.

Let us first consider the **pipe**.
The total travel time for the reflected GPR signal is given by:

.. math::
	t_p = \frac{2 L_2}{V} = \frac{2 \sqrt{ (x - x_p)^2 + d^2}}{V}


When we are directly over the pipe, we will have a minimum travel time equal to (blue dashed line):

.. math::
	t_0 = \frac{2d}{V}

By combining the two previous equations, we see that:

.. math::
	V = 2 \sqrt{\dfrac{(x - x_p )^2}{t^2 - t_0^2}}


where (:math:`x`, :math:`t`) represents are arbitrary point on the hyperbolic signature within the radargram.
Given that :math:`t_0` and :math:`x_p` can be obtained directly from the radargram, **any other point** on the hyperbola can be used to determine the propagation velocity of the medium.
This may come in handy when a portion of the hyperbola is obstructed by other signals.
Also note that once :math:`V` is determined, the definition of :math:`t_0` can be used to determine the depth of the object.

Notice that for locations to the left and to the right of the block, the total travel time behaves like a hyperbola.
Therefore, we can use the same approach.
The only difference being that :math:`x_p` is replaced by either :math:`x_L` or :math:`x_R`; which depends on the side of the block's signature you use.

Common Midpoint Survey
----------------------

The travel time for the radiowave signal is given by:

.. math::
	t = \frac{2 \sqrt{ x^2 + d^2 }}{V}


where :math:`d` is the thickness of the top layer and :math:`x` is the distance between the mid-point and either the transmitter or the receiver.
Once again by defining :math:`t_0 = 2d/V`, the top-layer velocity is given by:

.. math::
	V = 2 \sqrt{ \dfrac{x^2}{t^2 - t_0^2} }


Thus, **any point** on the parabola can be used to determine the top-layer velocity from a common mid-point survey.
And once :math:`V` is determined, the definition of :math:`t_0` can be used to obtain the thickness of the top layer.



