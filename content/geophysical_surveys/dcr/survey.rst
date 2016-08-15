.. _dcr_survey:

Survey
======

.. topic:: Purpose

   provide an overview of common survey set-ups nd instrumentation used in DC resistivity experiments


Basic Survey Setup
------------------

**Pole-dipole**: A DC/IP survey using a single current electrode (the second current electrode
is at "infinity" or many kilometers away from the nearest receiver electrode)
and two potential electrodes. Conventionally, for a 2D survey the receiver
electrodes are placed in a linear fashion away from the transmitter electrode
as shown in the figure below.

.. figure:: ./images/poledipole.png
   :scale: 80%
   :align: center

   `A pole-dipole survey <http://en.openei.org/wiki/DC_Resistivity_Survey_(Pole-Dipole_Array)>`_

**Dipole-dipole**: Similar to a pole-dipole survey except that both current electrodes are
located close to the receiver area. An example of a typical 2D dipole-dipole
survey layout with the plotting convention for a pseudo-section is shown
below.  A pseudo-section is a method for plotting the data using the geometry
of the survey to place the data points. The plotting point is located half-way
between the nearest current electrode and the receiver electrode at a depth of
one-half the horizontal transmitter-receiver separation.

.. figure:: images/pole-dipole_pseudo.jpg
   :scale: 100%
   :align: center

   `A dipole-dipole survey and psuedo-section <http://gpg.geosci.xyz/en/latest/content/DC_resistivity/DC_measurements_and_data.html>`_

**Distributed array** : A distributed array is composed of receiver electrodes that are deployed and
connected in conventional 2D lines or as a 3D grid network. For any current
electrode position, data is acquired simultaneusly at all receiver locations,
commonly as a time-series. With post-processing and use of the super-position
principle, voltage potentials can be calculated between any of the connected
receiver electrodes. This can create a vast amount of useful data for an
ensuing 3D inversion. An example of a distributed array is the MIMDAS system
shown in :numref:`MIMDAS_layout`.

**MIMDAS** :

.. figure:: images/MIMDASlayout.jpg
   :scale: 90%
   :align: center
   :name: MIMDAS_layout

   Overview of the `MIMDAS layout <http://www.austhaigeophysics.com/A%20Comparison%20of%202D%20and%203D%20IP%20from%20Copper%20Hill%20NSW%20-%20Extended%20Abstract.pdf>`_


.. _dcr_instrumentation:

Instrumentation
---------------

.. _dcr_transmitters:

Transmitters
************

A generator or battery provides a source of power for the transmitter in
geophysical surveys. A typical example of a generator used for a Direct
Current Induced Polarization (DC/IP) would have a power limit of 7500W or
greater. The transmitter sends out a desired current waveform through the
current wire. The electric current and voltage are measured and regulated by
the transmitter controller, and either quantity can be set to a particular
amount within the power limit. An example of a generator hooked up to a
transmitter in the field is shown in :numref:`generator_DC` below.

.. figure:: images/generator_transmitter.jpg
   :scale: 40%
   :align: center
   :name: generator_DC

   A typical generator hooked up to a transmitter in the field

**DC resistivity**: Current electrodes transmit electricity into the ground, and as such they need
good contact with the ground. Pouring salty water on the electrodes can help
to improve the contact with the ground, or wrapping the electrode with a
soaked cloth. Often the electrodes are steel or iron rods. A typical 12-gauge
current wire (red) used for a DC/IP survey is shown in
:numref:`current_receiver_wire_DC` along with 16-gauge receiver wires
(orange).

.. figure:: images/current_receiver_wire.png
   :scale: 10%
   :align: center
   :name: current_receiver_wire_DC

   Red current wire (12-gauge) with multiple receiver wires (16-gauge) in orange

A typical time-domain waveform for DC/IP is a two second on, two second off,
half-duty waveform as shown in :numref:`IP_waveform`. The name comes from the
fact that the current is only running for half of the time. The figure shows
that the current waveform has a two second positive on-time followed by a two-
second off-time, followed by a two-second negative on-time before a final two
second off-time. When no chargeable material is present in the ground, the
corresponding voltage curve will mirror that of the current curve. The
positive and negative on-times are done so that any self-potential in the
ground due to natural telluric currents, or currents induced by changing
mangetic fields in the atmosphere, will be cancelled out.  Generally many
cycles of the current waveform are transmitted into the ground in order to
stack many receiver voltage curves to reduce noise in the data. When
chargeable material is present the voltage curve will slowly ramp up during
the positive on-time and will discharge during the corresponding off-time. The
mirror image will happen during the negative on-time and off-time. Once again
these curves are stacked to reduce the noise.

.. figure:: images/IP_waveform.jpg
   :scale: 100%
   :align: center
   :name: IP_waveform

   A typical transmitter `waveform <http://gpg.geosci.xyz/en/latest/content/induced_polarization/induced_polarization_measurements_data.html>`_

The primary voltage, or DC component of the measured voltage is taken before
any IP effect has taken place, as noted by :math:`\mathrm{V}_{\sigma}` in
:numref:`IP_waveform2`, whereas the IP measurement is taken as an integral
beneath the voltage curve between two user defined time points (t1 and t2).
The Newmont standard is to take t1 = 450 ms and t2 = 1100 ms.

.. figure:: images/IP_waveform2.jpg
   :scale: 80%
   :align: center
   :name: IP_waveform2

   `Location of DC and IP measurements along the receiver voltage curve <http://gpg.geosci.xyz/en/latest/content/induced_polarization/induced_polarization_measurements_data.html>`_

.. _dcr_receivers:

Receivers
*********

**DC resistivity**: Two receiver electrodes are used to measure the voltage difference in a DC/IP
survey. Non-polarizing electrodes are commonly porous pots composed of a solid
metal wire in a salt solution. It is also common to use lead wire in a lead-
chloride mix or copper wire in a copper-sulphate solution. This eliminates
self potential between the wire and the ground, and it improves the quality of
the data. The voltage potential is measured between any combination of
receiver electrodes due to super-position theory, as long as the data was
collected simultaneously. An example of a porous pot receiver electrode for a
DC/IP survey with a copper sulphate solution is shown in
:numref:`porous_pot_receiver`.

.. figure:: images/receiver_electrode_porous_pots_receiver.jpg
   :scale: 70%
   :align: center
   :name: porous_pot_receiver

   A single porous pot electrode in the ground connected to a receiver.


