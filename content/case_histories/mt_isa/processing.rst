.. _mt_isa_processing:

Processing
==========

This section provides an overview of the data quality control measures and inversions completed on the Mt. Isa data sets. The DC data is first discussed. The results from those inversions are then used for IP inversions.

DCR Data
--------

The ultimate goal is to generate a 3D subsurface conductivity model. However, we first carry out 2D inversions. The three main reasons for this are:

(a) Data were collected in a 2D geometry, that is, the transmitter and receiver electrodes are along one line.

(b) The geology is principally 2D so the inversion results will provide an approximate result and/or maybe a starting model for a subsequent 3D inversion.

(c) 2D inversions are quick to perform and can reveal possible issues with data (e.g., bad data points, incorrect normalizations, etc.)

Data Quality Control
********************

As presented in the :ref:`previous<mt_isa_data>` section, the MIMDAS system collects simultaneously a pole-dipole (P-DP) and a dipole-pole (DP-P) data configuration. Accordingly, the P-DP and DP-P data were inverted separately in 2D. The uncertainties are assigned as 5% of the data amplitude with a minimum floor value of 0.02mV. The data are inverted with no noticably bad data points and with the correct normalizations (the data must be normalized by current). The figure :ref:`below <MIM_DC2D_Inv_QC>` shows the observed, predicted, and recovered models for both configurations and for each of the ten 2D lines. While smoothly varying, both the P-DP and DP-P configuration seem to agree on the general distribution of conductivities.

.. _MIM_DC2D_Inv_QC:

 .. list-table:: : Independent 2D inversions of the P-DP and DP-P DCR data
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/MIM_DC2D_Inv_QC.html
 
 

 .. figure:: images/MtIsa_Data_Merge.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_Data_Merge

    : Merge the P-DP and DP-P data configuration with their respective uncertainties

 .. figure:: images/MtIsa_DC2D_2_3DMesh.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_2D_2_3DMesh

    : Stacked 2D models recovered from 10 independent 2D inversions in 3D space.


As a final step of data quality control, the P-DP and DP-P configurations are merged (:numref:`MtIsa_Data_Merge`) and :ref:`re-inverted<MIM_DC2D_Inv_FULL>` in 2D to attempt to recover a single distribution of conductivity. In preperation for the 3D inversion, the individual 2D models are transferred onto a 3D mesh shown in :numref:`MtIsa_2D_2_3DMesh`. Since each 2D model is the result of an independent inversion, small-scale discrepancies are to be expected. We note, however, several features are recovered on all 10 lines, supporting the idea of a strongly north-south oriented "2D" earth. The two main anomalies consistent throughout the inversions are:

a) A resistive domain on the western edge of the survey, marked by a steeply dipping contact near location 11,300 m, which may correspond to the Surprise Creek Formation

b) A narrow, steeply dipping conductor near 12,300 m, adjacent to a more resistive unit, possibly the conductive Breakaway Shale within a resistive Native Bee Siltstone.

Consistent 2D inversions in good agreement with the known geology increases our confidence in the data.

.. _MIM_DC2D_Inv_FULL:

 .. list-table:: : 2D inversions of combined P-DP and DP-P DCR data
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/MIM_DC2D_Inv_FULL.html



3D Inversion
************

 .. figure:: images/MtIsa_3D_Topo.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_3D_Topo

    : Perspective view of topography and electrode locations over the 3-D domain.

In preparation for the 3D inversion of the DCR data, locations were geo-referenced in planimetry to the local grid (:numref:`MtIsa_3D_Topo`). The vertical position of the electrodes were re-assigned based on a global DEM provided by `Geoscience Australia`_ to minimize topographic effects. A model mesh was constructed to discretize the subsurface into 25 x 50 x 15 m blocks. In total, 3678 P-DP and DP-P observations were inverted. Additional smoothing in the N-S orientation was applied in order to compensate for the 500-m line spacing. The initial inversion had 21 data outside a normalized misfit of 3, meaning that those predicted data were more than three times their uncertainties away from the observed data. They were removed and the data set was re-inverted. 

Sections through the recovered 3D conductivity model are presented in :numref:`MtIsa_3D_DCModel`. This result confirms that the geology over the Cluny region is mostly 2D, with alternating regions of high and low conductivity trending north-south. Volume rendering of high conductivity (above 1 S/m) seems to indicate the geology to be steeply dipping. See the :ref:`Interpretation Section <mt_isa_interpretation>` for more details.

 .. figure:: images/MtIsa_3D_DCModel.png
    :align: center
    :figwidth: 100%
    :name: MtIsa_3D_DCModel

    : Sections through the recovered conductivity model and a volume rendered image of conductivities above 1 S/m. The topographic surface and electrode locations (white dots) are shown for reference.


.. _Geoscience Australia: http://www.ga.gov.au/metadata-gateway/metadata/record/gcat_aac46307-fce8-449d-e044-00144fdd4fa6/

IP Data
-------

Similar to the DCR data, the ultimate goal here is to generate a 3D subsurface chargeability model. Again, 2D inversions are carried out using the conductivity models that were recovered in the preceding section.

Data Quality Control
********************


As presented in the :ref:`previous<mt_isa_data>` section, the MIMDAS system collects simultaneously a pole-dipole (P-DP) and a dipole-pole (DP-P) data configuration. Accordingly, the P-DP and DP-P data were inverted separately in 2D. The uncertainties are assigned as 5% of the data amplitude with a minimum floor value of 2V. The data are inverted, but the inversions struggled to reproduce the observed anomalies. The :ref:`desired data misfit <inversion>` was increased by four times. The data were re-inverted and the figure :ref:`below <MIM_IP2D_Inv_QC>` shows the observed, predicted, and recovered models for both configurations and for each of the ten 2D lines. The increase of the desired misfit allowed more :ref:`model regularization <inversion>` to produce a smoothly varying model with both the P-DP and DP-P configurations agreeing on the general distribution of chargeabilities.


.. _MIM_IP2D_Inv_QC:

 .. list-table:: : Independent 2D inversions of the P-DP and DP-P IP data
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/MIM_IP2D_Inv_LR.html


 .. figure:: images/MtIsa_IP2D_2_3DMesh.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_IP2D_2_3DMesh

    : Stacked 2-D models recovered from 10 independant 2-D inversions.


As a final step of data quality control, the P-DP and DP-P configurations are re-merged and :ref:`re-inverted<MIM_DC2D_Inv_FULL>` in 2D to attempt to recover a single subsurface distribution of chargeability. In preparation for the 3D inversion, the individual 2D models are transferred onto a 3D mesh shown in :numref:`MtIsa_IP2D_2_3DMesh`. Since each 2D model is the result of an independent inversion, small-scale discrepancies are to be expected. We note, however, the sections are quite varying from line to line. 


.. _MIM_IP2D_Inv_FULL:

 .. list-table:: : 2D inversions of merged P-DP and DP-P IP data
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/MIM_IP2D_Inv_FULL.html



3D Inversion
************

In preparation for the 3D inversion of the IP data, locations were geo-referenced in planimetry to the local grid (:numref:`MtIsa_3D_Topo`). The vertical position of the electrodes were re-assigned based on a global DEM provided by `Geoscience Australia`_ to minimize topographic effects.The model mesh constructed for the 3D DCR inversion were used as well as the 3D recovered conductivity model. In total, 3678 P-DP and DP-P observations were inverted. Additional smoothing in the N-S orientation was applied in order to compensate for the 500-m line spacing. The desired data misfit was set to four times the number of data as with the 2D inversions. Sections through the recovered 3D chargeability model are presented in :numref:`MtIsa_3D_IPModel`. 


 .. figure:: images/MtIsa_3D_IPModel.png
    :align: center
    :figwidth: 100%
    :name: MtIsa_3D_IPModel

    : Sections throughout the recovered chargeability model with a 3D volume rendered image of chargeabilities higher than 40msec. The topography surface and electrode locations (white dots) are shown for reference.

