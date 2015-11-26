============================================
Effects of Topography: Numerical experiments
============================================

Using the depressed hemi-sphere solution for DC problem, we want to identify effects of topography in terms of two aspects:

- Numerical accuracy of 3D DC forward modelling algorithm (UBC DCIP3D)
- Understanding charge-build up and correspoding electrical fields 

First item is important since we use this forward modelleing algorithm for the inversion of DC data. If this topographic effect is not accurately computed, then this will generate artefacts in the recovered resistivity model. In addition, if numerical and analytic solution show compatible match, this will provide us cross-checks for both numerical and analytic solutions.

.. note::

   There can be errors on derived analytic solutions!

Without physical understanding of electromagnetic fields in the earth, proper use of EM geophysics is difficult thus, second item is always crucial. To investigate effects only due to topography, we subtract primary potential (:math:`\psi^p = \frac{I\rho}{2\pi R}`) from total potential, :math:`\psi (C/m^3)`  which yields secondary potential (:math:`\psi^s`):

.. math::

   \psi^s = \psi - \psi^p

By taking gradient, then electric field :math:`\vec{e}` and total charge density (:math:`\rho_T`) can be computed using below equations:

.. math::

   \vec{e}=-\nabla \phi

   \rho_T = \epsilon_0 \nabla \cdot \vec{e}

Observations of total, primary, and secondary electric field and charge density will provide us comprehensive understanding of topographic effects in DC problem. 

Numerical validations
=====================

We consider a pole transmitter injected to the ground. Fig. XXX shows 3D resistivity model and injected current source location in the vertical section which acrosses center of the depresed hemisphere. For numerical comptuation 3D mesh with 5 m core cell size is used. Resistivity of the hemi-sphere and half-space are set to :math:`10^8` ohm-m (close to infinity) and :math:`10^3` ohm-m. We compute potentials in every cells in 3D domain. Top and middle panels of Fig. XXX shows computed numerical and analytici potentials, respectively. White lines delineate boundary of the depressed hemi-sphere. Bottom panel of Fig. XXX shows relative error, and blank region close to the source has errors greater than 10 percent. Even at the boundary hemi-sphere, we have less than 4 percent. This is reasonable accuracy considering that our noise level is roughly about 10 percent for DC problem.
This shows our numerical solution has capability to accurately compute those topographic effects, although our choice of discretization should be effective. For more careful observation, we provide similar comparison for secondary potential. Top, middle and bottom panels of Fig. XXX correspondingly show numerical, analytic, and absolute errors of secondary potentials. Maximum error occurs at hemi-sphere boundary close to the current source, but it is less than 20 percent. 

.. figure:: ./figures/resismodel.png
   :align: center
   :name: resismodel

   Section view of 3D resistivity model for depressed hemi-sphere. 

.. figure:: ./figures/ComparisonTotFine.png
   :align: center
   :name: ComparisonTotFine

   Comparisons of numerical and analytic total potentials with topography (depressed hemisphere).

.. figure:: ./figures/ComparisonSecFine.png
   :align: center
   :name: ComparisonSecFine

   Comparisons of numerical and analytic secondary potentials with topography (depressed hemisphere).   

Interpretations
===============


.. figure:: ./figures/ComparisonSecFineChargs.png
   :align: center
   :name: ComparisonSecFineChargs

   XXX

.. figure:: ./figures/ComparisonSecFineEfield.png
   :align: center
   :name: ComparisonSecFineEfield

   XXX


.. |resismodel| image:: ./figures/resismodel.png
.. |ComparisonTotFine| image:: ./figures/ComparisonTotFine.png
.. |ComparisonSecFine| image:: ./figures/ComparisonSecFine.png
.. |ComparisonSecFineChargs| image:: ./figures/ComparisonSecFineChargs.png
.. |ComparisonSecFineEfield| image:: ./figures/ComparisonSecFineEfield.png

