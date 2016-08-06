.. _dcr_interpretation:

Interpretation
==============

.. topic:: Purpose

    Interpret the data generated from the :ref:`two-sphere
    problem<dcr_physics>`.

 .. figure:: images/TwoSphere_AppRes.png
    :align: right
    :figwidth: 50%
    :name: DCR_AppRes

    Pseudo-section of apparent conductivity (log10) as predicted by the forward
    simulation. Outlines for the location of the sphere anomalies are shown for
    reference.

As a convention, the observed voltages are usually converted to apparent
conductivity {link} and plotted in a pseudosection format. As illustrated in
:numref:`DCR_AppRes`, the pseudosection is useful as a presentation and
quality-control tool, especially if the data have been acquired along a single
line. Spurious measurements can generally identified when compared to
neighbouring source-receiver observations. While the pseudosection can
provide some idea of lateral changes in conductivity, little can be said about
the shape and location of the anomalies.

 .. figure:: images/TwoSphere_Inv2D_DOI.png
    :align: right
    :figwidth: 50%
    :name: DCR_Inv2D

    Inverted 2D conductivity model with DOI mask.

Extracting information about the conductivity structure requires the data to
be inverted {link}. :numref:`DCR_Inv2D` shows the recovered 2D conductivity
model obtained after convergence of the algorithm. Both spheres are imaged at
the right depth and approximate conductivity values. Regions of low confidence
are set to transparent using a :ref:`Depth of
Investigation<depth_of_investigation>` analysis.


.. _depth_of_investigation:

Depth of Investigation
----------------------

An important component of geophysical inversion is to determine the level of
confidence in the recovered model. It is recognized that the inverse problem
is nonunique and that the  DCR data are sensitive to conductivity only in a
region in the vicinity of the electrode array. As proposed by
:cite:`LiDWO1999`, the Depth of Investigation method can be used to quantify
the resolving power of a given DCR experiment.

 .. figure:: images/TwoSphere_Inv2D_Ref.png
    :align: right
    :figwidth: 50%
    :name: DCR_Inv2D_Refs

    Two solutions from a 2D inversion using a (a) :math:`100 \; \Omega \cdot m`
    and (b) :math:`50 \; \Omega \cdot m` reference conductivity model.

In its simplest form, the DOI analysis requires the data to be inverted twice
with slightly different assumptions. Back to the two-sphere example, the
synthetic data is inverted once with a reference half-space conductivity of
:math:`10^{-2}` S/m, and a second time with a conductivity of
:math:`5\cdot10^{-2}` S/m. :numref:`DCR_Inv2D_Refs` shows both recovered 2D
conductivity models obtained after convergence of the algorithm. Note that the
region away from the electrode locations returns to a uniform conductivity
value close to the reference model.

 .. figure:: images/TwoSphere_DOI_mask.png
    :align: right
    :figwidth: 50%
    :name: DCR_Inv2D_DOI_Mask

    Calculated depth of investigation index. The :math:`80^{th}` percentile
    is chosen as a cut-off value, below which the model is deemed unreliable.

We now have a discretized volume of the Earth and two conductivity models that
can equally reproduced the observed data. Let :math:`\sigma_1, \sigma_2` be
the conductivity values recovered at some location (*x,z*), let:

.. math::
   DOI(x,y) = 1 - \big| \frac{\sigma_1(x,y) - \sigma_2(x,y)}{\sigma_1^{ref} - \sigma_2^{ref}} \big|\;,

where the DOI index will approach 1 for similar model values obtained with
both inversions  regardless of the chosen reference models
:math:`\sigma_1^{ref}, \sigma_2^{ref}`. Conversely, the ratio will approach 0
where the recovered models diverge to their respective reference conductivity.
:numref:`DCR_Inv2D_DOI_Mask` presents the calculated DOI index for the two-
sphere problem, showing a lower confidence over the bottom half of the domain.
Note that the DOI index decreases more rapidly inside the conductive sphere,
as expected from weaker potentials measurements over conductors.

.. _hypothesis_testing:

Hypothesis Testing
------------------

Blabla hypothesis testing

