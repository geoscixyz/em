.. _maxwell2_dc_boundary_conditions:

Boundary Conditions
===================

.. _maxwell2_dc_boundary_conditions_dcr:

DCR
---

In :ref:`steady_state_equations`, we introduced the governing equations for
the DCR problem

.. include:: ../../equation_bank/dcr_fwd.rst

In order to construct a boundary value problem to determine the potential for
a given source and conductivity model, :eq:`dcr_fwd` must be supplemented by
appropriate boundary conditions. While different boundary conditions are
possible, we will only discuss the common case of applying a homogeneous
Neumann condition at the earth's surface and homogeneous Dirichlet conditions
elsewhere.

To derive the Dirichlet condition at the sides and bottom of the domain, it is
first important to note that electrical potential is only unique up to an
arbitrary constant, which is determined by convention. DC surveys measure
potential differences so this is not important for field measurements but it
is important in solving :eq:`dcr_fwd`. We use the standard convention that the
potential is zero infinitely far from all charges and currents. In solving for
the discrete approximation to the potential, we make the boundaries at the
sides and bottom of the domain far enough from any sources that the potential
is approximately zero there. We then use homogeneous Dirichlet conditions on
those boundaries in solving the discrete problem.

We derive the earth surface boundary condition from the fact that currents
cannot flow into the air. Mathematically this can be stated as

.. math::
  \mathbf{j}\cdot \hat{\mathbf{n}} = 0 \qquad \text{on} \quad \partial_s \Omega,

where :math:`\partial_s \Omega` indicates the surface of the earth and
:math:`\hat{\mathbf{n}}` is the unit surface normal vector. Applying Ohm's law
in the earth, this becomes

.. math::
  \sigma \mathbf{e}\cdot\hat{\mathbf{n}} = 0. 

Since :math:`\sigma` must be strictly positive in the earth, we divide by it
to give

.. math::
  \mathbf{e}\cdot\hat{\mathbf{n}} = 0 

at the surface. Finally, writing the electric field as the negative gradient
of the electric potential gives the surface boundary condition

.. math::
  (\boldsymbol{\nabla}\phi) \cdot \hat{\mathbf{n}} = 0 \qquad \text{on} \quad \partial_s \Omega.

