.. _Maxwell_Discretization:

An introduction to solving the quasi-static Maxwell equations on a computer
---------------------------------------------------------------------------

Maxwell's equations can only be solved exactly for a few special cases where the conductivity model (and possibly the source-receiver geometry) has some special symmetry. To model an arbitrary geophysical survey over an earth with topography and complicated conductivity, approximate methods are required. These methods break the earth into a series of discrete cells. There are multiple ways to approach this. The simplest methods assume the earth is vertically layered, with constant conductivity in each layer. Next we can assume it varies vertically and in one horizontal direction, and finally, we an assume a full 3D model. This is illustrated in figure :fig:`1dTo3d`.

.. figure:: 1-2-3.png

  Increasing complexity with increasing dimensionality
  :label: 1dTo3d

In 3D we do this:

.. figure:: Yee-cube-w-b.png

  Yee cube with e on edges, b on faces, phi on nodes, phys properties at cell centres

Accuracy goes up with number of cells but so does the computational complexity.

[Insert graphic showing error and time vs num cells, alongside mesh].

