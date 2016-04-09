.. _dcr_example:

Example
=======

 .. figure:: images\TwoSphere_model.png
    :align: right
    :figwidth: 50%
    :name: DCR_TwoSpheres

    Two-spheres model with pole-dipole survey configuration.

We illustrate the DCR experiment on a typical pole-dipole survey acquired
over a synthetic model (:numref:`DCR_TwoSpheres`). This simple conductivity
model is made up of a conductive (:math:`10^{-1}` S/m) and a resistive
(:math:`10^{-3}` S/m) sphere embedded in a uniform half-space (:math:`10^{-2}`
S/m). Using numerical codes, we can model the flow and accumulation of charges
due to conductivity contrasts as shown in the animation below.
The arrows denote the current flow, while the color indicates the
strenght and sign of accumulated charges. The source location is marked by
a triangle.

 .. raw:: html
    :file: images\TwoSphere_Current_Anim.html

(Press play) Note the behaviour of the current lines as the source passes over the
conductive sphere. The current density increases inside the conductor but
decreases around it, which is often refered to as `current channeling`
effects.

(Pause) High charge density are accumulated at the interface between
conductivity contrasts. Important to note the difference in polarity between
the conductive and resistive anomaly (:ref:`Electrostatic sphere<_electrostatic_sphere>`).
