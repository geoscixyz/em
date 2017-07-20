.. _tkc_processing:

.. figure:: images/TKC_7Steps_Processing.png
    :align: right
    :figwidth: 30%


Processing
==========

This section provides an overview of the data quality control and inversion
procedure of the geophysical data.

Gravity
-------

In preparation for the inversion, the following processing steps were taken
on the ground gravity data:

- Since elevation information were only provided for the southern survey, the vertical position of the gravity stations were assigned from the topography model.

- The Bouguer corrected hovered around 1800 mGal, from which we subtracted a regional field of 1803.163 mGal.

:numref:`fig_Processing_Grav` compares the gravity data before and after
leveling. The processed data shows a substantial negative density contrast in
the area of the two pipes and a smaller negative contrast between them.

.. figure:: images/Processing_Grav.png
    :align: center
    :figwidth: 75%
    :name: fig_Processing_Grav

Data were then inverted with the UBC-`GRAV3D`_ inversion software. Uncertainty
of 0.045 mGal were assigned to the gravity data Inversion parameters for the
mesh and regularization are presented below.

+--------------------------------------------------------------+-----------------+
| Number of cells                                              | 105 x 114 x 49  |
+--------------------------------------------------------------+-----------------+
| Core cell size                                               | 20 x 20 x 20    |
+--------------------------------------------------------------+-----------------+
| Regularization :math:`[\alpha_s,\alpha_y,\alpha_x,\alpha_z]` | 1e-4, 1, 1, 1   |
+--------------------------------------------------------------+-----------------+
| Target chi factor (:math:`\phi_d^*`)                         | 1.0             |
+--------------------------------------------------------------+-----------------+


Sections through the recovered density model are presented in
:numref:`fig_Processing_Inv_Grav`. We note a two density lows near at the
location of the kimberlite pipes and extending at depth. A continuous density
low is also observed between the two pipes but appears to be limited to
roughly 75 m below topography.

.. figure:: images/gravFinalCrop.png
    :align: center
    :figwidth: 50%
    :name: fig_Processing_Inv_Grav


.. _GRAV3D: http://grav3d.readthedocs.io/en/latest/

Magnetics
---------

.. figure:: images/Processing_Mag.png
    :align: right
    :figwidth: 50%
    :name: fig_Processing_Mag

We have three magnetic datasets collected with different instruments and at
different times. Before inverting the data, we first proceeded with the
following leveling steps:

- Data extent from the VTEM and DIGHEM surveys was reduced to the extent of
  the AeroTEM survey.

- We subtracted a constant from the DIGHEM and VTEM magnetic data such that
  the values away from the main anomalies were zero. The removal of a DC
  component was preferred over a polynomial fit because the latter can remove

- In case of the AeroTEM magnetic data, it was noticed that each individual
  line had a varying DC shift. By comparing data points that have similar
  locations to those of the VTEM magnetic data, we were able to level each line
  in the AeroTEM magnetic data separately.

:numref:`fig_Processing_Mag` compares each datasets before and after leveling.
The peak magnetic anomalies measured over DO-27 are consistent across surveys.
The signal from both DO-27 and DO-18 are now visible on the AeroTEM data set.

Data sets were combined and inverted with the UBC-`MAG3D`_ inversion software.
We use the same mesh as for the density inversion. Sections through the
recovered density model are presented in :numref:`fig_Processing_InvInd_Mag`.
We note that the largest susceptibilities are concentrated on the outer edge
of DO-27. Moderate to low susceptibilities are recovered exactly at the center
of DO-18 and at depth.

.. figure:: images/vtemIndCrop.png
    :align: center
    :figwidth: 50%
    :name: fig_Processing_InvInd_Mag

.. _MAG3D: http://mag3d.readthedocs.io/en/latest/

