.. _norseminde_processing:

Processing
==========

After data collection the raw data was processed in the Aarhus Workbench to remove noise.  Coupled data arising from man-made installations such as buildings, power lines, cables, roads and railroads was also removed. :numref:`fignoise_processing` shows the data before (:numref:`fignoise_processing` a) and after removal of data affected by noise and couplings (:numref:`fignoise_processing` b).

.. figure:: images/fig_noiseprocessing.png
    :align: center
    :figwidth: 100%
    :name: fignoise_processing

    Data soundings (a) before removal of data affected by noise and couplings and (b) after culling the coupled and noisy data.


.. figure:: images/fig_soundingcurve.png
    :align: right
    :figwidth: 50%
    :name: figcurve_processing

The average flight speed of the entire survey was approximately 100 km/h or 28 metres per second. The average flight height for the transmitter frame was 30 metres above ground level. Typically, a repetition frequency of one full measure¬ment every half second is used, thus, with a flight speed of 28 metres per second the lateral distance between the raw data sets is approx¬imately 14 metres. Raw data is stacked during processing to enhance the signal-to-noise relationship, and in reality the resolution is 25-50 metres horizontally and less than a few metres vertically. :numref:`figcurve_processing` shows a db/dt sounding curve from the survey with LM and HM curves. The circles indicate the times that are actually used for interpretation of the data. 

After initial processing, the data is interpreted using an interpretation algorithm implemented in the Aarhus Workbench software yielding a quasi 3D model of the resistivity of the subsurface down to 100 metres below ground level. Subsequently the geophysical models are presented as average resistivity maps at various elevation or depth intervals (:numref:`figresistivity_processing`) or in profiles (:numref:`figprofile_processing`).

.. figure:: images/fig_thumbnail.png
    :align: center
    :figwidth: 70%
    :name: figresistivity_processing

    The mid resistivity map for a depth of 15-20 metres. The position of the profile in :numref:`figprofile_processing` is marked in a black line. The map also shows the contours, in many places with a direct correlation with the geology. 


.. figure:: images/fig_profile.png
    :align: center
    :figwidth: 100%
    :name: figprofile_processing

    Resistivity profiles. (a) Profile along line in :numref:`figresistivity_processing`. (b) and (c) are zoomed in profiles from (a).
