.. _time_domain_equations:

Maxwell's Equations: Time Domain
================================

.. purpose::

    Here, :ref:`Faraday's law<faraday>` and the :ref:`Ampere-Maxwell<ampere_maxwell>` equation are used to construct lossy wave equations for both :math:`\mathbf{e}` and :math:`\mathbf{h}`, respectively. This is accomplished by assuming we are in a homogeneous medium. Detailed derivations can be found in the :ref:`Appendix<maxwell1_appendix_wave_eq_derivation_time>`. Various components of the resulting 2nd order differential equations in time are discussed. The physical understanding of equations derived here can be extended to more complex applications throughout EM GeoSci.

Let us begin with the differential form of :ref:`Faraday's Law <faraday>` and the :ref:`Ampere-Maxwell's equation <ampere_maxwell>`, respectively:

.. math::
    \boldsymbol{\nabla} \times \mathbf{e}
    = -\frac{\partial \mathbf{b}}{\partial t}
    :label: faraday_time

.. math::
    \boldsymbol{\nabla} \times \mathbf{h}
    = \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t}
    :label: ampere_maxwell_time

as well as the three :ref:`constitutive relations<physical_properties_index>`:

.. math::
    \mathbf{j} = \sigma \mathbf{e}
    :label: ohms_law_time

.. math:: \mathbf{d} = \epsilon \mathbf{e}
    :label: depse

.. math:: \mathbf{b} = \mu \mathbf{h}
    :label: bmuh

Our goal is to combine these equations to obtain an equation which depends solely on :math:`\mathbf{e}` or :math:`\mathbf{h}`. For :math:`\mathbf{e}`, we begin by taking the curl of :eq:`faraday_time`. We then use Eqs. :eq:`ohms_law_time` and :eq:`depse` to reduce the number of variables. Assuming all of the physical properties are constant in space and time, we can take them outside curl operators and time derivatives. Ultimately, we obtain Eq. :eq:`hme7`:

.. math::  \boldsymbol{\nabla}^2 \mathbf{e} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}  = 0
    :label: hme7

A similar procedure can be used to obtain an equation that involves only :math:`\mathbf{h}`. We start from Eq. :eq:`ampere_maxwell_time`, and by using Eqs. :eq:`faraday_time` and :eq:`bmuh` we obtain:

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \mu \sigma \frac{\partial \mathbf{h}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}  = 0
    :label: hmh7

The detailed derivations of Eqs. :eq:`hme7` and :eq:`hmh7` can be found :ref:`here <maxwell1_appendix_wave_eq_derivation_time>`.

The Lossy Wave Equation
-----------------------

Eqs. :eq:`hme7` and :eq:`hmh7` have identical form and are both characterized using the **lossy wave equation**. Thus, electromagnetic signals propagate as waves that are also subject to diffusion. The first term in each equation is called the Laplacian (:math:`\nabla^2`). The second term, which contains a first order time derivative, controls the diffusive behaviour of the electromagnetic signal. The third term, which contains a second order time derivative, represents an energy conservation term. The propagation velocity, diffusion and other behaviours of electromagnetic waves are discussed when presenting materials on :ref:`transient planewaves in homogeneous media<transient_planewaves_homogeneous_index>`.

Quasi-Static Regime
-------------------

In the quasi-static regime, the diffusive term is much larger than the conservation term, i.e.:

.. math::
    \sigma \frac{\partial \mathbf{e}}{\partial t} \gg \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} \;\;\;\;\; \textrm{and} \;\;\;\;\; \sigma \frac{\partial \mathbf{h}}{\partial t} \gg \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}

In this case, both :math:`\mathbf{e}` and :math:`\mathbf{h}` behave according to the **heat equation**, with:

.. math::
    \nabla^2 \mathbf{e} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} = 0

and

.. math::
    \nabla^2 \mathbf{h} - \mu\sigma \frac{\partial \mathbf{h}}{\partial t} = 0

The rate of diffusion is controlled by the product of :math:`\mu\sigma`. Recall from :ref:`physical properties<physical_properties_index>` however, that :math:`\mu \approx \mu_0` for most materials and that :math:`\sigma` varies over many orders of magnitude. As a result, the diffusive properties of electromagnetic signals are primarily dependent on the conductivity. The diffusive behaviour of EM signals is a very important aspect of time-domain electromagnetic (:ref:`TDEM<airborne_tdem_index>`) methods.


Wave Regime
-----------

In the wave regime, the diffusive term is much smaller than the conservation term, i.e.:

.. math::
    \sigma \frac{\partial \mathbf{e}}{\partial t} \ll \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} \;\;\;\;\; \textrm{and} \;\;\;\;\; \sigma \frac{\partial \mathbf{h}}{\partial t} \ll \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}

In this case, both :math:`\mathbf{e}` and :math:`\mathbf{h}` behave according to the classic **wave equation**, with:

.. math::
    \nabla^2 \mathbf{e} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} = 0

and

.. math::
    \nabla^2 \mathbf{h} - \mu\epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2} = 0

Here, energy is conserved and both :math:`\mathbf{e}` and :math:`\mathbf{h}` propagate as waves. The properties of the waves (wavelength, propagation velocity, etc...) depend on the product of :math:`\mu\epsilon`. Recall from :ref:`physical properties<physical_properties_index>` however, that :math:`\mu \approx \mu_0` for most materials and that :math:`\epsilon` varies over several orders of magnitude. As a result, the wave properties are primarily dependent on the dielectric permittivity. Wave properties are an important aspect of ground-penetrating radar (:ref:`GPR<gpr_index>`) surveys.


