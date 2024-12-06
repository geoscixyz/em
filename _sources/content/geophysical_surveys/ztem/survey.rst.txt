.. _ztem_survey:

Survey
======

.. raw:: html
    :file: ../../../underconstruction.html

.. figure:: images/ztem_survey.png
        :name: img_ztem_survey
        :align: right
        :figwidth: 50%

        A ZTEM survey uses a helicopter or fixed-wing aircraft to measure the vertical magnetic field component while the horizontal magnetic field components are measured at a reference station on the surface.
 
The z-axis tipper electromagnetic (ZTEM) method, shown in Figure :numref:`img_ztem_survey`, is an airborne system, using either a helicopter or fixed-wing aircraft. Like MT, it does not require a transmitter. Instead, the inducing fields are natrally occuring electromagnetic fields. Solar winds and interaction with Earth's magnetosphere generate EM fields at low frequencies while fields for higher frequencies are generated from thunderstorm activity. These are the same inducing fields that are used for the :ref:`magnetotelluric method <mt_physics>`.

ZTEM  is also similar to the MT method for the receivers. While in MT, both the electric and magnetic fields are measured on the earth's surface, the ZTEM method measures the vertical component of the magnetic field from a helicopter or fixed-wing aircraft, which tows the receiver. The receiver is a loop similar to the receivers for :ref:`FDEM airborne surveys <airborne_fdem_survey>`. For Geotech's helicopter-borne system, the receiver is towed 90 m below the helicopter and the loop is 7.4 m in diameter.

The receiver measures the vertical magnetic field at a set of distinct frequencies. In the case of Geotech's helicopter-borne ZTEM system, those frequencies are 30, 45, 90, 180, 360, and 720 Hz. Their fixed-wing system collects the same frequencies except the lowest and highest values. The lowest frequency collected usually depend on the speed of the aircraft and the highest frequency on the data sampling rate, signal strenght, and noise :cite:`holtham2010`. The data are generally decomposed into real (in-phase) and imaginary (out-of-phase or quadrature)  components.

Finally, a reference (or base) station is used to measure the horizontal components of the magnetic field. These are assumed not to change much over the survey region and are thus only measured in a single location during acquisition of the airborne data. The base station should be located in a region where the subsurface is relatively homogeneous or uniformly layered.
