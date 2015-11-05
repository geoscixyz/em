.. _boundary_conditions:

Boundary conditions:
====================

There are a variety of ways to formulate the solution for the EM problem.  Relevant boundary conditions are needed for 
(a) Potentials
(b) Electric fields
(c) Current density

Consider the following basic homogeneous equations in the stady state form 
.. math::
	\mathbf{\nabla \times} \mathbf{E} = \matbf{0},
	:label: cEe0

.. include:: ../equation_bank/gauss_electric_frequency.rst

.. math::
	\mathbf{\nabla \cdot} \mathbf{J} = \matbf{0},
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
% Caption: where \hat{n} denotes the unitary normal vector and \hat{t} enotes the tangential unit vector


Boundary conditions for the electric field:
-------------------------------------------
To derive the boundary conditions for the electric field, we apply standard `pill-box' arguments to equation (1), that is, integrating equation (1) leads to

% Figure 2 - make a figure of a pill box
% Caption - Pill box

		\int_{area} \curl vE da = \int E \cdot dl
% there is more math development here to be included

This implies that
		(vE_2 - vE_1) \cdot t = 0

That is, the tangential component of the electric field is continuous.  We denote this fact as
		E_{2t} = E_{1t}		 


Boundary conditions for the electric current displacement:
-------------------------------------------
To derive the boundary conditions for the electric current displacement



