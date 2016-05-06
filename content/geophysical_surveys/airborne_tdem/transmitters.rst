.. _airborne_tdem_transmitters:

Transmitters and receivers
==========================

Transmitter
-----------
Because an ATEM system covers a wide bandwidth using rapid change in the transmitter current waveform, only one transmitter loop is needed at a time. 

- Platform. If using a helicopter, the transmitter loop is usually attached to a round frame towed after the helicopter through a cable. If using a fixed-wing airplane, the transmitter loop is shaped as a diamond attached to the nose, tail and wingtips of the plane.

- Current. The actual current that goes through the coil may vary depending on the power of the generator and other constraints. A transmitter loop mounted on a fixed-wing aircraft usually carries larger current thanks to the lifting capability of a fixed-wing for more powerful generators.

- Moment. A loop in practice can be multiple-turned and is about tens of meters in radius. The product of current, number of turns and the area makes the magnetic dipole moment of the transmitter. Modern ATEM systems are equipped with a dipole moment over 1 million Am^2 to achieve a depth of penetration down to a couple of kilometers.

- Waveform. A time-varying transmitter current waveform is used to induce a time-dependent EM fields underground. Unlike time-harmonic functions used in AFEM, ATEM waveform usually consists of on-time (current is turned on and changing) and off-time (current is turned off and not changing). The transition from on-time to off-time often invovles rapid change of current, which introduces high-frequency excitation to the EM induction with the earth. ATEM waveforms are usually bipolar, so some systematic errors can be stacked out. The shape of an ATEM system's waveform is fixed, but how often a on-time pulse appears can be tuned by a parameter called base frequency (typically from 20 to 90 Hz). A lower base frequency allows larger transmitter moment, measuring at later delay times, and thus detection of deep geology. Within one period, there can be two pluses in opposite polarities, so some systematic errors can be stacked out during data processing. 

.. figure:: ./images/atem_waves.jpg
 :align: center
 :scale: 80%
 :name: atem_waves

Common ATEM waveforms.


Receiver
--------

- Coil. ATEM uses another loop to measure the time-derivative of the magnetic field, in a way similar to AFEM.  The current in the transmitter loop and the induced current in the earth can both generated time-varying magnetic field. At the receiver coil, an electromotive force (measured in Volt) can be induced along the loop. The rate of change of the magnetic field (dB/dt) is proportional to the measured voltage. The coils can be multi-turned and the effective area of the receiver loop is an important parameter in understanding the data.

- Measurement. The dB/dt data measured at the receiver is the total field, including both the primary and the secondary field. Traditional TEM theory meaures the EM field during off-time when the primary is zero, so only the secondary is considered. But in practice both on-time and off-time data are acquired as time series. It has been shown that on-time TEM data are useful in the search of good conductors.


Configuration
-------------

- Orientation. The transmitter loop in an ATEM system is usually a horizontal loop, which is relatively easier to manufacture and implement in the field operation. The receiver loop can be much smaller, and three loops can be oriented orthogonally to measure three-component dB/dt. 

- Separation. Basic physical model for ATEM is a configuration called "coincident loop" or "central loop", in which the recevier is at the center of the transmitter loop. This has been strictly used in same ATEM systems, but there are variants. For example, the receiver can be mounted to the tail of the transmitter loop or suspended above the transmitter loop. In a fixed-wing system, the receiver is usually towed effectively a couple of hundreds meters after and below the transmitter loop. Such separation is negligible for low induction number, but must be taken into account when interpreting early time channels or over conductive geology.

.. figure:: ./images/atem_configs.jpg
 :align: center
 :scale: 80%
 :name: atem_configs

Common ATEM configurations.







