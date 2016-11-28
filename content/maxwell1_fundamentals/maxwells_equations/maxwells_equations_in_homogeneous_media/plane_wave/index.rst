.. _maxwells_equations_in_homogeneous_media_plane_wave_index:

Maxwell's Equations for Plane Wave Sources
==========================================

.. purpose::

    Plane wave solutions to Helmholtz’s equations exist when the medium is homogeneous. By exploring the plane wave solution in both frequency and time domain, we understand how the plane EM wave propagates. Our content parallels that offered in many EM resources :cite:`ward1988,griffiths1999,stratton1941`


Setup
-----

Consider a situation where infinite current sheet at :math:`z` =0 m, and plane EM wave propagating downward (negative :math:`z` direction) due to this. We focus on a specific situation where only :math:`E_x` and :math:`H_y` are existing. For the frequency domain case, the sheet current can be considered alternating in time (e.g. :math:`I_x=I_0cos(\omega t)`). Lightening can be considered for the domain, and impulse current will be the closest option for its mathematical representation ( :math:`I_x = I_0\delta (t)` ), where :math:`\delta (t)` is a Dirac-Delta function.

.. figure:: images/planewavedown.png
   :align: center
   :scale: 60%
   :name: planewavedown

   Setup diagram of plane EM wave propagation heading downward (negaitve :math:`z`).

EM fields propagation will be dependent upon:

- Physical properties: :math:`\sigma`, :math:`\epsilon`, and :math:`\mu`

- Time (:math:`t`) or Frequency (:math:`f`)

- Spatial location (:math:`z`)

Therefore, arbitrary plane EM fields in frequency domain can be

.. math::
    \mathbf{F}(\sigma, \epsilon, \mu; z; \omega),

where :math:`\omega=2\pi f`, and corresponding time domain EM fields can be written as

.. math::
    \mathbf{f}(\sigma, \epsilon, \mu; z; t).


Solving plane wave equations
----------------------------

Analytic solution exists for this simple setup, and we first obtain solution in frequency domain, then tranform that to time domain using inverse Fourier or Laplace tranform.

:ref:`Maxwell's equations in the frequency domain <frequency_domain_equations>`, without source terms, are:

.. math::
    \boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  = 0
    :label: fd_helmholtz_e

.. math::
    \boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  = 0
    :label: fd_helmholtz_h

where :math:`k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}` is the complex wave number. To solve above equations, a boundary condition is required. We consdier two options: a) :math:`\mathbf{E}(z=0) = \mathbf{E}_0` and b) :math:`\mathbf{H}(z=0) = \mathbf{H}_0`.
Consider Eq. :eq:`fd_helmholtz_e` with a), solution of the electric field will be

.. math::
    \mathbf{E} = \mathbf{E}_0 e^{ikz}

Then corresponding manetic field can be derived with Faraday's Law:

.. math::
    \mathbf{H} = - i \omega \mu \nabla \times (\mathbf{E}_0 e^{ikz}).

Our strategy to obtain time domain solution is transforming above to time domain: :math:`\mathbf{e}(t) = \mathcal{F}^{-1}[\mathbf{E}(\omega)]`
Equivalent setup for the time domain PDE will be:

.. math::

    \boldsymbol{\nabla}^2 \mathbf{e} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t}    = 0,

with an initial condition:

.. math::
    \mathbf{e}(t=0)=\delta(t)\mathbf{E}_0, \ \text{when} \ z=0,

    \mathbf{e}(t=0)=0, \ \text{when} \ z\neq 0.

If boundary condition of b) is used in frequency domain for solving Eq. :eq:`fd_helmholtz_h`, then solution of the magnetic field will be:

.. math::
    \mathbf{H} = \mathbf{H}_0 e^{ikz}.

And equivalent setup for the time domain PDE is

.. math::

    \boldsymbol{\nabla}^2 \mathbf{h} - \mu\epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{h}}{\partial t}    = 0,

with an initial condition:

.. math::
    \mathbf{h}(t=0)=\delta(t)\mathbf{H}_0, \ \text{when} \ z=0,

    \mathbf{h}(t=0)=0, \ \text{when} \ z\neq 0.

Physical meaning of this case could be a lightening, which would be an impulse current resulting in impulse magnetic field at a specific point from Ampere's law. The other case where impulse electric field exists can correspond to a long-lasting lightening then abruptly shut-off (like step function), which can be inferred from Faraday's law.

.. note::

    Time derivative of step function :math:`u(t)` is :math:`\delta(t)`.

On our following derivation we focus on solving Maxwell's equation for the electric field with b) in both frequency and time domain.


In following sections, we derive analytic expressions for the plane EM fields in both frequency and time domain, understand important physical behavior of them (Analytic Solution section), discuss relationship between EM fields (Fields section).
Further, using plane wave apps, we simulate plane EM fields, and visualize them (Simulation section).

**Contents**

.. toctree::
    :maxdepth: 2

    frequency/index
    time/index

.. Since only :math:`E_x` and :math:`H_y` exists, we have :math:`\mathbf{E} = E_x \mathbf{u}_x` and :math:`\mathbf{H} = H_y \mathbf{u}_y`.
