.. _quick_guide_maxwell:

Quick Guide to Maxwell's Equations
==================================

In this section we first present a synopsis of Maxwell's equations in three forms:

(a) :ref:`differential_equations_time`
(b) :ref:`integral_equations_time`
(c) :ref:`differential_equations_frequency`

These are designed to be a quick access to the relevant equations with proper
:ref:`notation<introduction_notation>` and units. Each of the four fundamental
Maxwell equations, as well as the conservation of charge, is then explored in
more detail to promote a physical understanding and provide insight as to
where the law is useful. In addition we provide a short synopsis of the
scientists involved in discovering the law.

Maxwell's equations connect electric and mangetic fields, fluxes and physical properties. 


.. include:: maxwell_variables.rst


.. _differential_equations_time:


Differential equations in time
------------------------------


- :ref:`Faraday's Law <faraday_differential_time>`
    .. include:: ../equation_bank/faraday_time.rst


- :ref:`Ampere Maxwell Law <ampere_maxwell_differential_time>`
    .. include:: ../equation_bank/ampere_maxwell_time.rst


- :ref:`Gauss's Law for Electric Fields <gauss_electric_differential>`
    .. include:: ../equation_bank/gauss_electric_time.rst

- :ref:`Gauss's Law for Magnetic Fields <gauss_magnetic_differential>`
    .. include:: ../equation_bank/gauss_magnetic_time.rst



.. _integral_equations_time:

Integral equations in time
---------------------------

.. summary of relevant equations

- :ref:`Gauss's Law for Magnetic Fields <gauss_magnetic_integral>`
    .. include:: ../equation_bank/gauss_magnetic_int_time.rst

.. _differential_equations_frequency:

Differential equations in frequency
-----------------------------------

- :ref:`Gauss's Law for Magnetic Fields <gauss_magnetic_frequency>`
    .. include:: ../equation_bank/gauss_magnetic_frequency.rst

.. summary of relevant equations

.. _boundary_conditions:

Boundary Conditions
-------------------


.. This because of the include statement, we don't need a toctree entry for the maxwell variables page (and want to suppress warnings)

.. toctree::
    :hidden:

    maxwell_variables
