.. _harmonic_planewaves_homogeneous_wavenumber:

Wavenumber
==========

The wavenumber characterizes all properties of electromagnetic waves described by the Helmholtz equation. Recall that the wave number :math:`k` is given by:

.. math:: k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}.

and that it may be decomposed into real and imaginary components such that:

.. math:: k = \alpha - i \beta

According to :cite:`stratton1941,ward1988`, :math:`\alpha` and :math:`\beta` depend on the frequency and the physics properties of the media, where:

.. math:: \alpha = \omega \left ( \frac{\mu \epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right )^{1/2} + 1 \right ] \right )^{1/2} \geq 0

.. math:: \beta = \omega \left ( \frac{\mu\epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right)^{1/2} - 1 \right ] \right ) ^{1/2} \geq 0

Let us now examine a wave travelling in the negative z-direction with the following form:

.. math::
    \mathbf{E} = \mathbf{E}_0^- \, e^{\beta z}e^{i(\alpha z-\omega t)}
    :name: E_downgoing

As we already discussed during our derivation, :math:`\beta` controls the rate of decay with respect to :math:`z`. And :math:`\alpha` controls the oscillatory behaviour.



**Quasi-Static Regime:**

In the quasi-static regime (:math:`\epsilon\omega \ll \sigma`), the wavenumber simplifies to:

.. math::
    k \approx \sqrt{- i \mu \sigma \omega}

where it can be shown that:

.. math::
    \alpha = \beta = \left ( \frac{\omega \mu \sigma}{2} \right ) ^{1/2}

In this case, the waves oscillate and decay as they propagate.

**Wave Regime:**

In the wave regime (:math:`\epsilon\omega \gg \sigma`), the wavenumber simplifies to:

.. math::
    k \approx \alpha = \sqrt{\mu \epsilon \omega^2} = \omega \sqrt{\mu \epsilon}

and

.. math::
    \beta \approx \frac{\sigma}{2} \sqrt{\frac{\mu}{\epsilon}} \sim 0

For a perfect wave equation, :math:`\beta = 0` and the waves do not decay in amplitude as they propagate. In geophysical problems (:ref:`ground-penetrating radar<gpr_index>` for example), signals still experience amplitude loss as they propagate through the Earth.
