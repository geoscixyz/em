.. _tkc_data:

.. figure:: images/TKC_7Steps_Data.png
    :align: right
    :figwidth: 30%

Data
====

This section reviews the data that was graciously provided by `Peregrine
Diamonds Ltd`_. We review the units, normalization and observations that can
be made by simple visual inspection of the data. Important to note that
*survey reports* were missing for few data sets. Some of the technical
information had to be infered from different surveys acquired during the same
period.


.. _Peregrine Diamonds Ltd: https://www.pdiam.com/projects/peregrine-exploration


.. _tkc_data_grav:

Gravity
-------

.. figure:: images/Data_Grav.png
    :align: right
    :figwidth: 50%
    :name: fig_Data_Grav

    Observed ground gravity data. Observation locations are denoted by white
    dots.

Two ground gravity surveys were provided, measuring the vertical gravity field
(:math:`g_z`) in mGal. The surveys were initially not reference to the same
coordinate system and no correction had been done to compensate for the
different instrumental level.  Leveling was done in post- processing by
:cite:`Jansen2004`, and supplied to us as *Bouguer corrected* (2.67 g/cc)
data.

Three main features are observed in the gravity data:

- Low gravity anomalies over DO-27 and DO-18
- Low gravity anomaly connecting the two kimberlite pipes.

Initial interpretation of the gravity data supported the idea of both pipes
being connected at depth.


.. _tkc_data_mag:

Magnetics
---------

.. .. figure:: images/Data_Mag.png


..     :align: right
..     :figwidth: 50%
..     :name: fig_Data_Mag

..     The subsets of the observed magnetic data from the (a) DIGHEM, (b)
..     AeroTEM, and (c) VTEM surveys over the TKC kimberlite complex.

.. raw:: html
	:file: ./images/Data_Mag.html


We review the magnetic data acquired along side the :ref:`DIGHEM<survey_DIGHEM>`, :ref:`AeroTEM II<survey_AeroTEM>` and
:ref:`VTEM<survey_VTEM>` surveys. All three systems are equipped with a cesium vapour magnetometer,
recording Total Field Intensity (TMI) magnetic data in *nT* as shown below. Differences in TMI levels
can be attributed to changes in the inducing field and variable flight heights.

Two main features are observed on all three datasets:

- A positive anomaly over DO-27 and DO-18
- A negative anomaly on the north-eastern flank of DO-27

From the larger footprint of the DIGHEM survey, we can also identify two
larger magnetic trends. The narrow magnetic anomaly strikes :math:`315^\circ`
N, found throughout the Lac de Gras region, corresponds to the Mackenzie dyke
swarm  :cite:`Buchan2009`. A weaker but still distinguishable narrow anomaly
appears to be striking at :math:`45^\circ` N. This feature may be part of the
MacKey dyke swarm.


+------------------------------+-----------+--------+-----------+
| **System**                   | **DIGHEM**|**VTEM**|**AeroTEM**|
+------------------------------+-----------+--------+-----------+
| Number of data               | 6274      | 26334  |  22561    |
+------------------------------+-----------+--------+-----------+
| Field strength (nT)          | 59500     | 59580  | 59500     |
+------------------------------+-----------+--------+-----------+
| Inclination (:math:`^\circ`) | 83.0      | 83.3   |  83.0     |
+------------------------------+-----------+--------+-----------+
| Declination (:math:`^\circ`) | 21.0      | 19.5   | 20.0      |
+------------------------------+-----------+--------+-----------+


.. _tkc_data_FEM:

Frequency-Domain EM
-------------------

The DIGHEM system coil configuration allows to collect the vertical (z) and in-
line (x) components of the magnetic field in the frequency domain. A bucking coil
is used to cancel the primary signal from the transmitter loop. The receiver
records the in-phase and quadrature components secondary field in *parts-per-
million* (ppm) of the primary field :math:`B_{P}` such that:

:math:`B_{ppm} = B / B_{P} * 10^6`

From the data provided, the quadrature data of the in-line data (x) were
missing. Hence only the vertical co-planar data were used in this study.

.. raw:: html
	:file: ./images/Data_DIGHEM_InPhase.html

.. raw:: html
	:file: ./images/Data_DIGHEM_Quadrature.html

FEM data are often interpreted by simple visual inspection of each
frequencies. From the :ref:`skin
depth<harmonic_planewaves_homogeneous_skindepth_formula_quasi>` approximation,
the highest frequencies can be used to delineate near-surface conductors
whereas deeper structures can potentially be detected at the lower
frequencies. As observed on the 56,000 Hz channel, both DO-18 and DO-27 give
rise to a strong quadrature component. The quadrature component correlates
well with the hydrography, agreeing with a shallow response from the lake
bottom sediments and glacial till layer. Two elongated and narrow negative
anomalies appears in the in-phase maps of the 900 Hz and 7,200 Hz. These
features are associated with intrusive dyke swarms known to be strong magnetic
susceptibility anomalies. The quadrature component of both frequencies also
highlight well the location of two pipes.


.. _tkc_data_TEM:

Time-Domain EM
--------------
The AeroTEM transmitter waveform
(Figure 2) is a triangular current pulse of 1150  microseconds duration
operating at a base frequency of 150 Hz. The transmitter loop consists of 8
turns of copper wire, 5 m in diameter, with a maximum current  of 250 A that
produces a peak moment of 40,000 Am2.

.. raw:: html
	:file: ./images/Data_AeroTEM.html

VTEM survey

.. raw:: html
    :file: ./images/Data_VTEM.html
