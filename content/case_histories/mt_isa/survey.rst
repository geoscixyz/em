.. _mt_isa_survey:

Survey
======

From the :ref:`Property<mt_isa_properties>` segment of the case history, it is expected that the mineralization is both conductive and chargeable. A DCIP survey is therefore appropriate. Other factors that suggest this is a good choice is that there is minimal topography in the area and DCIP surveys have been successfully carried out in other areas of the Mt. Isa region.

DC Resistivity (DCR)
--------------------

The fundamentals for a DCR survey can be found in the :ref:`Geophysical
Surveys: DCR<DCR_index>` section. Many choices are possible for electrode
layouts and the final choice is motivated by the following factors:


(a) MIM, the company who was exploring the property, had developed their own
data acquistion system `MIMDAS`_.  The cable had xxxx connections, each of
which could serve as a current electrode or potential electrode.

.. _MIMDAS: http://www.smedg.org.au/Sym01NS.htm

(b) The area of interest is approximately 5km x 5km. Although full 3D coverage
was desireable, the field acquistion was limited to 10 east-west lines. A
full set of xxx electrodes were deployed along each line.

(c) The choice of a pole-dipole was motivated by past experience that this was
an effective survey for deep targets. The layout shown in {figure} indicates
a current electrode at postion 1 with potentials measured across all other
dipoles. This produces a :ref:`pseudo-section<dcr_pseudosection>`.


Survey Design
-------------

 .. figure:: ./images/MtIsa_DCIP2D_Inv.png
    :align: right
    :figwidth: 50%
    :name: DC2D_Inv

    (Top) Pseudo conductivity section (log10) along the geologicalsection.
    ((Bottom) Recovered 2D conductivity model from the inversion of DCR data.
    (The true conductivity model is shown in grey scale for reference.

 .. figure:: ./images/MtIsa_DCIP2D_Inv_NoTarget.png
    :align: right
    :figwidth: 50%
    :name: DC2D_Inv_NoTarget

    (Top) Pseudo conductivity section (log10) along the geologicalsection.
    ((Bottom) Recovered 2D conductivity model from the inversion of DCR data.
    (The true conductivity model is shown in grey scale for reference.

The geologic structures are primarily striking north-south and a cross-section
of the geologic units and their resistivities is shown in. The unit of
interest is the Mt. Novit Horizon which is conductive compared to the host
Moondarra Siltsone. Two forward modellings are generated. The first is without
the conductor, the second is with.  The pole-dipole pseudo-sections obtained
with 15 electrodes spaced 100 meters apart is shown in :numref:`DC2D_Inv`.

To determine if the survey is well designed we use the criteria in
{link:general  basics of survey design where we look at the absolute
difference and relative difference  ?Sarah} The difference sections are shown
in {figure}. They show xxx If errors are assigned as 5% + floor 0.0001 V then
the secondary signal from the target is detectable.

Inversion of Synthetic data Following the work {link: general basics of survey
design} we invert the synthetic data using 2D algorithm.  The parameters used
in the inversion were:  xxxxx. The Mt. Norvit Horizon is evident.

Using 2D forward modelling, we can also simulate current flows that could be
expected at Mt. Isa. Note in particular the current channeling into the
conductive Breakaway Shale as well as through the deeper mineralization.

.. _Mt_Isa_Simulation:
.. list-table:: : DCR simulation over a synthetic Mt. Isa conductivity model
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: ./images/Mt_Isa_Current_Anim.html

Current density (arrows) and charge density (color) for a range of source
locations (Powered by: `SimPEG <http://www.simpeg.xyz/>`_).

