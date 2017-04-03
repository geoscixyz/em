.. _solving_maxwells_equations:

Solving Maxwell's Equations in Practice
=======================================

.. purpose::

    Here, we provide a general overview on how to solve Maxwell's equations in practice. The approaches used to solve specific problems are covered later in EM GeoSci.


The practice of solving Maxwell's equations for an applied problem can be broken into three parts:

    1) **Defining the problem:** here, Maxwell's equations are modified, reformulated or approximated to suite a particular physical problem.
    2) **Setting boundary and initial conditions:** these are invoked so that solutions to Maxwell's equations are uniquely solved for a particular application.
    3) **Solving with analytic or numerical approaches:** once the problem, boundary conditions and initial conditions have been defined, the final solution is obtained through analytic or numerical approaches.

.. _solving_maxwells_equations_problem:

Defining the Problem
--------------------

In ":ref:`quick_guide_maxwell`", we presented general formulations for Maxwell's equations. In most cases however, Maxwell's equations can be modified, reformulated or approximated to simplify an applied problem. Failure to choose an appropriate formulation may result in the problem being difficult or impossible to solve using current means. 

**Examples (to be discussed in more detail throughout EM GeoSci):**

- :ref:`DC Resistivity:<dcr_index>`

.. math::
	\nabla \cdot \sigma \phi = \nabla \cdot \mathbf{J_s}

where :math:`\mathbf{J_s}` is an electrical current source and :math:`\phi` is a scalar potential such that :math:`\mathbf{E} = -\nabla \phi`.

- :ref:`Frequency Domain Electromagnetics:<airborne_fdem_index>`

.. math::
	\begin{align}
	\nabla\times\nabla\times\mathbf{E} + i\omega \mu_0 \sigma \mathbf{E} &= - i\omega \mu_0 \mathbf{J_s}\\
	\nabla\times\mathbf{E} + i\omega \mathbf{B} &= 0
	\end{align}

where :math:`\mathbf{J_s}` is an electrical current source. For this problem, the magnetic properties of the Earth are typically neglected (i.e. :math:`\mu\approx \mu_0`). Furthermore, we operate in the quasi-static regime (:math:`\sigma \gg \omega \varepsilon`), allowing us to neglect electric displacement.

- :ref:`Time Domain Electromagnetics:<airborne_tdem_index>`

.. math::
	\begin{align}
	\nabla\times\nabla\times\mathbf{e} + \mu_0 \sigma \frac{\partial \mathbf{e}}{\partial t} &= - \mu_0 \frac{\partial \mathbf{j_s}}{\partial t}\\
	\nabla\times\mathbf{e} + \frac{\partial \mathbf{b}}{\partial t} &= 0
	\end{align}

where :math:`\mathbf{j_s}` is an electrical current source. This equation is the time-dependent equivalent to the one used in frequency domain electromagnetics.

- :ref:`Time-Dependent Wave Equation:<time_domain_equations>`

.. math::
	\nabla^2 \mathbf{e} - \frac{1}{v^2} \frac{\partial^2 \mathbf{e}}{\partial t^2} = \mu \frac{\partial \mathbf{j_s}}{\partial t}

where :math:`\mathbf{j_s}` defines an electrical current source and :math:`v=1/\!\sqrt{\mu\varepsilon}`. For this problem, electric displacement dominates the current density and we can use the wave regime approximation (:math:`\sigma \ll \omega \varepsilon`). The Laplacian operator results from assuming the physical properties defining discrete regions within the domain are homogeneous.


.. note::
	These are only a few examples. Other problems in electromagnetic geosciences may require different formulations. Additionally, there may be multiple formulations of Maxwell's equations which can be used to solve a particular problem. It is up to the researcher to choose the one which is the most effective.

Boundary and Initial Conditions
-------------------------------

Boundary Conditions
^^^^^^^^^^^^^^^^^^^

.. figure:: images/domain.png
		:align: right
		:figwidth: 35%
		:name: fig_solving_maxwells_domain

		Illustration of domain and boundary.

Boundary conditions ensure that a the problem is well-posed; that is, it has a unique solution. This is necessary when using Maxwell's equations to solve applied problems in electromagnetic geosciences. Differential equations corresponding to a physical problem are defined within a region, or "domain" (denoted by :math:`\Omega`). To make the problem well-posed, boundary conditions are applied to the edges of this domain (denoted by :math:`\partial \Omega`). There are three types of boundary conditions, which are listed below:

**Dirichlet Boundary Conditions:** Dirichlet boundary conditions are by far the most straightforward and easy to implement. Dirichlet conditions directly define the value of the solution on the boundary, i.e.:

.. math::
	 \mathbf{F(r)} \, \Big |_{\partial \Omega} = \mathbf{g(r)}

where :math:`\mathbf{F}` is some vector field/flux defined within the domain, :math:`\mathbf{g}` is a spatially-dependent function and :math:`\mathbf{r} = (x,y,z)`. In many cases, the Dirichlet condition is given as a constant value; such as, all fields go to zero at the boundary.

**Neumann Boundary Conditions:** Neumann boundary conditions are imposed by specifying the spatial derivatives of the solution on the boundary. Commonly, Neumann conditions define the directional derivatives normal to the surface of the domain, i.e.:

.. math::
	\frac{\partial F_n}{\partial \mathbf{n}} \bigg |_{\partial \Omega} = \mathbf{g(r)}

where :math:`\mathbf{n}` is the unit vector direction perpendicular to the domain boundary :math:`\partial \Omega`, :math:`F_n = \mathbf{F \cdot \hat n}\;` is the component of a vector field/flux :math:`\mathbf{F}` along :math:`\mathbf{n}`, :math:`\mathbf{g}` is a spatially-dependent function and :math:`\mathbf{r} = (x,y,z)`. Physically, Neumann conditions are used to define the rate of flux through the boundary. This is frequently applied to problems which behave according to the heat equation.

**Robin (Mixed) Boundary Conditions:** Robin boundary conditions are a linear combination of Dirichlet and Neumann conditions, i.e.:

.. math::
	\bigg [ a\mathbf{F(r)} + b\frac{\partial F_n}{\partial \mathbf{n}} \bigg ] \Bigg |_{\partial \Omega} = \mathbf{g(r)}

where :math:`a` and :math:`b` are constants, :math:`\mathbf{n}` is the unit vector direction perpendicular to the domain boundary :math:`\partial \Omega`, :math:`F_n = \mathbf{F \cdot \hat n}\;` is the component of a vector field/flux :math:`\mathbf{F}` along :math:`\mathbf{n}`, :math:`\mathbf{g}` is a spatially-dependent function and :math:`\mathbf{r} = (x,y,z)`. Robin conditions are used when the rate of flux leaving the domain is dependent on the value of the field at the boundary.

Initial Conditions
^^^^^^^^^^^^^^^^^^

Initial conditions, in addition to boundary conditions, are required to solve time-dependent problems. Because the solutions to problems in the physical sciences are causal, the fields and fluxes at a particular time depend on the fields and fluxes at earlier times. Generally, we set initial conditions to define the solution at :math:`t=0` and we are interested in the bahaviour of the fields and fluxes at :math:`t\geq 0`. If the differential equation being solved has only first order derivatives in time, initial conditions may be given by:

.. math::
	\mathbf{F}(\mathbf{r},t) \big |_{t=0} = \mathbf{F_0}(\mathbf{r})

where :math:`\mathbf{F}` is a vector field/flux and :math:`\mathbf{F_0}` is the vector field/flux at :math:`t=0`. This type of condition would be needed to solve the time-domain electromagnetic equation presented in ":ref:`solving_maxwells_equations_problem`".

**Multiple Variables and Higher Order Time-Derivatives** 

If the differential equation contains multiple variables and higher order time-derivatives, we cannot solve the problem by simply setting initial conditions on the fields/fluxes at :math:`t=0`. Where :math:`k` is the highest order time-derivative found in the problem and :math:`n` is the number of time-dependent variables, we would require :math:`nk` total initial conditions to solve the problem. These initial conditions would take the form:

.. math::
	\frac{\partial^k \mathbf{F}}{\partial t^k} \bigg |_{t=0} = \mathbf{g^k(r)}

where :math:`\mathbf{F}` is the vector field/flux associated with variable :math:`n`, and :math:`\mathbf{g^k}` is a time-dependent function defined throughout the entire domain for the :math:`k^{th}` derivative. An example of this is the time-dependent wave equation presented in ":ref:`solving_maxwells_equations_problem`", which requires initial conditions on both :math:`\mathbf{e}` and its first-order time-derivative :math:`\partial \mathbf{e}/\partial t`.


Analytic and Numeric Solutions
------------------------------

Having formulated Maxwell's equations appropriately, as well as implementing boundary conditions and initial conditions, we can now solve the problem. There are two ways in which meaningful solutions can be obtained: analytically and numerically.

Analytic Solutions
^^^^^^^^^^^^^^^^^^

Ideally, one would derive an analytic solution. The problem becomes even more tractable if the solution is a closed-form expression; can be evaluated using a finite number of simple operations. Analytic solutions are generally only possible if the problem is simplified or exhibits a sufficient degree of geometric symmetry. We prefer analytic solutions because they are rapid to compute and explicitly show how the solution depends on its input variables.

Some solutions may be called **semi-analytic**. Semi-analytic solutions generally require the numerical evaluation of one or more integral functions, infinite series and/or limits. In this case, the solution is not a closed form expression. However, semi-analytic solutions can be very useful in practice.

Numerical Solutions
^^^^^^^^^^^^^^^^^^^

Numerical solutions are used to approximate the fields and fluxes to a desired level of accuracy. Numerical approaches are able to solve problems without relying on geometric symmetries. The process of obtaining a numerical solution can be broken down into three parts:

1) **Discretizing the Domain**
2) **Defining Fields and Fluxes**
3) **Applying Computer Algorithms**

A conceptual understanding of the aforementioned steps will be provided here. However, we will not present all the required background for solving these problems in practice; as it is extensive.

**Discretizing the Domain:**

In order to obtain a numerical solution, the domain is first discretized; i.e. subdivided into a collection of small volumes/regions. The collection of these volumes is called a 'mesh'. The physical properties within each volume are considered constant. The size and shape of each volume depends on the geometry of the problem, the size of the domain and the quantity of available computer memory. In :numref:`fig_solving_maxwells_discretization` a, we see a 1D discretization. The 1D discretization works well when, locally, the Earth displays a layered structure. For problems with irregular geometries, we may choose to use a 2D or 3D discretization (:numref:`fig_solving_maxwells_discretization` b). As a rule, the finer the discretization (as the dimensions of the cells decrease), the better our numerical solution will approximate the true solution to our problem.

.. figure:: images/discretization.png
		:align: center
		:figwidth: 100%
		:name: fig_solving_maxwells_discretization

		Discretization of Earth's structure. (a) 1D discretization. (b) 3D discretization.

**Defining Fields, Fluxes and Potentials**

.. figure:: images/Yee-cube-w-b.png
	:align: right
	:figwidth: 50%
	:name: fig_solving_maxwells_cube
	
	Definition of fields (:math:`\mathbf{E}`), fluxes (:math:`\mathbf{B}`) and potentials :math:`\phi` on a cubic cell.

The fields, fluxes and/or potentials pertaining to a particular problem are defined throughout the entire domain. Once the domain has been discretized however, evaluation of these quantities is only possible at a finite number of locations. The fields, fluxes and/or potentials being computed depend on the formulation of Maxwell's equations. The locations of these quantities for each cell depend both on the problem and the corresponding interface conditions. 

As an example, consider :numref:`fig_solving_maxwells_cube` where:

- the potential :math:`\phi` is defined on the cell nodes.
- cartesian components of the electric field :math:`\mathbf{E}` are defined on the cell edges.
- cartesian components of the magnetic flux density :math:`\mathbf{B}` are defined on the cell faces.
- physical properties :math:`\sigma` and :math:`\mu` are defined at the cell centers.

For problems involving :math:`\mathbf{E}` and :math:`\mathbf{B}`, this approach is ideal because it naturally respects the interface conditions for electromagnetic fields. Recall from ":ref:`maxwell1_fundamentals_interface_conditions_index`" that tangential components of the electric field and normal components of the magnetic flux are continuous are continuous across interfaces.

**Applying Computer Algorithms:**

As a final step, the numerical problem is commonly written as a linear system and solved using computer algorithms. The system can be formed using finite difference, finite volume or finite element methods. It generally takes the form:

.. math::
	\mathbf{A(m)u=q_s}

where :math:`\mathbf{u}` contains the fields and/or fluxes at discrete locations throughout the domain, :math:`\mathbf{q_s}` is a vector corresponding to the source term and :math:`\mathbf{A(m)}` is a linear operator that depends on the physical properties (:math:`\sigma,\mu,\varepsilon`) which make up a physical property model :math:`\mathbf{m}`. In electromagnetic geosciences, we are frequently interested in the "inverse problem". i.e., can we recover a physical property model :math:`\mathbf{m}` if :math:`\mathbf{u}` and :math:`\mathbf{q_s}` are known?




.. **aka: A (very) brief introduction to solving Maxwell's equations on a computer**

.. Maxwell's equations can only be solved exactly for a few special cases where
.. the conductivity model (and possibly the source-receiver geometry) has some
.. special structure and symmetry. To model an arbitrary geophysical survey over
.. an earth with topography and arbitrary conductivity, approximate methods that
.. can be implemented in a computer are required. These methods are known as
.. discretizations of Maxwell's equations because they break the earth into a set
.. of discrete volumes, or cells, with the physical properties held constant in
.. each cell.

.. It is possible to construct a discretization based on either the integral or
.. differential form of Maxwell's equations in the time and frequency domains.
.. For simplicity, we will restrict this discussion to discretizations of the
.. differential form of Maxwell's equations in the frequency domain.

.. Discrete approximations of Maxwell's equations used in geophysical prospecting
.. fall into three general categories based on the complexity of earth model they
.. can represent. The simplest discretizations assume that conductivity varies
.. only with depth but not laterally. The subsurface can then be divided into a
.. set of flat layers, with physical properties constant in each layer.

.. One may model a much larger class of geoelectric structures by assuming that
.. conductivity may vary with depth and in one lateral direction. This is known
.. as 2D modelling and requires dividing a two-dimensional (2D) section of the
.. earth into a set of discrete polygons, usually rectangles or triangles. This
.. provides a compromise between the computational difficulty of full three-
.. dimensional (3D) modelling and the limitations of 1D modelling. Of course, to
.. model the most complex terrain and conductivity variation, 3D modelling is
.. required. In 3D modelling the earth is divided into a set of discrete volumes,
.. usually cuboids or tetrahedra, with physical properties constant in each cell.
.. These three types of earth models, with their increasing complexity, are
.. illustrated in figure 1.

.. .. figure:: ../../images/1-2-3.png

..   Visualization of 1D, 2D, and 3D discretizations.

.. 1D modelling methods write the electric and magnetic fields due to a source
.. above a layered earth in terms of `Hankel transform
.. <https://en.wikipedia.org/wiki/Hankel_transform>`_ integrals that are
.. evaluated approximately. Two and three dimensional frequency domain
.. discretizations transform Maxwell's equations into a system of linear
.. algebraic equations for the electric field or magnetic flux density at
.. discrete points in space, at a single frequency. In all these methods there is
.. a tradeoff between solution accuracy and computational complexity. A finer
.. mesh will lead to a more accurate solution but also to a larger linear system
.. that must be solved to compute the fields or fluxes.

.. Now let us restrict our attention to three dimensions. There are several ways
.. to discretize Maxwell's equations in 3D, including finite difference, finite
.. element and finite volume approaches. Here we consider a mimetic finite volume
.. approach applied to a uniform grid. For a full description see chapters 3 and
.. 4 of :cite:`haber2014`. Consider Faraday's law and the quasi-static Ampere's law in the
.. frequency domain

.. .. math::
..   \boldsymbol{\nabla\times}\mathbf{E} = -i\omega\mathbf{B}
..   :label: FaradayAnal

.. .. math::
..   \boldsymbol{\nabla\times}\mu^{-1}\mathbf{B} - \sigma\mathbf{E} = \mathbf{J}_s,
..   :label: AmpereAnal

.. where :math:`\mathbf{J}_s` is the source current density and currents flowing
.. in the ground are represented using Ohm's law,
.. :math:`\mathbf{J}_{\text{ground}} = \sigma\mathbf{E}`. Almost all
.. discretizations of Maxwell's equations used in geophysical prospecting apply
.. the quasi-static approximation, meaning that they ignore the electric
.. displacement term :math:`-i\omega\mathbf{D}` in :ref:`Ampere's law
.. <ampere_maxwell>`. In broad terms, ignoring displacement is justified when the
.. area of interest is smaller than the source wavelength. See :cite:`ward1988` for more
.. information.

.. We divide the earth into a grid of cubic cells. The edges of the grid are
.. aligned with the axes of a cartesian coordinate system, as shown in figure 12.
.. The x-directed component of the electric field is discretely represented by
.. it's values at the centre of cell edges that point in the x-direction. The y
.. and z components of the electric field are similarly represented at the
.. centres of the y and z-directed cell edges. In the parlance of partial
.. differential equations, we say that :math:`\mathbf{E}` is discretized on the
.. cell edges. The magnetic flux density :math:`\mathbf{b}` is discretized at the
.. centres of cell faces. When electrical potential is considered (in
.. electrostatic problems) it is discretized at cell corners, called the mesh
.. nodes.

.. .. figure:: ../../images/Yee-cube-w-b.png

..   Cubic cell with :math:`\mathbf{E}` discretized onto cell edges,
..   :math:`\mathbf{b}` onto cell faces, and physical properties onto cell
..   centres. Electrical potential :math:`\phi` is discretized onto the mesh
..   nodes.

.. By constructing discrete approximations to the differential operators in
.. equations :eq:`FaradayAnal` and :eq:`AmpereAnal`, we can construct a system of
.. equations to solve for the electric field at the cell edges and/or the
.. magnetic flux at cell faces. The discrete versions of equations are
.. :eq:`FaradayAnal` and :eq:`AmpereAnal`

.. .. math::
..   \mathbf{C} \tilde{\mathbf{E}} -i\omega\tilde{\mathbf{B}} = 0
..   :label: FarDiscrete

.. .. math::
..   \mathbf{C}^T \mathbf{M}_{\mu^{-1}}^f \tilde{\mathbf{B}} - \mathbf{M}_{\sigma}^e\tilde{\mathbf{E}} = \tilde{\mathbf{s}},
..   :label: AmpDiscrete

.. where:

.. - :math:`\mathbf{C}` is the discrete curl operator (all discrete operators are sparse matrices)
.. - :math:`\mathbf{M}_{\sigma}^e` contains information on the discrete conductivity
.. - :math:`\mathbf{M}_{\mu}^f` contains information on the discrete magnetic permeability
.. - :math:`\tilde{\mathbf{E}}` is a vector containing the approximate electric field at each cell edge
.. - :math:`\tilde{\mathbf{B}}` is a vector containing the approximate magnetic flux at each cell face.
.. - :math:`\tilde{\mathbf{s}}` is a vector containing an approximation of the source discretized onto the cell edges.

.. We can now combine equations :eq:`FarDiscrete` and :eq:`AmpDiscrete` and use
.. the methods of sparse linear algebra to solve a large system of equations to
.. determine :math:`\tilde{\mathbf{e}}` and :math:`\tilde{\mathbf{b}}`
.. simultaneously. We can also combine the two equations to form two smaller
.. systems of equations to solve for :math:`\tilde{\mathbf{e}}` and
.. :math:`\tilde{\mathbf{b}}` independently.








