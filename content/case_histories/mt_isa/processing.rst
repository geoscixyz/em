.. _mt_isa_processing:

Processing
==========

This section provides an overview of the data quality control, 2-D and 3-D
inversion completed on the Mt. Isa-DCR data set.

DCR Data
--------

Although our ultimate goal is to generate a 3-D conductivity model there are
multiple reasons for first carrying out 2-D inversions:

(a) Data were collected in a 2D geometry, that is, the transmitter and
(receiver electrodes are along one line.

(b) The geology is principally 2D so the inversion results will provide an
(approximate result and/or maybe a starting model for a subsequent 3D
(inversion.

(c) 2D inversions are quick to implement and can reveal possible issues with
(i.e. bad data points, incorrect normalizations, etc.)

Data Quality Control
********************

As presented in the :ref:`previous<mt_isa_data>` section, the MIMDAS system
collects simultaneously a pole-dipole (P-DP) and a dipole-pole (DP-P) data
configuration.   were adjusted accordingly in order to get an equivalent
response from both configurations. The P-DP and DP-P data were inverted
seperatly in 2-D in order to estimate their respective noise level and to
adjust their :ref:`uncertainties<MIM_Data_Uncert>` accordingly.

.. _MIM_Data_Uncert:

.. list-table:: : Assigned uncertainties
   :header-rows: 1
   :widths: 10 10 10
   :stub-columns: 1

   *  -
      - DP-P
      - P-DP
   *  - Percent (:math:`\% |d|`)
      - 2
      - 6
   *  - Floor (:math:`V`)
      - 2e-5
      - 4e-5

Observed, predicted and recovered models for all 10 lines are presented
:ref:`below<MIM_DC2D_Inv_QC>`. While smoothly varying, both the P-DP and DP-P
configuration seems to agree on the general distribution of conductivities.

.. _MIM_DC2D_Inv_QC:

.. list-table:: : Independent 2-D inversions of the P-DP and DP-P data
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/MIM_DC2D_Inv_QC.html

DCR: 2-D Inversion
******************

 .. figure:: images/MtIsa_Data_Merge.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_Data_Merge

    Merge the P-DP and DP-P data configuration with their respective
    uncertainties

 .. figure:: images/MtIsa_DC2D_2_3DMesh.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_2D_2_3DMesh

    : Stacked 2-D models recovered from 10 independant 2-D inversions.

As a final step of data quality control, the P-DP and DP-P configuration are
merged (:numref:`MtIsa_Data_Merge`) and :ref:`re-inverted<MIM_DC2D_Inv_FULL>`
in 2-D using their respective uncertainties. In preperation for the 3-D
inversion, the individual 2-D models are transfered onto a 3-D mesh as shown
in :numref:`MtIsa_2D_2_3DMesh`. Since each 2-D model is the result of an
independant inversion, small scales discrepancies are expected. We note
however several features recovered on all 10 lines, supporting the idea of a
strongly 2-D earth along N-S:

a) A resistive domain on the western edge of the survey, marked by a steeply
dipping contact near location 11,300 m, which may correspond to the Surprise
Creek Formation

b) A narrow, steeply dipping conductor near 12,300 m, adjacente to a more
resistive unit, possibly the conductive Breakaway Shale within a resistive
Native Bee Siltstone.

Consistant 2-D inversions in good agreement with the known geology gradually
increases our confidence in the data.

.. _MIM_DC2D_Inv_FULL:

 .. list-table:: : 2-D inverions of combined P-DP and DP-P data
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/MIM_DC2D_Inv_FULL.html



DCR: 3-D Inversion
******************

 .. figure:: images/MtIsa_3D_Topo.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_3D_Topo

    : Perspective view of topography and electrode locations over the 3-D domain.

In preparation for the 3-D inversion, data locations were geo-referenced in
planimetry to the local grid (:numref:`MtIsa_3D_Topo`). In order to minimize
topographic effects, the vertical position of the electrodes were re-assigned
based on a global DEM provided by `Geoscience Australia`_. In total, 3678 P-DP
and DP-P observations were inverted. Additional smoothing in the N-S
orientation was applied in order to compensate for the 500 m line spacing.

Sections through the recovered 3-D conductivity model is presented in
:numref:`MtIsa_3D_DCModel`. This result confirms that the geology over the
Cluny region is mostly 2-D, with alternating regions of high and low
conductivity trending north-south. Volume rendering of high conductivity (1
S/m) seems to indicate the geology to be steeply dipping. See the
:ref:`Interpretation Section`<mt_isa_interpretation>` for more details.

 .. figure:: images/MtIsa_3D_DCModel.png
    :align: center
    :figwidth: 100%
    :name: MtIsa_3D_DCModel

    : Sections through the recovered conductivity model and 3-D volume rendering of high conductivity (1 S/m). Topography and electrode locations are shown for reference.


.. _Geoscience Australia: http://www.ga.gov.au/metadata-gateway/metadata/record/gcat_aac46307-fce8-449d-e044-00144fdd4fa6/

IP Data
-------

Data Quality Control
********************

As presented in the :ref:`previous<mt_isa_data>` section, the MIMDAS system
collects simultaneously a pole-dipole (P-DP) and a dipole-pole (DP-P) data
configuration.   were adjusted accordingly in order to get an equivalent
response from both configurations. The P-DP and DP-P data were inverted
seperatly in 2-D in order to estimate their respective noise level and to
adjust their :ref:`uncertainties<MIM_DCData_Uncert>` accordingly.

.. _MIM_DCData_Uncert:

.. list-table:: : Assigned uncertainties
   :header-rows: 1
   :widths: 10 10 10
   :stub-columns: 1

   *  -
      - DP-P
      - P-DP
   *  - Percent (:math:`\% |d|`)
      - 5
      - 5
   *  - Floor (:math:`V`)
      - 2
      - 2

Observed, predicted and recovered models for all 10 lines are presented
:ref:`below<MIM_IP2D_Inv_QC>`. While smoothly varying, both the P-DP and DP-P
configuration seems to agree on the general distribution of conductivities.

.. _MIM_IP2D_Inv_QC:

.. list-table:: : Independent 2-D inversions of the P-DP and DP-P data
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/MIM_IP2D_Inv_LR.html

IP: 2-D Inversion
*****************

 .. figure:: images/MtIsa_IP2D_2_3DMesh.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_IP2D_2_3DMesh

    : Stacked 2-D models recovered from 10 independant 2-D inversions.

As a final step of data quality control, the P-DP and DP-P configuration are
merged and :ref:`re-inverted<MIM_IP2D_Inv_FULL>`
in 2-D using their respective uncertainties. In preperation for the 3-D
inversion, the individual 2-D models are transfered onto a 3-D mesh as shown
in :numref:`MtIsa_IP2D_2_3DMesh`. Since each 2-D model is the result of an
independant inversion, small scales discrepancies are expected. We note
however several features recovered on all 10 lines, supporting the idea of a
strongly 2-D earth along N-S:

a) A resistive domain on the western edge of the survey, marked by a steeply
dipping contact near location 11,300 m, which may correspond to the Surprise
Creek Formation

b) A narrow, steeply dipping conductor near 12,300 m, adjacente to a more
resistive unit, possibly the conductive Breakaway Shale within a resistive
Native Bee Siltstone.

Consistant 2-D inversions in good agreement with the known geology gradually
increases our confidence in the data.

.. _MIM_DC2D_Inv_FULL:

 .. list-table:: : 2-D inverions of combined P-DP and DP-P data
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/MIM_IP2D_Inv_FULL.html



IP: 3-D Inversion
*****************

In preparation for the 3-D inversion, data locations were geo-referenced in
planimetry to the local grid (:numref:`MtIsa_3D_Topo`). In order to minimize
topographic effects, the vertical position of the electrodes were re-assigned
based on a global DEM provided by `Geoscience Australia`_. In total, 3678 P-DP
and DP-P observations were inverted. Additional smoothing in the N-S
orientation was applied in order to compensate for the 500 m line spacing.

Sections through the recovered 3-D conductivity model is presented in
:numref:`MtIsa_3D_IPModel`. This result confirms that the geology over the
Cluny region is mostly 2-D, with alternating regions of high and low
conductivity trending north-south. Volume rendering of high conductivity (1
S/m) seems to indicate the geology to be steeply dipping. See the
:ref:`Interpretation Section`<mt_isa_interpretation>` for more details.

 .. figure:: images/MtIsa_3D_IPModel.png
    :align: center
    :figwidth: 100%
    :name: MtIsa_3D_IPModel

    : Sections through the recovered conductivity model and 3-D volume rendering of high conductivity (1 S/m). Topography and electrode locations are shown for reference.
