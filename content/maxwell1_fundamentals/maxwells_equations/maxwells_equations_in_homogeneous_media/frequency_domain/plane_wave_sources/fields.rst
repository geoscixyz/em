.. _frequency_domain_planewave_sources_fields:

Fields
======

.. topic:: Purpose

    Provide explicit expressions for both eletric and magnetic fields for plane EM wave equations, and understand the concept of the impedance and polarization ellipse.

.. todo::
	Show a figure for the set up.

By solving plane EM wave equations in frequency domain, we obtain solution for the magnetic field as

.. math:: \mathbf{H} (z,\omega) = \mathbf{H}_0^+ e^{-ikz} + \mathbf{H}_0^-  e^{ikz}.

Here superscript :math:`+` and :math:`-` represents up- and down-going waves. In this section we focus our attentiont to down-going wave, hence

.. math:: \mathbf{H} (z,t) = \mathbf{H}_0^- e^{ikz}.

Since magnetic field only exists in :math:`y`-direction (:math:`\mathbf{H} = H_y \mathbf{u}_y`), then we obtain

.. math:: H_y = H_{y \ 0}^{-} e^{ikz}

From Ampere's law with the knowledge that we only have two components of EM fields :math:`E_x` and :math:`H_y`, we obtain

.. math::
	\frac{\partial H_y}{\partial z} + (\sigma+\imath \omega \epsilon) E_x = 0

By evaluating differentiation, and rearranging the equation yields

.. math::
	E_x = -\frac{k}{(\sigma+\imath \omega \epsilon)} H_{y \ 0}^{-} e^{ikz} = E_{x \ 0} ^{-} e^{ikz},

where :math:`E_{x \ 0}^{-} = -\frac{k}{(\sigma+\imath \omega \epsilon)} H_{y \ 0}^{-}`.

Therefore, we have otained full expressions of electric and magnetic fields for the plane wave equations assuming :math:`H_{y \ 0}^{-}` is known.

.. math::
	\mathbf{H} = H_y \mathbf{u}_y = H_{y \ 0}^{-} e^{ikz} \mathbf{u}_y

	\mathbf{E} = E_x \mathbf{u}_x = -\frac{k}{(\sigma+\imath \omega \epsilon)} H_{y \ 0}^{-} e^{ikz} \mathbf{u}_x

We define impedance between :math:`E_x` and :math:`H_y` as

.. math::
	Z_{xy} = -\frac{E_x}{H_y} = \frac{k}{(\sigma+\imath \omega \epsilon)}

This can be simplified using quais-static or wave approximation:

- Quasi-static (:math:`\epsilon \omega \ll \sigma`):

.. math::
    Z_{xy} = \frac{\sqrt{-\imath\omega\mu\sigma}}{\sigma} = \sqrt{-\imath} \sqrt{\frac{\omega\mu}{\sigma}}

- Wave (:math:`\epsilon \omega \gg \sigma`):

.. math::
    Z_{xy} = \frac{\omega \sqrt{\mu\epsilon}}{\imath \omega \epsilon}
    = -\imath\sqrt{\frac{\mu}{\epsilon}}

When the earth medium is not homogeneous (e.g. :math:`\sigma(x, y, z)`), :math:`Z_{xy}`
