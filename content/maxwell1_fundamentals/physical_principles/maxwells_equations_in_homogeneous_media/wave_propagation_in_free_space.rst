.. _wave_propagation_in_free_space:

Wave Propagation in Free Space
==============================

.. todo:: illustration of how Ampere-Maxwell-Faraday interact to propagate energy in free space. this page is under construction

In this section, we look at getting the second-order differential equations from Maxwell's equations. We first do the analysis in time-domain and then use Fourier transforms to get the frequency-domain counterparts.

Wave equations in time-domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We begin with :ref:`Faraday <faraday>` and :ref:`Ampere-Maxwell <ampere_maxwell>` equations:

.. include:: ../../../equation_bank/faraday_time.rst

.. include:: ../../../equation_bank/ampere_maxwell_time.rst

and the the three constitutive relations:

.. include:: ../../../equation_bank/ohms_law_time.rst

.. math:: \mathbf{d} = \epsilon \mathbf{e}
        :name: depse

.. math:: \mathbf{b} = \mu \mathbf{h}
        :name: bmuh

We first take the curl of Equations :eq:`faraday_time` and :eq:`ampere_maxwell_time`:

.. math:: \boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{e}) = - \boldsymbol{\nabla} \times \frac{\partial \mathbf{b}}{\partial t}
        :name: hme1

.. math:: \boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{h}) = \boldsymbol{\nabla} \times \mathbf{j} + \boldsymbol{\nabla} \times \frac{\partial \mathbf{d}}{\partial t}
        :name: hmh1

The constitutive relations can be substituted into Equations :eq:`hme1` and :eq:`hmh1` to get the following expressions in terms of only :math:`\mathbf{e}` and :math:`\mathbf{h}`:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \boldsymbol{\nabla} \times \left (  \frac{\partial}{\partial t} (\mu \mathbf{h}) \right )
        :name: hme2

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \boldsymbol{\nabla} \times (\sigma \mathbf{e}) + \boldsymbol{\nabla} \times \left (  \frac{\partial}{\partial t} (\epsilon \mathbf{e}) \right )
        :name: hmh2

Because we assume a homogenous space, the physical properties :math:`\mu`, :math:`\epsilon`, and :math:`\sigma` can be moved out front of the derivative terms, simplifying the above expressions.

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \boldsymbol{\nabla} \times \frac{\partial \mathbf{h}}{\partial t}
        :name: hme3

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \sigma \boldsymbol{\nabla} \times \mathbf{e} + \epsilon \boldsymbol{\nabla} \times \frac{\partial \mathbf{e}}{\partial t}
        :name: hmh3

If we further assume that we can take the first and second derivatives of :math:`\mathbf{e}` and :math:`\mathbf{h}`, we can either take the spatial derivatives first or the time derivatives. Equations :eq:`hmh2` and :eq:`hmh3` can then also be written as:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \boldsymbol{\nabla} \times \mathbf{h} \right )
        :name: hme4

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \sigma \boldsymbol{\nabla} \times \mathbf{e} + \epsilon \frac{\partial}{\partial t} \left ( \boldsymbol{\nabla} \times \mathbf{e} \right )
        :name: hmh4

These expressions are now in terms of :math:`\boldsymbol{\nabla} \times \mathbf{e}` and :math:`\boldsymbol{\nabla} \times \mathbf{h}`. Thus, we can use Equations :eq:`faraday_time` and :eq:`ampere_maxwell_time` to generate two equations with either only :math:`\mathbf{e}` or :math:`\mathbf{h}`. We first start with Equation :eq:`hme4`, substitute in Equation :eq:`ampere_maxwell_time`, and simplify using the constitutive relations:

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t} \right )

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \sigma \mathbf{e} + \frac{\partial (\epsilon \mathbf{e})}{\partial t} \right )

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}
        :name: hme5

Additionally, we can simplify the first term of this expression by using the vector identity :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{x} = \boldsymbol{\nabla} \boldsymbol{\nabla} \cdot \mathbf{x} - \boldsymbol{\nabla}^2 \mathbf{x}`. Recalling that :math:`\boldsymbol{\nabla} \cdot \mathbf{e}` and :math:`\boldsymbol{\nabla} \cdot \mathbf{h}` are zero in a homogenous space, the vector identity simply becomes :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{x} = - \boldsymbol{\nabla}^2 \mathbf{x}`. If we now substitute that into :eq:`hme5`, we get the following equation:

.. math::  \boldsymbol{\nabla}^2 \mathbf{e}  - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} = 0
        :name: hme6

This is the wave equation for the electric field in the time-domain. The same approach can be done for the magnetic field, starting with Equation :eq:`hmh4`:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \frac{\partial \mathbf{b}}{\partial t} - \epsilon \frac{\partial}{\partial t} \left (\frac{\partial \mathbf{b}}{\partial t} \right )

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \frac{\partial (\mu \mathbf{h}) }{\partial t} - \epsilon \frac{\partial}{\partial t} \left (\frac{\partial (\mu \mathbf{h})}{\partial t} \right )

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2}

.. math:: - \boldsymbol{\nabla}^2 \mathbf{h} = - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2}

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2} - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} = 0
        :name: hmh6

Equation :eq:`hmh6` is then the wave equation for the magnetic field in the time-domain.

We now have two wave equations or second-order differential equations; one for the electric field and one for the magnetic field, summarized in Equations :eq:`hme7` and :eq:`hmh7`.

.. math::  \boldsymbol{\nabla}^2 \mathbf{e} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}  = 0
        :name: hme7

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \mu \sigma \frac{\partial \mathbf{h}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}  = 0
        :name: hmh7

Immediately apparent is that the two equations are very similar. Replace :math:`\mathbf{e}` with :math:`\mathbf{h}` in one wave equation and you get the other wave equation. The first temr is the Laplacian, the second term involves a first derivative, and the third term has a second-order time-dependence. If :math:`\sigma` is zero, the second term vanishes and the equations become a pure wave equation. Alternatively, if the third term were zero, the equations reduce to the heat equation and the field is diffusive. This becomes clearer when the equations are transformed to the frequency-domain.

Wave equations in frequency-domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: use the fourier transform to get the frequency-domain expressions

