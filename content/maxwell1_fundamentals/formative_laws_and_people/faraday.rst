.. _faraday:

Faraday's Law
=============

Faraday's law is named after English scientist Michael Faraday (1791-1867), and describes the manner in which time-varying magnetic fields induce electric fields. 

Integral Form in the Time-Domain
--------------------------------

Faraday's law in integral form can be expressed using the following equation:

.. include:: ../../equation_bank/faradays_law_int_time.rst

where :math:`{\bf e}` is the electric field (:math:`V/m`) defined around a closed path :math:`C`, :math:`{\bf b}` is the magnetic flux density (:math:`Wb/m^2`) defined over a surface :math:`A` contoured by :math:`C`.and :math:`{\boldsymbol \Phi_B}` is the total magnetic flux (:math:`Wb`) moving through surface :math:`A`. 

.. Seogi: How about breaking apart above equations..

The first two terms in Eq. :eq:`faradays_law_int_time` are related using Stokes' theorem.
Eq. :eq:`faradays_law_int_time` states that the time-dependent rate of change in total magnetic flux, through a surface bounded by a closed path, is negatively proportional to the line integral of the electric field over that path.

.. Seogi: We can possibly link what is outward normal
.. The unit vector :math:`\hat n` is used to define the direction perpendicular to incrementally small portions of surface area :math:`da` within surface :math:`A`. 
Here :math:`\hat n` is outward normal, and :math:`d{\bf l}` is an incrementally small unit of length along closed path :math:`C`.

.. note:: Negative sign in RHS of Eq. :eq:`faradays_law_int_time` denotes conservation of electromagnetic energy.


Differential Form in the Time-Domain
------------------------------------
.. This was obtained by applying Stokes' theorem to the first term
.. As a result, Faraday's law in differential form can be expressed as:
The integrands of second and third terms in Eq. :eq:`faradays_law_int_time` are identical, and hence Faraday's law in differential form can be expressed as:

.. include:: ../../equation_bank/faradays_law_diff_time.rst

.. Therefore, the time dependent change in magnetic flux density at any location is negatively proportional to the curl of the electric field.
.. For magnetic fields which change rapidly with respect to time, we expect to observe a larger electric field.
Above equation physically means that time varying magnetic fields will induce rotational electric fields. 


Faraday's Law in the Frequency-Domain
-------------------------------------

Frequency-domain representation of Faraday's law can be obtained by applying a Fourier transform to Eqs. :eq:`faradays_law_int_time` and :eq:`faradays_law_diff_time`.
The integral form of Faraday's law in the frequency domain is:

.. include:: ../../equation_bank/faradays_law_int_freq.rst

.. Similarly to Eq. :eq:`faradays_law_int_freq`, the first two terms in Eq.() are related using Stokes' theorem.
Similarly, the differential form of Faraday's law is:

.. include:: ../../equation_bank/faradays_law_diff_freq.rst

where :math:`\omega` is the angular frequency in (rad/s). 

.. Seogi: I possibly need better wording about this. 
.. We can see from Eq. :eq:`faradays_law_diff_freq` that sinusoidal magnetic fields characterized by higher frequencies will result in stronger electric fields.

.. , :math:`{\bf E}` is the frequency-dependent electric field and :math:`{\bf B}` is the frequency-dependent magnetic flux density.


Units
-----

Discovery of Faraday's Law
--------------------------

Faraday's law is best understood using 3 experiments, which Faraday conducted and summarized in 1831.
For each of these experiments, an electromagnet was used to create a time-dependent magnetic field, which we will represent using the magnetic flux density :math:`{\bf {b}}`.
A loop of wire with area :math:`A`, contoured by a closed path :math:`C`, was then held in proximity of the electromagnet.
This resulted in a magnetic flux :math:`{\boldsymbol \Phi_b}` through the area within the loop, defined by:

.. include:: ../../equation_bank/magnetic_flux_time.rst

Once again, :math:`\hat n` is the unit vector perpendicular to an incrementally small area :math:`da` within surface :math:`A`.
In the first experiment, Faraday moved the loop of wire while the electromagnet remained stationary.
In the second experiment, the electromagnet was moved while the loop of wire remained stationary.
For the third experiment, both the loop of wire and electromagnet remained at a fixed position, however, the strength of the magnetic field was varied as a function of time.
Faraday noticed that in all 3 experiments, an electromotive force :math:`\varepsilon` was induced in the wire, resulting in a measurable electric current.
The electromotive force :math:`\varepsilon` is related to the electric field :math:`{\bf e}` by integrating over the path of the wire:

.. include:: ../../equation_bank/electromotive_force_time.rst

In an ideal circuit, this is equivalent to the Voltage :math:`V` experienced by the wire.
For a circuit with resistance :math:`R`, Ohm's law :math:`V=IR` can be used to show that an EMF results in current :math:`I`.
Faraday's breakthrough came by proposing that a time-dependent change in magnetic flux through the wire loop was responsible for the EMF experienced by the wire.
Empirically, he determined the following relationship:

.. include:: ../../equation_bank/lenzs_law_time.rst

The relationship in Eq.() is also known as Lenz's law.
By substituting the definition of magnetic flux from Eq.() and the definition of electromotive force from Eq.() into Eq.(), Faraday was able to define the relationship between time-varying magnetic fields and the electric fields they induce in matter.

History of Michael Faraday
--------------------------

Faraday's law is named after English scientist Michael Faraday (1791-1867), and describes the manner in which time-varying magnetic fields induce electric fields in matter.
Although Faraday is most recognized for his pioneering research in the field of electromagnetics, he is also accredited with significant contributions to the field of electrochemistry; including the discovery of benzene, and creating the laws of electrolysis. 