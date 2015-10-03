.. _ampere_maxwell:

Ampere-Maxwell
==============


Integral Equation
-----------------

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


Differential equation in the time domain
----------------------------------------

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




Differential equations in the frequency domain
---------------------------------------------- 

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


Discovers of the law
--------------------