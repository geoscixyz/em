.. _dcr_transmitters:

Transmitters
============

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

.. figure:: images/current_receiver_wire.jpg
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

   A typical transmitter `waveform <http://www.eos.ubc.ca/ubcgif/iag/methods/meth_2/3measurements.htm>`_

The primary voltage, or DC component of the measured voltage is taken before
any IP effect has taken place, as noted by :math:`\mathrm{V}_{\sigma}` in
:numref:`IP_waveform2`, whereas the IP measurement is taken as an integral
beneath the voltage curve between two user defined time points (t1 and t2).
The Newmont standard is to take t1 = 450 ms and t2 = 1100 ms.

.. figure:: images/IP_waveform2.jpg
   :scale: 80%
   :align: center
   :name: IP_waveform2

   `Location of DC and IP measurements along the receiver voltage curve <http://www.eos.ubc.ca/ubcgif/iag/methods/meth_2/3measurements.htm>`_
