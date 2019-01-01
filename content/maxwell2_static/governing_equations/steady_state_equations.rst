.. _steady_state_equations:

Steady State Equations
======================

.. _steady_state_equations_dcr:

Direct Current Resistivity
---------------------------

A DC resistivity survey is ultimately an electromagnetic phenomenon and is
therefore governed by Maxwell's equations. However, the fact that the ground
is energized with a time invariant direct current allows us to use a much
simpler model.

.. _steady_state_equations_deriving_the_dcr_equations:

Deriving the DCR Equations
**************************

We can start from time domain differential form of the Ampere-Maxwell equation
equation (equation (5) on :ref:`ampere_maxwell`)

.. math::
    \boldsymbol{\nabla} \times \mathbf{h} = \mathbf{j}_{total} + \frac{\partial \mathbf{d}}{\partial t},
    :label: ampere_maxwell_differential_hjd

where :math:`\mathbf{h}` is the magnetic field, :math:`\mathbf{j}_{total}` is
the total current in the system, and :math:`\mathbf{d}` is the electric
displacement. We can divide up :math:`\mathbf{j}_{total}` as follows

.. math::
    \mathbf{j}_{total} = \sigma\mathbf{e} + \mathbf{j}_{source},
    :label: jsep

which states that the total current densisty can be divided into the current
in the ground (:math:`\sigma\mathbf{e}` due to Ohm's law) and the current in
the source wires (:math:`\mathbf{j}_{source}`). Since we are in the steady
state case, :math:`\frac{\partial \mathbf{d}}{\partial t}=0`. Using that
assumption and substituting :eq:`jsep` into
:eq:`ampere_maxwell_differential_hjd` we obtain

.. math::
    \boldsymbol{\nabla} \times \mathbf{h} - \sigma\mathbf{e} = \mathbf{j}_{source}.
    :label: ampere_maxwell_differential_jsep

Faraday's law is also simplified in steady state. It becomes

.. math::
    \boldsymbol{\nabla \times} \mathbf{e} = \mathbf{0}.

In other words it is a potential field. In particular, this means that

.. math::
    \mathbf{e} = -\boldsymbol{\nabla}\phi,
    :label: epot

where :math:`\phi` is the electric potential. This allows us to write
:eq:`ampere_maxwell_differential_jsep` as

.. math::
    \boldsymbol{\nabla} \times \mathbf{h} + \sigma\boldsymbol{\nabla}\phi = \mathbf{j}_{source}.
    :label: ampere_maxwell_differential_phi

Taking the divergence of both sides of :eq:`ampere_maxwell_differential_phi`
gives the governing equation for DC resistivity

.. math::
    \boldsymbol{\nabla} \cdot \sigma\boldsymbol{\nabla}\phi = \boldsymbol{\nabla}\cdot\mathbf{j}_{source}.
    :label: dcr_fwd
