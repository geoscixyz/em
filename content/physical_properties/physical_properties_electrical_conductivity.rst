.. _physical_properties_electrical_conductivity: 

Electrical Conductivity
=======================

Electrical conductivity is a physical property that describes how easily electric currents can flow through a medium. Conductivity, and its reciprocal, "resistivity", are used interchangeably.  
The conductivity of earth materials depends on many factors but primarily upon mineral content, porosity, saturating fluids, connecting paths and temperature.



.. note:: 
    The measured conductivity (or resistivity) often shows a frequency dependence. Effectively the material can act like a capacitor and build up a charge when an electric field is applied. The ability to accumulate charge is called "chargeability" and the survey designed to measure the effect is called an IP (Induced Polarization) or, SIP (spectral IP) survey. Chargeabilty is often listed as an independent physical property (such as density, magnetic suspectibilty) and we will continue with that in this EM resource. It is however, just an element that is necessary in order to provide a complete description of electrical conductivity.



ToC: Contents: 
(a) Lab setup/measurements
(b) Units (also difference between resistance, resistivity; R=rho L/A)
(c) Factors that affect electrical conductivity (metallic, ionic, semi-conductor, fluids, connectivity)
(d) Some mathematical relationships (eg Archie's law,) (big topic but low priority. A placeholder will do. )
(e) Tables of conductivty (one from GPG, other tables for rocks and minerals)
(f) Where conductivity can be a diagnostic physical property.

References: Rock and Mineral Properties: Keller SEG Vol 1 Electromagnetic Methods in Applied Geophysics

Knight and Enders: An introduction to Rock Physics Principles for near surface geophysics: Investigations in geophysics No13; SEG Near;-Surface Geophysics edited by Dwain Butler

Stan Ward: Resistivity ad Induced Polarization Methods (p147..)
Investigations in geophysics #5; Geotechical and environemental geophysics.




Chargeability
=============

ToC: Contents: 
(a) Lab setup/measurements
(b) Impedance curve with frequency (Z(w)); sigma(w); definition of eta from the asymptotic values; transforming to time to get time dependent conductivity; over-voltage diagram; using V_inf and V_0 to theoretically define eta. 
(c) Factors that affect chargeabilty (microscopic phenomenon (images from GPG); conceptual models metallic and membrane polarization illustrating charge accumulation)
(d) Some mathematical relationships (Cole-Cole (conductivity and resistivity); stretched exponential.   (maybe here is python widget for Cole-Cole) )
(e) Units: the intinsic chargeabilty is dimensionless. [0,1]. In practise surveys are explicitly designed to find chargeable material and the field data acquire units that correspond to the survey.  In this regard, any datum that is connected with chargeable .
(e) Tables of chargeability (one from GPG, other tables for rocks and minerals)
(f) Where chargeabilty can be a diagnostic physical property.

References: Rock and Mineral Properties: Keller SEG Vol 1 Electromagnetic Methods in Applied Geophysics

Knight and Enders: An introduction to Rock Physics Principles for near surface geophysics: Investigations in geophysics No13; SEG Near;-Surface Geophysics edited by Dwain Butler

Stan Ward: Resistivity ad Induced Polarization Methods (p147..)
Investigations in geophysics #5; Geotechical and environemental geophysics.


---------  Scraps:  to be included as it fits into the above framework. 
The electrical conductivity of a material can depend upon frequency. In Ohm's Law, \\J=\\sigma E\\, \\sigma\\ is a complex number. The underlying microscopic phenomonae accounting for this is complicated and depends upon the minerals, grain sizes, and surface-to-volume ratios and the abundance of clays. There is no simple mathematical formula that describes the relation between conductivity and frequency but one that has some practical use is the Cole-Cole model.

Formula for conductivity and for resistivity. Definitions of variables. eta is the "chargeability" (dimensionless 0<eta<1); eta is often related to the concentration of a chargeable mineral, for instance eta is related to the total percentage of sulfide minerals. tau is a time constant generally thought to be related to grain size; c is a variable associated with (?distribution of grain size?)

Historically "chargeabilty" has been referred to as "over-voltage". The description arises from geophysial surveys in the 1950's and is illustrated in the following diagram:

Our generic diagram in GPG (or equivalent), showing 1/2 duty waveform, V_inf, V_0, eta, V_s

