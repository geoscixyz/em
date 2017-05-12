.. _harmonic_planewaves_homogeneous_index:

Harmonic Planewaves in Homogeneous Media
========================================

.. purpose::

    We have already shown that in a homogeneous media, electromagnetic signals in the frequency domain behave according to the :ref:`Helmholtz<frequency_domain_equations>` equation. Here, we discuss the properties of harmonic planewave solutions in the frequency domain. Educational content is augmented by using the :ref:`interactive apps<apps_index>` provided to answer a set of fundamental questions. We also discuss the relationships between the electric and magnetic fields carried by planewaves. The content here parallels materials provided in many EM resources (see :cite:`ward1988,griffiths1999,stratton1941`).

Introduction
------------

We have previously shown that in homogeneous media, the propagation of electromagnetic signals in the frequency domain is governed by the :ref:`Helmholtz equation<frequency_domain_equations>`. One solution to this equation is a planewave, where electric and magnetic fields lie in a 2D plane and the wave propagates in a direction perpendicular to that plane. Physically, the planewave solutions offer good approximations to what is happening far away from electromagnetic sources. As a result, planewaves form a primary basis for understanding the fundamental behaviours of many electromagnetic phenomena. 

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_index_freq_1

   Geometry of an EM planewave propagating downwards.

Here, we explore the propagation of planewaves in the frequency domain (for harmonic signals). The content provided here parallels materials from many EM resources (see [WH88][Gri99][Str41]). :ref:`Apps<harmonic_planewaves_homogeneous_index_app>` are provided that allow you to explore the concepts of wavelength, attenuation and other aspects of the propagating EM fields. To compliment the app, :ref:`questions<harmonic_planewaves_homogeneous_questions>` are provided to promote interactive learning. The resource is augmented with derivations and equations that quantify the information learned through using the apps. 

**Quick Links:**

    - :ref:`Deriving the planewave solution<harmonic_planewaves_homogeneous_derivation>`
    - :ref:`Supporting math for the app<harmonic_planewaves_homogeneous_derivation_app>`
    - :ref:`Question to be answered using the app<harmonic_planewaves_homogeneous_questions>`

Planewave Properties
--------------------

There are numerous properties which can be used to understand the propagation of planewaves in the frequency domain. Understanding these properties is very important, as they can be used to describe the behaviours of EM waves in more general cases. Here, we will discuss the following properties:

    - :ref:`Wavenumber<harmonic_planewaves_homogeneous_wavenumber>`: A fundamental constant which characterizes planewaves at a particular frequency.
    - :ref:`Attenuation<harmonic_planewaves_homogeneous_skindepth>`: The amplitude loss of a planewave as it propagates.
    - :ref:`Skin Depth<harmonic_planewaves_homogeneous_skindepth>`: The distance an EM wave travels before it experiences an amplitude loss of :math:`1/e`.
    - :ref:`Wavelength<harmonic_planewaves_homogeneous_wavelength>`: The wavelength of a planewave.
    - :ref:`Phase Velocity<harmonic_planewaves_homogeneous_phasevelocity>`: The velocity at which planewaves at a certain frequency travel.
    - :ref:`Impedance<harmonic_planewaves_homogeneous_impedance>`: A medium property which characterizes the relationship between perpendicular components of the electric and magnetic fields supported by EM waves.
    - :ref:`Apparent Resistivity<harmonic_planewaves_homogeneous_apparentresistivity>`: An approximation of a medium's electrical resistivity based on the relationship between the electric and magnetic fields.

.. _harmonic_planewaves_homogeneous_index_app:

FDEM Planewave App
------------------

.. geosciapp::
    While navigating through the subsequent materials on planewaves in homogeneous media, it is suggested that you go to the :ref:`apps page<apps_index>` and open the Jupyter notebook for the **FDEM_Planewave_Wholespace** app.

.. A fundamental understanding of planewave propagation in the frequency domain can be obtained by using the **"FDEM_Planewave_Wholespace"** App; which plots the associated EM fields and demonstrates how the planewave properties depend on frequency and the properties of the medium. Here, we provide a cursory description of planewaves in the frequency domain by considering a downward propagating planewave. A separate page is devoted to deriving the planewave solution and defining frequency-dependent planewave properties in detail (link).



Contents
--------

.. toctree::
    :maxdepth: 1

    derivation
    wavenumber
    skindepth
    wavelength
    phasevelocity
    impedancephase
    apparentresistivity
    questions
