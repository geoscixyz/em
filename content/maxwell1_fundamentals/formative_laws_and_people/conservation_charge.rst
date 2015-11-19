.. _ppl_conservation_charge:

Conservation of charge
======================

General description
-------------------

Physically, conservation of charge indicates that the net quantity of electrical charge is always conserved. An obvious example is that the net charge in the universe is zero; that is, there are equal quantities of positive and negative charge. 

Mathematical formulation
------------------------

To mathematically formulate this law, we define current :math:`I` (C/s or A) as 

.. math::

	I = - \int_S \mathbf{j} \cdot \mathbf{n} \ dS

where  :math:`\mathbf{j}` is current density (:math:`A/m^2`), :math:`S` denotes a closed surface enclosing the volume (:math:`V`), and :math:`\mathbf{n}` is a unit outward normal. 
Applying Divergence therom yields

.. math::

	I = - \int_V \nabla \cdot \mathbf{j} \ dV. 

The net current into a volume must be equal the net change in charge in the volume:

.. math::

	\frac{dq}{dt} = - \int_V \nabla \cdot \mathbf{j} \ dV, 

where :math:`q = \int_V \rho_f dV` is total charge in the volume and :math:`\rho_f` is free charge density (:math:`C/m^3`).  
Above equation can be written as 

.. math::

	\int_V (\nabla \cdot \mathbf{j} + \frac{\partial \rho_f}{\partial t}) dV, 

which yieds the continuity equation in differential form:

.. math::

	\nabla \cdot \mathbf{j} + \frac{\partial \rho_f}{\partial t} = 0.

Intergral form of this equation can be written as

.. math::

	\int_S \mathbf{j} \cdot \mathbf{n} \ dS = -\frac{\partial q}{\partial t}

Above equation literally says tht total current out through a closed surface :math:`S` is equal to the time rate of depletion of charge within the volume :math:`V` bounded by the surface :math:`S`. 
Negative sign in L.H.S is important because this makes not increase but decrease in net charge as current pass through closed surface, which preserves conservation of charge. 


Connection to Maxwell's equations
---------------------------------

Another way to dervie this continuity equation is from Ampere's circuit law with Maxwell's addition:

.. math::

	\nabla \times \mathbf{b} - \mathbf{j} - \frac{\partial \mathbf{d}}{\partial t} = 0,

where :math:`\mathbf{b}` is magnetic flux density (:math:`Wb/m^2`) and :math:`\mathbf{d}` electric displacement field (:math:`C/m^2`). By taking divergence yields

.. math::

	\nabla \cdot \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t} = 0.

Then with Gauss's law for dielectric

.. math::

	\nabla \cdot \mathbf{d} = \rho_f

We can obtain same continuity equation in differential form. 

Connection to Boundary conditions
---------------------------------

For :math:`\mathbf{dc}` case when we do not have any time dependency the continuity equation can be reduced as 

.. math::

	\nabla \cdot \mathbf{j} = 0,

and this makes normal component of the current continuous at the interface. However, for :math:`\mathbf{ac}` case, due to the time derivative of charge, the normal component of the current is not continuous at the interface.  

