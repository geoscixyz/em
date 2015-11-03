.. _faraday:

Faraday's Law
=============

Faraday's law is named after English scientist Michael Faraday (1791-1867), and describes the manner in which time-varying magnetic fields induce rotational electric fields. 

Integral Form in the Time-Domain
--------------------------------

Faraday's law in integral form can be expressed using the following equation:

.. include:: ../../equation_bank/faradays_law_int_time.rst

where :math:`{\bf e}` is the electric field defined around a closed path :math:`C`, :math:`{\bf b}` is the magnetic flux density defined over a closed surface :math:`A` contoured by :math:`C`, :math:`\hat n` is an outward normal unit vector perpendicular to :math:`da` , and :math:`d{\bf l}` is a vector element of length along contour :math:`C`.
Eq. :eq:`faradays_law_int_time` states that the time-dependent rate of change in magnetic flux, through a surface bounded by a closed path, is negatively proportional to the line integral of the electric field it induces over that path.

Differential Form in the Time-Domain
------------------------------------

By applying Stokes's theorem to left-hand side of Eq. :eq:`faradays_law_int_time`, we can obtain the differential form of Faraday's law:

.. include:: ../../equation_bank/faradays_law_diff_time.rst

.. Therefore, the time dependent change in magnetic flux density at any location is negatively proportional to the curl of the electric field.
.. For magnetic fields which change rapidly with respect to time, we expect to observe a larger electric field.
.. TODO: Put some links: rotational field 

Eq. :eq:`faradays_law_diff_time` states that time varying magnetic fields will induce rotational electric fields.
Furthermore, the curl of the induced electric fields opposes time-dependent changes in the inducing magnetic field.


Faraday's Law in the Frequency-Domain
-------------------------------------

Frequency-domain representation of Faraday's law can be obtained by applying a Fourier transform to Eqs. :eq:`faradays_law_int_time` and :eq:`faradays_law_diff_time`.
The integral form of Faraday's law in the frequency domain is:

.. include:: ../../equation_bank/faradays_law_int_freq.rst

Similarly using Stokes' theorem, the differential form of Faraday's law is:

.. include:: ../../equation_bank/faradays_law_diff_freq.rst

where :math:`\omega` is the angular frequency, :math:`{\bf E}` is the frequency-dependent electric field and :math:`{\bf B}` is the frequency-dependent magnetic flux density.
From a theoretical perspective, it is common practice to consider :math:`{\bf E}` and :math:`{\bf B}` as sinusoidal functions.
From Eq. :eq:`faradays_law_diff_freq` , we can infer two things:

1. Induced rotational electric fields are proportional to the angular frequency; this implies that electromagnetic induction is larger at higher frequencies.
2. Induced rotational electric fields, and the frequency-dependent magnetic fields responsible for them, are 90 degrees out of phase.

.. that sinusoidal magnetic fields characterized by higher frequencies will result in stronger electric fields.
.. Seogi: I possibly need better wording about this. 
.. We can see from Eq. :eq:`faradays_law_diff_freq` that sinusoidal magnetic fields characterized by higher frequencies will result in stronger electric fields.
.. , :math:`{\bf E}` is the frequency-dependent electric field and :math:`{\bf B}` is the frequency-dependent magnetic flux density.

Discovery of Faraday's Law
--------------------------

Faraday's law is best understood using three experiments, which Faraday conducted and summarized in 1831.
For each of these experiments, an electromagnet was used to create a time-dependent magnetic field, which we will represent using the magnetic flux density :math:`{\bf {b}}`.
A loop of wire with area :math:`A`, contoured by a closed path :math:`C`, was then held in proximity of the electromagnet.
This resulted in a magnetic flux :math:`{\boldsymbol \Phi_b}` defined by:

.. include:: ../../equation_bank/magnetic_flux_time.rst
Faraday's then conducted the following three experiments:

1. The loop of wire was mobed while the electromagnet remained stationary.
2. the electromagnet was moved while the loop of wire remained stationary.
3. both the loop of wire and electromagnet remained stationary, however, the strength of the magnetic field was varied as a function of time.

Faraday noticed that in all three experiments, an electromotive force :math:`\mathcal{E}` was induced in the wire, resulting in a measurable electric current.
The electromotive force :math:`\mathcal{E}` can be defined in terms of the electric field :math:`{\bf e}` by integrating over the path of the wire as follows:

.. include:: ../../equation_bank/electromotive_force_time.rst

In an ideal circuit, the electromotive force is equivalent to the Voltage :math:`V` experienced by the wire.
For a circuit with resistance :math:`R`, Ohm's law :math:`V=IR` can be used to show that electromotive forces are associated with currents :math:`I`.
Faraday's breakthrough came by proposing that a time-dependent change in magnetic flux through the wire loop was responsible for the resulting electromotive force.
In 1833, Heinrich Lenz determined that the time dependent change in magnetic flux was negatively proportional to the electromotive force it generated.
The contributions made by Faraday and Lenz are represented by the following equation:

.. include:: ../../equation_bank/faraday_lenz_time.rst

Lenz's contribution to Faraday's discovery not only provides the equality in Eq. :eq:`faraday_lenz_time` , but determines the direction of force on free charges in response to changes in an applied magnetic field. For a more complete description see the :doc:`lenz` page. By substituting the definition of magnetic flux from Eq. :eq:`magnetic_flux_time` and the definition of electromotive force from Eq. :eq:`electromotive_force_time` into Eq. :eq:`faraday_lenz_time`, we can obtain Faraday's law in integral form according to Eq. :eq:`faradays_law_int_time` .

Units
-----
Consider the units of quantities on the left and right-hand sides of Eq. :eq:`faradays_law_int_time`.
Using dimensional analysis, we obtain:

	.. math::

		V = Wb / s

.. TODO: parapharase this (I copy and paste wiki)

Therefore the above expression states that a change in magnetic flux, equal to 1 Webber per second, will induce an electromotive force of 1 Volt along a closed path.
Useing the aforementionned expression, the Webber (:math:`Wb`) can be expressed as:

	.. math::

		Wb = V \cdot s = J/A, 

where :math:`J` is the Joule, and :math:`A` is Amps.
Joules are used to represent a unit of energy, or work.
Thus we can interpret the magnetic flux as a unit of work per unit current. 

Geophysical Applications Faraday's Law
--------------------------------------

When performing electromagnetic surveys, various instruments are used to generate time-dependent magnetic fields.
These fields are commonly refered to as primary fields.
According to Eqs. :eq:`faradays_law_diff_time` , this will induce rotational electric fields within the surrounding region.
For a rock unit defined by conductivity :math:`\sigma` , Ohm's law (put a link here) :math:`{\bf j} = \sigma {\bf e}` implies that a current density :math:`{\bf j}` is also induced by the primary field.
These induced currents are parallel to :math:`{\bf e}` , and have a magnitude which depends on the physical properties of the rock.
Therefore, we can use Faraday's law in differential form to understand the manner in which rotational currents are induced in conductive objects, by an artificially generated primary field.

According to the Biot-Savart law (add link), current densities are responsible for generating magnetic fields.
This implies that currents induced by the primary field will result in the creation of an anomalous magnetic field, commonly refered to as the secondary field.
The secondary field can be measured at locations above the Earth's surface, and provides important information regarding subsurface geological structures.
But how is the secondary field measured?

If placed in a region where secondary fields are observable, a receiver loop of wire will experience an electromotive force according to Eq. :eq:`faraday_lenz_time` .
From Eq. :eq:`electromotive_force_time` , we know that the electromotive force is equivalent to the voltage being induced in the wire.
Therefore we can use voltage measurements to represent information regarding the secondary field, as opposed to measuring the field directly.

The explanation provided in this section may also be understood in the frequency-domain.
However, the voltage induced within the receiver coils will have both real and imaginary components.

