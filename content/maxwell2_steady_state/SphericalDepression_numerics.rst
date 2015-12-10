============================================
Effects of topography: Numerical experiments
============================================

Using the depressed hemi-sphere solution for DC problem, we want to identify effects of topography in terms of two aspects:

- Numerical accuracy of 3D DC forward modelling algorithm (UBC DCIP3D)
- Understanding charge-build up and correspoding electrical fields 

First item is important since we use this forward modelleing algorithm for the inversion of DC data. If this topographic effect is not accurately computed, then this will generate artefacts in the recovered resistivity model. In addition, if the numerical and analytic solution show a compatible match, this will provide with us cross-checks for both numerical and analytic solutions.

.. note::

   There can be errors on derived analytic solutions!

Without a physical understanding of electromagnetic fields in the earth, the proper use of EM geophysics is difficult, thus it is important to develop a thorough understanding of electromagnetic theory.
To investigate effects only due to topography, we subtract the primary potential (:math:`\psi^p = \frac{I\rho}{2\pi R}`) from the total potential, :math:`\psi`  which yields the secondary potential (:math:`\psi^s`):

.. math::

   \psi^s = \psi - \psi^p

By taking the gradient, then the electric field :math:`\bf{e}` and total charge density (:math:`\rho_T`) can be computed using equations below:

.. math::
   \bf{e}=-\nabla \phi    
   :label: elec

.. math::
   \rho_T = \epsilon_0 \nabla \cdot \bf{e}
   :label: charg

Observations of total, primary, and secondary electric fields and charge density will provide us with a comprehensive understanding of topographic effects in the DC problem. 

Numerical validations
=====================

.. figure:: ./figures/resismodel.png
   :align: center
   :name: resismodel

   Section view of 3D resistivity model for depressed hemi-sphere. 

The above resistivity model shows a depressed hemisphere model. The resistivity of the depressed hemi-sphere is set to :math:`10^8` ohm-m (close to infinity) to simulate air, and the half-space is set to and :math:`10^3` ohm-m. 
To compute potentials from the above depressed hemi-sphere model, we first use numerical solutions using DCIP3D code (CITEXXX). Then to check the accuracy of our numerical algorithm we use analytic solution of a sphere problem that we derived in Section :ref:`effecttopo_theory`. For the numerical evaluation of that an analytic solution we use :ref:`effecttopo_code`. To proceed with this validation, we consider a pole transmitter injected in the ground. In the above figure, injected current source location is shown. 

For numerical computations, a 3D mesh with 5 m core cells is used. We compute potentials in every cells in the 3D domain. Top and middle panels of the below figure shows computed numerical and analytic potentials, respectively. White lines delineate the boundary of the depressed hemi-sphere. The bottom panel of below figure shows relative error, and blank region close to the source has errors greater than 10 percent. Even at the boundary of the hemi-sphere, we have less than 4 percent error. This is a reasonable accuracy considering that our noise level is roughly 10 percent for the DC problem.
This shows our numerical solution has a capability to accurately compute those topographic effects, although our choice of discretization is clearly important.

.. figure:: ./figures/ComparisonTotFine.png
   :align: center
   :name: ComparisonTotFine

   Comparisons of numerical and analytic total potentials with topography. White line depicts the boundary of the depressed hemisphere.

For a more careful observation, we provide a similar comparison for the secondary potential in 3D space. The top, middle and bottom panels of the below figure correspondingly show numerical, analytic, and absolute errors of secondary potentials. The maximum error occurs at the hemi-sphere boundary close to the current source, but it is less than 20 percent. 

.. figure:: ./figures/ComparisonSecFine.png
   :align: center
   :name: ComparisonSecFine

   Comparisons of numerical and analytic secondary potentials with topography. White line depicts the boundary of the depressed hemisphere.

Interpretations
===============

Using Eqs. :eq:`elec` and :eq:`charg`, we can compute both electric fields and charge density in 3D. First, we consider charge density. The below figure shows total, primary, and secondary charge densities. From the total and primary charge densities (top and middle panels), we clearly see secondary charge build-up due to the topographic effects is difficult to be recognized because of positive charges due to the input current. The secondary charge density clearly shows the topographic effects. Positive and negative charges are built up on 
the left side of the depressed hemi-sphere, closest to the input current. Since the air region are act as an insulator, all postive charge cannot pass through this hemi-sphere region and accumulated on the left side closer to the input current. The magnitude of negative charge build-up on the right side is much smaller than the postive charge on the other side. These postive and negative charges will generate electric fields based on Coulomb's law (See Section :ref:`coulomb`).  

.. figure:: ./figures/ComparisonSecFineChargs.png
   :align: center
   :name: ComparisonSecFineChargs

   Section views of total (top panel), primary (middle panel), and secondary (bottom panel) charge densities.

A rule of thumb for understanding electric fields from charges is:

.. note::

   The electric field is coming out from a postive charge and coming into negative charge. 

Based on the above principle, first imagine how electric fields are going to be distributed in 3D, then check your conjecture with the figure below, which shows total, primary, and secondary electric fields. From the total electric field shown in the top panel, we reconize that thedominant electric field is due to injected current, although we can recognize the distortion of electric fields due to charge build-up at the hemi-spherical boundry. By subtracting the primary from the total electric field we obtain a secondary electric field as shown in the bottom panel. Outside of the hemi-sphere, the electric field is dipolar in shape, while inside the hemi-sphere, the electric fields flow straight from the positive to negative charges.

.. figure:: ./figures/ComparisonSecFineEfield.png
   :align: center
   :name: ComparisonSecFineEfield

   Section views of total (top panel), primary (middle panel), and secondary (bottom panel) electric fields. 

.. |resismodel| image:: ./figures/resismodel.png
.. |ComparisonTotFine| image:: ./figures/ComparisonTotFine.png
.. |ComparisonSecFine| image:: ./figures/ComparisonSecFine.png
.. |ComparisonSecFineChargs| image:: ./figures/ComparisonSecFineChargs.png
.. |ComparisonSecFineEfield| image:: ./figures/ComparisonSecFineEfield.png

