.. _frequency_domain_plane_wave_sources_fields:

Fields (Frequency Domain)
=========================

.. purpose::

    Provide explicit expressions for both eletric and magnetic fields for plane EM wave equations, and understand the concept of the impedance, apparent resistivity, and phase.

.. figure:: ../images/planewavedown.png
   :align: center
   :scale: 60%

   Setup diagram of plane EM wave propagation heading downward (negaitve :math:`z`).

EM fields
^^^^^^^^^

By solving plane EM wave equations in frequency domain, we obtain solution for the magnetic field as

.. math:: \mathbf{E} (z,\omega) = \mathbf{E}_0^+ e^{-ikz} + \mathbf{E}_0^-  e^{ikz}.

Here superscript :math:`+` and :math:`-` represents up- and down-going waves. In this section we focus our attentiont to down-going wave, hence

.. math:: \mathbf{E} (z,t) = \mathbf{E}_0^- e^{ikz}.

Since magnetic field only exists in :math:`y`-direction (:math:`\mathbf{E} = E_x \mathbf{u}_y`), then we obtain

.. math:: E_x = E_{x \ 0}^{-} e^{ikz}

From Ampere's law with the knowledge that we only have two components of EM fields :math:`E_x` and :math:`E_x`, we obtain

.. math::
  \frac{\partial E_x}{\partial z} + i \omega \mu H_y = 0

By evaluating differentiation, and rearranging the equation yields

.. math::
  H_y = - \frac{k}{\omega \mu} H_{y \ 0}^{-} e^{ikz} = E_{x \ 0} ^{-} e^{ikz},

where :math:`E_{x \ 0}^{-} = - \frac{\omega \mu}{k} H_{y \ 0}^{-}`.

Therefore, we have otained full expressions of electric and magnetic fields for the plane wave equations assuming :math:`E_{x \ 0}^{-}` is known.

.. math::
	\mathbf{E} = E_x \mathbf{u}_x = E_{x \ 0}^{-} e^{ikz} \mathbf{u}_x
	:label: FDplaneEx

.. math::
	\mathbf{H} = H_y \mathbf{u}_y = -\frac{k}{\omega \mu} E_{x \ 0}^{-} e^{ikz} \mathbf{u}_y
	:label: FDplaneHy

Impedance
^^^^^^^^^

We define impedance between :math:`E_x` and :math:`H_y` as

.. math::
	Z_{xy} = -\frac{E_x}{H_y} = \frac{\omega \mu}{k}

This can be simplified using quais-static or wave approximation:

- Quasi-static (:math:`\epsilon \omega \ll \sigma`):

.. math::
    Z_{xy} = \frac{\omega \mu}{\sqrt{-i\omega\mu\sigma}}
    = \sqrt{i} \sqrt{\frac{\omega \mu}{\sigma}}

.. math::
    \phi_{Z_{xy}} = \frac{\pi}{4},

where :math:`\phi_{Z_{xy}}` is the phase (rad) of the impedance.

- Wave (:math:`\epsilon \omega \gg \sigma`):

.. math::
    Z_{xy} = \frac{\omega \sqrt{\mu\epsilon}}{\omega \epsilon}
    = \sqrt{\frac{\mu}{\epsilon}}

.. math::
    \phi_{Z_{xy}} = 0


Apparent resisitivity and phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In magnetotelluric (MT) application, this impedance often considered as data, although this cannot be simply expressed since the earth medium is not homogeneous (e.g. :math:`\sigma(x, y, z)`). With the quasi-static approximation, apparent resistivity, :math:`\rho_{app}` can be written as

.. math::
    \rho_{app} = \frac{1}{\sigma}_{app} = \frac{|Z_{xy}|^2}{\omega \mu}
    :label: apparent_res

Apparent phase of the impedance, :math:`\phi_{Z_{xy}}` can be written as

.. math::
	\phi_{app} = tan^{-1} (Z_{xy}).

Note that within the quasi-static approximation for homogeneous medium, the phase of the impedance is constant (:math:`\phi_{Z_{xy}}=\frac{\pi}{4}`) on variable frequency indicating phase difference between the :math:`E_x` and :math:`H_y` is always constant for this specific setup.

.. todo::
    Add description for polarization ellipse

.. Dummy
.. .. math::
..  \frac{\partial H_y}{\partial z} + (\sigma+i \omega \epsilon) E_x = 0

.. .. math::
..   E_x = -\frac{i k}{(\sigma+i \omega \epsilon)} H_{y \ 0}^{-} e^{ikz} = H_{y \ 0} ^{-} e^{ikz},

.. .. math::
..   \mathbf{H} = H_y \mathbf{u}_y = E_{x \ 0}^{-} e^{ikz} \mathbf{u}_y
..   :label: FDplaneHy

.. .. math::
..   \mathbf{E} = E_x \mathbf{u}_x = -\frac{i k}{(\sigma+i \omega \epsilon)} H_{y \ 0}^{-} e^{ikz} \mathbf{u}_x
..   :label: FDplaneEx
