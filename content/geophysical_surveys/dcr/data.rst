.. _dcr_data:

Data
====

.. topic:: Purpose 

   To show how measured voltages are converted to apparent resistivity and plotted as a sounding curve or as a pseudo-section 

In a general DC resistivity survey (:numref:`dcr_Schlumberger_array`), one electrode, :math:`A`, is the 
positive side of a current source, and the other electrode, :math:`B`, is the negative 
side. The current into each electrode is equal, but of opposite sign. 

.. figure:: ./images/DCR_Gradient-Schlumberger_Array.svg
	:name: dcr_Schlumberger_array
	:align: right
	:figwidth: 50%

	A general 4 electrode DC resistivity array. A and B are the current electrodes while M and N are the potential electrodes. Distances between the electrodes are used to calculate the geometry factor and apparent resistivity discussed below.	

Measured potential differences
------------------------------
Given these 2 current (source) electrodes, the measured voltage, which is the 
**difference** in potential at the two receiver electrodes M and N, is the superposition 
of the effects from the current source and current sink. The flow of currents between the 
current electrodes causes charges to build up on interfaces between regions of differing conductivity, 
as discussed on the :ref:`DC Resistivity: Physics page <dcr_physics>`. The total potential difference 
that we measure is the sum of the potentials due to all of the accumulated charges.

In a uniform halfspace, where the only interface is between the air and the earth, the measured potential 
difference is given by the following expression:

.. math::
	\Delta V &= V_M - V_N \textrm{, with} \\[0.8em]
	V_M &= \frac{I \rho}{2 \pi} \left \{ \frac{1}{r_{AM}}  -  \frac{1}{r_{BM}} \right \} \textrm{ and}  \\[0.8em]
	V_N &= \frac{I \rho}{2 \pi} \left \{ \frac{1}{r_{AN}}  -  \frac{1}{r_{BN}} \right \} \textrm{, so} \\[0.8em]
	\Delta V &= \frac{I \rho}{2 \pi} \left \{ \frac{1}{r_{AM}} - \frac{1}{r_{BM}} - \frac{1}{r_{AN}} + \frac{1}{r_{BN}} \right \}\\[0.8em]
	\Delta V &=I \rho G

where :math:`G` is a geometric factor which depends upon the geometry of all four electrodes, 
:math:`I` is the magnitude of the injection current,  and :math:`\rho` is the halfspace resistivity.

Calculating apparent resistivity
--------------------------------
Rearranging the expression above, we define *apparent resistivity* as the resistivity 
of a halfspace which produces the observed potential from a particular electrode geometry:

.. math::
		\rho_a = \frac{\Delta V}{IG}

Similarly, the apparent conductivity is

.. math::
		\sigma_a = \frac{1}{\rho_a} = \frac{IG}{\Delta V}

Apparent resistivity is equal the earth’s true resistivity *only* when 
the earth is a uniform halfspace. When the earth is more complicated, the measured 
apparent resistivity will lie between the maximum and the minimum of the true resistivities.

Visualizing data
----------------

For DC resistivity soundings, plots of the apparent resistivity versus current electrode 
separation distance are often created. For simple horizontally layered 
environments these sounding curves can to provide incite into the relative thickness and 
resistivity of layers (See Figure below).  

.. raw:: html
    :file: images/sounding_radio_buttons.html

Pseudo-sections are often used to visualize data from 2D profiles. To account for the fact 
that measurements with larger electrode separations sample deeper portions of the earth, 45 
degree angles are drawn from the mid-points of the current and potential electrode pairs and 
the datum is plotted at the intersection of these lines. In cases where a pole transmitter 
or receiver is used the 45 degree angles are drawn directly from the electrode location. 
The figure below shows how an apparent resistivity pseudo-section is built up for a simple 
dipole-dipole profile.  

.. raw:: html
    :file: images/pseudosection_radio_buttons.html

On the following :ref:`DC Resistivity: Interpretation page <dcr_interpretation>` page we show how 
these plots can be utilized to improve our understanding of the subsurface and discuss some of 
their limitations.