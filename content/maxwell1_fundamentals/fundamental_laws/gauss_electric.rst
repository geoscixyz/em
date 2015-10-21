.. _gauss_electric:

Gauss's Law for Electric Fields
===============================

Gauss’s law for the electric field states that the electric flux through any closed surface is proportional to the total electric charge enclosed by the surface, with constant of proportionality :math:`\epsilon_0`. In integral equation form it reads:

.. math::
	\oint_{S} \mathbf{e} \cdot \hat{\mathbf{n}} \; \mathrm{d}a = \frac{Q}{ \epsilon_{0} }\;,
	:label: Gauss_e_int
where the integral is over a closed surface :math:`S`, :math:`\mathbf{e}` is the electric field, :math:`\hat{\mathbf{n}}` is a unit vector normal to :math:`S` and :math:`Q` is the total charge enclosed by :math:`S`. 

Differential Form
-----------------

When considering charge in a continously distributed body, we can consider the concept of charge density rather than total charge. The total charge in a body is then the volume integral of charge density :math:`\rho` over the body such that:

.. math::
	Q = \int_V \rho \; \mathrm{d}V\;.
	:label: charge_density
Using this definition and applying the divergence theorem to the left hand side of equation :eq:`charge_density`, we can rewrite it as:

.. math::
	\int_V \nabla \cdot \mathbf{e} \; \mathrm{d}V = \int_V \rho \; \mathrm{d}V \;.
	:label: 
Since this must be true for any volume , we can equate the integrands, giving the differential form of Gauss's law:

.. math::
	\nabla \cdot \mathbf{e} = \frac{\rho}{\epsilon_0}.
	:label: Gauss_e_diff

Equivalence to Coulomb's law
----------------------------

Coulomb's law is often one of the first quantitative laws encountered by students of electromagnetism. It describes the force between two electric charges idealized as point sources. Coulomb's law states that the force between two electric charges is proportional to the inverse square of the distance between them acting in the direction of a line connecting them. If the charges are of opposite sign, the force is attractive and if the charges are of the same sign, the force is repulsive. Mathematically, Coulomb's law is written as:

.. math::
  \mathbf{F} = \frac{q_1q_2}{4\pi r^2}\hat{\mathcal{r}} \;,
  :label: Coulomb_q
where :math:`F` is the force between the two charges :math:`q_1` and :math:`q_2`, :math:`r` is the distance between the charges and :math:`\hat{\mathcal{r}}` is a unit vector in the direction of the line separating the two charges.

Having defined Coulomb's law, one might next naturally ask the question how would a standard reference charge behave in the presence of any distribution of electric charge we might dream up? Answering this question brings us to the concept of the electric field. We follow the presentation of [2]_. Let us define the electric field as:

.. math::
       e = \frac{\mathbf{F}}{q_0},
       :label: Force_per_q
where :math:`q_0` is a positive charge of unit magnitude. We can now write Coulomb's law as:

.. math::
      \mathbf{e} = \frac{q}{4\pi\epsilon_0 r^2}\hat{\mathcal{r}}\;.
      :label: e_charge_q
If we replace :math:`q` with a continuous charge distribution it becomes

.. math::
  \mathbf{e} = \frac{1}{4\pi\epsilon_0}\int_V \frac{\rho}{r^2}\mathrm{d}\hat{\mathcal{r}}
  :label: e_charge_den
where :math:`r` is now the distance from a point in the charge distribution to the point at which the electric field is to be evaluated. 

We can show that this is equivalent to the differential form of Gauss's law by taking the divergence of both sides. Doing this we get 

.. math::
   \nabla \cdot \mathbf{e} = \frac{1}{4\pi\epsilon_0}\int_V \nabla \cdot\left(\frac{1}{r^2}\right)\rho\mathrm{d}\hat{\mathcal{r}} = \frac{\rho}{\epsilon_0}
   :label: Gauss_diff
For a full derivation see pages 65-70 of [2]_.

Notes on Electric flux
----------------------

Flux is a measure of the strength of a field passing through a surface. Electric flux is defined in general as 

.. math::
	\boldsymbol{\Phi} = \int_s \mathbf{e} \cdot d\mathbf{s})
	:label: e_flux
So we can also think of electric field as flux density. Gauss’s law tells us that the net electric flux through any closed surface is zero unless the volume bounded by that surface contains a net charge. 

Units
-----


References
----------
.. [1] A student’s guide to Maxwell’s equations (PDF)

.. [2] Griffiths, David J. Introduction to Electrodynamics, 3rd edition. Prentice Hall, Upper Saddle River, New Jersey. 1999.
