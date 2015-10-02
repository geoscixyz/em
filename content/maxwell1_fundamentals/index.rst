.. _maxwell1_fundamentals_index:

ME I: Fundamentals
==================

Overview of Maxwell's Equations
-------------------------------

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

To reference an equation by number, :eq:`faraday_time`. Some inline math looks like \\(\\boldsymbol{\\nabla} \\times \\mathbf{e} = -\\frac{\\partial \\mathbf{b}}{\\partial t}\\). To include something from the equation bank...

.. include:: ../equation_bank/ohms_law_freq.rst

and to reference something from the equation bank by number :eq:`ohms_law_freq`. 

To reference another page, you do :ref:`constitutive_relations_index` (note that this is at the top of the file constitutive_relations/index.rst)


To **bold** and to *italicize*

.. Previous content (this is commented out)

In this chapter we first present a synopsis of Maxwell's equations in three forms: 
(a) Differential equation in time
(b) Integral equations in time
(c) Equations in the frequency domain

These are designed to be a quick access to the relevant equations with proper notation and units. Each of the four fundamental Maxwell equations, as well as the conservation of charge, is then explored in more detail to promote a physical understanding and provide insight as to where the law is useful. In addition we provide a short synopsis of the scientists involved in discovering the law. 

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

.. toctree::
    :maxdeepth:2

    formative_laws_and_people/index.rst

Constitutive Relationships and physical properties
For each of the constitutive relationships provide background regarding a basic (frequency domain) experiment by which to measure the physical property, whether it’s a scalar, tensor, or has frequency dependence. How the physical property links a field and flux.  (Links with sections in physical properties). 

.. toctree::
    :maxdepth: 2

    constitutive_relations/index.rst

