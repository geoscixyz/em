.. _mt_isa_survey:

Survey
======

It is expected that the mineralization is both  :ref:`conductive and chargeable <mt_isa_properties>`. A DC/IP survey is therefore an appropriate (and desired) choice for geophysical exploration. In this section, we explore the survey design used at the Cluny property.

DC Resistivity (DCR)
--------------------

The fundamentals for a DCR survey can be found in the :ref:`Geophysical Surveys <DCR_index>` section. Many choices are possible for electrode layouts, but the final choice at Cluny was motivated by the following factors:

(a) MIM, the company who was exploring the property, had developed their own data acquistion system `MIMDAS`_. The system had a 100-channel capacity distributed acquisition system, which means it each electrode could serve as a current or potential and it could acquire both DCR and IP data.

(b) The area of interest is approximately 2km by 5km. Although full 3D coverage was desireable, the field acquistion was limited to 10 east-west lines. The reason for this was two fold. Firstly, the 2D lines could be laid out across the East-West boundaries of Cluny region. Secondly, the fault structures were known to strike north-south, so it is natural to have the survey perpendicular to strike in order to generate the most physical property contrast along line. Most lines consisted of 21 current electrode locations (the three to the north had 19) with each current electrode having a maximum of 20 potential readings.

(c) The choice of a pole-dipole was motivated by past experience that this was an effective survey for deep targets. The layout shown in {figure} indicates a current electrode at position 1 with potentials measured across all other dipoles. This produces a :ref:`pseudo-section<dcr_pseudosection>`. Furthermore, with the MIMDAS system, a pole-dipole (P-DP) and dipole-pole (DP-P) could be acquired along each line at no additional cost. The system spaced each potential electrode 100-m apart. 


.. _MIMDAS: http://www.smedg.org.au/Sym01NS.htm


Survey Design
-------------

The geologic structures are primarily striking north-south and a cross-section of the geologic units and their resistivities is shown in :numref:`Geology_Section`. The unit of interest is the Mt. Novit Horizon which is conductive compared to the host Moondarra Siltsone. Two sets of data are forward modelled: one with and one without the conductor. The pole-dipole pseudo-sections obtained with 15 electrodes spaced 100 meters apart are shown below (:numref:`MIM_DPP_Simulation`).

.. _Mt_Isa_Simulation:
.. list-table:: : DCR simulation over a synthetic Mt. Isa conductivity model
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/Mt_Isa_Current_Anim.html

Current density (arrows) and charge density (color) for a range of source locations (Powered by: `SimPEG <http://www.simpeg.xyz/>`_).

 .. figure:: ./images/MIM_PDP_Simulation.png
    :align: right
    :figwidth: 50%
    :name: MIM_PDP_Simulation

 .. figure:: ./images/MIM_DPP_Simulation.png
    :align: right
    :figwidth: 50%
    :name: MIM_DPP_Simulation

    Log10 pseudo-conductivity section along the geological section and the recovered 2D conductivity model from the inversion of DCR data. The top two figures are for the pole-dipole survey and the bottom two images coorrespond to the dipole-pole survey along the same line. In both figures, the true conductivity model is shown in grey scale for reference.

.. todo::
  To determine if the survey is well designed we use the criteria for :ref:`detectability <surveyDetectability>` The difference sections are shown in {figure}. They show xxx If errors are assigned as 5% + floor 0.0001 V then the secondary signal from the target is detectable.

  Inversion of Synthetic data Following the work {link: general basics of survey design} we invert the synthetic data using 2D algorithm.  The parameters used in the inversion were:  xxxxx. The Mt. Norvit Horizon is evident.

  Using 2D forward modelling, we can also simulate current flows that could be expected at Mt. Isa. Note in particular the current channeling into the conductive Breakaway Shale as well as through the deeper mineralization.

