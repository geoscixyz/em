.. _gauss_electric:

Gauss's Law for Electric Fields
===============================

 .. figure:: images/GaussE.png
    :align: right
    :scale: 50% 
    :name: GaussE

    Charge enclosed. 

Gauss’s law for the electric field states that the electric flux through any closed surface is proportional to the total electric charge enclosed by the surface.



Integral Equation
-----------------

Gauss’s law in integral form is given below:

.. math::
	\oint_{S} \mathbf{e} \cdot \hat{\mathbf{n}} \; \mathrm{d}a = \frac{Q}{ \varepsilon_{0} }\;,
	:label: Gauss_e_int

where:

 - \\( \\mathbf{e} \\) is the electric field
 - \\( Q_{enc} \\) is the enclosed electric charge
 - \\( \\varepsilon_0 \\) is the electric permittivity of free space
 - \\( \\hat{\\mathbf{n}} \\) is the outward pointing unit-normal

Differential Form
-----------------

When considering a spatially extended charged body, we can think of its charge as being continously distributed throughout the body with density :math:`\rho`. The total charge is then given by the integral of the charge density over the volume of the body.

.. math::
	Q = \int_V \rho \; \mathrm{d}v\;.
	:label: charge_dens

Using this definition and applying the divergence theorem to the left hand side of Gauss's law :eq:`Gauss_e_int`, we can rewrite the law as:

.. math::
	\int_V \boldsymbol{\nabla} \cdot \mathbf{e} \; \mathrm{d}v = \int_V \frac{\rho}{\varepsilon_0} \; \mathrm{d}v \;.
	:label: 

Since this equation must hold for any volume :math:`V` , we can equate the integrands, giving the differential form of Gauss's law:

.. math::
	\boldsymbol{\nabla} \cdot \mathbf{e} = \frac{\rho}{\varepsilon_0}.
	:label: Gauss_e_diff

Equivalence to Coulomb's law
----------------------------

Coulomb's law is often one of the first quantitative laws encountered by students of electromagnetism. It describes the force between two point electric charges. It turns out that it is equivalent to Gauss's law. Coulomb's law states that the force between two point electric charges is proportional to the inverse square of the distance between them, acting in the direction of a line connecting them. If the charges are of opposite sign, the force is attractive and if the charges are of the same sign, the force is repulsive. Mathematically, Coulomb's law is written as

# Add diagram for two charges :math:'F_{Qq} = 1/4pie Qq/r^2 \hat{r}'

.. math::
  \mathbf{F} = \frac{qQ}{4\pi \varepsilon_0 |\mathbf{r}|^2}\hat{\mathbf{r}} \;,
  :label: Coulomb_q

where :math:`F` is the force between the two charges :math:`q` and :math:`Q`, :math:`|\mathbf{r}|` is the distance between the charges and :math:`\hat{\mathbf{r}}` is a unit vector in the direction of the line separating the two charges.

Having defined Coulomb's law, one might next naturally ask the question how would a standard reference charge behave in the presence of any distribution of electric charge we might dream up? Answering this question brings us to the concept of the electric field. We follow the presentation of [2]_. We can define the electric field of an arbitrary charge :math:`Q` as the force experienced by a unit charge :math:`q` due to :math:`Q`

.. math::
       \mathbf{e} = \frac{\mathbf{F}}{q}.
       :label: Force_per_q

Dividing both sides of Coulomb's law by :math:`q` and substituting the definition of :math:`\mathbf{e}`, we get that the electric field of a point charge :math:`Q` is

.. math::
      \mathbf{e}(\mathbf{r}) = \frac{Q}{4\pi\varepsilon_0 |\mathbf{r}|^2}\hat{\mathbf{r}}\;.
      :label: e_charge_q

It is important to note here that the electric field obeys the principle of superposition, meaning that the electric field of an arbitrary collection of point charges is equal to the sum of the electric fields due to each individual charge. 

# Note a vector: Alternative to this using divergence theorem page 36.

.. math::
   \mathbf{e}\left(\sum_{k=1,n} Q_i\right) = \sum_{k=1,n} \mathbf{e}(Q_i)
   :label:

If we consider the the electric field due to a spatially extended body with charge density :math:`\rho`, the sum becomes an integral over infinitesimal volume elements of the body

.. math::
  \mathbf{e} = \frac{1}{4\pi\varepsilon_0}\int_V \frac{\rho}{|\mathbf{r}|^2}\;\mathrm{d}v,
  :label: e_charge_den

where :math:`|\mathbf{r}|` is now the distance from a point in the charged body to the point at which the electric field is to be evaluated. The integral is over the charged body. 

To show that :eq:`e_charge_den` is equivalent to Gauss's law, start by taking the divergence of both sides

.. math::
   \boldsymbol{\nabla} \cdot \mathbf{e} = \frac{1}{4\pi\varepsilon_0}\int_V \boldsymbol{\nabla} \cdot\left(\frac{1}{|\mathbf{r}|^2}\right)\rho\;\mathrm{d}v.
   :label: Gauss_diff

Note that the divergence is taken with respect to the spatial variation of :math:`\mathbf{e}`, with :math:`\rho` held constant. Regardless of the volume of integration, the integral on the right hand side of equation :eq:`Gauss_diff` has the value

.. math::
   \int_V \boldsymbol{\nabla} \cdot\left(\frac{1}{|\mathbf{r}|^2}\right)\rho\;\mathrm{d}v = 4\pi\rho.
   
This establishes the desired result

.. math::
   \boldsymbol{\nabla} \cdot \mathbf{e} = \frac{\rho}{\varepsilon_0}.

For a more detailed derivation and discussion, see pages 65-70 of [2]_.

Notes on Electric flux
----------------------

Flux is a measure of the strength of a field passing through a surface. Electric flux is defined in general as 

.. math::
	\boldsymbol{\Phi} = \int_S \mathbf{e} \cdot \hat{\mathbf{n}} \, \mathrm{d}a.
	:label: e_flux

We can think of electric field as flux density. Gauss’s law tells us that the net electric flux through any closed surface is zero unless the volume bounded by that surface contains a net charge. Additionally, the flux depends only on the amount of charge contained and not on the specific surface chosen. This is illustrated in the figure below, which illustrates the flux due to a point charge. Note that as the surface moves further away from the charge at the origin, the magnitude of the field decreases with :math:`\frac{1}{|\mathbf{r}|^2}` spatial dependence but the volume of the surface increases with :math:`|\mathbf{r}|^2` dependence. Thus, regardless of the surface chosen, the flux through that surface remains the same.

.. figure:: images/Efield.gif
  
  Illustration of the electric flux through different Gaussian surfaces :math:`S` due to a point charge :math:`Q` at the origin. The color of the surface shows the magnitude of the electric field (or flux density). 

Units
-----

# Copy style of Ampere_Maxwell.

.. tabularcolumns:: |c|c|c|c|

+-----------------------+---------------------+---------------------------+---------------------------------------+
|        Quantity       |  Symbol             |  Units (abbreviation)     |  Equivalent                           |
+=======================+=====================+===========================+=======================================+
|     Surface area      |  :math:`S`          |Square meter :math:`(m^2)` |                                       |
+-----------------------+---------------------+---------------------------+---------------------------------------+
|     Volume            |  :math:`V`          |Cubic meter :math:`(m^3)`  |                                       |
+-----------------------+---------------------+---------------------------+---------------------------------------+
|     Electric charge   |  :math:`q, Q`       | Coulomb :math:`(C)`       |                                       |
+-----------------------+---------------------+---------------------------+---------------------------------------+
|Electric charge density| :math:`\rho`        | :math:`(C/m^3)`           |                                       |
+-----------------------+---------------------+---------------------------+---------------------------------------+
|     Electric field    | :math:`e`           | Volt/meter :math:`(V/m)`  |Newton/Coulomb :math:`(N/C)`           |
+-----------------------+---------------------+---------------------------+---------------------------------------+
|Electrical permittivity|:math:`\varepsilon_0`| Farads/meter :math:`(F/m)`|Coulomb/(Volt m)                       |
|                       |                     |                           | :math:`C/(V \cdot m )`                |
+-----------------------+---------------------+---------------------------+---------------------------------------+


References
----------
.. [1] A student’s guide to Maxwell’s equations (PDF)

.. [2] Griffiths, David J. Introduction to Electrodynamics, 3rd edition. Prentice Hall, Upper Saddle River, New Jersey. 1999.
