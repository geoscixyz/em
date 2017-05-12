.. _harmonic_planewaves_homogeneous_wavenumber:

Wavenumber
==========

For electromagnetic waves characterized by the Helmholtz equation, all of the corresponding wave properties can be derived from the wavenumber :math:`k`. The wavenumber at a particular frequency depends on the physical properties of the propagation medium and is given by:

.. math:: k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}

The wavenumber has both real and imaginary components and may be decomposed as follows:

.. math:: k = \alpha - i \beta

such that the :ref:`general solution<harmonic_planewaves_homogeneous_derivation>` for EM planewaves propagating in the vertical direction becomes:

.. math::
	\mathbf{E} = \mathbf{E}_0^- \, e^{\beta z}e^{i(\alpha z-\omega t)} + \mathbf{E}_0^+ \, e^{-\beta z}e^{-i(\alpha z+\omega t)}

According to :cite:`stratton1941,ward1988`, :math:`\alpha` and :math:`\beta` are given by:

.. math:: \alpha = \omega \left ( \frac{\mu \epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right )^{1/2} + 1 \right ] \right )^{1/2} \geq 0

.. math:: \beta = \omega \left ( \frac{\mu\epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right)^{1/2} - 1 \right ] \right ) ^{1/2} \geq 0

When deriving a :ref:`general solution<harmonic_planewaves_homogeneous_derivation>`, we stated that :math:`\alpha` (the real component of the wavenumber) determines the :ref:`wavelength<harmonic_planewaves_homogeneous_wavelength>` and :ref:`velocity<harmonic_planewaves_homogeneous_phasevelocity>` of the planewave. Whereas :math:`\beta` (the imaginary component of the wavenumber) determines the :ref:`attenuation<harmonic_planewaves_homogeneous_skindepth>`. The details of this can be learned visually through app as well as through the following material on planewave properties.

Approximations
--------------

Quasi-Static Approximation
^^^^^^^^^^^^^^^^^^^^^^^^^^

In the quasi-static regime (:math:`\epsilon\omega \ll \sigma`), the wavenumber simplifies to:

.. math::
    k \approx \sqrt{- i \mu \sigma \omega}

where it can be shown that:

.. math::
    \alpha = \beta = \left ( \frac{\omega \mu \sigma}{2} \right ) ^{1/2}

In this case, EM waves oscillate and decay as they propagate.

Wave Regime Approximation
^^^^^^^^^^^^^^^^^^^^^^^^^

In the wave regime (:math:`\epsilon\omega \gg \sigma`), the wavenumber simplifies to:

.. math::
    k \approx \alpha = \sqrt{\mu \epsilon \omega^2} = \omega \sqrt{\mu \epsilon}

and

.. math::
    \beta \approx \frac{\sigma}{2} \sqrt{\frac{\mu}{\epsilon}} \sim 0

For a perfect wave equation, :math:`\beta = 0` and the waves do not decay in amplitude as they propagate. In geophysical problems (:ref:`ground-penetrating radar<gpr_index>` for example), signals still experience amplitude loss as they propagate through the Earth.
