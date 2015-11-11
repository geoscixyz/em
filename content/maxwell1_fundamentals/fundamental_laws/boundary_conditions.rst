.. _boundary_conditions:

Boundary Conditions
===================

There are a variety of ways to formulate the solution for the EM problem.  Relevant boundary conditions are needed for 

(a) Electric fields
(b) Magnetic fluxes 
(c) Electrical current displacement
(d) Eletrical current density
(e) Magnetic fields

TODO:
-) Complete (b)
-) Complete (e)

Consider the following equations 

.. include:: ../../equation_bank/faradays_law_diff_time.rst

.. math::
    \boldsymbol{\nabla \cdot} \mathbf{d} = \rho_f,
    :label: gauss_electric_frequency

.. math::
	\boldsymbol{\nabla \cdot} \mathbf{j} = 0,
	:label: dJe0

.. include:: ../../equation_bank/gauss_magnetic_time.rst

	
and the constitutive relations for a linear isotropic medium given by

.. math::
	\mathbf{d} = \varepsilon \mathbf{e},
	:label: DepsE

.. math::
	\mathbf{j} = \sigma \mathbf{e}.
	:label: JsigE

Now, let us consider a two layer media where each layer has its corresponding physical properties (electrical conductivity (:math:`\sigma`) and electrical permittivity (:math:`\varepsilon`)), electric field (:math:`\mathbf{e}`), electric current displacement (:math:`\mathbf{d}`), and electrical current density (:math:`\mathbf{j}`).  The subindices 1 and 2 denote dependency on layer 1 and layer 2, respectively.  The orange rectangle represents a Gaussian pill-box of cross-sectional area A with boundary given by the curve C. 

.. figure:: images/BC_1.png
	:align: center

Fig 1.  Two layer media. Orange rectangle represent a Gaussian pill-box. 

Boundary Conditions for the Tangential Component of the Electric Field
----------------------------------------------------------------------
TO DO:
-) Update notation in figure (Luz)
-) Apply Faraday's law to (1) to get continuity of E in tangential component. (Patrick)

To derive the boundary conditions for the electric field (:math:`\mathbf{e}`), we apply `Stokes theorem`_ to equation (1) which leads to

.. _Stokes theorem: https://en.wikipedia.org/wiki/Stokes%27_theorem

.. math::
		\int_{A} \boldsymbol{\nabla \times} \mathbf{e} \boldsymbol{\cdot} \mathbf{\hat{n}} \, da = \oint_{C} \mathbf{e} \boldsymbol{\cdot} \mathbf{\hat{n}} dl,
		:label: intpillbox	

where :math:`A` denotes the area in the Gaussian pill-box illustrated in Figure 1, and :math:`C` denotes the curve enclosing such area (i.e. :math:`C=\partial A`).

Expression (6) implies that

.. math::
		(\mathbf{e}_2 - \mathbf{e}_1) \cdot \mathbf{\hat{t}} = \mathbf{0}.


That is, the tangential component of the electric field is continuous.  We denote this fact as

.. math::
		\mathbf{e}_{2t} = \mathbf{e}_{1t}.		 
		:label: Etcontinuous

Boundary Conditions for the Magnetic Flux
-----------------------------------------



Boundary Conditions for the Electric Current Displacement
---------------------------------------------------------

To derive boundary conditions for the electric current displacement (:math:`\mathbf{d}`), we apply the `Divergence theorem`_ to equation (2) yielding to

.. _Divergence theorem: https://en.wikipedia.org/wiki/Divergence_theorem

.. math::
		\int_V \boldsymbol{\nabla\cdot}\mathbf{d} \, dv &= \int_{S} \rho_f(\mathbf{r}) \, da,\\
		\int\mathbf{d}\cdot\hat{\mathbf{n}}\, da &= S (\mathbf{d}_2-\mathbf{d}_1)\cdot\hat{\mathbf{n}} \\
		 & = S\,\tau_f,
		:label: DonPillBox

where :math:`\tau_f` is a surface charge density, :math:`\mathbf{r}` denotes (DO YOU GUYS KWNO WHO IS r ???), :math:`V` is the volume enclosed by the green cylinder in Figure 1, and :math:`S` denotes the surface corresponding to the boundary of V (i.e. :math:`S=\partial V`).

Expression (8) implies that  

.. math::	
		 (\mathbf{d}_2-\mathbf{d}_1)\cdot\hat{\mathbf{n}} = \tau_f.
		 :label: Dndiscontinuous
		

That is, the normal component of the electric current displacement can be discontinuous if there is a free charge on the surface. 

Observe that when the materials are not polarizable or if :math:`\varepsilon` is constant, from equation (4) we have that

.. math::
		\mathbf{d}_2 &= \varepsilon_0\mathbf{e}_2,\\
		\mathbf{d}_1 &= \varepsilon_0\mathbf{e}_1, 

Hence,	

.. math::
		(\mathbf{e}_2-\mathbf{e}_1)\cdot\hat{\mathbf{n}} = \frac{\tau_f}{\varepsilon_0}. 	
		:label: EnotCont

Expression (10) implies that the normal component of the electric field can be discontinuous when there is free charge particularly on the surface.  In fact it can be discontinuous if there are free charges anywhere.  The previous statement can be shown by using :ref:`Gauss's law for electric fields<gauss_electric>`

.. math::
		\boldsymbol{\nabla\cdot}\mathbf{e} &= \frac{Q}{\varepsilon_0}, \quad\quad \text{ (Q is a total charge)}\\
		\text{so } (\mathbf{e}_2-\mathbf{e}_1)\cdot\hat{\mathbf{n}} &= \frac{Q}{\varepsilon_0}.
		:label: EnotCont2

Boundary Conditions for the Electric Current Density
----------------------------------------------------

Once again, we apply the `Divergence theorem`_ to equation (3) which yields to

.. math::
		\int_V \boldsymbol{\nabla\cdot}\mathbf{j} \, dv &= \int_{S} 0 \, da,\\

where V is the volume enclosed by the green cylinder in Figure 1 and S is its boundary. Hence, the above expression implies that

.. math::
		(\mathbf{j}_2-\mathbf{j}_1)\cdot\hat{\mathbf{n}} &= 0\\
		\mathbf{j}_{2n} &= \mathbf{j}_{1n}. 
		:label: JnCont

In other words, the normal component of current density is continuous.

Boundary Conditions for the Magnetic Field
-----------------------------------------

