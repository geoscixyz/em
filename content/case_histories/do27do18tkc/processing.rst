.. _tkc_processing:

.. figure:: images/TKC_7Steps_Processing.png
    :align: right
    :figwidth: 30%


Processing
==========

This section provides an overview of the data quality control

Gravity
-------

\plot{gravFinalCrop}{width=\columnwidth}{The recovered density contrast model from the inversion of the ground gravity data. A plan-view depth slice of the model at an elevation of 330 m (approximately 100 m below topography) is shown on the left. Cross-sections through DO-27 (right, bottom) and DO-18 (right, top) are also given to show both kimberlite pipes.}

The gravity data hover around 1800 mGal, from which we subtracted a
regional field of 1803.163 mGal.

.. figure:: images/Processing_Grav.png
    :align: center
    :figwidth: 100%
    :name: fig_Processing_Grav

We assign an uncertainty of 0.045 mGal to the gravity data, and invert the
data using the same mesh that was used to recover susceptibility. The results,
presented in :numref:`fig_Processing_Grav` (b), have a substantial negative
density contrast in the area of the two pipes and a smaller negative contrast
between them.

Two major challenges were faced in using the ground gravity data. The first
problem was the missing elevation over DO-18 and the assumptions that were
required to calculate that information. The second drawback became evident
when comparing the data to the gradiometry data. The center of the DO-18
anomaly differed by approximately 100 m (two ground survey lines) between the
two data sets suggesting that the two ground surveys may not have been
stitched together accurately. Therefore, we have more confidence in the
accuracy of the gradiometry data.


Data Quality Control
********************

As presented in



3D Inversion
************


The 3D model can be


Magnetic Data
-------------

.. figure:: images/Processing_Mag.png
    :align: right
    :figwidth: 50%
    :name: fig_Processing_Mag

Any non-zero background may result in
extra material (i.e., artifacts) in the recovered susceptibility model from
inversion. We subtracted a constant from the DIGHEM and VTEM magnetic data
such that the values away from the main anomalies were zero. The removal of a
DC component was preferred over a polynomial fit because the latter can remove
part of the kimberlite signal. The resulting leveled data are shown in
:numref:`fig_Processing_Mag` (d) and (f) respectively. In case of the AeroTEM magnetic
data, it was noticed that each individual line had a varying DC shift. By
comparing data points that have similar locations to those of the VTEM
magnetic data, we were able to level each line in the AeroTEM magnetic data
separately. The processed AeroTEM magnetic data is presented in
:numref:`fig_Processing_Mag` (e).
