.. _magnetic_permeability_lab_measurements:

Laboratory Measurements
=======================

Magnetic permeability measurements can be understood by considering a forced, in-series LC circuit (Figure needs reference).
math:`V` represents a driving voltage for the circuit, :math:`I` is the current in the wire, and :math:`C` is a known capacitive element.
:math:`L` represents a linear self-inductance, which ultimately depends on the rock's magnetic permeability.
The current within the wire is defined by the following ordinary differential equation:

.. math::
	\frac{d^2 I (t)}{d t} + \frac{1}{LC} I(t) = F(t)
	:label: Forced_Oscillator

where :math:`F(t)` represents the driving voltage. Eq. :eq:`Forced_Oscillator` has a natural resonance frequency of:

.. math::
	\omega_r = \frac{1}{\sqrt{LC}}
	:label: Omega_Resonance

In typical laboratory measurements, rock samples are placed in a holder.
Introduction of the sample changes the inductive element of the circuit, thus changing its resonance frequency. 
Each instrument has an experimentally derived curve, which defines the change in resonance frequency with or without the sample, as a function of the rock's magnetic permeability.
Therefore, the magnetic permeability of the rock can be determined by measuring the change in resonance frequency, and determining its position on the curve.

.. figure:: ./figures/figSuscMeasure.png
	:align: center
        :scale: 50%

The underlying physics of magnetic permeability measurements can be understood by considering the circuit diagram in Figure (needs reference).
For sensitive measurements, a portion of the wire is wound around a ferrite.
Ferrites are non-conductive and extremely permeable (:math:`\mu_{f} \sim 1000\mu_0`).
As a result, they become extremely magnetized when exposed to a magnetic field, but experience negligible EM induction under 5 kHz (reference?).
The ferrite does not form a closed path.
Within the gap, a rock of magnetic permeability :math:`\mu_s` is placed.
The coil-ferrite system acts as an inductive element for the circuit, and is denoted by :math:`L`.
Thus, the current within the wire can be describe using Eq. (reference).


The driving voltage generates a current within the wire.
This current creates a magnetic field :math:`H` within the coil.
If the material within the coil was conductive, it would experience an electromotive force.
Because ferrites are purely magnetic, they experience a magnetomotive force :math:`\mathcal{F}` instead.
Whereas electromotive forces oppose the magnetic field, magnetomotive forces re-enforce it.
By neglecting edge effects near the ends of the coil, the magnetomotive force experienced by the ferrite is:

.. math::
	\mathcal{F} = NI = H \Delta S
	:label: MMF

where :math:`N` is the number of turns the coil has, and :math:`\Delta S` is the length of the coil.
Because ferrites are so permeable, they behave like a magnetic circuit in this case.
The applied magnetomotive force generates a magnetic flux $\Phi$, which permeates through the material.
This can be described using Hopkinson's law, which is analogous to Ohm's law:

.. math::
	\mathcal{F} = \Phi \Re
	:label: Hopkinsons_Law

where :math:`\Phi` is the magnetic flux along the path of the ferrite, and :math:`\Re` is defined as the magnetic reluctance.
Magnetic reluctance represents the ratio of magnetomotive force to induced magnetic flux. 
If our ferrite formed a closed path, had uniform cross-sectional area :math:`A`, and total length :math:`\ell`, its magnetic reluctance would be given by:

.. math::
	\Re = \frac{\ell}{\mu_f A}
	:label: Reluctance

In our experiment however, there is a gap containing a rock sample.
Like electrically resistive elements, magnetically reluctant elements may be added in series.
If the cross-sectional area remains constant:

.. math::
	\Re = \sum_k \frac{\ell_k}{\mu_k A}
	:label: Reluctance_No_Sample

Eq. :eq:`Reluctance_No_Sample` can therefore be used to describe the magnetic reluctance of our system in the absence of a rock sample.
When a rock sample is placed within the gap, it affects the magnetic reluctance.
In most laboratory experiments, the magnetic reluctance is given by (Clark and Emerson, 1991):

.. math::
	\Re = \Re_0 + \frac{\alpha}{\mu_s}
	:label: Reluctance_Sample
	
where :math:`\Re_0` and $\alpha$ can be experimentally determined, and depend on the geometry of the instrument.
By definition of the self-inductance, and by using Eqs. :eq:`Hopkinsons_Law` and :eq:`Reluctance_Sample`:

.. math::
	L = \frac{N \Phi}{I} = \frac{N \mathcal{F}}{I \Re} = \frac{N^2}{\Re}
	:label: Inductance

Therefore, the self-inducance of the circuit is inversely proportional to the magnetic reluctance.
For our theoretical experiment, the magnetic permeability of a rock sample may be determined by:

1) Finding the resonance frequency :math:`\omega_r` of the circuit.

2) Using :math:`\omega_r` and :math:`C` to obtain the circuit's self-inductance :math:`L`.

3) Using :math:`L` to obtain the magnetic reluctance :math:`\Re`.

4) Then using :math:`\Re`, and experimentally derived parameters :math:`\Re_0` and :math:`\alpha`, to obtain the sample's magnetic permeability :math:`\mu_s`.