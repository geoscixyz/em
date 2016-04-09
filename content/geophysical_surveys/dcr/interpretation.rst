.. _dcr_interpretation:

Interpretation
==============

 .. figure:: images\TwoSphere_AppRes.png
    :align: right
    :figwidth: 50%
    :name: DCR_AppRes

    Pseudo-section of apparent resistivity (log10).

As a convention, the observed voltages are usually converted to apparent
resistivities. {link} and data are plotted in a  pseudosection format.  A
typical pseudosection is provided in :numref:`DCR_AppRes`. Pseudosections are
a valuable way to present and QC the data, especially if data have been
acquired along a single line. But extracting information about the
conductivity structure requires the data to be inverted {link}. The cross-
section below shows the 2D conductivity obtained by inverting the data shown
in :numref:`DCR_AppRes`. Regions of the recovered model with low confidence
are set to transparent using a :ref:`Depth of
Investigation<depth_of_investigation>` analysis.

 .. figure:: images/TwoSphere_Inv2D_DOI.png
    :align: center
    :figwidth: 50%
    :name: DCR_Inv2D

    Inverted 2D model.

.. _depth_of_investigation:

Depth of Investigation
----------------------

An important component of geophysical inversionis to determine
the level of confidence in the recovered model

 .. figure:: images/TwoSphere_Inv2D_Ref.png
    :align: center
    :figwidth: 50%
    :name: DCR_Inv2D_Refs

    Two solutions from a 2D inversion using a (a) :math:`100 \; \Omega \cdot m`
    and (b) :math:`50 \; \Omega \cdot m` reference conductivity model.

 .. figure:: images/TwoSphere_DOI_mask.png
    :align: center
    :figwidth: 50%
    :name: DCR_Inv2D_DOI_Mask

    Calculated depth of investigation index. The :math:`80^{th}` percentile
    is chosen as a cut-off value, below which the model is deemed unreliable.

 .. figure:: images/TwoSphere_Inv2D_DOI.png
    :align: center
    :figwidth: 50%
    :name: DCR_Inv2D_DOI

    Final conductivity model with DOI mask.


.. _hypothesis_testing:

Hypothesis Testing
------------------

Blabla hypothesis testing

