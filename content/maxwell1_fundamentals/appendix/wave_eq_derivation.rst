.. _maxwell1_appendix_wave_eq_derivation_time:

Derivation of the Wave Equation in Time
=======================================

Here, we derive the wave equations in time for the electric and magnetic fields.To accomplish this, we begin with :ref:`Faraday's Law <faraday>` and :ref:`Ampere-Maxwell's Law <ampere_maxwell>`:

.. include:: ../../equation_bank/faraday_time.rst

.. include:: ../../equation_bank/ampere_maxwell_time.rst

as well as the three constitutive relations:

.. include:: ../../equation_bank/ohms_law_time.rst

.. math:: \mathbf{d} = \epsilon \mathbf{e}
        :name: depse

.. math:: \mathbf{b} = \mu \mathbf{h}
        :name: bmuh

Derivation for the Electric Field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To derive the wave equation for :math:`\mathbf{e}`, we first take
the curl of Faraday's Law, shown in equation :eq:`faraday_time`:

.. math:: \boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{e}) = - \boldsymbol{\nabla} \times \frac{\partial \mathbf{b}}{\partial t}
        :name: hme1

The appropriate constitutive relations can be substituted into Equation
:eq:`hme1` to get the following expressions in terms of only the fields
:math:`\mathbf{e}` and :math:`\mathbf{h}` instead of fields and fluxes:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \boldsymbol{\nabla} \times \left (  \frac{\partial}{\partial t} (\mu \mathbf{h}) \right )
        :name: hme2

Assuming the physical properties are homogeneous throughout the domain, :math:`\mu`,
:math:`\epsilon`, and :math:`\sigma` can be moved out front of the derivative
terms. This simplifies the above expressions:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \boldsymbol{\nabla} \times \frac{\partial \mathbf{h}}{\partial t}
        :name: hme3

If we further assume that we can take the first and second derivatives of
:math:`\mathbf{e}`, we can either take the spatial derivatives first or the
time derivatives. Equation :eq:`hme3` can then also be written as:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \boldsymbol{\nabla} \times \mathbf{h} \right )
        :name: hme4

This expression is now solely in terms of :math:`\boldsymbol{\nabla} \times
\mathbf{e}` and :math:`\boldsymbol{\nabla} \times \mathbf{h}`. Thus, we can
use Equation :eq:`ampere_maxwell_time` to generate an equation with only
:math:`\mathbf{e}`. We substitute in Equation :eq:`ampere_maxwell_time` into
Equation :eq:`hme4` and simplify using the constitutive relations in Equations
:eq:`ohms_law_time` and :eq:`depse`:

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t} \right )

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \sigma \mathbf{e} + \frac{\partial (\epsilon \mathbf{e})}{\partial t} \right )

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}
        :name: hme5

Additionally, we can simplify the first term of this expression by using the
vector identity :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times
\mathbf{x} = \boldsymbol{\nabla} \boldsymbol{\nabla} \cdot \mathbf{x} -
\boldsymbol{\nabla}^2 \mathbf{x}`. Recalling that both
:math:`\boldsymbol{\nabla} \cdot \mathbf{e}` and :math:`\boldsymbol{\nabla}
\cdot \mathbf{h}` are zero in a homogenous space, the vector identity simply
becomes :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times
\mathbf{x} = - \boldsymbol{\nabla}^2 \mathbf{x}`. If we now substitute that
into :eq:`hme5`, we get the following expression:

.. math::  \boldsymbol{\nabla}^2 \mathbf{e}  - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} = 0
        :name: hme6

This is the wave equation for the electric field in the time domain.

Derivation for the Magnetic Field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To derive the wave equation for :math:`\mathbf{h}`, we repeat the above
derivation but start by taking the curl of Ampere's Law, shown in
equation :eq:`ampere_maxwell_time`:

.. math:: \boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{h}) = \boldsymbol{\nabla} \times \mathbf{j} + \boldsymbol{\nabla} \times \frac{\partial \mathbf{d}}{\partial t}
        :name: hmh1

The constitutive relations can be substituted into Equation :eq:`hmh1` to get
the following expressions in terms of only :math:`\mathbf{e}` and
:math:`\mathbf{h}`:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \boldsymbol{\nabla} \times (\sigma \mathbf{e}) + \boldsymbol{\nabla} \times \left (  \frac{\partial}{\partial t} (\epsilon \mathbf{e}) \right )
        :name: hmh2

We simplify the expression just like we did before for the electric field.

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \sigma \boldsymbol{\nabla} \times \mathbf{e} + \epsilon \boldsymbol{\nabla} \times \frac{\partial \mathbf{e}}{\partial t}
        :name: hmh3

We can assume that we can take the first and second derivatives of
:math:`\mathbf{e}` and :math:`\mathbf{h}` and can either take the spatial
derivatives or time derivatives first. Equation :eq:`hmh3` can then also be
written as:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \sigma \boldsymbol{\nabla} \times \mathbf{e} + \epsilon \frac{\partial}{\partial t} \left ( \boldsymbol{\nabla} \times \mathbf{e} \right )
        :name: hmh4

These expressions are now in terms of :math:`\boldsymbol{\nabla} \times
\mathbf{e}` and :math:`\boldsymbol{\nabla} \times \mathbf{h}`. Thus, we can
use Equation :eq:`faraday_time` to generate an equation with only
:math:`\mathbf{h}`. We then again use the vector identity
:math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{x} =
\boldsymbol{\nabla} \boldsymbol{\nabla} \cdot \mathbf{x} -
\boldsymbol{\nabla}^2 \mathbf{x}` and the fact that :math:`\boldsymbol{\nabla}
\cdot \mathbf{h}` is zero in a homogenous space to simplify the vector
identity to :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times
\mathbf{x} = - \boldsymbol{\nabla}^2 \mathbf{x}`. This is then substituted
into the wave equation. The following shows these derivations.

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \frac{\partial \mathbf{b}}{\partial t} - \epsilon \frac{\partial}{\partial t} \left (\frac{\partial \mathbf{b}}{\partial t} \right )

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \frac{\partial (\mu \mathbf{h}) }{\partial t} - \epsilon \frac{\partial}{\partial t} \left (\frac{\partial (\mu \mathbf{h})}{\partial t} \right )

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2}

.. math:: - \boldsymbol{\nabla}^2 \mathbf{h} = - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2}

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2} - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} = 0
        :name: hmh6

Equation :eq:`hmh6` is then the wave equation for the magnetic field in the time domain.


