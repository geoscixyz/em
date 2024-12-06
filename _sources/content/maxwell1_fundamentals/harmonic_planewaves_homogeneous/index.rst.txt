.. _harmonic_planewaves_homogeneous_index:

Harmonic Planewaves in Homogeneous Media
========================================

.. purpose::

    We have already shown that in a homogeneous media, electromagnetic signals in the frequency domain behave according to the :ref:`Helmholtz<frequency_domain_equations>` equation. Here, we discuss the properties of harmonic planewave solutions in the frequency domain. Educational content is augmented by using the :ref:`interactive apps<apps_index>` provided to answer a set of fundamental questions. We also discuss the relationships between the electric and magnetic fields carried by planewaves. The content here parallels materials provided in many EM resources (see :cite:`ward1988,griffiths1999,stratton1941`).

**Introduction**

We have previously shown that in homogeneous media, the propagation of electromagnetic signals in the frequency domain is governed by the :ref:`Helmholtz equation<frequency_domain_equations>`. One solution to this equation is a planewave, where electric and magnetic fields lie in a 2D plane and the wave propagates in a direction perpendicular to that plane. Physically, the planewave solutions offer good approximations to what is happening far away from electromagnetic sources. As a result, planewaves form a primary basis for understanding the fundamental behaviours of many electromagnetic phenomena.

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_index_freq_1

   Geometry of an EM planewave propagating downwards.

Here, we explore the propagation of planewaves in the frequency domain (for harmonic signals). The content provided here parallels materials from many EM resources (see [WH88][Gri99][Str41]). `An app <https://mybinder.org/v2/gh/geoscixyz/em-apps/main?filepath=index.ipynb>`__ is provided that allow you to explore the concepts of wavelength, attenuation and other aspects of the propagating EM fields. To compliment the app, :ref:`questions<harmonic_planewaves_homogeneous_questions>` are provided to promote interactive learning. The resource is augmented with derivations and equations that quantify the information learned through using the apps.

**Quick Links**

    - :ref:`Deriving the planewave solution<harmonic_planewaves_homogeneous_derivation>`
    - `Link to the FDEM Planewave Wholespace App <https://mybinder.org/v2/gh/geoscixyz/em-apps/main?filepath=index.ipynb>`__
    - :ref:`Supporting math for the app<harmonic_planewaves_homogeneous_derivation_app>`
    - :ref:`Question to be answered using the app<harmonic_planewaves_homogeneous_questions>`

**Planewave Topics**

There are numerous properties which can be used to understand the propagation of planewaves in the frequency domain. Understanding these properties is very important, as they can be used to describe the behaviours of EM waves in more general cases. Here, we will discuss the following properties:

    - :ref:`Wavenumber<harmonic_planewaves_homogeneous_wavenumber>`: A fundamental constant which characterizes planewaves at a particular frequency.
    - :ref:`Attenuation<harmonic_planewaves_homogeneous_skindepth>`: The amplitude loss of a planewave as it propagates.
    - :ref:`Skin Depth<harmonic_planewaves_homogeneous_skindepth>`: The distance an EM wave travels before it experiences an amplitude loss of :math:`1/e`.
    - :ref:`Wavelength<harmonic_planewaves_homogeneous_wavelength>`: The wavelength of a planewave.
    - :ref:`Phase Velocity<harmonic_planewaves_homogeneous_phasevelocity>`: The velocity at which planewaves at a certain frequency travel.
    - :ref:`Impedance<harmonic_planewaves_homogeneous_impedancephase>`: A medium property which characterizes the relationship between perpendicular components of the electric and magnetic fields supported by EM waves.
    - :ref:`Apparent Resistivity<harmonic_planewaves_homogeneous_apparentresistivity>`: An approximation of a medium's electrical resistivity based on the relationship between the electric and magnetic fields.

.. _harmonic_planewaves_homogeneous_index_app:

.. geosciapp::
    While navigating through the subsequent materials on planewaves in homogeneous media, it is suggested that you open the `FDEM Planewave Wholespace App <https://mybinder.org/v2/gh/geoscixyz/em-apps/main?labpath=notebooks%2Fem%2FFDEM_Planewave_Wholespace.ipynb>`__ from the notebooks page. Don't forget to sign in.

A fundamental understanding of planewave propagation in the frequency domain can be obtained by using the `FDEM Planewave Wholespace App <https://mybinder.org/v2/gh/geoscixyz/em-apps/main?labpath=notebooks%2Fem%2FFDEM_Planewave_Wholespace.ipynb>`__ (:numref:`FDEM_planewaves_wholespace_app`); which allows the user to simulate the electric and magnetic fields supported by a downward propagating planewave. The app allows the user to explore the effects of different parameters (e.g. conductivity, observer location, frequency) and answer a set of fundamental questions. For example, assume you are sending a harmonic EM planewave signal into the Earth and that the ground has a conductivity of 0.1 S/m.

    - For a harmonic signal at a particular frequency (100 Hz for example), how deep does the signal penetrate the Earth before it loses 90% of its amplitude?
    - By choosing a different frequency for the signal, can I change how deep the signal penetrates the Earth?

A host of additional questions which can be answered using the app are found :ref:`here<harmonic_planewaves_homogeneous_questions>`.

.. figure:: images/simulation_Ex.png
   :align: center
   :figwidth: 80%
   :name: FDEM_planewaves_wholespace_app

   Screen shot of the FDEM planewaves wholespace app.

**Contents**

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
