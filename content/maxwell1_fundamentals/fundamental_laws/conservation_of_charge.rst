.. _conservation_of_charge:

Conservation of Charge
======================


Integral form
-------------


Electrical charges cannot be created nor destroyed. The integral formulation of this is 


.. math::
    \int_A \mathbf{j} \cdot da =  - \frac{d}{dt} \int_V \rho dv = - \frac{dQ}{dt} 
    :label: charge_conservation_integral

 
where \\(\rho\\) is the volumetric charge density and \\(Q\\) is the total charge.

DWO: Check the following: this should be applicable to total charge and total currents. How do polarization charges and currents fit in.


Differential form:
------------------

With the use of the divergence theorem equation xxx can be written in  differential form:

.. math::
    \nabla \cdot \mathbf{j} = -\frac{\partial \rho}{\partial t}
    :label: charge_conservation_differential


Conservation of charge formula from Ampere-Maxwell's Law
--------------------------------------------------------

The conservation of charge equation is very useful but it is not an independent equation that needs to be included with Maxwell's equations. In fact, it can be derived from the Ampere-Maxwell law and Gauss's law for electric charges.

.. math::
    \nabla \times \mathbf{h} = j +  \frac {\partial \mathbf  d}{\partial t}
   

Taking the divergence and using \\(\\nabla \\cdot \\mathbf{d} = \\rho_f\\)and a vector identity yields 

.. math::
    \nabla \times \mathbf{h} = j +  \frac {\partial \mathbf  d}{\partial t}
	\nabla \cdot \mathbf{j} = - \frac{\partial \rho_f}{\partial t}

Note that in Maxwell's equations \\(\mathbf{j}\\) refers to the free charge density.


Uses of Conservation of Charge Law
----------------------------------

Starting equations for DC resistivity
-------------------------------------

If there is a source term, say a current \\(I\\) that is injected at a location \\(\mathbf{r_s}\\) then the law for conservation of charge  becomes

.. math::
	\nabla \cdot \mathbf{j} + \frac{\partial \rho_f}{\partial t} = I \delta (\mathbf{r} - \mathbf{r_s})


Note that the positive sign refers to positive current being injected into the medium. Under steady state conditions the time derivative term is zero and the equation reduces to 

.. math::
	\nabla \cdot \mathbf{j}  = I \delta (\mathbf{r} - \mathbf{r_s})

which is a starting equation for DC resistivity problems. 


Dissipation of free charge in a conducting medium
--------------------------------------------------


This is a classic but insightful computation (ref: stratton)
Consider a small volume having an intial charge density of \\(\rho_0\\). The charge is released in a homogeneous medium that has a conductivity \\( \sigma\\) and permittivity \\(\epsilon_0 \\). Using \\(\mathbf{j} = \sigma \mathbf{e}\\)  we write

.. math::
	\nabla \cdot \mathbf{j} = \frac{\sigma}{\epsilon_0} \nabla \cdot \mathbf{d} = \frac{\sigma}{\epsilon_0}\rho_f

The conservation of charge equation becomes

.. math::	
	\frac{\partial \rho_f}{\partial t} + \frac{\sigma}{\epsilon_0}\rho_f = 0

which has a solution

.. math::
	\rho_f(t)= \rho_0 e^{ \frac {\sigma}{\epsilon_0} t}


Even with very low conductivity, e.g. \\( \sigma= 10^{-5} \\) with \\( \\epsilon_0=8.85 e-12\\) the charge density at the location of release decreases by a factor of \\(e\\) in \\(10^{-6}\\) seconds. Thus for earth types of materials, a charge inserted into the earth dissipates extremely quickly.


