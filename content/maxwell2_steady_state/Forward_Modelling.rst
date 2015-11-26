.. _Forward_Modelling:

DC Forward Modelling
====================

A DC resistivity survey is ultimately an electromagnetic phenomenon and is therefore governed by Maxwell's equations. However, the fact that the ground is energized with a time invariant direct current allows us to use a much simpler model. 

Deriving the DC Equations
-------------------------

We can start from time domain differential form of the Ampere-Maxwell equation equation (equation (5) on :ref:`ampere_maxwell`)

.. math::
    \boldsymbol{\nabla} \times \mathbf{h} = \mathbf{j}_{total} + \frac{\partial \mathbf{d}}{\partial t},
    :label: ampere_maxwell_differential_hjd

where :math:`\mathbf{h}` is the magnetic field, :math:`\mathbf{j}_{total}` is the total current in the system, and :math:`\mathbf{d}` is the electric displacement. We can divide up :math:`\mathbf{j}_{total}` as follows

.. math::
    \mathbf{j}_{total} = \sigma\mathbf{e} + \mathbf{j}_{source},
    :label: jsep

which states that the total current densisty can be divided into the current in the ground (:math:`\sigma\mathbf{e}` due to Ohm's law) and the current in the source wires (:math:`\mathbf{j}_{source}`). Using :eq:`jsep` and the quasi static assumption we can write :eq:`ampere_maxwell_differential_hjd` as

.. math::
    \boldsymbol{\nabla} \times \mathbf{h} - \sigma\mathbf{e} = \mathbf{j}_{source}.
    :label: ampere_maxwell_differential_jsep

Now, since we are in the steady state case we know that the time derivatives all have to be zero, so we can invoke Faraday's law, that is

.. include:: ../equation_bank/faraday_time.rst

to say that :math:`\mathbf{e}` has no curl, in other words it is a potential field. In particular, this means that

.. math::
    \mathbf{e} = -\boldsymbol{\nabla}\phi,
    :label: epot

where :math:`\phi` is the electric potential. This allows us to write :eq:`ampere_maxwell_differential_jsep` as

.. math::
    \boldsymbol{\nabla} \times \mathbf{h} + \sigma\boldsymbol{\nabla}\phi = \mathbf{j}_{source}.
    :label: ampere_maxwell_differential_phi

Taking divergence in both sides of :eq:`ampere_maxwell_differential_phi` leads to

.. math::
    \boldsymbol{\nabla} \cdot \sigma\boldsymbol{\nabla}\phi = \boldsymbol{\nabla}\cdot\mathbf{j}_{source},
    :label: DCfwd

which is the equation for DC. 
    
Boundary Conditions for the DC problem
--------------------------------------

Electrical potential is unique up to a constant, which is determined by convention. DC surveys measure potential differences so this is not important for field measurements but it is important in solving the DC equations for :math:`\phi`. We use the standard convention that the potential is zero infinitely far from all charges and currents. In solving for the discrete approximation to the potential, we make the boundaries at the sides and bottom of the domain far enough from any sources that the potential is approximately zero there. We then consider homogeneous Dirichlet conditions on those boundaries in solving the discrete problem.

We derive the boundary condition at the surface from conservation of charge and the fact that currents cannot flow into the air. Mathematically this can be stated as

.. math::
  \mathbf{j}\cdot \hat{\mathbf{n}} = 0 \qquad \text{on} \quad \partial_s \Omega,

where :math:`\partial_s \Omega` indicates the surface of the earth. Applying Ohm's law in the earth this becomes

.. math::
  \sigma \mathbf{e}\cdot\hat{\mathbf{n}} = 0 

Since :math:`\sigma` must be non-zero in the earth, we divide by it to give

.. math::
  \mathbf{e}\cdot\hat{\mathbf{n}} = 0 

at the surface. Finally, writing the electric field as the negative gradient of potential, we have

.. math::
  (\boldsymbol{\nabla}\phi) \cdot \hat{\mathbf{n}} = 0 \qquad \text{on} \quad \partial_s \Omega.

In other words, we use a homogeneous Neumann boundary condition on the surface boundary. 

Charge Buildup at Boundaries
----------------------------

Consider the situation in the figure below, at a boundary between two media with different conductivities but both with dielectric permittivity :math:`\varepsilon = \varepsilon_0`.  

.. image:: images/boundryChargeBuildup.PNG
   :scale: 75 %
   :align: center
   
We will show how charge buildup occurs at such an interface using conservation of charge, Ohm's law and the interface condition on the normal component of electric displacement. Recall the integral equation expressing conservation of charge

.. math::
    \int_A \mathbf{j} \cdot da =  - \frac{d}{dt} \int_V \rho dv = - \frac{dQ}{dt}. 
    :label: charge_conservation_integral

In steady state, :math:`dQ/dt = 0`. Taking the surface of integration as our standard Gaussian pillbox (see boundary conditions page), the integral can be evaluated as

.. math::
		(\mathbf{j}_2-\mathbf{j}_1)\cdot\hat{\mathbf{n}} &= 0\\
		j_{2n} &= j_{1n}. 
		:label: JnCont

where :math:`j_{1n}` and :math:`j_{2n}` are the normal components of current density on either side of the interface. So we see that direct current is continuous across material interfaces. If we assume, linear, isotropic earth materials, we can apply Ohm's law (:math:`\mathbf{j}_f = \sigma\mathbf{e}`) to this equation, yielding

.. math::
		\sigma_2\mathbf{e}_{2n} &= \sigma_1\mathbf{e}_{1n}.
		:label: ohmsLawCurCont

Since we assume that both materials have dielectric permittivity :math:`\varepsilon = \varepsilon_0`, we can write the interface condition on the normal component of electric displacement in terms of the electric field

.. math::
		\mathbf{e}_{2n}-\mathbf{e}_{1n}\ &= \frac{\tau_f}{\varepsilon_0},
		:label: Ebound
   
where :math:`\tau_f` is the free surface charge density on the boundary. 

combining the two previous equations we can express the charge buildup in terms of the ratio of the two conductivities

.. math::
		\frac{\tau_f}{\varepsilon_0} &= \Big(\frac{\sigma_1}{\sigma_2}-1\Big)\mathbf{e}_{1n}.
		:label: chargeBuildup

In the case where current is flowing from a resistive layer to a more conductive layer (i.e. :math:`\sigma_2 > \sigma_1`),

.. image:: images/resOnTop.PNG
   :scale: 75 %
   :align: center

.. math:: 
		\sigma_1 < \sigma_2 \implies \tau_f <0

.. image:: images/negChargeBuildup.PNG
   :scale: 75 %
   :align: center

We get a buildup of negative charges on the boundary, and in the case where flow is from a resistive layer to a conductive layer (i.e. :math:`\sigma_1 > \sigma_2`) 

.. image:: images/condOnTop.PNG
   :scale: 75 %
   :align: center

.. math:: 
		\sigma_1 > \sigma_2 \implies \tau_f >0

.. image:: images/posChargeBuildup.PNG
   :scale: 75 %
   :align: center

We get a buildup of positive charges on the boundary.


Discretization
--------------------------

For an arbitrary conductivity model, equation xx cannot be solved exactly. In order to simulate a geophysical survey over an earth with a complicated conductivity distribution we need to solve an approximate discrete form of equation xx. Equation 4 

The equation can be discretized directly using, for example, standard finite difference, finite element, or finite volume methods[need reference]. However if we use a mimetic discretization of the full Maxwell equations, we can derive a discretization of the DC equation from the discrete Maxwell equations. For a brief discussion of the discretization of Maxwell's equation, see the section :ref:`Maxwell_Discretization` on this website. Our notation follows that page.

The discrete potential field condition is :math:`\tilde{\mathbf{e}} = \mathbf{G}\tilde{\phi}`. Substituting that into the discrete time-domain quasi-static Ampere equation gives

.. math::
  \mathbf{C}^T \mathbf{M}_{\mu^{-1}}^f \tilde{\mathbf{b}} - \mathbf{M}_{\sigma}^e\mathbf{G}\tilde{\phi} = \tilde{\mathbf{s}}.
  
where the tilde symbol denotes a grid function. Using the fact that the discrete divergence operator is equal to :math:`-\mathbf{G}^T`, we take the discrete divergence of Ampere's law to get 

.. math::
  -\mathbf{G}^T\boldsymbol{\nabla \times} \mu^{-1} \tilde{\mathbf{b}} - \mathbf{G}^T\mathbf{M}_{\sigma}^e\mathbf{G}\tilde{\phi} = \tilde{\mathbf{s}}.
  :label: divAmpere

Our discretization preserves the identity :math:`\boldsymbol{\nabla\cdot}\left(\boldsymbol{\nabla\times}\mathbf{b}\right) = 0` so we can throw away the first term of equation :eq:`divAmpere` to get the discrete DC potential equation

.. math::
  \mathbf{G}^T\mathbf{M}_{\sigma}^e\mathbf{G} \tilde{\phi} = -\mathbf{G}^T\tilde{\mathbf{s}}.
  :label: DCresDiscrete

  