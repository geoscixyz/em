.. _wave_equation_in_free_space:

Wave propagation in homogeneous media
=====================================

.. todo:: under construction!

In this section, we combine the first-order partial :ref:`differential equations <differential_equations_time>` into second-order equations for :math:`\mathbf{e}` or :math:`\mathbf{h}` and show how EM fields propagate in homogenous media. The plane wave solutions have propogation and attenuating components and the relative balance of these is determined by the complex wave number. When electrical conductivity :math:`\sigma` is zero, the electromagnetic waves propagate without attenuation. When :math:`\sigma` is large, as it is with most earth rocks, the EM waves are diffusive and attenuate rapidly within one or two wavelengths. In many problems, the wave propagation portion of the equation (or effectively, the displacement current), can be neglected and quasi-static Maxwell's equations can be solved. The following content parallels that offered in many EM resources :cite:`ward1988,griffiths1999,stratton1941`. We first generate the second-order differential equations in the time-domain and then use Fourier transforms to get the frequency-domain counterparts. The plane wave solution is described and notebooks allow the user to investigate concepts of wavenumber and skin depths.

The following pages present the important components and discuss the physical phenomena. Mathematical details are largely skipped but are provided in the :ref:`Details <wave_propagation_details>`.

**Contents**

.. toctree::
    :maxdepth: 2

    damped_wave_equation
    em_waves_free_space
    plane_wave_solution
    effect_conductivity_homogeneous_media
    details
