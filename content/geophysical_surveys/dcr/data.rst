.. _dcr_data:

Data
====

.. topic:: Purpose 

   To show how measured voltages are converted to apparent resistivity and plotted as a sounding curve or as a pseudo-section. 

A general DC resistivity survey setup is outlined in (:numref:`dcr_Schlumberger_array`). A current generator is attached to the :math:`A`, (positive) and :math:`B` (negative)electrodes and a current of magnitude :math:`I` is injected. M and N are the potential electrodes. The nominclature for referring to the distance between any two electrodes is denoted by r with appropriate subscripts. The electrodes can be deployed anywhere on the surface, or inside, the earth and they do not have to be co-linear. 

.. figure:: ./images/DCR_Gradient-Schlumberger_Array.svg
	:name: dcr_Schlumberger_array
	:align: right
	:figwidth: 50%

	The measured voltages constitute the data. Distances between the electrodes are used to calculate the geometry factor and apparent resistivity discussed below.	

Measured potential differences
------------------------------
The flow of currents in the ground causes charges to be built up on  interfaces between regions of differing conductivity. 
These charges contribute to the measured potential difference. 

In a uniform halfspace, the measured potential 
difference is given by the following expression:

.. math::
	\Delta V &= V_M - V_N \textrm{, with} \\[0.8em]
	V_M &= \frac{I \rho}{2 \pi} \left \{ \frac{1}{r_{AM}}  -  \frac{1}{r_{BM}} \right \} \textrm{ and}  \\[0.8em]
	V_N &= \frac{I \rho}{2 \pi} \left \{ \frac{1}{r_{AN}}  -  \frac{1}{r_{BN}} \right \} \textrm{, so} \\[0.8em]
	\Delta V &= \frac{I \rho}{2 \pi} \left \{ \frac{1}{r_{AM}} - \frac{1}{r_{BM}} - \frac{1}{r_{AN}} + \frac{1}{r_{BN}} \right \}\\[0.8em]
	\Delta V &=I \rho G

where :math:`G` is a geometric factor which depends upon the geometry of all four electrodes, 
:math:`I` is the magnitude of the injection current,  and :math:`\rho` is the halfspace resistivity.

.. _dcr_apparent_res:

Calculating apparent resistivity
--------------------------------
The measured voltages are numbers that can vary greatly in amplitude and they provide no direct insight about the structures at depth. As shown above, the potential difference is primarily dependent upon the geometry of the electrodes. By rearranging that formula we can recover the true resistivity

.. math::
		\rho = \frac{\Delta V}{IG}

When the earth is a halfspace any DCR datum is sufficient to evaluate the halfspace resistivity. 
For field data, it is still useful to eliminate the geometrical factor and define

.. math::
		\rho_a = \frac{\Delta V}{IG}

We refer :math:`\rho_a` as the *apparent resistivity* and it is understood to be the resistivity of a halfspace which produces the observed potential measured by a particular electrode geometry. Apparent resistivity is equal the earth’s true resistivity *only* when 
the earth is a uniform halfspace. When the earth is more complicated, the measured 
apparent resistivity will lie between the maximum and the minimum of the true resistivities. This conversion is extremely valuable for plotting data and making first pass assessments about the subsurface. If apparent conductivity is preferred,  

.. math::
		\sigma_a = \frac{1}{\rho_a} = \frac{IG}{\Delta V}


Visualizing data
----------------

.. _dcr_sounding:

Sounding
********

For DC resistivity soundings, plots of the apparent resistivity versus current electrode 
separation distance are often created. For simple horizontally layered 
environments these sounding curves can provide insight into the relative thickness and 
resistivity of layers (See Table below).  

 .. list-table:: : DC resistivity sounding curve
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: images/sounding_radio_buttons.html


.. _dcr_Pseudo_section:

Pseudo-section
**************
Pseudo-sections are often used to visualize data from 2D profiles. To account for the fact 
that measurements with larger electrode separations sample deeper portions of the earth, lines at :math:`45^\circ` 
degree angles are drawn from the mid-points of the current and potential electrode pairs and 
the datum is plotted at the intersection of these lines. In cases where a pole transmitter 
or receiver is used the 45 lines are drawn directly from the electrode location. 
The figure below shows how an apparent resistivity pseudo-section is built up for a simple 
dipole-dipole profile. 

 .. list-table:: : Apparent resistivity pseudo-section
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: images/pseudosection_radio_buttons.html

On the following :ref:`DC Resistivity: Interpretation page <dcr_interpretation>` page we show how 
these plots can be utilized to improve our understanding of the subsurface and discuss some of 
their limitations.