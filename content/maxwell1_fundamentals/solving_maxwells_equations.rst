.. _solving_maxwells_equations:

Solving Maxwell's Equations in Practice
=======================================

.. purpose::

    Here, we provide a general overview on how to solve Maxwell's equations in practice. The approaches used to solve specific problems are covered later in EM GeoSci.


The practice of solving Maxwell's equations for an applied problem can be broken into three parts:

    1) **Defining the problem:** here, Maxwell's equations are modified, re-formulated or approaximated to suite a particular physical problem.
    2) **Setting boundary and initial conditions:** these are envoked so that solutions to Maxwell's equations are uniquely solved for a particular application.
    3) **Solving through analytic or numerical approaches:** once the problem, boundary conditions and initial conditions have been defined, the final solution is obtained through analytic or numerical means.

In the first step, Maxwell's equations are modified to suite a particular application. 

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

where :math:`\mathbf{J_s}` is an electrical current source. For this problem, the magnetic properties of the Earth are typically neglected (i.e. :math:`\mu\approx \mu_0`). Furthermore, we operate in the quasi-static regime (:math:`\sigma \gg \omega \varepsilon`), which allows us to neglect electric displacement as well.

- :ref:`Time Domain Electromagnetics:<airborne_tdem_index>`

.. math::
	\begin{align}
	\nabla\times\nabla\times\mathbf{e} + \mu_0 \sigma \frac{\partial \mathbf{e}}{\partial t} &= - \mu_0 \frac{\partial \mathbf{j_s}}{\partial t}\\
	\nabla\times\mathbf{e} + \frac{\partial \mathbf{b}}{\partial t} &= 0
	\end{align}

where :math:`\mathbf{j_s}` is an electrical current source. This equation is the time-dependent equivalent to the one used in frequency domain electromagnetics.

.. note::
	These are only a few examples. There are other problems in electromagnetic geosciences which require different formulations. Furthermore, there can be multiple formulations of Maxwell's equations which can be used to solve a particular problem. It is up to the researcher to choose the one which is the most effective.

Boundary and Initial Conditions
-------------------------------

Boundary Conditions
^^^^^^^^^^^^^^^^^^^

Boundary conditions ensure that a the problem is well-posed; that is, it has a unique solution. This is necessary when using Maxwell's equations to solve applied problems in electromagnetic geoscience. Differential equations corresponding to a physical problem are defined within a region, or "domain" (denoted by :math:`\Omega`). To make the problem well-posed, boundary conditions are applied to the edges of this domain (denoted by :math:`\partial \Omega`). There are three types of boundary conditions. These are listed below:

**Dirichlet Boundary Conditions:** Dirichlet boundary conditions are by far the most straightforward and easy to implement. Dirichlet conditions directly define the value of the solution on the boundary, i.e.:

.. math::
	 \mathbf{F} \, \big |_{\partial \Omega} = \mathbf{g(r)}

where :math:`\mathbf{F}` is some vector field/flux defined within the domain, :math:`\mathbf{g}` is a spatially-dependent function and :math:`\mathbf{r} = (x,y,z)`. In many cases, the Dirichlet condition is given as a constant value; such as, all fields go to zero at sufficient distance from an electromagnetic source.

**Neumann Boundary Conditions:** Neumann boundary conditions are imposed by specifying the spatial derivatives of the solution on the boundary. Commonly, Neumann conditions define the directional derivatives normal to the surface of the domain, i.e.:

.. math::
	\frac{\partial F_n}{\partial \mathbf{n}} \bigg |_{\partial \Omega} = \mathbf{g(r)}

where :math:`\mathbf{n}` is the vector direction perpendicular to the domain boundary :math:`\partial \Omega`, :math:`F_n = \mathbf{F \cdot \hat n}\;` is the component of a vector field/flux :math:`\mathbf{F}` along :math:`\mathbf{n}`, :math:`\mathbf{g}` is a spatially-dependent function and :math:`\mathbf{r} = (x,y,z)`. Physically, Neumann conditions are used to define the rate of flux through the boundary. This is frequently applied to problems which behave according to the heat equation.

**Robin (Mixed) Boundary Conditions:** Robin boundary conditions are a linear combination of Dirichlet and Neumann conditions, i.e.:

.. math::
	\bigg [ a\mathbf{F(r)} + b\frac{\partial F_n}{\partial \mathbf{n}} \bigg ] \Bigg |_{\partial \Omega} = \mathbf{g(r)}

where :math:`a` and :math:`b` are constants, :math:`\mathbf{n}` is the vector direction perpendicular to the domain boundary :math:`\partial \Omega`, :math:`F_n = \mathbf{F \cdot \hat n}\;` is the component of a vector field/flux :math:`\mathbf{F}` along :math:`\mathbf{n}`, :math:`\mathbf{g}` is a spatially-dependent function and :math:`\mathbf{r} = (x,y,z)`. Robin conditions are used when the rate of flux leaving the domain is dependent on the value of the field at the boundary.

Initial Conditions
^^^^^^^^^^^^^^^^^^

Initial conditions, in addition to boundary conditions, are required to solve time-dependent problems. In the physical sciences, solutions are causal. That is, the fields and fluxes at a particular time depend on the the behaviour of fields and fluxes at earlier times. 

**Higher Order Time-Derivatives** 





Analytic and Numeric Solutions
------------------------------

Analytic Solutions
^^^^^^^^^^^^^^^^^^




Numerical Solutions
^^^^^^^^^^^^^^^^^^^






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








