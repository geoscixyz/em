.. _hoop_region_norway_index:

Predicting Resevoir Properties using CSEM, Pre-Stack Seismic and Well Log Data
==============================================================================

.. .. raw:: html
..     :file: ../../../underconstruction.html

.. - **Authors**: :ref:``
.. - **Reviewer**: :ref:``

.. topic :: Prelude

**Include link to paper(s)**
 

We present an example from the Hoop area of the Barents Sea showing a sequential quantitative integration approach to integrate seismic and CSEM attributes using a rock physics framework.  The example  illustrates a workflow to address the challenges of multi-physics and multi-scale data integration for reservoir characterization purposes.

A dataset consisting of 2D GeoStreamer® seismic and towed streamer electromagnetic data that were acquired concurrently in 2015 by PGS provide the surface geophysical measurements used in this study. Two wells in the area: Wisting Central (7324/8-1) and Wisting Alternative (7324/7-1S) provide calibration for the rock physics modeling and the quantitative integrated analysis.


In the first stage of the analysis, we invert pre-stack seismic and CSEM data separately for impedance and anisotropic resistivity respectively.  We then apply the the multi-attribute rotation scheme (MARS) to estimate rock properties from seismic data. This analysis verified that the seismic data alone cannot distinguish between commercial and non-commercial hydrocarbon saturation.  Therefore in the final stage of the analysis we invert the seismic and CSEM derived properties within a rock physics framework. The inclusion of the CSEM-derived resistivity information within the inversion approach allows for the separation of these two possible scenarios. Result show excellent correlation with known well outcomes. The integration of seismic, CSEM, and well data predicts very high hydrocarbon saturations at Wisting Central, and no significant saturation at Wisting Alternative, consistent with the findings of each well. Two further wells were drilled in the area and used as blind tests in this case:  The slightly lower saturation predicted at Hanssen (7324/7-2) is related to 3D effects in the CSEM data, but the positive outcome of the well is correctly predicted. At Bjaaland (7324/8-2), although the seismic indications are good, the integrated interpretation result predicts correctly that this well was unsuccessful. 


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    PARAPHRASE: DEVIN
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


    
.. figure:: images/survey_schematic.png
    :align: right
    :figwidth: 50%
    :name: fig_survey_schematic

    Schematic showing towed CSEM and seismic instruments over the Hoop Fault Complex, Barents Sea, Norway.
    

The accurate characterization of oil and gas reservoirs represents a primary goal for petroleum geologists, geophysicists and engineers.
Ultimately, we are interested in the dimensions, porosity, fluid saturation and lithology of the reservoir. 
Here, we present a case study which uses controlled source electromagnetic (CSEM), 2D seismic, and well-log data to obtain reservoir properties within the Hoop Fault Complex, Barents Sea, Norway. Survey data were collected in 2015 by `Petroleum Geo-Services (PGS) <https://www.pgs.com>`__ and the supporting literature was provided by `Solid Rock Images <http://www.rocksolidimages.com>`__ .


Over the last hundred years, technology and innovation have lead to the progressive use of 2D seismic (early 1920s), gravity, 3D seismic (late 1960s) and CSEM (early 2000s) methods as well as AVO analysis to characterize petroleum reservoirs. Recently developed approaches, which are more sophisticated and robust, work by integrating attributes of pre-stack seismic inversion and CSEM inversion within a rock physics framework. These approaches have been successful, in part, because 2D seismic and CSEM data provide both independent and complementary subsurface physical property models which can be validated by well log measurements.


Despite its advantages, the integration of CSEM and seismic data has its challenges. First, electric and elastic properties must be coupled through a single earth model that quantifies both accurately and consistently. Secondly, the sensitivity of the data to the properties for each geophysical method must be adequately balanced. Finally, seismic, CSEM and well log data sample the earth at very different scales. This must be reconciled when applying an integrated interpretation.



    - Something about how challenges arise when attempting to combine these data.
    - What is this paper all about
    - Something about how this case study fixes the problem. 
    - Finish by expressing how we were successful and what we were able to accomplish.





The inversion of CSEM data provides electromagnetic impedance and anisotropic resistvity models. Whereas the inversion of seismic data provides a structural framework and, through the use of the multi-attribute rotation scheme (MARS), can be used to estimate rock properties.


Seismic provides the structural framework and, from AVO information, the possibility to derive P-wave and S-wave impedance volumes; which can be linked to porosity, lithology, geomechanical properties and conditionally to fluid saturation prediction. CSEM data provide a lower resolution measure of resistivity. 

hen constrained with the structural framework and seismically derived volumes of porosity and lithology, can be linked to fluid saturation, overcoming seismic ambiguity related to similar AVO responses in both low- and high-saturated hydrocarbon reservoirs.




    
.. figure:: images/inversion_workflow.png
    :align: right
    :figwidth: 75%
    :name: fig_inversion_workflow

    Work-flow for quantitative interpretation of well log, seismic and CSEM data and inversions.
    






**Content**


.. toctree::
    :maxdepth: 1

    setup
    properties
    survey
    data
    processing
    interpretation
    synthesis
..    lessons
