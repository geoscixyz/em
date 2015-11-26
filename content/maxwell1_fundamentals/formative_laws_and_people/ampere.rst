.. _ppl_ampere:

Ampere
========================

Akin to Biot-Savard's Law, Ampere's law relates the electrical current to the magnetic field such that:

.. math::
    \oint_L \mathbf{H} \cdot dL = \int_{\Omega} J \cdot d\Omega  \;,
    :label: ampere_law_int

which states that the line integral around a closed loop multiplied by the magnetic field :math:`\mathbf{H}` in Amperes per meter [:math:`A/m`] is proportional to the electric current :math:`J` in Amperes [:math:`A`] flowing through the area [:math:`\Omega`] defined by the loop.
The same relatation can be written in differential form as:

.. math::
    \nabla \times \mathbf{H} =  \mathbf{J} \;.
    :label: ampere_law_diff

The law was named in honour of the French physicist Andre-Marie Ampere, who pioneered reseach in electrodynamics. 
Ampere's theoritical work made possible the conversion of electrical current into mechanical work, which would later contribute to the devolepment of the electric motor by {Micheal Faraday} in 1821.

Ampere's Law also appears in Maxwell's fouth equation as:

.. math::
    \nabla \times \mathbf{H} =  \mathbf{} + \frac{\partial \mathbf{E}}{\partial t}\;,
    :label: Maxwell_s_4th

which includes Maxwell's addition relating the magnetic field [:math:`\mathbf{H}`] to the time-varying electric field [:math:`\mathbf{E}`].