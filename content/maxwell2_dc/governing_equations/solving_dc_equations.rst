.. _solving_dc_equations:

Solving DC Equations
====================

.. include:: ../../equation_bank/dcr_fwd.rst

.. _solving_dc_equations_analytic:

Analytic
--------

.. _solving_dc_equations_numeric:

Numeric
-------

For an arbitrary conductivity model, equation :eq:`dcr_fwd` cannot be solved
exactly. In order to simulate a geophysical survey over an earth with a
complicated conductivity distribution we need to solve an approximate discrete
form of this equation.

The equation can be discretized directly using, for example, standard finite
difference, finite element, or finite volume methods. However if we use a
mimetic discretization of the full Maxwell equations, we can derive a
discretization of the DC equation from the discrete Maxwell equations. For a
brief discussion of the discretization of Maxwell's equation, see the section
:ref:`numeric_discretization` on this website. The following notation for the
discrete system in this section comes from that page.

The discrete potential field condition is :math:`\tilde{\mathbf{e}} =
\mathbf{G}\tilde{\phi}`. Substituting that into the discrete time-domain
quasi-static Ampere equation gives

.. math::
  \mathbf{C}^T \mathbf{M}_{\mu^{-1}}^f \tilde{\mathbf{b}} - \mathbf{M}_{\sigma}^e\mathbf{G}\tilde{\phi} = \tilde{\mathbf{s}},

where the tilde symbol denotes a grid function. Using the fact that the
discrete divergence operator is equal to :math:`-\mathbf{G}^T`, we take the
discrete divergence of Ampere's law to get

.. math::
  -\mathbf{G}^T\mathbf{C}^T \mathbf{M}_{\mu^{-1}}^f \tilde{\mathbf{b}} + \mathbf{G}^T\mathbf{M}_{\sigma}^e\mathbf{G}\tilde{\phi} = - \mathbf{G}^T\tilde{\mathbf{s}}.
  :label: divAmpere

Since we used a mimetic discretization method,
:math:`\mathbf{G}^T\mathbf{C}^T` is identically zero, which corresponds the
vector calculus identity
:math:`\boldsymbol{\nabla\cdot}\left(\boldsymbol{\nabla\times}\mathbf{b}\right) = 0`.
Hence the first term of equation
:eq:`divAmpere` vanishes, which yields the discrete DC potential equation

.. math::
  \mathbf{G}^T\mathbf{M}_{\sigma}^e\mathbf{G} \tilde{\phi} = -\mathbf{G}^T\tilde{\mathbf{s}}.
  :label: DCresDiscrete



