.. _boundary_conditions:

Boundary Conditions
===================

It's important to understand how the electromagnetic fields change at boundaries between media of differing material properties. We will derive these boundary, or interface, conditions from Maxwell's equations in time domain integral form. To recap, the equations are

.. math::
  \oint_A \mathbf{d}\cdot \hat{\mathbf{n}}\,da = Q_{\text{enc}}
  :label: GaussEint
  
.. math::
  \oint_A \mathbf{b}\cdot \hat{\mathbf{n}}\,da = 0
  :label: GaussMint
  
.. include:: ../../equation_bank/faradays_law_int_time.rst

.. math::
   \oint_C \mathbf{h} \cdot \mathbf{dl} = I_{enc} + \int_S \frac{\partial\mathbf{d}}{\partial t} \cdot \hat{\mathbf{n}} ~\text{ds}.
  :label: AmpMaxInt
	
Recall also that :math:`\mathbf{D}` and :math:`\mathbf{H}` are related to :math:`\mathbf{E}` and :math:`\mathbf{B}`, respectively, through constitutive relations. Assuming linear isotropic media, the constitutive relations are

.. math::
	\mathbf{d} = \varepsilon \mathbf{e},
	:label: DepsE

.. math::
	\mathbf{b} = \mu \mathbf{h},
	:label: BmuH

where :math:`\varepsilon` and :math:`\mu` are called, respectively, the dielectric permittivity and the magnetic permeability.

In the following derivations we will consider a two layer medium where each layer has its corresponding physical properties. The subindices 1 and 2 denote dependency on layer 1 and layer 2, respectively. We will also make use of a rectangular surface and Gaussian pill-box that straddle the boundary.

.. figure:: images/BC_1.png
	:align: center

Fig 1.  Two layer media. Orange rectangle is an open surface with area A, bounded by the curve C. Green pillbox has volume V. 

Normal Component of Electric Displacement
-----------------------------------------

We derive the boundary condition on the normal component of electric displacement :math:`\mathbf{d}` using Gauss's law formulated in terms of :math:`\mathbf{d}`, applied to the Gaussian pillbox in figure 1. Consider a pillbox of height h and cross-sectional area :math:`A`, small enough that :math:`\mathbf{d}` is constant across the top and bottom. The integral is then 

.. math::
  d_{1n} A - d_{2n} A + \int\limits_{-h/2}^{h/2}\int\limits_0^{2\pi} d_r~ \mathrm{d}\theta\mathrm{d}z = Q_{\text{enc}}

where :math:`d_{1n}` and :math:`d_{2n}` are the components of the electric displacement normal to the top and bottom of the pillbox and :math:`d_r` is the radial component. In the limit that :math:`h` approaches 0 while :math:`A` remains constant, the integral remaining on the left hand side becomes zero and the charge enclosed can be represented by the free surface charge density :math:`\tau_f` (assumed constant over the pillbox) times the area of the top of the pillbox. This gives the expression

.. math::
  d_{1n} A - d_{2n} A = \tau_f A.

Cancelling the :math:`A` terms gives the interface condition on the normal component of :math:`\mathbf{d}`

.. math::
  d_{1n} - d_{2n} = \tau_f.
  
If the medium is linear and isotropic, the condition can be written in terms of the electric field as

.. math::
  \varepsilon_1 e_{1n} -\varepsilon_2 e_{2n} = \tau_f.

Normal Component of Magnetic Flux
-----------------------------------------

The interface condition on the normal component of the magnetic flux is derived from the integral form of Gauss's law for the magnetic flux. We follow the exact argument as for the electric displacement. However, since the right hand side of Gauss's law for magnetic flux is always zero, we have the interface condition on the normal magnetic flux

.. math::
  b_{1n} - b_{2n} = 0.
  
Tangential Component of the Electric Field
------------------------------------------

The interface condition on the tangential component of the electric field is derived from Faraday's law in integral form. Consider Faraday's law applied to the rectangle of height :math:`h` and width :math:`l` shown in figure 1, with surface normal parallel to the interface. As with the Gaussian pillbox in the electric displacement derivation, we assume the rectangle to be small enough that the tangential electric field is constant on both horizontal edges. Then, we take the limit as :math:`h` approaches 0 while holding :math:`l` constant, which means the contour integral in Faraday's law becomes

.. math::
  \oint_C \mathbf{e}\cdot d\mathbf{l} = e_{1t}l - e_{2t}l,

where :math:`e_{1t}` and :math:`e_{2t}` are the tangential components of the electric field on the top and bottom edges of the Gaussian rectangle, respectively. Taking :math:`h` to 0 also causes the surface integral on the right hand side of Faraday's law to vanish, implying the interface condition

.. math::
  e_{1t} - e_{2t} = 0.

Tangential Component of the Magnetic Field
------------------------------------------

The interface condition on the tangential component of the magnetic field is derived from the integral form of the Ampere-Maxwell equation applied to the same Gaussian rectangle as for the tangential electric field. Using the same reasoning as for the electric field, we have

.. math::
  \oint_C \mathbf{h}\cdot d\mathbf{l} = h_{1t}l - h_{2t}l.

In the limit that the height of the Gaussian rectangle approaches zero, the electric displacement integral term vanishes and the current enclosed by the rectangle can be represented as a surface current density on the interface :math:`\kappa` times the width of the rectangle :math:`l`. This gives

.. math::
  h_{1t}l - h_{2t}l = \kappa l

Cancelling the :math:`l` terms yields the interface condition on the tangential magnetic field

.. math::
  h_{1t}- h_{2t} = \kappa.