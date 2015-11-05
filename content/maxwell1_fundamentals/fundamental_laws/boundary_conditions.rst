.. _boundary_conditions:

Boundary conditions
===================

There are a variety of ways to formulate the solution for the EM problem.  Relevant boundary conditions are needed for 

(a) Potentials
(b) Electric fields
(c) Current density

Consider the following basic homogeneous equations in the stady state form 

.. math::
	\boldsymbol{\nabla \times} \mathbf{E} = \mathbf{0},
	:label: cEe0

.. include:: ../equation_bank/gauss_electric_frequency.rst

.. math::
	\boldsymbol{\nabla \cdot} \mathbf{J} = \mathbf{0},
	:label: dJe0
	
and the constitutive relations for the linear isotropic medium given by

.. math::
	\mathbf{D} = \varepsilon \mathbf{E},
	:label: DepsE

.. math::
	\mathbf{J} = \sigma \mathbf{E},
	:label: JsigE

Now, we consider a two layer media as illustrated in the figure below


% Figure 1  - describe a two layered media

Boundary conditions for the electric field
------------------------------------------

To derive the boundary conditions for the electric field, we apply `Stokes theorem`_ to equation (1) which leads to

.. _Stokes theorem: https://en.wikipedia.org/wiki/Stokes%27_theorem

% Figure 2 - make a figure of a pill box

.. math::
		\int_{A} \boldsymbol{\nabla \times} \mathbf{E} \, da = \oint_{C} \mathbf{E} \cdot dl,
		:label: intpillbox	

where :math:`A` denotes the area enclosed by the pill box in Figure 2 and :math:`C` denotes the curve enclosing such area (i.e. :math:`C=\partial A`).

Expression (5) implies that

.. math::
		(E_2 - E_1) \cdot \mathbf{\hat{t}} = 0


That is, the tangential component of the electric field is continuous.  We denote this fact as

.. math::
		E_{2t} = E_{1t}.		 
		:label: Etcontinuous

Boundary conditions for the electric current displacement
---------------------------------------------------------

To derive the boundary conditions for the electric current displacement



