.. _mt_isa_processing:

Processing
==========

**Purpose:**This section provides an overview of the quality control and processing steps required prior to the 3-D inversion.

DCR
---

Although our ultimate goal is to generate a 3-D conductivity model there are
multiple reasons for first carrying out 2-D inversions:

(a) Data were collected in a 2D geometry, that is, the transmitter and
(receiver electrodes are along one line.

(b) The geology is principally 2D so the inversion results will provide an
(approximate result and/or maybe a starting model for a subsequent 3D
(inversion.

(c) 2D inversions are quick to implement and can reveal possible issues with
(i.e. bad data points, incorrect normalizations, etc.)

As presented in the :ref:`Data<mt_isa_data>` section, the MIMDAS system
collects simulataneously pole-dipole (P-DP) and dipole-pole (DP-P) data. While
sensing the same Earth, these two configurations can yield different responses
and consequently be subject to different noise levels. After inspection, data
uncertainties assigned to the DP-P configuration were increased to account for
the consistantly weaker potentials.

Observed, predicted and recovered models for all 10 lines are presented below.
While smoothly varying, both the P-DP and DP-P configuration seems to agree on
a strong conductor between stations 11,750 and 12,500 m. Since each model is
the result of an independant inversion, small scales discrepancies are
expected. We note however that strong features are recovered on all 10 lines,
supporting the idea of a strongly 2-D earth along N-S.

.. raw:: html
    :file: ./images/MIM_DC2D_Inv_LR.html


3D inversion of DCR data Summary about what was done for the DCR inversion and
final models.
