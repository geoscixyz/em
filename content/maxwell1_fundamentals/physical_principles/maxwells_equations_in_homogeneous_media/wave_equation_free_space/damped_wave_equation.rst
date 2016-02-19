.. _damped_wave_equation:

Damped wave equation
^^^^^^^^^^^^^^^^^^^^

.. todo:: Purpose, summary, goal

We begin with :ref:`Faraday <faraday>` and :ref:`Ampere-Maxwell <ampere_maxwell>` equations in the time-domain:

.. include:: ../../../../equation_bank/faraday_time.rst

.. include:: ../../../../equation_bank/ampere_maxwell_time.rst

and the three constitutive relations:

.. include:: ../../../../equation_bank/ohms_law_time.rst

.. math:: \mathbf{d} = \epsilon \mathbf{e}
        :name: depse

.. math:: \mathbf{b} = \mu \mathbf{h}
        :name: bmuh

The goal is to combine these equations to obtain a single equation that involves :math:`\mathbf{e}` or :math:`\mathbf{h}`. For instance, to develop an equation for :math:`\mathbf{e}`, we take the curl of :eq:`faraday_time` and use Equations :eq:`ohms_law_time` and :eq:`depse` to reduce the number of variables. Because all of the physical properties are assumed to be constant in space and time, they are not affected by curl operators or time derivatives. Thus the equation for :math:`\mathbf{e}` becomes Equation :eq:`hme7`. 

.. math::  \boldsymbol{\nabla}^2 \mathbf{e} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}  = 0
        :name: hme7

A similar procedure can be used to obtain an equation that involves only :math:`\mathbf{h}`, starting from Equation :eq:`ampere_maxwell_time` and using Equations :eq:`faraday_time` and :eq:`bmuh`, we obtain:

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \mu \sigma \frac{\partial \mathbf{h}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}  = 0
        :name: hmh7

The detailed derivation of Equations :eq:`hme7` and :eq:`hmh7` can be found :ref:`here <wave_propagation_in_free_space_details>`.

The equations for :math:`\mathbf{e}` and :math:`\mathbf{h}` are identical in form. The first term is the Laplacian, the second term involves a first derivative in time, and the third term has a second order time derivative. This is the general form taken by a propagating and attenuating wave. If :math:`\sigma` = 0, the second term vanishes and the equations become a pure wave equation so that the energy propagates without loss. Alternatively, if the third term were zero, the equations reduce to the heat equation and the field is diffusive.




