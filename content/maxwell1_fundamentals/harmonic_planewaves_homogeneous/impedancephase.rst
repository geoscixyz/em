.. _harmonic_planewaves_homogeneous_impedancephase:

Wave Impedance and Phase
========================

**Impedance** is defined as the negative ratio between perpendicular components of corresponding electric and magnetic fields. For the setup shown in :numref:`planewave_down_fields`, the impedance is given by:

.. math::
	Z_{xy} = -\frac{E_x}{H_y} = \frac{\omega \mu}{k}

The impedance can be used to tell us about the **phase difference** between the electric and magnetic fields. The phase difference between the electric and magnetic field is given by:

.. math::
    \phi_{Z_{xy}} = \textrm{tan}^{-1} \Bigg ( - \frac{\textrm{Im}[Z_{xy}]}{\textrm{Re}[Z_{xy}]} \Bigg )

where :math:`0 \leq \phi_{xy} \leq \pi/4`. According to our definition, the electric field lags the magnetic field.

.. figure:: images/EHquasi.gif
   :align: right
   :figwidth: 50%
   :name: waves_homogeneous_freq_EHquasi

   Electric and magnetic fields of an EM wave propagating in the x-direction (quasi-static regime).

**Quasi-Static Regime:**

In the quasi-static regime (:math:`\epsilon \omega \ll \sigma`), the wavenumber becomes :math:`\sqrt{-i\omega\mu\sigma}` and the impedance simplifies to:

.. math::
    Z_{xy} = \frac{\omega \mu}{\sqrt{-i\omega\mu\sigma}}
    = \sqrt{\frac{i \omega \mu}{\sigma}}

The phase of the impedance is given by:

.. math::
    \phi_{Z_{xy}} = \textrm{tan}^{-1} \Bigg ( \frac{\textrm{Im}[Z_{xy}]}{\textrm{Re}[Z_{xy}]} \Bigg ) = \frac{\pi}{4}

In this case, the electric field lags the magnetic field by :math:`\pi/4` radians.

.. figure:: images/EHwave.gif
   :align: right
   :figwidth: 50%
   :name: waves_homogeneous_freq_EHwave

   Electric and magnetic fields of an EM wave propagating in the x-direction (wave regime).

**Wave Regime:**

In the wave regime (:math:`\epsilon \omega \gg \sigma`), the wavenumber simplifies to :math:`\omega \sqrt{\mu\epsilon}` and the impedance simplifies to:

.. math::
    Z_{xy} = \frac{\omega \mu}{\omega \sqrt{\mu\epsilon}}
    = \sqrt{\frac{\mu}{\epsilon}}

where the phase is equal to:

.. math::
    \phi_{Z_{xy}} = \textrm{tan}^{-1} \Bigg ( \frac{\textrm{Im}[Z_{xy}]}{\textrm{Re}[Z_{xy}]} \Bigg ) = 0

In this case, the electric and magnetic fields are in phase with one another.
