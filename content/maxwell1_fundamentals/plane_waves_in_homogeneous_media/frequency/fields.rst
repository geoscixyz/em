.. _frequency_domain_plane_wave_sources_fields:

Fields (Frequency Domain)
=========================

.. purpose::

    Here, we provide explicit expressions for the electric and magnetic fields supported by plane waves. Relationships between the electric and magnetic fields are discussed and used to define useful quantities such as: impedance, apparent resistivity and phase.

.. figure:: ../images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewave_down_fields

   Setup diagram of plane EM wave propagation heading downward (negaitve :math:`z`).

By :ref:`solving the Helmholtz equation<frequency_domain_plane_wave_sources_analytic_solution>` for the electric field, we obtain a general solution of the form:

.. math:: \mathbf{E} (z,\omega) = \mathbf{E}_0^-  e^{ikz} + \mathbf{E}_0^+ e^{-ikz} 

where :math:`\mathbf{E}_0^-` and :math:`\mathbf{E}_0^+` are the amplitudes of the down-going and up-going waves, respectively. In this section, analysis will be performed by considering only the down-going wave (:numref:`planewave_down_fields`), thus:

.. math:: \mathbf{E} (z,\omega) = \mathbf{E}_0^- e^{ikz}

According to the figure, we are considering the case where the electric field only has components in the x-direction. Thus our solution for the electric field can be expressed as:

.. math:: \mathbf{E} (z,\omega) = E_x (z,\omega) \, \mathbf{u_x} = E_{x,0}^{-} e^{ikz} \mathbf{u_x}

where :math:`\mathbf{u_x}` is a unit vector in the x-direction. Using Faraday's law, we find that the corresponding magnetic field only has components in the y-direction. This can be described by the following ODE:

.. math::
  \frac{\partial E_x}{\partial z} + i \omega \mu H_y = 0

We could have also deduced this by considering the :ref:`Poynting vector<plane_waves_in_homogeneous_media_index_Poynting>`. Solving for the y component of the magnetic field, we obtain:

.. math::
  H_y (z,\omega ) = H_{y,0}^- e^{ikz} = -\frac{k}{\omega \mu} E_{x,0}^- e^{ikz}

where 

.. math:: H_{y , 0}^{-} = - \frac{k}{\omega \mu} E_{x, 0}^{-} 

We have now otained full analytic expressions for the electric and magnetic fields for the plane wave equations. Assuming :math:`E_{x ,0}^{-}` is known, these solutions are given below:

.. math::
	\mathbf{E} = E_x \mathbf{u}_x = E_{x,0}^{-} \, e^{ikz} \mathbf{u}_x
	:label: FDplaneEx

.. math::
	\mathbf{H} = H_y \mathbf{u}_y = H_{y,0}^{-}\, e^{ikz} \mathbf{u}_y= -\frac{k}{\omega \mu} E_{x \ 0}^{-} \, e^{ikz} \mathbf{u}_y
	:label: FDplaneHy

This result can be extended to plane waves in any direction. It states that the electric and magnetic fields supported by an EM wave are perpendicular to one another and perpendicular to the propagation direction.

.. _frequency_domain_plane_wave_sources_fields_impedance:

Impedance and Phase
^^^^^^^^^^^^^^^^^^^

**Impedance** is defined as the negative ratio between perpendicular components of corresponding electric and magnetic fields. For the setup shown in :numref:`planewave_down_fields`, the impedance is given by:

.. math::
	Z_{xy} = -\frac{E_x}{H_y} = \frac{\omega \mu}{k}

The impedance can be used to tell us about the **phase difference** between the electric and magnetic fields. The phase difference between the electric and magnetic field is given by:

.. math::
    \phi_{Z_{xy}} = \textrm{tan}^{-1} \Bigg ( \frac{\textrm{Im}[Z_{xy}]}{\textrm{Re}[Z_{xy}]} \Bigg )

where :math:`0 \leq \phi_{xy} \leq \pi/4`. According to our definition, the electric field lags the magnetic field.

.. figure:: ../images/EHquasi.gif
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

.. figure:: ../images/EHwave.gif
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


.. _frequency_domain_plane_wave_sources_fields_resistivity:

Apparent Resistivity
^^^^^^^^^^^^^^^^^^^^

The resistivity value obtained using simplified geometry and physics is known as the apparent resistivity. It is useful in providing a ball-park estimate of the Earth's electric properties. Various definitions for apparent resistivity will be provided when learning about :ref:`direct current resistivity<dcr_index>` and :ref:`magnetotelluric<mt_index>` methods.

Here, we present the definition for apparent resistivity which is most relevant to magnetotellurics. According to our quasi-static approximation for the impedance, where resistivity is the reciprocal of the conductivity:

.. math::
    \rho_{app} = \frac{1}{\sigma_{app}} = \frac{| Z_{xy}|^2}{\omega \mu}

Therefore, if perpendicular components of the electric and magnetic fields are known within a homogeneous medium, it is possible to estimate the electrical resisitivity of that medium; assuming also that the Earth is approximately non-permeable (:math:`\mu = \mu_0`). For a half-space model, the Earth's true resistivity is equal to the apparent resistivity.


