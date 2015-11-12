.. _boundary_conditions:

Boundary Conditions
===================

It's important to understand how the electromagnetic fields and fluxes change at boundaries between media of differing material properties. In this section, we derive these boundary, or interface, conditions from Maxwell's equations in time domain integral form. To recap, the equations are

.. math::
  \oint_A \mathbf{d}\cdot \hat{\mathbf{n}}\,da = Q_{\text{enc}},
  :label: GaussEint
  
.. math::
  \oint_A \mathbf{b}\cdot \hat{\mathbf{n}}\,da = 0,
  :label: GaussMint
  
.. include:: ../../equation_bank/faradays_law_int_time.rst

.. math::
   \oint_C \mathbf{h} \cdot \mathbf{dl} = I_{\text{enc}} + \int_S \frac{\partial\mathbf{d}}{\partial t} \cdot \hat{\mathbf{n}} ~\text{ds},
  :label: AmpMaxInt

where :math:`{\bf b,d,e,h}` are the electromagnetic fields and fluxes, :math:`Q_{\text{enc}}` denotes {ADD THIS}, and :math:`I_{\text{enc}}` denotes {ADD THIS}. 	

Recall also that :math:`\mathbf{d}` and :math:`\mathbf{h}` are related to :math:`\mathbf{e}` and :math:`\mathbf{b}`, respectively, through constitutive relations. Assuming linear isotropic media, the constitutive relations are

.. math::
	\mathbf{d} = \varepsilon \mathbf{e},
	:label: DepsE

.. math::
	\mathbf{b} = \mu \mathbf{h},
	:label: BmuH

where :math:`\varepsilon` denotes the dielectric permittivity and :math:`\mu` denotes the magnetic permeability.

In the following derivations, we consider a two layer medium where each layer has its corresponding physical properties. The subindices 1 and 2 denote dependency on layer 1 and layer 2, respectively. We also make use of a rectangular surface and a Gaussian pillbox that straddle the boundary.  This is illustrated in Figure 1. 

.. figure:: images/BC_1.png
	:align: center

Fig 1.  Two layer medium. Orange rectangle is an open surface with area A, bounded by the curve C. Green pillbox has volume V, bounded by the surface S. 

Normal Component of Electric Displacement
-----------------------------------------

To derive the boundary condition on the normal component of electric displacement, denoted as :math:`\mathbf{d}_{n}`, we apply Gauss's law formulated in terms of :math:`\mathbf{d}` to the Gaussian pillbox in Figure 1. Consider a pillbox of height h and cross-sectional area :math:`A`, small enough that :math:`\mathbf{d}` is constant across the top and bottom. The integral is then 

.. math::
  \mathbf{d}_{1n} A - \mathbf{d}_{2n} A + \int\limits_{-h/2}^{h/2}\int\limits_0^{2\pi} \mathbf{d}_r~ \mathrm{d}\theta\mathrm{d}z = Q_{\text{enc}},

where :math:`\mathbf{d}_{1n}` and :math:`\mathbf{d}_{2n}` are the components of the electric displacement normal to the top and bottom of the pillbox, and :math:`\mathbf{d}_r` is the radial component. In the limit, when :math:`h` approaches 0 while :math:`A` remains constant, the integral remaining on the left hand side vanish and the charge enclosed can be represented by the free surface charge density :math:`I_f` (assumed constant over the pillbox) times the area of the top of the pillbox. This gives the expression

.. math::
  \mathbf{d}_{1n} A - \mathbf{d}_{2n} A = I_f A,

which yields the interface condition on the normal component of :math:`\mathbf{d}`

.. math::
  \mathbf{d}_{1n} - \mathbf{d}_{2n} = I_f.
  
If the medium is linear and isotropic, the condition can be written in terms of the electric field as

.. math::
  \varepsilon_1 \mathbf{e}_{1n} -\varepsilon_2 \mathbf{e}_{2n} = I_f.

Normal Component of Magnetic Flux
-----------------------------------------

The interface condition on the normal component of the magnetic flux, denoted as :math:`\mathbf{b}_{n}`, is derived from the integral form of Gauss's law for the magnetic flux. We follow the exact argument as for the electric displacement, see previous section. However, since the right hand side of :ref:`Gauss's law<gauss_magnetic>` is always zero, we have the interface condition on the normal magnetic flux

.. math::
  \mathbf{b}_{1n} - \mathbf{b}_{2n} = \mathbf{0}.
  
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