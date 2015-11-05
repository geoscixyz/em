.. _transmitters_receivers_index:

Survey instruments 
==================

- :ref:`power_supply`
- :ref:`transmitters`
- :ref:`receivers`
- :ref:`survey_layouts`
- :ref:`survey_acquisition`

.. _power_supply:

Power supply
____________
A generator or battery provides a source of power for the tranmitter in geophysical surveys. A typical example of a generator used for a Direct Current Induced Polarization (DC/IP) survey is shown below, with a power limit of 7500W.
 	
.. figure:: images/generator_dcip_7500W.jpg
   :scale: 40%
   :align: center

   A typical generator (`source <http://williamsonneelectric.com/sgx50005000wattsubaruportablegenerator.aspx>`_)

.. _transmitters:

Transmitters/sources
____________________
A transmitter sends out a desired current waveform through the current wire. The electric current and voltage are measured and regulated by the transmitter controller, and either quantity can be set to a particular amount within the power limit. A typical example of a transmitter used for a DC/IP survey is shown below with a power limit of 5000W.



.. figure:: images/transmitter_dcip_vip5000.jpg
   :scale: 60%
   :align: center

   A transmitter (source_)

.. _source: http://www.hazzazi-sa.com/agents/iris-instruments?page=1/

**DC resistivity**: Current electrodes transmit electricity into the ground, and as such they need good contact with the ground. Pouring salty water on the electrodes can help to improve the contact with the ground, or wrapping the electrode with a soaked cloth. Often the electrodes are steel or iron rods. A typical 12 gauge current wire used for a DC/IP survey is shown below.

.. figure:: images/current_wire.jpg
   :scale: 50%
   :align: center

   Current wire (`source <http://www.aliexpress.com/item/In-stock-8-Gauge-1-ft-Red-Car-Auto-Audio-Power-Ground-Wire-Cable-line-AWG/619638915.html>`_)

**Frequency-domain EM**:

**Time-domain EM**:

**Natural source EM**:

.. _receivers:

Receivers
_________

**DC resistivity**: Two receiver electrodes are used to measure the voltage difference in a DC/IP survey. Non-polarizing electrodes are commonly porous pots composed of a solid metal wire in a salt solution. It is also common to use lead wire in a lead-chloride mix or copper wire in a copper-sulphate solution. This eliminates self potential between the wire and the ground, and it improves the quality of the data. The voltage potential is measured between any combination of receiver electrodes due to super-position theory, as long as the data was collected simultaneously. An example of a porous pot receiver electrode for a DC/IP survey with a copper sulphate solution is shown below.

.. figure:: images/receiver_electrode_porous_pots.jpg
   :scale: 70%
   :align: center

   A type of electrode (`source <http://www.agiusa.com/agicatalog.shtml>`_)

**Electromagnetics**:

.. _survey_layouts:

Common survey layouts
_____________________

Below are common survey layouts that can be used. *Maybe better suited for the survey design page?*

**Pole-dipole**: A DC/IP survey using a single current electrode (the second current electrode is at "infinity" or many kilometers away from the nearest receiver electrode) and two potential electrodes. Conventionally, for a 2D survey the receiver electrodes are placed in a linear fashion away from the transmitter electrode as shown in the figure below.

.. figure:: images/poledipole.png
   :scale: 80%
   :align: center
   
   A pole-dipole survey (`source <http://en.openei.org/wiki/DC_Resistivity_Survey_(Pole-Dipole_Array)>`_)

**Dipole-dipole**: Similar to a pole-dipole survey except that both current electrodes are located close to the receiver area. An example of a typical 2D dipole-dipole survey layout with the plotting convention for a pseudo-section is shown below.  A pseudo-section is a method for plotting the data using the geometry of the survey to place the data points. The plotting point is located half-way between the nearest current 
electrode and the receiver electrode at a depth of one-half the horizontal transmitter-receiver separation.

.. figure:: images/pole-dipole_pseudo.jpg
   :scale: 100%
   :align: center

   A dipole-dipole survey and psuedo-section (`source <http://www.eos.ubc.ca/ubcgif/iag/methods/meth_1/measurements.htm>`_)

.. _survey_acquisition:

Common survey acquisition systems
_________________________________

*include a bit more about electrode layouts, a waveform/pulse for transmitter, when the measurement is made, placeholders for IP, *

Below are common acquisition systems that are used in industry to collect DC resistivity, electromagnetic, and/or MT and ZTEM data.

**MIMDAS**:

**NEWDAS**:

**DIGHEM**:

**VTEM**:

**ZTEM**:

