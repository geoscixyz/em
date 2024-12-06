.. _gauss_magnetic:

Gauss's Law for Magnetic Fields
===============================

.. figure:: images/BarMagnet.png
    :figwidth: 50%
    :align: right
    :name: barmagnet

    When a bar magnet is cut in two, you get two bar magnets.

 
Gauss's law for magnetism states that no magnetic monopoles exists and that
the total flux through a closed surface must be zero. This page describes the
time-domain integral and differential forms of Gauss's law for magnetism and
how the law can be derived. The frequency-domain equation is also given. At
the end of the page, a brief history of the Gauss's law for magnetism is
provided.

.. _gauss_magnetic_integral:

Integral equation
-----------------

The Gauss's law for magnetic fields in integral form is given by:

.. math::
    \oint_S \mathbf{b} \cdot \mathbf{da} =  0,
    :label: gauss_magnetic_integral

where:

- :math:`\mathbf{b}` is the magnetic flux
    
The equation states that there is no net magnetic flux :math:`\mathbf{b}`
(which can be thought of as the number of magnetic field lines through an
area) that passes through an arbitrary closed surface :math:`S`. This means
the number of magnetic field lines that enter and exit through this closed
surface :math:`S` is the same. This is explained by the concept of a magnet
that has a north and a south pole, where the strength of the north pole is
equal to the strength of the south pole (:numref:`barmagnet`). This is
equivalent to saying that a magnetic monopole, meaning a solitary north or
south pole, does not exist because for every positive magnetic pole, there
must be an equal amount of negative magnetic poles.

.. _gauss_magnetic_differential:

Differential equation
---------------------

Gauss's law for magnetic fields in the differential form can be derived using
the divergence theorem. The divergence theorem states:

.. math::
        \int_V (\mathbf{\nabla} \cdot \mathbf{f}) dv = \oint_S \mathbf{f} \cdot \mathbf{da},

where :math:`\mathbf{f}` is a vector. The right-hand side looks very similar
to Equation :eq:`gauss_magnetic_integral`. Using the divergence theorem,
Equation :eq:`gauss_magnetic_integral` is rewritten as follows:

.. math::
        0 = \oint_S \mathbf{b} \cdot d\mathbf{a} = \int_V ( \nabla \cdot \mathbf{b} ) dv.
        :label: gauss_magnetic_div_theorem

Because the expression is set to zero, the integrand :math:`(\nabla \cdot
\mathbf{b})` must be zero also. Thus the differential form of Gauss's law
becomes:

.. math::
        \nabla \cdot \mathbf{b} = 0.
        :label: gauss_magnetic_diff_time


Derivation using Biot-Savart law
--------------------------------

Gauss's law can be derived using the :ref:`Biot-Savart law <biot_savart>`,
which is defined as:

.. math::
        \mathbf{b}(\mathbf{r}) = \frac{\mu_0}{4\pi} \int_V \frac{(\mathbf{j} (\mathbf{r'}) dv) \times ~\mathbf{\hat{\underline{r}}}}{\lvert \mathbf{r} - \mathbf{r'} \rvert ^2},
       :label: gauss_biot_savart 

where:

- :math:`\mathbf{b}(\mathbf{r})` is the magnetic flux at the point :math:`\mathbf{r}`
- :math:`\mathbf{j}(\mathbf{r'})` is the current density at the point :math:`\mathbf{r'}`
- :math:`\mu_0` is the magnetic permeability of free space.

Taking the divergence of both sides of Equation :eq:`gauss_biot_savart` yields:

.. math::
        \nabla \cdot \mathbf{b}(\mathbf{r}) = \frac{\mu_0}{4\pi} \int_V \nabla \cdot \frac{(\mathbf{j} (\mathbf{r'}) dv) \times ~\mathbf{\hat{\underline{r}}}}{\lvert \mathbf{r} - \mathbf{r'} \rvert ^2}.
        :label: gauss_bs_div

To carry through the divergence of the integrand in Equation
:eq:`gauss_bs_div`, the following vector identity is used:

.. math::
        \nabla \cdot (\mathbf{A} \times \mathbf{B}) = \mathbf{B} \cdot (\nabla \times \mathbf{A}) - \mathbf{A} \cdot (\nabla \times \mathbf{B}).

Thus, the integrand becomes:

.. math::
        \left[ \mathbf{j} (\mathbf{r'}) \cdot \left( \nabla \times \frac{~\mathbf{\hat{\underline{r}}}}{\lvert \mathbf{r} - \mathbf{r'} \rvert ^2} \right) \right] - \left[ \frac{~\mathbf{\hat{\underline{r}}}}{\lvert \mathbf{r} - \mathbf{r'} \rvert ^2} \cdot \left( \nabla \times \mathbf{j} (\mathbf{r'}) \right) \right]
        :label: gauss_inside_div

The first part of Equation :eq:`gauss_inside_div` is zero as the curl of
:math:`\frac{~\mathbf{\hat{\underline{r}}}}{\lvert \mathbf{r} -
\mathbf{r'} \rvert ^2}` is zero. The second part of Equation
:eq:`gauss_inside_div` becomes zero because :math:`\mathbf{j}` depends on
:math:`r'` and :math:`\nabla` depends only on :math:`r`. Plugging this back
into :eq:`gauss_bs_div`, the right-hand side of the expression becomes zero.
Thus, we see that:

.. math::
        \nabla \cdot \mathbf{b}(\mathbf{r}) = 0,

which is Gauss's law for magnetism in differential form.


Differential equation in the frequency-domain
---------------------------------------------

The equation can also be written in the frequency-domain as:

.. math::
        \nabla \cdot \mathbf{B} = 0.
        :label: gauss_magnetic_diff_freq

.. _gauss_magnetic_frequency:

Units
-----

+----------------------------+-------------------+-------------------------------------+-------------------------+
|Magnetic flux               | :math:`\mathbf{b}`| T                                   | tesla                   |
+----------------------------+-------------------+-------------------------------------+-------------------------+
|Electric current density    | :math:`\mathbf{j}`|:math:`\frac{\text{A}}{\text{m}^2}`  | ampere per square meter |
+----------------------------+-------------------+-------------------------------------+-------------------------+


**Constants** 

+--------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Magnetic constant        | :math:`\mu_0 = 4\pi ×10^{−7} \frac{\text{N}}{\text{A}^2} \approx 1.2566370614...×10^{-6} \frac{\text{T}\cdot \text{m}}{\text{A}}`|
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------+


Discoverers of the law
----------------------

Gauss's law for magnetism is a physical application of Gauss's theorem (also
known as the divergence theorem) in calculus, which was independently
discovered by Lagrange in 1762, Gauss in 1813, Ostrogradsky in 1826, and Green
in 1828. Gauss's law for magnetism simply describes one physical phenomena
that a magnetic monopole does not exist in reality. So this law is also called
"absence of free magnetic poles".

People had long been noticing that when a bar magnet is divided into two
pieces, two small magnets are created with their own south and north poles.
This can be explained by Ampere's circuital law: the bar magnet is made of
many circular currents rings, each of which is essentially a magnetic dipole;
the macroscopic magnetism is from the alignment of the microscopic magnetic
dipoles. Because a small current ring always generates an equivalent magnetic
dipole, there is no way of generating a free magnetic charge. So far, no
magnetic monopole has been found in experiments, despite that many theorists
believe a magnetic monopole exists and are still searching for it.

However, as pointed out by Pierre Curie in 1894, magnetic monopoles can exist
conceivably. Introducing fictitious magnetic charges to the Maxwell's
equations can give Gauss's law for magnetism the same appearance as Gauss's
law for electricity, and the mathematics can become symmetric.
