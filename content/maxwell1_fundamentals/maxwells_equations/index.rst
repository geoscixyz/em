.. _maxwells_equations_index:

Maxwell's Equations
===================

.. topic:: Purpose

    In this section, we combine the first-order partial :ref:`differential
    equations <differential_equations_time>` into second-order equations for
    :math:`\mathbf{e}` or :math:`\mathbf{h}`. In the time domain the equations have both a
    wave propagation and a diffusion term and shows that the wave is
    attenuated as it travels. In the frequency domain, the :math:`\mathbf{e}` or
    :math:`\mathbf{h}` field satisfies a vector Helmholtz equation and the balance
    between propagation and diffusion is controlled by a complex wavenumber.
    For homogeneous media, the EM fields can propagate as plane waves.  When
    electrical conductivity :math:`\sigma` is zero, the electromagnetic waves
    propagate without attenuation. When :math:`\sigma` is large, as it is with most
    earth rocks, the EM waves are diffusive and attenuate rapidly within one
    or two wavelengths. We describe this plane wave solution and provide some
    notebooks that allow the user  to investigate how the wavenumber, skin
    depth, phase velocity and wavelength vary with frequency and with the
    physical properties of the media. In many problems, the wave propagation
    portion of the equation (or effectively, the displacement current), can be
    neglected and quasi-static Maxwell's equations can be solved.

**Contents**

.. toctree::
    :maxdepth: 2

    time_domain_equations
    frequency_domain_equations
    maxwells_equations_in_homogeneous_media/index
    details
