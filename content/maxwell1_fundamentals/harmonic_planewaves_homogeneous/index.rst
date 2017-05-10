.. _harmonic_planewaves_homogeneous_index:

Harmonic Plane Waves in Homogeneous Media
=========================================

.. purpose::

    We have already shown that in a homogeneous media, harmonic electromagnetic signals behave according to the :ref:`Helmholtz<frequency_domain_equations>` equation. Here, we discuss the properties of harmonic plane wave solutions in the frequency domain. Educational content is augmented by using the :ref:`interactive apps<apps_index>` provided to answer a set of fundamental questions. We also discuss the relationships between the electric and magnetic fields carried by plane waves. The content here parallels materials provided in many EM resources (see :cite:`ward1988,griffiths1999,stratton1941`).

Introduction
------------

We have previously shown that in homogeneous media, the propagation of electromagnetic signals in the frequency domain is governed by the :ref:`Helmholtz equation<frequency_domain_equations>`. One solution for this equation is a plane wave, where electric and magnetic fields lie in a 2D plane and the wave propagates in a direction perpendicular to that plane. Physically, the planewave solution offer a good approximation to what is happening far away from an electromagnetic source. As a result, planewaves form a primary basis for understanding and working with many electromagnetic phenomena. 

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 40%
   :name: planewavedown_index_freq_1

   Geometry of an EM plane wave propagating downwards.

Here, we explore the propagation of plane waves in the frequency domain (for harmonic signals). :ref:`Apps<harmonic_planewaves_homogeneous_index_app>` are provided that allow you to explore the concepts of wavelength, attenuation and other aspects of the propagating EM fields. :ref:`Questions<harmonic_planewaves_homogeneous_questions>` are provided to promote interactive learning. The resource is augmented with derivations and equations that quantify the information learned through using the apps. 

    - The supporting derivation for the planewave solution is found :ref:`here<harmonic_planewaves_homogeneous_derivation>`.
    - Questions which can be solved using the app are found :ref:`here<harmonic_planewaves_homogeneous_questions>`.

The content provided here parallels materials from many EM resources (see [WH88][Gri99][Str41]).

Plane Wave Properties
---------------------

There are numerous properties which can be used to understand the propagation of planewaves in the frequency domain. Understanding these properties is very important, as they can be used to describe the behaviours of EM waves in more general cases. Here, we will discuss the following properties:

    - :ref:`Wavenumber<harmonic_planewaves_homogeneous_wavenumber>`: A fundamental constant which characterizes plane waves at a particular frequency.
    - :ref:`Attenuation<harmonic_planewaves_homogeneous_attenuation>`: The amplitude loss of a plane wave as it propagates.
    - :ref:`Skin Depth<harmonic_planewaves_homogeneous_skindepth>`: The distance an EM wave travels before it experiences an amplitude loss of :math:`1/e`.
    - :ref:`Phase Velocity<harmonic_planewaves_homogeneous_phasevelocity>`: The velocity at which plane waves at a certain frequency travel.
    - :ref:`Wavelength<harmonic_planewaves_homogeneous_wavelength>`: The wavelength of a plane wave.
    - :ref:`Impedance<harmonic_planewaves_homogeneous_impedance>`: A medium property which characterizes the relationship between perpendicular components of the electric and magnetic fields supported by EM waves.
    - :ref:`Apparent Resistivity<harmonic_planewaves_homogeneous_apparentresistivity>`: An approximation of a medium's electrical resistivity based on the relationship between the electric and magnetic fields.

.. _harmonic_planewaves_homogeneous_index_app:

FDEM Planewave App
------------------

.. geosciapp::
    While navigating through the subsequent materials on planewaves in homogeneous media, it is suggested that you go to the :ref:`apps page<apps_index>` and open the Jupyter notebook for the **FDEM_Planewave_Wholespace** app.

A fundamental understanding of planewave propagation in the frequency domain can be obtained by using the **"FDEM_Planewave_Wholespace"** App; which plots the associated EM fields and demonstrates how the planewave properties depend on frequency and the properties of the medium. Here, we provide a cursory description of planewaves in the frequency domain by considering a downward propagating planewave. A separate page is devoted to deriving the planewave solution and defining frequency-dependent planewave properties in detail (link).

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_freq_index

   Geometry of an EM plane wave propagating downwards.

In the frequency domain, the EM fields supported by planewaves in a homogeneous medium are characterized by the vector Helmholtz equation:

.. math::
    \boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  &= 0\\
    \boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  &= 0
    :name: Helmholtz_full_analytic

where the properties of the EM waves are defined by a complex wavenumber:

.. math::
    k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}
    :name: Helmholtz_complex_wavenumber

The App considers a downward propagating planewave which results from an infinite current sheet on the xy-plane at :math:`z` = 0 m. The current sheet is polarized with a current :math:`I(\omega ) = I_x \textrm{cos}(\omega t)` such that it only generates electric field components along the x-direction. By Faraday's law, the corresponding magnetic field only has components along the y-direction. The analytic solution for the electric field in this case is given by:

.. math::
    \mathbf{E}(\omega) = E_{x,0}^- \, e^{ikz} \mathbf{u_x}
    :name:

where :math:`E_{x,0}^-` is the scalar amplitude and :math:`\mathbf{u_x}` is the unit vector in the x-direction. Where :math:`\mathbf{u_y}` is the unit vector in the y-direction, the analytic solution for the corresponding magnetic field is given by:

.. math::
    \mathbf{H}(\omega) = - \frac{k}{\omega \mu} E_{x,0}^- \, e^{ikz} \mathbf{u_y}

Contents
--------

.. toctree::
    :maxdepth: 1

    derivation
    wavenumber
    attenuation
    skindepth
    phasevelocity
    wavelength
    impedance
    apparentresistivity
    questions
