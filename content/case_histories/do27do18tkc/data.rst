.. _tkc_data:

Data
====

.. _tkc_data_grav:

Gravity
-------

Three main features are observed in the gravity data (:numref:`fig_Data_Grav` (a)): low gravity anomalies over DO-27 and DO-18, and also a
low gravity anomaly connecting the two kimberlite pipes. The gravity data
hover around 1800 mGal, from which we subtracted a regional field of 1803.163
mGal.  We assign an uncertainty of 0.045 mGal to
the gravity data, and invert the data using the same mesh that was used to
recover susceptibility. The results, presented in :numref:`fig_Data_Grav` (b), have a substantial negative density contrast in the
area of the two pipes and a smaller negative contrast between them.

.. figure:: images/gravData.png
    :align: center
    :figwidth: 100%
    :name: fig_Data_Grav

    Observed (a) raw and (b) processed ground gravity data after removal of DC
    shift. Observation locations are denoted by white dots.


.. _tkc_data_mag:

Magnetics
---------

.. figure:: images/magData.png
    :align: right
    :figwidth: 50%
    :name: fig_Data_Mag

    The subsets of the observed magnetic data from the (a) DIGHEM, (b)
    AeroTEM, and (c) VTEM surveys over the TKC kimberlite complex. The
    respective leveled magnetic data that were inverted are shown in (d), (e),
    and (f).

The DO-27 anomaly to the south and its northern smaller partner DO-18, are
clearly visible in all three data sets (:numref:`fig_Data_Mag` (a-c)). However,
each data set has a regional trend. Any non-zero background may result in
extra material (i.e., artifacts) in the recovered susceptibility model from
inversion. We subtracted a constant from the DIGHEM and VTEM magnetic data
such that the values away from the main anomalies were zero. The removal of a
DC component was preferred over a polynomial fit because the latter can remove
part of the kimberlite signal. The resulting leveled data are shown in
:numref:`fig_Data_Mag` (d) and (f) respectively. In case of the AeroTEM magnetic
data, it was noticed that each individual line had a varying DC shift. By
comparing data points that have similar locations to those of the VTEM
magnetic data, we were able to level each line in the AeroTEM magnetic data
separately. The processed AeroTEM magnetic data is presented in
:numref:`fig_Data_Mag` (e).



.. _tkc_data_FEM:

Frequency-Domain EM
-------------------

The data were first converted from their native coordinate
systems to NAD27 for consistency. In our investigation, only a subset of the
DIGHEM and VTEM datasets that cover the area of interest was used since the
datasets span a large spatial area.

.. _tkc_data_TEM:

Time-Domain EM
--------------
The AeroTEM transmitter waveform
(Figure 2) is a triangular current pulse of 1150  microseconds duration
operating at a base frequency of 150 Hz. The transmitter loop consists of 8
turns of copper wire, 5 m in diameter, with a maximum current  of 250 A that
produces a peak moment of 40,000 Am2.
