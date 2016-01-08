.. _theory_3loops:

Theory for three-loop systems
-----------------------------

.. figure:: images/ThreeLoops.png
    :name: loops
    :figwidth: 40%
    :align: right

    The three-loop system consists of a transmitter (TX), a receiver (RX), and a target.

.. figure:: images/LoopOrientations.png
    :name: looporient
    :figwidth: 30%
    :align: right

    The orientation of the loops can be changed by adjusting the inclination `I` and the declination `D`.

A lot can be gleaned from considering a three-loop system, as shown in :numref:`loops`. The system consists of a transmitter loop (TX), a receiver loop (RX), and a target. The target resembles a conductive anomaly and its response depends on its inductance and its resistance as well as the frequency used by the TX-RX.
    
A current in the transmitter generates a primary magnetic field. This induces a current in the target loop, which in turn generates a secondary magnetic field in opposing direction as per :ref:`Lenz's law <lenz>`. The primary and secondary magnetic field are measured at the receiver. If the primary and secondary field are in opposing directions at the receiver, we consider this to be a negative datum. If they are in the same direction, the datum is positive.

The description of electromagnetic induction can be expressed mathematically as follow:

.. math::
        \frac{\mathbf{H}^s}{\mathbf{H}^p} = - A * f(\alpha),
        :label: l1

where `A` is a coupling term that described the locations and orientations of the loops while \\( f(\\alpha) \\) is the induction term that depends on the properties of the target loop. In full, Equation :eq:`l1` can be expressed as:

.. math:: 
        \frac{\mathbf{H}^s}{\mathbf{H}^p} = - \frac{M_{12} M_{23}}{L M_{13}} \frac{\alpha^2 + i \alpha}{1 + \alpha^2},
        :label: l2

where `M` is the mutual inductance between two loops and \\( \\alpha \\) is the inductive response number, written as:

.. math::
        \alpha = \frac{\omega L}{R},

where `L` and `R` are the inductance and resistance of the target loop and \\( \\omega \\) is the angular frequency. We can plot the real and imaginary response \\( f(\\alpha) \\) for a range of  \\( \\alpha \\) values (:numref:`RvsAlpha`). The plot shows that at low induction numbers, both the real and imaginary responses are small and that at high induction numbers, the real component is large but the imaginary component is small. Thus, the ratio of the real and imaginary component provides an idea of the induction number and can therefore be used when looking at data to get a first-order estimate of the conductivity.

.. figure:: images/ResponseVsAlpha.png
    :name: RvsAlpha
    :align: center

    Real and imaginary response vs induction number

Equation :eq:`l2` also depends on the mutual inductance between the loops. The three mutual inductance terms are defined as follows:

- \\( M_{12} \\) = mutual inductance between TX (1) and target (2)
- \\( M_{23} \\) = mutual inductance between target (2) and RX (3)
- \\( M_{13} \\) = mutual inductance between TX (1) and RX (3)

The mutual inductance can be derived from the :ref:`Biot-Savart law <biot_savart>`, which gives us the magnetic field. Assume we are looking at two loops and the magnetic field due to the first loop is \\( \\mathbf{B}_1 \\). We can calculate the flux \\( \\Phi_2 \\)of this magnetic field through the second loop as follows:

.. math::
        \Phi_2 = \int \mathbf{B}_1 \cdot da_2 = M_{12} I_1.
        :label: phi2
    
This flux is then equal the mutual inductance times the current. We can solve for the mutual induction in a few more steps. Using Stokes' Theorem and the vector potential of \\( \\mathbf{B}_1 \\), Equation :eq:`phi2` becomes a line integral:

.. math::
        \Phi2 = \int \mathbf{B}_1 \cdot da_2 = \int (\nabla \times \mathbf{A}_1) \cdot da_2 = \oint \mathbf{A}_1 \cdot dl_2,
        :label: phi22

where \\( \\mathbf{A}_1 \\) is derived using the Biot-Savart law:

.. math::
        \mathbf{A}_1 = \frac{\mu_0 I_1}{4\pi} \oint \frac{dl_1}{\lvert \mathbf{r} - \mathbf{r'}\rvert^2}.
        :label: A1
     
By subbing Equation :eq:`A1` into :eq:`phi22`, we get the following integral expression for the flux:

.. math::
        \Phi_2 = \frac{\mu_0 I_1}{4\pi} \oint \left ( \oint \frac{dl_1}{\lvert \mathbf{r} - \mathbf{r'}\rvert^2} \right ) \cdot dl_2.
        :label: phi23

We can then write the mutual inductance between two loops as:

.. math::
        M_{12} = \frac{\mu_0}{4\pi} \oint \oint \frac{dl_1 \cdot dl_2}{\lvert \mathbf{r} - \mathbf{r'}\rvert^2}.
        :label: m12

There are a few significant things about Equation :eq:`m12`:

- \\( M_{12} \\) depends purely on geometry, such as the size, shape, and relative positions of the two loops
- This expression doesn't change if we look at the flux in the first loop due to the second loop, meaning that \\( M_{12} = M_{21} \\).

So,  by solving Equation :eq:`m12` for the three mutual inductances for a three-loop system, we can analytically solve Equation :eq:`l2` and determine the data \\( \\mathbf{H}^s / \\mathbf{H}^p \\) over different targets, using differing frequencies, loop orientations, and loop separations. This can provide meaningful understanding about three-loop systems (such as the EM-31 and Resolve systems) and their data.

TODO: link to Python app for three-loop system

List of variables:

- `I` = inclination (degrees)
- `D` = declination (degrees)
- `L` = inductance (H)
- `R` = resistance (ohm)
- \\( \\omega \\) = angular frequency: \\( \\omega = 2 \\pi f\\)
- `f` = frequency (Hz)
- \\( \\alpha \\) = inductive response number
- \\(\\mathbf{H}^p\\) = primary magnetic field
- \\(\\mathbf{H}^s\\) = secondary magnetic field
- \\(\\mathbf{A}\\) = vector potential of \\(\\mathbf{B}\\)
- `I` = current (A)
