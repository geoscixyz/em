.. _ip_physics:

Physics
=======

.. purpose::

    Demonstrate the fundamental physical principles governing the IP experiment

.. figure:: images/resistivity.png
    :align: right
    :figwidth: 40%
    :name: resistivity

    Complex conductivity in frequency domain. Pelton's Cole-Cole model :cite:`pelton1978` model is used (:math:`\eta` = 0.4, :math:`\tau` = 0.01 s, :math:`c` = 0.4).

In the :ref:`DC experiment <dcr_index>` we assumed non-dispersive electrical resistivity, i.e. not frequency-depndent. However, in reality resistivity of the earth material is dispersive, and effectively generate polarization charge buildup when electric field is applied to a chargeable medium. For instance, :numref:`resistivity` shows complex-valued resistivity in frequency domain. They have real and imaginary parts, and vary in frequency.

To understand the impact of complex resisitivty, we only consider the end member of the resistivity at zero and infinte frequency: :math:`\rho_0` and :math:`\rho_{\infty}`,  respectively. Chargeability, :math:`\eta` can be defined as

.. math::
    \eta = \frac{\rho_0-\rho_{\infty}}{\rho_0}

Now considering a homoegenous earth with Ohm's law (:math:`V=IR`), we redefine

.. math::
    \eta = \frac{V_0-V_{\infty}}{V_0}
    :label: charg_V

where :math:`V_0` and :math:`V_{\infty}` are voltages at zero and infinte frequency, respectively.

.. figure:: images/Overvoltage_single.png
    :align: right
    :figwidth: 40%
    :name: Overvoltage_single

    Overvoltage curve in time domain.

In time domain, measured voltage will look like :numref:`Overvoltage_single` with a half-duty cylcle current. For inhomogeneous earth medium Eq. :eq:`charg_V` should be modifed as

.. math::
    \eta_a = \frac{V_0-V_{\infty}}{V_0}
    :label: charg_app

where :math:`\eta_a` is an apparent chargeability. Therefore, in general induced polarization (IP) effects can be considered as a perturbation of voltage due to a small resistivity change. :math:`V_0` is a voltage when polarization charge buildup is at maxium, and hence a voltage due to IP effects can be defined as

.. math::
    V_{IP} = V_0-V_{\infty}

Similarly, aribitrary IP current density and electric field can be defined as

.. math::
    \mathbf{J}_{IP} = \mathbf{J}_0-\mathbf{J}_{\infty}

.. math::
    \mathbf{E}_{IP} = \mathbf{E}_0-\mathbf{E}_{\infty}

And corresponding polarization charge density can be defined as

.. math::
    q_{IP} = \nabla \cdot \mathbf{E}_{IP}


.. figure:: images/DCIP.png
    :align: right
    :figwidth: 50%
    :name: DCIP_concept

    DC and IP charge buildup concept.

Considering a time domain measurement, in the on-time when currents are injected, DC currents will dominate IP currents as shown in :numref:`DCIP_concept` hence currents are channeled into good conductors and flow around resistors; sign of charges built around the conductor and the resistor are opposite. In the off-time, DC currents are disappeared only IP currents flows, and importantly direction of IP currents are opposite to DC currents inside of both chargeable spheres resulting in same sign of charges built around both chargeable spheres. Therefore, chargeable bodies act as like a resistor.


.. _two_sphere_setup_ip:

Two-sphere problem
******************

We illustrate the DC-IP experiment with a synthetic pole-dipole survey as
illustrated in :numref:`TwoSphereIP`. This simple resistivity model is made up of two spheres in a uniform half-space Earth, and both spheres are chargeable (:math:`\eta` = 100 mV/V). Currents are injected into the ground from the source, and potentials are measured at different locations. Similarly, we only consider both end members of voltage at zero and infinite frequency: :math:`V_0` and :math:`V_{\infty}`, and by subtracting :math:`V_{\infty}` from :math:`V_{0}` we evaluate IP voltage, :math:`V_{IP}`. The source location is marked by a triangle.

Here to understand how currents flow and charges are built up in both DC and IP cases, we present both currents and charges at a vertical section crossing the center of the two spheres for each case.

.. figure:: images/TwoSphereIP.png
    :align: center
    :figwidth: 100%
    :name: TwoSphereIP

    Pole-dipole DC-IP experiment over a synthetic model. Right panel shows conductivity model made up of a conductive (:math:`10^{-1}` S/m) and a resistive (:math:`10^{-3}` S/m) sphere embedded  in a uniform half-space (:math:`10^{-2}` S/m). Left panel shows

DC currents and charges
^^^^^^^^^^^^^^^^^^^^^^^

As mentioned earlier, DC datum can be measured at a late on-time when DC charges dominate IP charges thus, current pathes are mostly distorted due to the conductor and resistor reflected in :math:`\rho_0`.

.. note::

    `[Press play]` Note the behaviour of the current lines as the point source passes over the
    conductor. The current density increases inside the sphere but
    decreases around it; this is often referred to as :ref:`current channeling<dc_e_field>`.
    Conversely, current lines get deflected around the resistor.

    `[Pause]` Charges accumulate at the interface between
    conductivity contrasts. Note the difference in charge polarity as the current flows
    into the conductive and resistive spheres. The polarities
    agree with those predicted by :ref:`theory<bound_charge_Q>`.
    Also note how the spatial distribution of charges on the spheres changes
    as the current source is moved.

.. raw:: html
    <hr width=20 >
    :file: images/TwoSphereDC_Current_Anim.html

|

IP currents and charges
^^^^^^^^^^^^^^^^^^^^^^^

IP datum can be measured at an off-time when DC currents are gone. At this time only polarization charges exists resulting in IP currents and measured IP voltages.

.. note::

    `[Press play]`  The conductive and chargeable sphere (left) acts like dipolar currents with the opposite direction to the DC currents. The current density decreases as the distance from the sphere increases. Similar pattern of IP currents can be observed for the resistive and chargeable sphere (right), but with smaller amplitude than the other one.

    `[Pause]` Charges accumulate at the interface between
    chargeability contrasts. Note the same charge polarity as the current flows into the conductive and resistive spheres (both chargable). Considering the polarity a chargeable body acts like a resistor.

.. raw:: html
    <hr width=20 >
    :file: images/TwoSphereIP_Current_Anim.html
