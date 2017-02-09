.. _sagd_processing:

Processing
==========

One way to better gauge how well the survey detects the growing steam chambers i by calculating the relative difference between each time step. The relative difference is computed as following: 

.. math:: RD = \left| \frac{F^2 - F^1}{F^1} \right| * 100,

where :math:`F^1` and :math:`F^2` are the data from an early and later time step, respectively. If we compare the background model and the middle time step, the relative differences is 78% using the eastern transmitter and 51% using the northern transmitter. This indicates that the survey is sensitive to the resistivity change, and hence detects the steam chamber. These values also suggest that the eastern transmitter has a greater sensitivity to the reservoir than the northern transmitter. This difference stems from how the transmitters couple differently with the target and emphasizes the importance of using multiple transmitters (i.e., subsurface excitations) if possible.

To further understand the data and what changes happen within the reservoir, the data need to be :ref:`inverted in 3D <inversion>`. Uncertainties are assigned as a percentage of the data plus a noise floor. For each inversion, a background 1D model was used as the initial and reference model. Resistivity changes are limited to the reservoir between elevations of 263 and 318 m. 

Because the steam is expected to decrease the resistivity, the resistivities in the recovered model were limited to be no higher than 147 :math:`\Omega` m, which was the resistivity of the McMurray Formation. In addition, the orientation of the horizontal well pairs are well known, so we impose increased model smoothness in that direction by changing :math:`\alpha_y` from 1 to 10. 

The data from the earliest time step was inverted first and its recovered model was used to start the inversion for the second time step. This second model was then used as the initial model for the final time step. This “cascading” inversion method reduces computation time by providing the inversion with a model that is assumed to better fit the data than the 1D background model.

The models are shown and interpreted on the :ref:`next page <sagd_interpretation>`.

