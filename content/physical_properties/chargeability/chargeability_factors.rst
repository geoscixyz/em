.. _chargeability_factors:

Factors that affect chargeability
=================================

The chargeability of earth materials is essentially an electrochemical effect caused by many factors, not all of which are completely understood. If ground is chargeable, it responds as if resistivity was a complex quantity - it behaves somewhat like a leaky capacitor. Therefore the chargeability can be measured in a number of ways using time domain or frequency domain techniques. 
Aspects affecting the chargeability of a sample include:

	 - the grain size of particles in the sample;
	 - the type and mobility of ions within the pore fluids;
	 - the details of microscopic interactions between solid surfaces and fluids;
	 - the amount of surface area within a specific volume.

The surface area-to-volume ratio is an important factor. Clays tend to be chargeable while sandstones are not, and the images here illustrate one reason why this is true. In addition, the surface interactions between clay minerals and fluids enhance the ability of these materials to hold charges.


Two microscopic effects cause macroscopic chargeability
-------------------------------------------------------

There are two primary causes of chargeability. In both cases the re-distribution of charges takes some time to occur when an external DC electric field is applied. Equivalently, it takes the same time to revert to a balanced charge distribution once the electric field is removed. "Charging" is hard to measure in practice. "Discharging" is measured using time domain IP survey techniques. The effect of finite charging time on sinusoidal signals at different frequencies also can be measured using frequency domain or phase IP surveys. The two types of polarization are called "membrane polarization" and "electrode polarization."

Membrane polarization
^^^^^^^^^^^^^^^^^^^^^

Membrane polarization occurs when pore space narrows to within several
boundary layer thicknesses (which is the thickness of ions adsorbed to a
surface).

 .. figure:: ./figures/memb1.gif
	:align: center
	:scale: 100 %

Charges cannot flow easily, so they accumulate when an electric field is
applied.

 .. figure:: ./figures/memb2.gif
	:figclass: center
	:align: center
	:scale: 100 %


The result is a net charge dipole which adds to any other voltages measured at
the surface.

 .. figure:: ./figures/memb3.gif
	:align: center
	:scale: 100 %

A second form of membrane polarization is similar to the first:

 .. figure:: ./figures/memb_pol_2nd_type.gif
	:align: right
	:scale: 100	%

This occurs where clay particles partially block ionic solution paths, as in
the adjacent figure. Upon application of an electric potential, positive
charge carriers pass easily, while negative carriers accumulate. There is an
"ion-selective membrane."

A surplus of both cations and anions occurs at one end of the membrane, while
a deficiency occurs at the other end. The reduction of mobility is most
obvious at frequencies slower than the diffusion time of ions between adjacent
membrane zones; i.e. slower than around 0.1 Hz. Conductivity increases at
higher frequencies.

Electrode polarization
^^^^^^^^^^^^^^^^^^^^^^

Electrode polarization occurs when pore space is blocked by metallic
particles. Again, charges accumulate when an electric field is applied.

 .. figure:: ./figures/elec_pol_1.gif
	:align: center
	:scale: 100 %

The result is two electrical double layers which add to voltages measured at
the surface.

.. figure:: ./figures/elec_pol_2.gif
	:align: center
	:scale: 100 %

Comments on electrode polarization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. figure:: ./figures/elec_pol_3.gif
	:align: right
	:scale: 100 %

Some remarks are appropriate here in order to provide some sense of the
complexity of the chargeability phenomenon.

At an interface between ionic and metallic conduction (for example, an ore
grain in pore water), there is an impedance involved in getting current to
flow across the barrier. These interfaces look like the top figure and have
the simplified circuit analogue shown in the bottom figure.

 .. figure:: ./figures/elec_pol_4.gif
	:align: right
	:scale: 100 %

Current can flow via charge transfer (or ion diffusion), which involves
electrochemical processes, or via a capacitive effect (no charge transfer),
involving diffusion currents.

Ion diffusion is not easy to model with circuit elements. The process is
called the Warburg impedance. Its magnitude varies as approximately
1/frequency.

Note that, while it is useful to understand simplified models of the relevant
electrical behaviour of surface-electrolyte interactions, all rocks are, in
fact, "dirty" in the sense that they are not simply pure "electrodes"
(semiconducting mineral grains) and electrolytes (pore solutions).  There are
other materials and particles affecting ionic behaviour within and outside the
diffuse layer, and some of the sample's constituents will affect the behaviour
of the fixed layer near and on the liquid-solid interfaces.

Summary of what affects the chargeability of material
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	- Induced polarization is greater when there are larger regions of
	  adsorbed anomalous charge (adjacent to an interface); i.e. when there is
	  a large surface area-to-volume ratio.

	- Non-ionic fluids (such as contaminants) can markedly change the
	  behaviour of surface-electrolyte interactions.

	- Changes in ion concentration (such as increased salinity) will also
	  affect both types of polarization.

	- Both effects (membrane and electrode polarization) are related to grain
	  size as much as material type. Therefore, discrimination of mineral type
	  on the basis of chargeability alone is not recommended.

.. todo:: 
    Factors that affect chargeabilty (microscopic phenomenon (images from GPG); conceptual models metallic and membrane polarization illustrating charge accumulation)

