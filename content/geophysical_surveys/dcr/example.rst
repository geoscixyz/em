.. _dcr_example:

Example
=======

**Goal:** Simulate numerically a DCR experiment.

 .. figure:: images/TwoSphere_model.png
    :align: right
    :figwidth: 50%
    :name: DCR_TwoSpheres

    Pole-dipole DCR experiment over a synthetic model made up of a conductive
    (:math:`10^{-1}` S/m) and a resistive (:math:`10^{-3}` S/m) sphere
    embedded  in a uniform half-space (:math:`10^{-2}` S/m).

We illustrate the DCR experiment on a synthetic pole-dipole survey as
illustrated in :numref:`DCR_TwoSpheres`. This simple
:ref:`conductivity<electrical_conductivity_index>` model is made up of two
spheres in a uniform half-space Earth. Charges are injected into the ground
from the source and potentials are measured at different locations. Using
:ref:`numerical methods<solving_maxwells_equations>`, we can model the flow
and accumulation of charges due to conductivity contrasts as shown in the
animation below. The arrows denote the :ref:`current
density<current_density_J>`, while the color indicates the strength and sign
of :ref:`accumulated charges<bound_charge_Q>`. The source location is marked
by a triangle.

`[Press play]` Note the behaviour of the current lines as the point source passes over the
conductor. The current density increases inside the sphere but
decreases around it, which is often refered to as :ref:`current channeling<dc_e_field>`.
Conversely, current lines get deflected around the resistor.

`[Pause]` The accumulation of charges occurs at the interface between
conductivity contrasts. Important to note the difference in polarity between
the conductive and resistive anomaly as predicted by the :ref:`theory<bound_charge_Q>`.

 .. raw:: html
    :file: images/TwoSphere_Current_Anim.html