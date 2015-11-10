.. _boundary_conditions:

Boundary Conditions
===================

There are a variety of ways to formulate the solution for the EM problem.  Relevant boundary conditions are needed for 

(a) Potentials
(b) Electric fields
(c) Current density

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

Boundary Conditions for the Electric Field
------------------------------------------
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

Boundary Conditions for Potentials
----------------------------------

Electric potential (:math:`\psi`) is defined

.. math::
		\mathbf{E} = \boldsymbol{\nabla\cdot}\psi
		:label: potentialDef

We know that electric potential is continuous at a boundary  :math:`\psi_1 = \psi_2` (Daniel:  From where do we know this?? Can you include a reference, please?). To determine the relation for the normal derivative of the potential across a boundary, we start from the continuity of the normal component of the current density (see equation (12))

.. math::
		\mathbf{J}_{2n} = \mathbf{J}_{1n},
		:label: curCont

Applying Ohm's law, (see equation (5)), to the previous expression we obtain

.. math::
		\sigma_2\mathbf{E}_{2n} = \sigma_1\mathbf{E}_{1n}.
		:label: aux1

Now, from the definition of electric potential (see equation (13)) and using this definition in equation (14), gives us the relation of the normal derivative of the potential across a boundary between two regions with different properties.

.. math::
		\sigma_2\frac{\partial \psi_2}{\partial n} &= \sigma_1\frac{\partial \psi_1}{\partial n}.
		:label: potDerivRelation


Charge Buildup at a Boundary
----------------------------

If we have a boundary between two media with different conductivities, as in the figure below  

.. image:: images/boundryChargeBuildup.PNG
   :scale: 75 %
   :align: center

then from the arguments presented in the previous section, we can determin the buildup of charges on boundaries between regions with differing conductivities. Starting from the continuity of the normal component of the current density (see equation (12))

.. math::
		\mathbf{J}_{2n} &= \mathbf{J}_{1n},\\
		:label: curCont

and using Ohm's law, (see equation (5)) we get

.. math::
		\sigma_2\mathbf{E}_{2n} &= \sigma_1\mathbf{E}_{1n}.
		:label: ohmsLawCurCont


Then, using to boundry conditions for the electric field (see equation (10)) we get

.. math::
		\mathbf{E}_{2n}-\mathbf{E}_{1n}\ &= \frac{\tau_f}{\varepsilon_0}.
		:label: Ebound

Solving the system made by (18) and (19), we get

.. math::
		\mathbf{E}_{2n} &= \frac{\sigma_1}{\sigma_2}\mathbf{E}_{1n}\quad\text{from (18)}\\
		\text{into (19)}\quad \Big(\frac{\sigma_1}{\sigma_2}-1\Big)\mathbf{E}_{1n} &= \frac{\tau_f}{\varepsilon_0}\\
		\frac{\tau_f}{\varepsilon_0} &= \Big(\frac{\sigma_1}{\sigma_2}-1\Big)\mathbf{E}_{1n}.
		:label: chargeBuildup

Which quantifies the charge buildup on a boundary. So in case 1, were the resistive layer is on top i.e. :math:`\sigma_1 < \sigma_2`

.. image:: images/resOnTop.PNG
   :scale: 75 %
   :align: center

.. math:: 
		\sigma_1 < \sigma_2 \implies \tau_f <0

.. image:: images/negChargeBuildup.PNG
   :scale: 75 %
   :align: center

We get a buildup of negative charges on the boundary, and in case 2, were the resistive layer is on top i.e. :math:`\sigma_1 > \sigma_2` 

.. image:: images/condOnTop.PNG
   :scale: 75 %
   :align: center

.. math:: 
		\sigma_1 > \sigma_2 \implies \tau_f >0

.. image:: images/posChargeBuildup.PNG
   :scale: 75 %
   :align: center

We get a buildup of positive charges on the boundary.
