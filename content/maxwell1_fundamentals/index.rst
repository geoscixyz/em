.. _maxwell1_fundamentals_index:

ME I: Fundamentals
==================

Overview of Maxwell's Equations
-------------------------------
In this chapter we first present a synopsis of Maxwell's equations in three forms: 
(a) Differential  equation in time
(b) Integral  equations in time
(c) Equations in the frequency domain

These are designed to be a quick access to the relevant equations with proper notation and units. Each of the four fundamental Maxwell equations, as well as the conservation of charge, is then explored in more detail to promote a physical understanding and provide insight as to where the law is useful. In addition we provide a short synopsis of the scientists involved in discovering the law. 


Differential equations in time

.. math::
    \boldsymbol{\nabla} \times \mathbf{e} = -\frac{\partial \mathbf{b}}{\partial t}
    :label: faraday_time

.. math:: 
    \boldsymbol{\nabla} \times \mathbf{h} = \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t} 
    :label: ampere_time

.. math::
    \boldsymbol{\nabla \cdot} \mathbf{d} = \rho_f
    :label: gauss_electric_time

.. math:: 
    \boldsymbol{\nabla \cdot} \mathbf{b} = 0
    :label: gauss_magnetic_time


Integral equations in time
... summary of relevant equations

Differential equations in frequency
..... summary of relevant equations



-----   Begin commentary 

To reference an equation by number, :eq:`faraday_time`. Some inline math looks like \\(\\boldsymbol{\\nabla} \\times \\mathbf{e} = -\\frac{\\partial \\mathbf{b}}{\\partial t}\\). To include something from the equation bank...

.. include:: ../equation_bank/ohms_law_freq.rst

and to reference something from the equation bank by number :eq:`ohms_law_freq`. 

To reference another page, you do :ref:`constitutive_relations_index` (note that this is at the top of the file constitutive_relations/index.rst)


To **bold** and to *italicize*

.. Previous content (this is commented out)



---- Template for organizing material for each law:
(a) Gauss's law for electric fields
(b) Gauss's law for magnetic fields
(c) Faraday's law
(d) Ampere-Maxwell
(e) Conservation of charge


For each law:
(Use the notation in Ward and Hohmann, except use lower case for integral equations. They were inconsistent in their Appendix. Also, check their use of partial and total derivatives with time. Rely on Fleisch's book (or other EM book) to delineate the subtle but important aspect of this.) 
(a) Integral equation 
(b) Differential equation
(c) Units
(d) Primary scientist contributing to the discovery of the law. If one of these is mentioned then have a short "Discovers of the law" 
a short synopsis of who they were, when they
lived, what their “law” is, and how it contributed to Maxwell’s equations and list or examples of applications.  (eg Faraday’s
law is fundamental to electric generators or transformers).

-----------  end commentary ----------

.. TODO toc

..     Ampere-Maxwell Law

Integral form: 
-----------------------

The Ampere-Maxwell equation in integral form is given below:

.. math::
    \int_A \nabla \times \mathbf{b} \cdot \mathbf{da} =  \int_C \mathbf{b} \cdot \mathbf{dl} = \mu_0 ( I_{enc} + \epsilon_0 \frac{d}{dt} \int \mathbf{e} \cdot \hat{\mathbf{n}} da)
    :label: ampere_maxwell_integral


The first portion of the equation is due to Ampere. It shows the relationship between a current \\(I_{enc}\\) and the circulation of the magnetic field around any closed contour line. \\(I_{enc}\\) refers to all currents irrespective of their physical origin.

The second portion of the equation is due to Maxwell and shows that a circulation of magnetic field is also caused by a time rate of change of electric flux. This explained how current in a simple circuit involving a battery and capacitor can flow. (ref). The term is pivotal in showing that electromagnetic energy propagates as waves.

The integral forumulations are physically insightful and closely relate to the experiments that gave rise to them. They are also play a formative role in generating boundary conditions for waves that propagate through different materials. 

When dealing with the propagation of EM waves in matter the currents \\(I_{enc}\\) are usually dealt with in terms of current densities. The integral equation above is thus written as 


.. math:: 
    \int \nabla \times \mathbf{b} \cdot \mathbf{da} =  
    \int \mathbf{b} \cdot \mathbf{dl} = \mu_0 (\int \mathbf{j_f} + \frac{\partial \mathbf{p}}{\partial t} + \nabla \times \mathbf{m} +   \epsilon_0 \frac{d}{dt}  \int \mathbf{e} \cdot \mathbf{n} da)
    :label: ampere_maxwell_integral_p&m

where the current densities are:
\\(\\mathbf{j_f}\\)= free current caused by moving charges
\\(\\mathbf{j_b} = \\frac{\\partial \\mathbf{p}}{\\partial t}\\)  where \\(\\mathbf{p}\\) is the electric polarization resulting from bound charges in dielectrics
\\(\\mathbf{j_p} = \\nabla \\times \\mathbf{m}\\) is the magnetic polarization current. That is currents needed to generate the magnetization \\( \\mathbf{m}\\). 


Differential form:

There are a number of ways of writing the equation in differential form. Each provides its own insight.

Variables:   \\(\\mathbf{e, b, p, m} \\)

.. math::
    \nabla \times \mathbf{b} - \epsilon_0 \mu0 \frac {\partial \mathbf{e}}{\partial t} = \mu_0( \mathbf{j_f} + \frac {\partial \mathbf{p}}{\partial t} + \nabla \times \mathbf{m}) 
    :label: ampere_maxwell_differential_ebpm


Variables: \\(\\mathbf{e, b, d, h }\\)

where \\(\\mathbf{d}= \\epsilon_0 \\mathbf{e} + \\mathbf{p}\\)and \\( \\mathbf{b} = \\mu_0(\\mathbf{h} + \\mathbf{m})\\)

.. math:: 
    \boldsymbol{\nabla} \times \mathbf{h} = \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t} 
    :label: ampere_time_duplicate




Differential equations in the frequency domain. 

We use the Fourier transform definition in xxxx

The equation becomes  (check signs!!)

.. math::
    \nabla \times \mathbf{H}  + i \omega \mathbf{D} = \mathbf{J}_f
    :label: ampere_maxwell_frequency


If we deal with linear isotropic media then we have

.. math::
    \mathbf{D}(\omega)=\epsilon \mathbf{E}(\omega)

    \mathbf{J}_f(\omega)=\sigma \mathbf{E}\omega)

and the Ampere-Maxwell equations can be written as 

.. math::
    \nabla \times \mathbf{H}  - (\sigma - i \omega \epsilon \mathbf{E}) = 0






.. toctree::
    :maxdeepth:2

    formative_laws_and_people/index.rst

Constitutive Relationships and physical properties
For each of the constitutive relationships provide background regarding a basic (frequency domain) experiment by which to measure the physical property, whether it’s a scalar, tensor, or has frequency dependence. How the physical property links a field and flux.  (Links with sections in physical properties). 

.. toctree::
    :maxdepth: 2

    constitutive_relations/index.rst

