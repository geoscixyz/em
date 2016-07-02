.. _mt_isa_synthesis:

Synthesis
=========

 .. figure:: images/MtIsa_DC3D_Old_vs_New.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_DC3D_Old_vs_New

    : Comparative sections through the recovered 3D conductivity model presented in :cite:`rutley2001` (left) and this study (right).

 .. figure:: images/MtIsa_IP3D_Old_vs_New.png
    :align: right
    :figwidth: 50%
    :name: MtIsa_IP3D_Old_vs_New

    : Comparative sections through the recovered 3D chargeability model presented in :cite:`rutley2001` (left) and this study (right).

This example demonstrates the two important lessons. The first highlights the
ability for modern inversion capabilities to distinguish subtleties in the
subsurface. Figure :numref:`MtIsa_DC3D_Old_vs_New` and :numref:`MtIsa_IP3D_Old_vs_New` compares the recovered
conductivity and chargeability models presented in :cite:`rutley2001` with the
updated model presented in this study. Both studies used identical datasets
and inversion parameter, at the exception of the finer cell size
discretization: from 40 x 100 m to 25 x 50 m.

This is highlighted further when interpreting with multiple physical
properties. Here, the Breakaway shale was a major conductor and the Moondarra
siltstone a moderate one. However, the shale is unimportant for exploration in
this region when compared to the Moondarra that hosts the Mt Norvit Horizon.
Once the induced polarization was introduced, it highlighted the Mt Horvit
Horizon within the Moondarra and the mineralized zone in the Native Bee
siltstone. The shale is then exposed as just conductive and the main feature
in the conductivity model is delineated as non-mineral bearing. This was
available in the original inversion presented in the case study. However, the
Eastern Quartz Volcanics is much more evident as a resistive feature
separating the Moondarra and Native Bee siltstones.

The second lesson here is the importance of a 3D inversion even in the
presence of 2D geology :numref:`MtIsa_DC2D_vs_3DModel`. The 2D inversions, in
general, reproduce the large-scale features of the subsurface. However, when
the geology becomes more complex, the 3D inversion can show the changes in
strike cause by folding and faulting, or where mineralisation grade changes.
This is most evident in the Mt Norvit Horizon, where the chargeability is
north-south in general yet has variability along strike.

 .. figure:: images/MtIsa_DC2D_vs_3DModel.png
    :align: center
    :figwidth: 100%
    :name: MtIsa_DC2D_vs_3DModel

    : Comparative sections through the recovered 2D (left) and 3D (right) inversion.

