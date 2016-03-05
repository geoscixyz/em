.. _bookpurnong_interpretation:

Interpretation
==============

Interpretation is the process that extracts information in the data to make decisions or to derive geologic knowledge. Depending on the specific geologic questions asked, and the resources available, geophysicists can choose from a wide spectrum of approaches ranging from trivial and low-resolution to sophisticated and high-resolution. The following is a list of commonly available options for the interpretation of loop-loop EM data.

(1) Qualitative assessment of data. In some cases, the data itself showing highs and lows can reveal the distribution of the relative physical property. Sometimes simple data transform techniques can also be used to isolate the anomaly and aid the interpretation. This type of approach can include: direct data plotting, conductivity meter (link to EM31 and the data-conductivity transform), empirical template method, etc. Qualitative approach was once the mainstream, but has shown drawbacks in complex geological setting and lacks the ability to decode the conductivity values from the data. However, it still has its value in data quality control and preliminary interpretation.

(2) Time constant (decay constant) analysis. For a time domain system, the voltage measured off time at the receiver is roughly an exponentially decaying function of time. The decay rate is an indicator of the overall conductivity of the ground: good conductors have slower decays (greater time constant) and poor conductors have faster decays (smaller time constant). Time constant method offers a first-order interpretation of the overall conductivity of the ground. Link to time constant page.

(3) Apparent conductivity and conductivity-depth imaging/transform (CDI or CDT). Apparent conductivity is another semi-qualitative method that further ties the data to the conductivity of the ground. It is defined as the conductivity of a uniform half-space that would generate the same data at a particular time or frequency. Apparent conductivities at different times or frequencies can be assigned to corresponding depths using diffusion depth or skin depth. Along a survey line, this would give a CDI image of conductivity on a cross section. It can be considered as a lumping averaging of the conductivities around the measurement location. So again, apparent conductivity method may not work well if the conductivity varies laterally (2D or 3D earth). Link to apparent conductivity page.

(4) Plate modeling. Some geologic targets can be characterized as conductive thin plates that give rise complicated EM responses due to the geometry and mutual coupling (Link to 3-loop). Plate modeling method attempts to find the geometry and conductivity of a few conducting plate in a uniform hackground that is responsible for most of the anomalous data. It has the advantages of being able to handle the 3D coupling effect efficiently, but may have trouble dealing with too many plates in more complex situations. Link to plate modeling page.

(5) 1D layered earth model inversion. This approach assume the earth's codnuctivity only varies as a function of depth. At each measurement location, the inversion find a layered model that explains the entire decay curve in time or the entire spectrum in frequency-domain. Many layered models at multiple locations then can be stitched together to form a pseudo-3D volume for visualization. Advanced techniques also consider the correlation between adjacent locations by imposing lateral constraints, etc. Link to 1D inversion page.

(6) Full 3D inversion. The previous interpreting methods all assume the earth has a particular structure so simplified calculations can be used. Any violation of those assumptions would result in failures. A 3D inversion discretizes the entire earth to many discrete cells, each of which has a constant conductivity. Then the Maxwell's equations are solved on the mesh. The obtained images of the subsurface are in 3D voxel format. 3D inversions provides the best resolution and works for any complicated models, but it is more computational expensive. Link to 3D inversion page.

The geology at Bookpurnong is mostly flat strata of floodplain. Therefore, an 1D inversion would be the most cost-effective solution for the data interpretation. In the following, we will go through the 1D inversion of the three data sets. 


1D inversion of RESOLVE data
----------------------------

.. figure:: ./images/booky-resolvefit.jpg
    :align: left
    :scale: 80% 
    :name: booky-resolvefit

.. figure:: ./images/booky-resolvemodel1.jpg
    :align: left
    :scale: 80% 
    :name: booky-resolvemodel1
    
.. figure:: ./images/booky-resolvemodel2.jpg
    :align: left
    :scale: 80% 
    :name: booky-resolvemodel2
    
 

1D inversion of SkyTEM(HM) data
-------------------------------

.. figure:: ./images/booky-skytemfit.jpg
    :align: left
    :scale: 80% 
    :name: booky-skytemfit

.. figure:: ./images/booky-skytemmodel1.jpg
    :align: left
    :scale: 80% 
    :name: booky-skytemmodel1
    
.. figure:: ./images/booky-skytemmodel2.jpg
    :align: left
    :scale: 80% 
    :name: booky-skytemmodel2
    

1D inversion of SkyTEM(LM) data
-------------------------------

TBD

