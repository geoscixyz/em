.. _frequency_domain_equations:

Maxwell's Equations: Frequency Domain
=====================================

.. purpose::

    Here, :ref:`Faraday's law<faraday>` and the :ref:`Ampere-Maxwell<ampere_maxwell>` equation are used to construct vector Helmholtz equations for both :math:`\mathbf{E}` and :math:`\mathbf{H}`, respectively. This is accomplished by assuming we are in a homogeneous medium. Various components of the resulting differential equations in frequency are discussed. The physical understanding of equations derived here can be extended to more complex applications throughout EM GeoSci.

To obtain the frequency-domain wave equations, we use the Fourier transform with
an :math:`e^{i\omega t}` time dependence. The derivative of :math:`e^{i\omega
t}` with respect to time is :math:`i\omega e^{i\omega t}`. Thus, we can easily
convert the :ref:`time-domain wave equations <time_domain_equations>` to the
frequency-domain by replacing :math:`\partial/\partial t` with :math:`i
\omega` and  :math:`\partial^2/\partial t^2` with :math:`-\omega^2`. The
frequency-domain equations are therefore given by:

.. math::  \boldsymbol{\nabla}^2 \mathbf{E} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{E}  = 0
        :name: hme8

and

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{H}  = 0
        :name: hmh8

Eqs. :eq:`hme8` and :eq:`hmh8` are generally expressed in the following form:

.. math::
	\boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  = 0
	:name: hme9

and 

.. math:: 
	\boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  = 0
	:name: hmh9

where :math:`k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}` is the known as the wave number. 

Helmholtz Equation
------------------

Eqs. :eq:`hme9` and :eq:`hmh9` have identical form and are both characterized by the **vector Helmholtz equation**. In electromagnetics, the vector Helmholtz equation is the frequency-domain equivalent of the :ref:`lossy wave equation<time_domain_equations>`. The properties of :math:`\mathbf{E}` and :math:`\mathbf{H}` depend on the wavenumber :math:`k`. Solutions to the Helmholtz equation are frequently proportional to :math:`e^{\pm i k r}`, where :math:`r` defines some travelled distance for the signal. For these solutions, the real component of :math:`k` defines the amplitude loss as the signal travels. The imaginary component of :math:`k` defines the oscillatory behaviour of the signal. This is discussed in much more detail when talking about :ref:`plane waves in homogeneous media<frequency_domain_plane_wave_sources_analytic_solution>`.

Quasi-Static Regime
-------------------

In the quasi-static regime, the conductivity dominates the properties of the EM signal, i.e.:

.. math::
	\sigma \gg \omega \epsilon

and the wavenumber is approximately equal to:

.. math::
	k \approx \sqrt{-i\omega\mu\sigma}

The wavenumber still has real and imaginary components. As a result, the EM signal experiences both attenuation and oscillation. The wavenumber is controlled by the product of :math:`\mu\sigma`. Recall from :ref:`physical properties<physical_properties_index>` however, that :math:`\mu \approx \mu_0` for most materials and that :math:`\sigma` varies over many orders of magnitude. As a result, the properties of :math:`\mathbf{E}` and :math:`\mathbf{H}` are primarily controlled by the conductivity. The relationship between :math:`\sigma` and EM signals is very important to frequency-domain electromagnetic (:ref:`TDEM<airborne_fdem_index>`) methods.


Wave Regime
-----------

In the wave regime, the dielectric permittivity dominates the properties of the EM signal, i.e.:

.. math::
	\sigma \ll \omega \epsilon

and the wavenumber is approximately equal to:

.. math::
	k \approx \sqrt{\omega^2 \mu\epsilon}

In this case, the wavenumber only contains real components and therefore the amplitude of :math:`e^{\pm i k r}` is constant. This would make sense given that energy is conserved in a lossless wave equation. The wavenumber is controlled by the product of :math:`\mu\epsilon`. Recall from :ref:`physical properties<physical_properties_index>` however, that :math:`\mu \approx \mu_0` for most materials and that :math:`\epsilon` varies over several orders of magnitude. As a result, the properties of :math:`\mathbf{E}` and :math:`\mathbf{H}` are primarily controlled by the dielectric permittivity. The relationship between :math:`\epsilon` and EM signals is very important to frequency-domain ground-penetrating radar.



