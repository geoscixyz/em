.. _hoop_region_norway_index:


.. |Res| unicode:: 0xAE
   :ltrim:

Reservoir properties prediction using CSEM, pre-stack seismic and well log data: Case Study in the Hoop Area, Barents Sea, Norway
=================================================================================================================================


- **Authors**: :ref:`palvarez`, :ref:`aalvarez`, :ref:`lmacgregor`, :ref:`fbolivar`, :ref:`rkeirstead` and :ref:`tmartin`
- **Reviewer**: :ref:`dccowan`

.. topic :: Prelude

    This case history has been taken from the paper `"Predicting resevoir properties using CSEM, pre-stack seismic and well log data: case study in Hoop area, Barents Sea, Norway" <http://www.rocksolidimages.com/pdf/2016_Case_Study_Multiphysics.pdf>`__ , which was supplied by `Rock Solid Images <http://www.rocksolidimages.com>`__ . Survey data were collected by `Petroleum Geo-Services (PGS) <https://www.pgs.com>`__ in 2015.

**Abstract**

We present an example from the Hoop area of the Barents Sea showing a sequential quantitative integration approach to integrate seismic and CSEM attributes using a rock physics framework.  The example  illustrates a workflow to address the challenges of multi-physics and multi-scale data integration for reservoir characterization purposes.


.. figure:: images/survey_schematic.png
    :align: right
    :figwidth: 50%
    :name: fig_survey_schematic_title

    Schematic showing towed CSEM and seismic instruments over the Hoop region, Barents Sea, Norway.
    

A dataset consisting of 2D GeoStreamer |Res| seismic and towed streamer electromagnetic data that were acquired concurrently in 2015 by PGS provide the surface geophysical measurements used in this study. Two wells in the area: Wisting Central (7324/8-1) and Wisting Alternative (7324/7-1S) provide calibration for the rock physics modeling and the quantitative integrated analysis.


In the first stage of the analysis, we invert pre-stack seismic and CSEM data separately for impedance and anisotropic resistivity respectively.  We then apply the the multi-attribute rotation scheme (MARS) to estimate rock properties from seismic data. This analysis verified that the seismic data alone cannot distinguish between commercial and non-commercial hydrocarbon saturation.  Therefore in the final stage of the analysis we invert the seismic and CSEM derived properties within a rock physics framework. The inclusion of the CSEM-derived resistivity information within the inversion approach allows for the separation of these two possible scenarios. Result show excellent correlation with known well outcomes. The integration of seismic, CSEM, and well data predicts very high hydrocarbon saturations at Wisting Central, and no significant saturation at Wisting Alternative, consistent with the findings of each well. Two further wells were drilled in the area and used as blind tests in this case:  The slightly lower saturation predicted at Hanssen (7324/7-2) is related to 3D effects in the CSEM data, but the positive outcome of the well is correctly predicted. At Bjaaland (7324/8-2), although the seismic indications are good, the integrated interpretation result predicts correctly that this well was unsuccessful. 





    
.. figure:: images/inversion_workflow.png
    :align: center
    :figwidth: 100%
    :name: fig_inversion_workflow_title

    Workflow for quantitative interpretation of well log, seismic and CSEM data and inversions.
    



**Content**


.. toctree::
    :maxdepth: 1

    setup
    properties
    surveydata
    processinginterpretation
    synthesis
..    lessons
