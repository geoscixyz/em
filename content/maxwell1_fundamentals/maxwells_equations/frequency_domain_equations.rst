.. _frequency_domain_equations:

Maxwell's equations in frequency
================================

.. raw:: html
    :file: ../../../underconstruction.html



.. topic:: Purpose

    By taking the Fourier transform of Maxwell's wave equation in the time
    domain, we obtain the vector Helmholtz equation for the :math:`\mathbf{e}`
    or :math:`\mathbf{h}` fields. This is the starting equation for many
    problems in electromagnetics.

To get the frequency-domain wave equations, we use the Fourier transform with an :math:`e^{i\omega t}` time dependence. The derivative of :math:`e^{i\omega t}` with respect to time is :math:`i\omega e^{i\omega t}`. Thus, we can easily convert the :ref:`time-domain wave equations <time_domain_equations>` to the frequency-domain by replacing :math:`\partial/\partial t` with :math:`i \omega` and  :math:`\partial^2/\partial t^2` with :math:`-\omega^2`. The frequency-domain equations are then expressed as:

.. math::  \boldsymbol{\nabla}^2 \mathbf{E} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{E}  = 0
        :name: hme8

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{H}  = 0
        :name: hmh8

Equations :eq:`hme8` and :eq:`hmh8` can be written in a simpler form:

.. math:: \boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  = 0

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  = 0

where :math:`k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}` is the wave number. These equations are referred to as the vector Helmholtz equations.

..todo:: alter equations to include source terms.
