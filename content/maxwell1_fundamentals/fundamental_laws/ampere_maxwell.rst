.. _ampere_maxwell:

Ampere-Maxwell
==============

Integral Equation
-----------------

The Ampere-Maxwell equation in integral form is given below:

.. math::
    \int_S \boldsymbol{\nabla} \times \mathbf{b} \cdot \mathbf{ds} =  \oint_C \mathbf{b} \cdot \mathbf{dl} = \mu_0 \left( I_{enc} + \epsilon_0 \frac{d}{dt} \int_S \mathbf{e} \cdot \hat{\mathbf{n}} ~\text{ds} \right)
    :label: ampere_maxwell_integral

where:

 - \\( \\mathbf{b} \\) is the magnetic flux
 - \\( \\mathbf{e} \\) is the electric field
 - \\( I_{enc} \\) is the enclosed current
 - \\( \\mu_0 \\) is the magnetic permeability of free space
 - \\( \\epsilon_0 \\) is the electric permittivity of free space
 - \\( \\hat{\\mathbf{n}} \\) is the outward pointing unit-normal

The first portion of the equation was discovered by Ampere. It shows the relationship
between a current \\(I_{enc}\\) and the circulation of the magnetic field, \\(\\mathbf{b}\\),
around any closed contour line. \\(I_{enc}\\) refers to all currents
irrespective of their physical origin.

The second portion of the equation is Maxwell's contribution and shows that a
circulation of magnetic field is also caused by a time rate of change of
electric flux. This explains how current in a simple circuit involving a
battery and capacitor can flow. (ref). The term is pivotal in showing that
electromagnetic energy propagates as waves.

The integral forumulations are physically insightful and closely relate to the
experiments that gave rise to them. They are also play a formative role in
generating boundary conditions for waves that propagate through different
materials.

When dealing with the propagation of EM waves in matter the currents
\\(I_{enc}\\) are usually dealt with in terms of current densities. The
integral equation above is thus written as


.. math:: 
    \int_S \boldsymbol{\nabla} \times \mathbf{b} \cdot \mathbf{ds} =  
    \oint_C \mathbf{b} \cdot \mathbf{dl} = 
    \mu_0 \left(\int_S \left(\mathbf{j_f}  
        + \frac{\partial \mathbf{p}}{\partial t} 
        + \boldsymbol{\nabla} \times \mathbf{m}\right)\cdot \mathbf{ds} 
        +  \epsilon_0 \frac{d}{dt}  \int_S \mathbf{e} \cdot \mathbf{\hat{n}} ~\text{ds}\right)
    :label: ampere_maxwell_integral_p&m

where the current densities are:
\\(\\mathbf{j_f}\\)= free current caused by moving charges
\\(\\mathbf{j_b} = \\frac{\\partial \\mathbf{p}}{\\partial t}\\)  where \\(\\mathbf{p}\\) is the electric polarization resulting from bound charges in dielectrics
\\(\\mathbf{j_p} = \\nabla \\times \\mathbf{m}\\) is the magnetic polarization current. That is currents needed to generate the magnetization \\( \\mathbf{m}\\). 


A note on the total current
***************************

The total current involved in the Ampere-Maxwell equation consists of free
current and bound current, although all currents are essentially the same from
a microscopic perspective. Treating free current and bound current differently
offers physical insights to the Ampere-Maxwell equation in different contexts.

The free current is caused by moving charges which are not tied to atoms, often
referred to as conduction current. In contrast, the bound current is induced by
a magnetization or a polarization in bulk materials. When a magnetic material is
placed in an external magnetic field, a magnetization current will be induced
due to the motion of electrons in atoms. Likewise, when an external electric
field is applied to a dielectric, the positive and negative bound charges within
the dielectric can separate and induce a polarization current density internally.

Then the total current density can be described as

.. math::
    \mathbf{j} = \mathbf{j}_f + \mathbf{j}_m + \mathbf{j}_p

where
\\(\\mathbf{j}_f = \\sigma \\mathbf{e} \\) is the free current density caused by
moving charges,
\\(\\mathbf{j}_m = \\nabla \\times \\mathbf{m}\\) is the bound current due to
magnetization,
\\(\\mathbf{j}_p = \\frac{\\partial \\mathbf{p}}{\\partial t} \\) is the polarization
current density due to the time-dependent bound charges.

Treating free current and bound current separately and combining the
constitutive equations, the Ampere-Maxwell equation can be reformulated as
in integral form:

.. math::
    \int_S \boldsymbol{\nabla} \times \mathbf{h} \cdot \mathbf{ds} = \oint_C \mathbf{h} \cdot \mathbf{dl} = \int_S \left( \mathbf{j}_f + \frac{\partial \mathbf{d}}{\partial t} \right) \cdot \hat{\mathbf{n}} ~\text{ds}

and in differential form,

.. math::
    \boldsymbol{\nabla} \times \mathbf{h} = \mathbf{j}_f + \frac{\partial \mathbf{d}}{\partial t}

Note that the bound charge due to magnetization is integrated into the magnetic
field \\(\\mathbf{h}\\), whereas the bound charge due to electric polarization is
integrated into the displacement field \\(\\mathbf{d}\\).


Differential equation in the time domain
----------------------------------------

There are a number of ways of writing the equation in differential form. Each
provides its own insight.

Variables:   \\(\\mathbf{e, b, p, m} \\)

.. math::
    \boldsymbol{\nabla} \times \mathbf{b} 
        - \epsilon_0 \mu_0 \frac{\partial \mathbf{e}}{\partial t} 
    = \mu_0\left( \mathbf{j_f} 
        + \frac {\partial \mathbf{p}}{\partial t} 
        + \boldsymbol{\nabla} \times \mathbf{m}\right) 
    :label: ampere_maxwell_differential_ebpm

Variables: \\(\\mathbf{e, b, d, h }\\)

where \\(\\mathbf{d}= \\epsilon_0 \\mathbf{e} + \\mathbf{p}\\) and \\( \\mathbf{b} = \\mu_0(\\mathbf{h} + \\mathbf{m})\\)

.. include:: ../../equation_bank/ampere_maxwell_time.rst




Differential equations in the frequency domain
---------------------------------------------- 

We use the \\(e^{i\\omega t}\\) :ref:`fourier_transform_convention` 

The equation becomes 

.. math::
    \boldsymbol{\nabla} \times \mathbf{H}  - i \omega \mathbf{D} = \mathbf{J}_f
    :label: ampere_maxwell_frequency


If we deal with linear isotropic media then we have

.. math::
    \mathbf{D}(\omega)=\epsilon \mathbf{E}(\omega)

    \mathbf{J}_f(\omega)=\sigma \mathbf{E}(\omega)

and the Ampere-Maxwell equations can be written as 

.. math::
    \boldsymbol{\nabla} \times \mathbf{H}  - (\sigma + i \omega \epsilon) \mathbf{E} = 0

Units
-----

Magnetic B-field \\(\\mathbf{b}\\): tesla \\([T]\\). One tesla equals one weber (the SI unit of magnetix flux) per square metre: \\(1 T = 1 \\frac{Wb}{m^{2}} = 1 \\frac{V\\cdot s}{m^{2}}\\).

Electric field intensity \\(\\mathbf{e}\\): volt per metre \\([\\frac{V}{m}]\\)

Electric current \\(I\\): ampere \\([A]\\). One ampere equals one coulomb (the SI unit of electric charge) per second: \\(1 A = 1 \\frac{C}{s}\\).

Electric current density \\(\\mathbf{j}\\): ampere per square metre \\([\\frac{A}{m^{2}}]\\)

Magnetization \\( \\mathbf{m} \\):

Electric polarization \\(\\mathbf{p}\\):

Magnetic H-field \\(\\mathbf{h}\\): ampere per metre \\([\\frac{A}{m}]\\)

Electric displacement \\(\\mathbf{d}\\): coulomb per square metre \\([\\frac{C}{m^{2}}]\\)

Magnetic constant \\(\\mu_0 = 4\\pi ×10^{−7} \\frac{N}{A^2} \\approx  1.2566370614...×10^{-6} \\frac{T\\cdot m}{A} \\). 

Vacuum permittivity \\(\\epsilon_0  \\approx 8.854 187 817... × 10^{−12} \\frac{F}{m} \\) (farads per metre).

Discovers of the law
--------------------

The first observation that bring researchers to look for the relationship linking magnetic field and current is due to Hans Christian Ørsted in 1820, who notices electric currents were deflected magnetic needles. This leads several physicists in Europe to study this phenomenon in parallels. While Jean-Baptiste Biot and Félix Savart were experimentating with a setup closed to Ørsted's experiment (that lead them to define in 1820 a relationship known now as the Biot-Savart's law), André-Marie Ampère's experiment focus on measuring the forces that two electric wires were exercing on each other.He expressed the Ampere’s circuital law in 1826 [1]_,
which relates the magnetic field associated with a closed loop to the electric
current passing through it. In its original form, the current enclosed by the
loop only refers to free current caused by moving charges, causing several issues
regarding the conservation of electric charge and the propagation of
electromagnetic energy.

In 1861 [2]_, James Clerk Maxwell extended the Ampere’s law by introducing the
displacement current into the electric current term in the equation to satisfy
the continuity equation of electric charge. Based on the idea of displacement
current, in 1864 [3]_, Maxwell had established the theory of electromagnetic
field, predicating the wave propagation of electromagnetic field and the
equivalence of light propagation and electromagnetic wave.

Until the late 1880s [4]_, Heinrich Hertz had experimentally proved the existence
of electromagnetic waves predicated by Maxwell’s electromagnetic theory, and
demonstrated the equivalence of electromagnetic wave and light.

These efforts have lain solid foundations for the development of modern electromagnetism.

.. LJH comment: I think we can combine what is below into the explination under the integral equation



**References**

.. [1] David J. Griffiths, Introduction to electrodynamics, 3rd Edition, Prentice Hall. 1999.
.. [2] James C. Maxwell. On physical lines of force, part III, the Philosophical Magazine and Journal of Science, 1861
.. [3] James C. Maxwell. A dynamical theory of the electromagnetic field. 1864
.. [4] Heinrich Hertz. Electric waves: being researches on the propagation of electric action with finite velocity through space, Dover publications. 1893.
