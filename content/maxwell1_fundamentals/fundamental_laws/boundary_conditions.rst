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
-) Add base equations (from upper sections)
-) Complete (b)
-) Complete (e)

Consider the following basic homogeneous equations in the stady state form 

.. math::
	\boldsymbol{\nabla \times} \mathbf{E} = \mathbf{0},
	:label: cEe0

.. math::
    \boldsymbol{\nabla \cdot} \mathbf{D} = \rho_f,
    :label: gauss_electric_frequency

.. math::
	\boldsymbol{\nabla \cdot} \mathbf{J} = \mathbf{0},
	:label: dJe0
	
and the constitutive relations for a linear isotropic medium given by

.. math::
	\mathbf{D} = \varepsilon \mathbf{E},
	:label: DepsE

.. math::
	\mathbf{J} = \sigma \mathbf{E}.
	:label: JsigE

Now, let us consider a two layer media where each layer has its corresponding physical properties (electrical conductivity (:math:`\sigma`) and electrical permittivity (:math:`\varepsilon`)), electric field (:math:`\mathbf{E}`), electric current displacement (:math:`\mathbf{D}`), and electrical current density (:math:`\mathbf{J}`).  The subindices 1 and 2 denote dependency on layer 1 and layer 2, respectively.  The orange rectangle represents a Gaussian pill-box of cross-sectional area A with boundary given by the curve C. 

.. figure:: images/BC_1.png
	:align: center

Fig 1.  Two layer media. Orange rectangle represent a Gaussian pill-box. 

Boundary Conditions for the Tangential Electric Field
-----------------------------------------------------
TO DO:
-) Change notation to time domain (lower case)  (Luz)
-) Change equation (1) to Faraday's law.   (Luz)
-) Update notation in figure
-) Apply Faraday's law to (1) to get continuity of E in tangential component. (Patrick)

To derive the boundary conditions for the electric field (:math:`\mathbf{E}`), we apply `Stokes theorem`_ to equation (1) which leads to

.. _Stokes theorem: https://en.wikipedia.org/wiki/Stokes%27_theorem

.. math::
		\int_{A} \boldsymbol{\nabla \times} \mathbf{E} \boldsymbol{\cdot} \mathbf{\hat{n}} \, da = \oint_{C} \mathbf{E} \boldsymbol{\cdot} \mathbf{\hat{n}} dl,
		:label: intpillbox	

where :math:`A` denotes the area in the Gaussian pill-box illustrated in Figure 1, and :math:`C` denotes the curve enclosing such area (i.e. :math:`C=\partial A`).

Expression (6) implies that

.. math::
		(\mathbf{E}_2 - \mathbf{E}_1) \cdot \mathbf{\hat{t}} = \mathbf{0}.


That is, the tangential component of the electric field is continuous.  We denote this fact as

.. math::
		\mathbf{E}_{2t} = \mathbf{E}_{1t}.		 
		:label: Etcontinuous

Boundary Conditions for the Magnetic Flux
-----------------------------------------



Boundary Conditions for the Electric Current Displacement
---------------------------------------------------------

To derive boundary conditions for the electric current displacement (:math:`\mathbf{D}`), we apply the `Divergence theorem`_ to equation (2) yielding to

.. _Divergence theorem: https://en.wikipedia.org/wiki/Divergence_theorem

.. math::
		\int_V \boldsymbol{\nabla\cdot}\mathbf{D} \, dv &= \int_{S} \rho_f(\mathbf{r}) \, da,\\
		\int\mathbf{D}\cdot\hat{\mathbf{n}}\, da &= S (\mathbf{D}_2-\mathbf{D}_1)\cdot\hat{\mathbf{n}} \\
		 & = S\,\tau_f,
		:label: DonPillBox

where :math:`\tau_f` is a surface charge density, :math:`\mathbf{r}` denotes (DO YOU GUYS KWNO WHO IS r ???), :math:`V` is the volume enclosed by the green cylinder in Figure 1, and :math:`S` denotes the surface corresponding to the boundary of V (i.e. :math:`S=\partial V`).

Expression (8) implies that  

.. math::	
		 (\mathbf{D}_2-\mathbf{D}_1)\cdot\hat{\mathbf{n}} = \tau_f.
		 :label: Dndiscontinuous
		

That is, the normal component of the electric current displacement can be discontinuous if there is a free charge on the surface. 

Observe that when the materials are not polarizable or if :math:`\varepsilon` is constant, from equation (4) we have that

.. math::
		\mathbf{D}_2 &= \varepsilon_0\mathbf{E}_2,\\
		\mathbf{D}_1 &= \varepsilon_0\mathbf{E}_1, 

Hence,	

.. math::
		(\mathbf{E}_2-\mathbf{E}_1)\cdot\hat{\mathbf{n}} = \frac{\tau_f}{\varepsilon_0}. 	
		:label: EnotCont

Expression (10) implies that the normal component of the electric field can be discontinuous when there is free charge particularly on the surface.  In fact it can be discontinuous if there are free charges anywhere.  The previous statement can be shown by using :ref:`Gauss's law for electric fields<gauss_electric>`

.. math::
		\boldsymbol{\nabla\cdot}\mathbf{E} &= \frac{Q}{\varepsilon_0}, \quad\quad \text{ (Q is a total charge)}\\
		\text{so } (\mathbf{E}_2-\mathbf{E}_1)\cdot\hat{\mathbf{n}} &= \frac{\rho_t}{\varepsilon_0}.
		:label: EnotCont2

Boundary Conditions for the Electric Current Density
----------------------------------------------------

Once again, we apply the `Divergence theorem`_ to equation (3) which yields to

.. math::
		\int_V \boldsymbol{\nabla\cdot}\mathbf{J} \, dv &= \int_{S} 0 \, da,\\

where V is the volume enclosed by the green cylinder in Figure 1 and S is its boundary. Hence, the above expression implies that

.. math::
		(\mathbf{J}_2-\mathbf{J}_1)\cdot\hat{\mathbf{n}} &= 0\\
		\mathbf{J}_{2n} &= \mathbf{J}_{1n}. 
		:label: JnCont

In other words, the normal component of current density is continuous.

