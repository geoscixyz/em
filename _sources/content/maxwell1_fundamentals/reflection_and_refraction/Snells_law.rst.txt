.. _Snells_law:

Reflection and Snell's Law
==========================

.. purpose::

    Here, we derive the propagation angles of reflected and refracted waves at a horizontal interface. Snell's law is then used to characterize the refraction angle in terms of the complex wavenumber for both media.

Setup
-----

Here, we will consider the reflection and refraction of a uniform, linearly polarized, homogeneous plane wave at a horizontal interface (:numref:`snells_law_setup`). The incident wave is confined to the xz-plane. The interface is denoted by :math:`S`, has a normal vector :math:`\mathbf{\hat n}` and separates two homogeneous media with physical properties :math:`\sigma_1`, :math:`\mu _1`, :math:`\epsilon_1` and :math:`\sigma_2`, :math:`\mu _2`, :math:`\epsilon_2`.

For the setup in :numref:`snells_law_setup`, the incident wave (:math:`k_i`) arrives at angle :math:`\theta_i`. Once this wave reaches the interface, it breaks into two parts, a reflected wave (:math:`k_r`) and a transmitted wave (:math:`k_t`). The transmitted was experiences a change in propagation direction, thus it is a refracted wave. The reflected and refracted waves travel in directions characterized by angles :math:`\theta_r` and :math:`\theta_t`, respectively.

.. figure:: images/snellslaw_setup.png
   :align: center
   :figwidth: 70%
   :name: snells_law_setup

   Geometry for Snell's law. Modified from :cite:`ward1988` Figure 3.1.


.. _Snells_law_derive:

Snell's Law, Reflection and Refraction
--------------------------------------

The reflection and refraction angles (:math:`\theta_r` and :math:`\theta_t`) can be derived by considering either the electric field or the magnetic field carried by the incident EM wave. Here, we will derive these angle by considering an electric field. The respective incident, reflected and refracted waves are given by:

.. math::
	\mathbf{E_i} = \mathbf{E_{i,0}} \, e^{-i \mathbf{k_i \cdot r}}, \;\;\; \mathbf{E_r} = \mathbf{E_{r,0}} \, e^{-i \mathbf{k_r \cdot r}}, \;\;\; \textrm{and} \;\;\; \mathbf{E_t} = \mathbf{E_{t,0}} \, e^{-i \mathbf{k_t \cdot r}}
	:label:

where :math:`\mathbf{k}` is the wave vector (Poynting vector) for each wave and:

.. math::
	\mathbf{E \times H} = \mathbf{k}
	:label:

Within formative laws, we discussed the :ref:`interface conditions<maxwell1_fundamentals_interface_conditions_index>` required for electric and magnetic fields. They state that components of the electric field parallel to surface :math:`S` must be equal across the interface. As a result:

.. math::
	\mathbf{\hat n} \times \big ( \mathbf{E_i} + \mathbf{E_r} \big ) = \mathbf{\hat n} \times \mathbf{E_t}
	:label:

Using the previous three expressions, we find that:

.. math::
	\theta_i = \theta_r
	:label: eq_reflected

and

.. math::
	k_i \, \textrm{sin}\theta_i = k_t \, \textrm{sin}\theta_t
	:label: eq_Snells_law

According to Eq. :eq:`eq_reflected`, the reflected angle and the incident angle relative to :math:`\mathbf{\hat n}` are the same. Eq. :eq:`eq_Snells_law` is known as **Snell's Law**. Snell's law defines the refraction angle corresponding to the transmitted wave. Thus depending on the physical properties of each medium, the transmitted wave can be refracted either towards the vertical or towards the horizontal.

.. _Snells_law_Snells_law:

Snell's Law Approximations
--------------------------

The most common definition of Snell's law is given by:

.. math::
	k_1 \, \textrm{sin}\theta_1 = k_2 \, \textrm{sin}\theta_2
	:label: eq_Snells_law_2

where :math:`k_1` is the wavenumber for the incident wave with angle :math:`\theta_1` and :math:`k_1` is the wavenumber of the refracted wave with angle :math:`\theta_2`. Here, we discuss a few properties of Snell's law.

**Quasi-Static Regime**

In the quasi-static regime (:math:`\sigma \gg \omega \varepsilon`), the wavenumber becomes:

.. math::
	k \approx \sqrt{-i \omega \mu \sigma}
	:label:

In this case, Snell's law reduces to:

.. math::
	\sqrt{\mu_1 \sigma_1} \, \textrm{sin}\theta_1 = \sqrt{\mu_2 \sigma_2} \, \textrm{sin} \theta_2


**Wave Regime**

In the wave regime (:math:`\sigma \ll \omega \varepsilon`), the wavenumber becomes:

.. math::
	k \approx w \sqrt{\mu \varepsilon}
	:label:

where the velocity of the wave is given by:

.. math::
	V = \frac{1}{\sqrt{\mu \varepsilon}}
	:label:

Using the two previous expressions, Snell's law in the wave regime becomes:

.. math::
	\frac{V_1}{V_2} = \frac{sin \theta_1}{sin \theta_2}
	:label: eq_Snells_law_3

In this case, the angle of incidence and refraction are directly related to the propagation velocity of EM waves within each media. This relationship is especially important when considering :ref:`ground penetrating radar<gpr_index>`.










