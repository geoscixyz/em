.. _transient_planewaves_homogeneous_peakdistance:

Peak Distance (Diffusion Distance)
==================================

At a particular time, the distance at which the signal amplitude is largest is the peak depth. The peak depth observed in :numref:`Ward1988Fig1_2` (b) can be dervied by setting the depth derivative of Eq. :eq:`e_impulse_quasistatic` to zero:

.. math::
    z_{max} = \sqrt{\frac{2 t}{\mu\sigma}} \approx 1260 \sqrt{\frac{ t}{\sigma}}.
    :label: zmax

This quantity is frequently referred to as the **diffusion distance**. It acts as a time domain equivalent for the :ref:`skin depth<frequency_domain_plane_wave_sources_skindepth>`.

.. figure:: images/Ward1988Fig1_2.png
   :align: center
   :scale: 40%
   :name: fig_planewaves_peakdistance

   Electric field as a function of time 100 m from a 1D impulse in the field in a 0.01 S/m whole space (a). Electric field at t = 0.03 ms as a function of distance (Modifed from :cite:`ward1988`) (b).
