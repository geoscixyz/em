.. _Maxwell_Discretization:

An introduction to solving the quasi-static Maxwell equations on a computer
---------------------------------------------------------------------------

Maxwell's equations can only be solved exactly for a few special cases where the conductivity model (and possibly the source-receiver geometry) has some special structure and symmetry. To model an arbitrary geophysical survey over an earth with topography and arbitrary conductivity, approximate methods that can be implemented in a computer are required. These methods are known as discretizations of Maxwell's equations because they break the earth into a set of discrete volumes, or cells, with the physical properties held constant in each cell. 

It is possible to construct a discretization based on either the integral or differential form of Maxwell's equations in the time and frequency domains. For simplicity, we will restrict this discussion to discretizations of the differential form of Maxwell's equations in the frequency domain. 

Discrete approximations of Maxwell's equations used in geophysical prospecting fall into three general categories based on the complexity of earth model they can represent. The simplest discretizations assume that conductivity varies only with depth but not laterally. The subsurface can then be divided into a set of flat layers, with physical properties constant in each layer.

One may model a much larger class of geoelectric structures by assuming that conductivity may vary with depth and in one lateral direction. This is known as 2D modelling and requires dividing a two-dimensional (2D) section of the earth into a set of discrete polygons, usually rectangles or triangles. This provides a compromise between the computational difficulty of full 3D modelling and the limitations of 1D modelling. Of course, to model the most complex terrain and conductivity variation, three-dimensional (3D modelling is required. In 3D modelling the earth is divided into a set of discrete volumes, usually cuboids or tetrahedra, with physical properties constant in each cell. These three types of earth models, with their increasing complexity, are illustrated in figure :fig:`./images/1-2-3.png`.

.. figure:: ./images/1-2-3.png
  
  Increasing complexity with increasing dimensionality

1D modelling methods write the electric and magnetic fields due to a source above a layered earth in terms of `Hankel transform <https://en.wikipedia.org/wiki/Hankel_transform>`_ integrals that are evaluated approximately. Two and three dimensional frequency domain discretizations transform Maxwell's equations into a system of linear algebraic equations for the electric field or magnetic flux density at discrete points in space, at a single frequency. In all these methods there is a tradeoff between solution accuracy and computational complexity. A finer mesh will lead to a more accurate solution but also to a larger linear system that must be solved to compute the fields or fluxes.

Now let us restrict our attention to three dimensions. There are several ways to discretize Maxwell's equations in 3D, including finite difference, finite element and finite volume approaches. Almost all discretizations of Maxwell's equations used in geophysical prospecting apply the quasi-static approximation, meaning that they ignore the electric displacement term :math:`-i\omega\mathbf{D}` in :ref:`Ampere's law <ampere_maxwell>`. To give one brief example, we will describe a mimetic finite volume discretization of Maxwell's equations on a staggered grid. We divide the earth into a set of cubes. 




In 3D we do this:

.. figure:: ./images/Yee-cube-w-b.png

  Yee cube with e on edges, b on faces, phi on nodes, phys properties at cell centres

Accuracy goes up with number of cells but so does the computational complexity.

[Insert graphic showing error and time vs num cells, alongside mesh].

