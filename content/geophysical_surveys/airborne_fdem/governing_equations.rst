.. _airborne_fdem_governing_equations:

Governing Equations
===================

To understand the theory of airborne FEM, knowledge in Maxwell3 and Maxwell4 are required. In particular, the following items are essential:
- Magnetic dipole in freq-domain. The physical model of airborne transmitter and recevier is a magnetic dipole. It can be effectively represented by a sufficiently small loop. In a frequency domain survey, the current in the loop varies in a sinsoid waveform at a particular frequency, then the dipole moment osillates in phase with the current. (LINK to magnetic dipole) 
- A conceptual model involving three inductively coupled loops can be used to undertand airborne EM. The airborne transmitter, receiver and the earth are represented by three loops in a certain orientation. The receiver is directly coupled with the transmitter loop for the primary field. It is also indirectly coupled with the transmitter loop through the earth loop, which generates the secondary field. The ratio of the secondary to the primary therefore contains the information about the conductivity of the earth loop. The 3-loop model is a useful concept, because by tuning the induction number (function of conductivity and frequency), we can see how a FEM system behaves in the resistive or inductive limits. We can further explore the effect of mutual coupling of the loop in the data for the qualitative understanding of data in practice. (LINK to 3-loop model)





