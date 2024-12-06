.. _conservation_of_charge:

Conservation of Charge
======================

The conservation of charge states that electrical charges cannot be created or
destroyed. It is not an independent equation since it can be derived from
other Maxwell equations but it is a useful starting point for solving some
problems. It can be written in integral and differential forms.


Integral form
-------------


The integral formulation of conservation of charge is


.. math::
    \int_A \mathbf{j} \cdot da =  - \dfrac{d}{dt} \int_V \rho dv = - \dfrac{dQ}{dt} 
    :label: charge_conservation_integral

where:

- :math:`\mathbf{j}` is the current density
- :math:`\rho` is the volumetric charge density
- :math:`Q` is the total charge inside the volume
- :math:`A` is the surface area of the volume 
- :math:`V` is the volume


DWO: Check applicability for total or free charges.


Differential form:
------------------

With the use of the divergence theorem equation
:eq:`charge_conservation_integral` can be written in  differential form:

.. math::
    \nabla \cdot \mathbf{j} = -\dfrac{\partial \rho}{\partial t}
    :label: charge_conservation_differential


Conservation of charge formula from Ampere-Maxwell's Law
--------------------------------------------------------

The conservation of charge equation is not an independent equation that needs
to be included with Maxwell's equations. It can be derived from the Ampere-
Maxwell law and Gauss's law for electric charges.

.. math::
    \nabla \times \mathbf{h} = j +  \dfrac {\partial \mathbf  d}{\partial t}
   

Taking the divergence and using :math:`\nabla \cdot \mathbf{d} = \rho_f` and
a vector identity yields

.. math::
    \nabla \times \mathbf{h} = j +  \dfrac {\partial \mathbf  d}{\partial t}
	\nabla \cdot \mathbf{j} = - \dfrac{\partial \rho_f}{\partial t}

Note that in Maxwell's equations :math:`\mathbf{j}` refers to the free charge density.


Uses of Conservation of Charge
------------------------------

Starting equations for DC resistivity
*************************************

If there is a source term, say a current :math:`I` that is injected at a
location :math:`\mathbf{r_s}` then the law for conservation of charge  becomes

.. math::
	\nabla \cdot \mathbf{j} + \dfrac{\partial \rho_f}{\partial t} = I \delta (\mathbf{r} - \mathbf{r_s})


Note that the positive sign refers to positive current being injected into the
medium. Under steady state conditions the time derivative term is zero and the
equation reduces to

.. math::
	\nabla \cdot \mathbf{j}  = I \delta (\mathbf{r} - \mathbf{r_s})

which is a starting equation for DC resistivity problems. 


Dissipation of free charge in a conducting medium
*************************************************


This is a classic but insightful computation (ref: stratton) Consider a small
volume having an intial charge density of :math:`\rho_0`. The charge is released
in a homogeneous medium that has a conductivity :math:`\sigma` and permittivity
:math:`\epsilon_0`. Using :math:`\mathbf{j} = \sigma \mathbf{e}`  we write

.. math::
	\nabla \cdot \mathbf{j} = \dfrac{\sigma}{\epsilon_0} \nabla \cdot \mathbf{d} = \dfrac{\sigma}{\epsilon_0}\rho_f

The conservation of charge equation becomes

.. math::	
	\dfrac{\partial \rho_f}{\partial t} + \dfrac{\sigma}{\epsilon_0}\rho_f = 0

which has a solution

.. math::
	\rho_f(t)= \rho_0 e^{ \frac {-\sigma}{\epsilon_0} t}


Even with very low conductivity, e.g. :math:`\sigma= 10^{-5}` with :math:`
\epsilon_0=8.85 \times 10^{-12}` the charge density at the location of
release decreases by a factor of :math:`e` in :math:`10^{-6}` seconds. Thus for
earth types of materials, a charge inserted into the earth dissipates
extremely quickly.


