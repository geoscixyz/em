.. _mt_physics:

Physics
=======

.. raw:: html
    :file: ../../../underconstruction.html
 
The natural source fields travel as plane waves and the physics behind these are explained in high detail on the :ref:`page for fundamentals of natural sources <MT_N_layered_Earth>`. At the surface of the Earth, the fields are :ref:`transmitted <reflection_and_refraction_index>` vertically into the subsurface, creating vertically propagating plane waves that generate sheet currents, as shown :ref:`below <mt_refltransmovie>`. This :ref:`fundamentals page <MT_refl_transcoeff>` provides more details and reflection and transmission for MT.

.. _mt_refltransmovie:

.. list-table:: : Reflection at the interface
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: images/Reflection_Transmission.html
   *  - Powered by: `SimPEG <http://simpeg.xyz/>`_

.. todo:: step-by-step from plane source to apparent resistivity (radio button widget): (1) plane waves, (2) skin depth), (3) phase difference between E and H (tie back to 1D stuff Thibaut already did)

The fields propogate at different frequencies and each frequency provides different information about the subsurface. Low frequencies penetrate deeper while high frequencies provide information near the surface. The plane wave attenuates with depth and a skin depth is the distance at which the amplitude has decreased by :math:`1/e`. This is explained in detail :ref:`on the fundamentals page <MT_skindepthdoi>`. :ref:`The movie below <mt_sd_envelopes>` shows the magnetic field at different frequencies and how it attenuates in the subsurface.

.. _mt_sd_envelopes:

.. list-table:: : Given the same conductivity model, the skin depth decreases as the frequency increases.
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: images/SkinDepth_envelope.html
   *  - Powered by: `SimPEG <http://simpeg.xyz/>`_


In the :ref:`movie below <mt_doimovie>`, we see that even at very high frequencies (20,000 Hz), MT is still a deep exploration method in resistive environments. The skin depth for this scenario is about 1125 m, providing an estimate of the survey's depth of investigation.

.. _mt_doimovie: 

.. list-table:: : Depth of investigation in MT.
   :header-rows: 0
   :widths: 10
   :stub-columns: 0

   *  - .. raw:: html
            :file: images/MT_EH_fields_movie.html
   *  - Powered by: `SimPEG <http://simpeg.xyz/>`_


**Impedance**

Because the source fields are not known, we calculate a ratio based on the measured electric (:math:`\mathbf{E}`) and magnetic (:math:`\mathbf{H}`) fields. This ratio is referred to as the impedance :math:`Z`:

.. math:: 
        \mathbf{E} = Z \mathbf{H},

where the impedance is a matrix defined as:

.. math:: 
        Z = \left( \begin{matrix} Z_{xx} && Z_{xy}\\ Z_{yx} && Z_{yy}\end{matrix} \right)

and :math:`\mathbf{E} = \left( \begin{matrix} \mathbf{E}_{x}\\ \mathbf{E}_{y} \end{matrix} \right)` and :math:`\mathbf{H} = \left( \begin{matrix} \mathbf{H}_{x}\\ \mathbf{H}_{y} \end{matrix} \right)`. The electric and magnetic fields are perpendicular to each other.

For a halfspace earth, the impedance simplifies to a single component of the matrix: :math:`Z_{xy} = \frac{\mathbf{E}_x}{\mathbf{H}_y}`. From the impedance, we can calculate the apparent resistivity :math:`\rho_a` and the phase :math:`\Phi`:

.. math:: \rho_a = \frac{1}{\omega \mu_0} \left| Z_{xy} \right| ^2

.. math:: \Phi = \tan^{-1} \left( \frac{Im(Z_{xy})}{Re(Z_{xy})} \right) = -\frac{\pi}{4}

For a one-dimensional Earth, the off-diagonal components of the impedance are zero and the on-diagonal components are equal to each other:

.. math:: 
        Z_{1D} = \left( \begin{matrix} 0 && Z_{xy}\\ Z_{yx} && 0\end{matrix} \right)

.. math:: Z_{xy} = -Z_{yx}

For a two-dimensional Earth, the on-diagonal components are no longer identical but the off-diagonal parts remain zero:

.. math:: 
        Z_{2D} = \left( \begin{matrix} 0 && Z_{xy}\\ Z_{yx} && 0\end{matrix} \right)

.. math:: Z_{xy} \neq Z_{yx}

There is no symmetry for a 3D Earth and all components of the impedance are non-zero.

**Tipper**

A ratio can be also be calculated using just the magnetic fields. This is referred to as the tipper and is defined as following:

.. math:: 
        \mathbf{H}_z = T \mathbf{H} = \left( \begin{matrix} T_{zx} && T_{zy} \end{matrix} \right) \left( \begin{matrix} \mathbf{H}_x \\ \mathbf{H}_y \end{matrix} \right).

For a 1D Earth, :math:`T_{zx} = T_{zy} = 0`.

In 3D, all components of the tipper are non-zero. A special case of a tipper survey is when the horizontal components of the magnetic field are measured at a single reference station and the vertical component is measured using an airborne system. This is known as a :ref:`ZTEM survey <ztem_index>`.


