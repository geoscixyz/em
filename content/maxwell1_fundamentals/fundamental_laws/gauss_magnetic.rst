.. _gauss_magnetic:

Gauss's Law for Magnetic Fields
===============================


Integral equation
-----------------

The Gauss's law for magnetic fields in integral form is given below:

.. math::
    \oint_S \mathbf{b} \cdot d\mathbf{s} =  0
    :label: gauss_magnetic_integral
    
The equation states that there is no net magnetic flux \\(\\mathbf{b}\\) that passes through an arbitrary closed surface \\(\\mathbf{s}\\). This means the number of magnetic field lines that enter and exit through this closed surface \\(\\mathbf{s}\\) is the same. This is explained by the concept of a magnet that has a north and a south pole, where the strength of the north pole is equal to the strength of the south pole. This is equivalent to saying that a magnetic monopole, meaning a solitary north or south pole, does not exist.

Differential equation in the frequency-domain
----------------------------------------
Gauss's law for magnetic fields in differential form is written as:

.. math::
        \nabla \cdot \mathbf{B} = 0
        :label: gauss_magnetic_diff_freq

This formulation can be derived from the integral form using the divergence theorem:

.. math::
        0 = \oint_S \mathbf{B} \cdot d\mathbf{S} = \int_V ( \nabla \cdot \mathbf{B} ) d\mathbf{V}
        :label: gauss_magnetic_div_theorem

Alternatively, Gauss's law can be derived from the Biot-Savart law:

.. math::
        \nabla \cdot \mathbf{B}(r) = \frac{\mu_0}{4\pi} \int \nabla \cdot \frac{\mathbf{J}(r') \times \hat{w}}{w^2} dV

The variable \\(w\\) relates \\(r\\) and \\(r'\\): \\(w = (x-x') \\hat{x} + (y-y') \\hat{y} + (z-z') \\hat{z} \\). To carry through the divergence, the integrand can be expanded into:

.. math::
        \frac{\hat{w}}{w^2} \cdot (\nabla \cdot \mathbf{J}) - \mathbf{J} \cdot \left ( \nabla \times \frac{\hat{w}}{w^2} \right )

The first part becomes zero because \\(\\mathbf{J}\\) depends on \\(r'\\) and \\(\\nabla\\) depends only on \\(r\\). The second part is also zero as the curl of \\(\\frac{\\hat{w}}{w^2}\\) is zero.

Differential equation in the time-domain
---------------------------------------------

.. math::
        \nabla \cdot \mathbf{b} = 0
        :label: gauss_magnetic_diff_time

Units
-----

The units of magnetic flux \\(\\mathbf{B}\\) is the Tesla [T], which is equal to a Newton per Ampere-meter or \\(\\left [ \\frac{N}{Am} \\right ]\\).

Discoverers of the law
----------------------

