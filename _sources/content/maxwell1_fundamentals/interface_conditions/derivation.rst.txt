.. _maxwell1_fundamentals_interface_conditions_derivation:

Derivation of Interface Conditions
==================================

Here, we derive the interface conditions for fields :math:`\mathbf{e}` and :math:`\mathbf{h}` as well as for fluxes :math:`\mathbf{j}`, :math:`\mathbf{d}` and :math:`\mathbf{b}` according to Griffiths (:cite:`griffiths1999`). This can be accomplished by using Maxwell's equations in integral form in the time-domain, where:

.. math::
  \oint_S \mathbf{d} \cdot d \mathbf{a} = Q_f
  :label: GaussEint

.. math::
  \oint_S \mathbf{b}\cdot d \mathbf{a} = 0
  :label: GaussMint

.. math::
  \oint_C \mathbf{e} \cdot d\mathbf{l} = - \int_S \frac{\partial \mathbf{b}}{\partial t} \cdot d\mathbf{a}
  :label: FaradayInt

.. math::
  \oint_C \mathbf{h} \cdot d\mathbf{l} = \int_S \bigg ( \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t} \bigg ) \cdot d\mathbf{a}
  :label: AmpMaxInt


Recall that :math:`Q_f` and :math:`\mathbf{j}` are the total enclosed free charge and free current density, respectively. The fields and fluxes are related through the following constitutive relationships:

.. math::
  \mathbf{j} = \sigma \mathbf{e},
  :label: JsigE

.. math::
  \mathbf{d} = \varepsilon \mathbf{e},
  :label: DepsE

.. math::
  \mathbf{b} = \mu \mathbf{h},
  :label: BmuH

where :math:`\sigma` denotes the electric conductivity, :math:`\varepsilon` denotes the dielectric permittivity and :math:`\mu` denotes the magnetic permeability.

Components Normal to the Interface
==================================

Here, we consider components of the fields and fluxes which are normal to the interface.

Electric Displacement
^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/pillbox.png
    :align: right
    :figwidth: 35%
    :name: pillbox

    Gaussian pillbox.

Although it may seem counter-intuitive, we will first derive the interface condition for normal components of the electric displacement. Consider an extremely small Gaussian pillbox of height :math:`h` and cross-sectional area :math:`S_{\text{top}} = \pi r_{\text{top}}^2` (:numref:`pillbox`). By applying Eq. :eq:`GaussEint` to our Gaussian pillbox, we obtain:


.. math::
  \int_0^{2\pi}\int_0^{r_{\text{top}}} d_1^\perp ~drd\theta - \int_0^{2\pi}\int_0^{r_{\text{top}}} d_2^\perp ~ dr d \theta + \int\limits_{-h/2}^{h/2}\int\limits_0^{2\pi} d^\parallel ~ d \theta dz = Q_f

where :math:`d_{1}^\perp` and :math:`d_{2}^\perp` are the components of the electric
displacement normal to the top and bottom of the pillbox, respectively. The radial component (parallel to the interface) is denoted by :math:`d^\parallel`. Since the pillbox is extremely small, we can assume that :math:`d_{1}^\perp` and :math:`d_{2}^\perp` are constant over the top and bottom of the pillbox, respectively. Under this assumption, the previous expression can be simplified to:

.. math::
  d_{1}^\perp S_{\text{top}} - d_{2}^\perp S_{\text{top}} + \int\limits_{-h/2}^{h/2}\int\limits_0^{2\pi} d^\parallel ~ d \theta dz = Q_f.
  :label: eq_d_perp_pillbox

If we take the limit as :math:`h\rightarrow 0` while letting :math:`S_{\text{top}}` remain
fixed, the integral term on the left hand side of Eq. :eq:`eq_d_perp_pillbox` vanishes. Additionally, as the vertical dimension of the pillbox goes to zero, the total enclosed free charge :math:`Q_f` becomes the product of a free surface charge density :math:`\tau_f` and the area of the top of the pillbox; assuming the distribution of surface charges is constant. This results in the following expression:

.. math::
  d_{1}^\perp S_{\text{top}} - d_{2}^\perp S_{\text{top}} = \tau_f S_{\text{top}}

Dividing both sides by the top area of the pillbox, the interface condition for normal components of the electric displacement are given by:

.. math::
  d_{1}^\perp - d_{2}^\perp = \tau_f
  :label: interface_d_n

Thus, the normal component the electric displacement is discontinuous at the interface. Furthermore, the discontinuity is associated with an accumulation of electrical charges.

Electric Field
^^^^^^^^^^^^^^

To obtain the interface condition for normal components of the electric field, we can combine Eqs. :eq:`DepsE` and :eq:`interface_d_n`. Thus:

.. math::
  \varepsilon_1 e_{1}^\perp -\varepsilon_2 e_{2}^\perp = \tau_f
  :label: interface_e_n

Current Density
^^^^^^^^^^^^^^^

To obtain the interface condition for normal components of the electric current density, we can combine Eqs. :eq:`JsigE` and :eq:`interface_e_n`. Thus:

.. math::
  \frac{\varepsilon_1}{\sigma_1} j_{1}^\perp - \frac{\varepsilon_2}{\sigma_2} j_{2}^\perp = \tau_f
  :label:

In the case where there is no difference in dielectric properties across the interface, this equation simplifies to the following:

.. math::
  \frac{j_{1}^\perp}{\sigma_1}  - \frac{j_{2}^\perp}{\sigma_2}  = \frac{\tau_f}{\varepsilon_0}
  :label:

**Special Cases: Steady-State Current**

To examine this case, let us consider the continuity equation for :ref:`conservation of charge<conservation_of_charge>`:

.. math::
  \int_A \mathbf{j} \cdot d\mathbf{a} = -\frac{dQ_f}{dt}
  :label:

In the steady-state, the density of free charge on the interface is static in time. Thus the right hand side of the previous equation is zero. If we use the Gaussian pillbox from :numref:`pillbox` and follow the same arguments used to derive interface conditions for :math:`d^\perp`, we find that:

.. math::
  j_1^\perp = j_2^\perp
  :label:

Thus in the steady state, the normal component of the current density is continuous across the interface. If we let :math:`j_1^\perp = j_2^\perp = j^\perp`, the interface condition for the electric current density in the absence of dielectrics simplifies to:

.. math::
  \bigg ( \frac{1}{\sigma_1}  - \frac{1}{\sigma_2} \bigg ) j^\perp = \big ( \rho_1 - \rho_2 \big ) j^\perp = \frac{\tau_f}{\varepsilon_0}
  :label:

where :math:`\rho = 1/\sigma` is the electric resistivity. Although accumulation of electrical charge is complete in this case, it is important to note that the difference in electrical properties across the interface is responsible for the accumulation of electrical charge.



Magnetic Flux Density
^^^^^^^^^^^^^^^^^^^^^

The interface condition for the normal component of the magnetic flux density is derived from Eq. :eq:`GaussMint`; i.e. Gauss's law for magnetic fields. For this, we may follow the exact same argument used to obtain interface conditions for the electric displacement. However, since the right hand side of Eq. :eq:`GaussMint` is always zero, the interface condition for the normal component of the magnetic flux density is given by:

.. math::
  b_{1}^\perp - b_{2}^\perp = 0
  :label: interface_b_n

Therefore, normal components of the magnetic flux density are continuous across interfaces.

Magnetic Field
^^^^^^^^^^^^^^

To obtain the interface condition for normal components of the magnetic field, we can combine Eqs. :eq:`BmuH` and :eq:`interface_b_n`. Thus:

.. math::
  \mu_1 h_{1}^\perp -\mu_2 h_{2}^\perp = 0


Components Tangential to the Interface
======================================

Here, we consider components of the fields and fluxes which are tangential to the interface.

Electric Field
^^^^^^^^^^^^^^

.. figure:: images/rectangle.png
    :align: right
    :scale: 70%
    :name: rectangle

    Gaussian rectangle.

Although it may seem strange given the previous ordering, we will first derive the interface condition for tangential components of the electric field. Consider a Gaussian rectangle of height :math:`h`, width :math:`l` and area :math:`A` (:numref:`rectangle`). The surface of this rectangle is perpendicular to the interface.

We begin by applying Eq. :eq:`FaradayInt` to our rectangle. Assuming the rectangle is small enough such that the tangential electric field is constant along both horizontal edges, we obtain the following:

.. math::
  \oint_C \!\mathbf{e}\cdot d\mathbf{l} = e_{1}^\parallel \, l - e_{2}^\parallel \, l + \int_{-h/2}^{h/2} e^\perp (x \! =\! -l/2) ~dz - \int_{-h/2}^{h/2} e^\perp (x \! = \! l/2) ~dz = - \!\int_A \frac{\partial \mathbf{b}}{\partial t}\cdot d \mathbf{a}
  :label: eq_e_para_rectangle

where :math:`e_{1}^\parallel` and :math:`e_{2}^\parallel` are the tangential components of the electric field on the top and bottom edges of the Gaussian rectangle, respectively. Normal components of the electric field are denoted by :math:`e^\perp`.

If we take the limit :math:`h \rightarrow 0` while leaving the width :math:`l` fixed, the integrals on the left hand side of Eq. :eq:`eq_e_para_rectangle` go to zero. Additionally, this limit causes the surface area of the rectangle to go to zero, thus the integral on the right hand side of Eq. :eq:`eq_e_para_rectangle` is also zero. Thus:

.. math::
   e_{1}^\parallel \, l - e_{2}^\parallel \, l = 0
   :label:

Dividing the previous equation by :math:`l`, we obtain the interface condition for tangential components of the electric field:

.. math::
  e_{1}^\parallel - e_{2}^\parallel = 0.
  :label: interface_e_t


The tangential component of the electric field is continuous across the
interface. As a result, tangential components of the electric field are not responsible for any build-up of electrical charges at the interface.

Electric Displacement
^^^^^^^^^^^^^^^^^^^^^

To obtain the interface condition for tangential components of the electric displacement, we can combine Eqs. :eq:`DepsE` and :eq:`interface_e_t`. Thus:

.. math::
  \frac{ d_{1}^\parallel}{\varepsilon_1} - \frac{d_{2}^\parallel}{\varepsilon_2} = 0
  :label:

Current Density
^^^^^^^^^^^^^^^

To obtain the interface condition for tangential components of the electric current density, we can combine Eqs. :eq:`JsigE` and :eq:`interface_e_t`. Thus:

.. math::
  \frac{ j_{1}^\parallel}{\sigma_1} - \frac{j_{2}^\parallel}{\sigma_2} = \rho_1 j_1^\parallel - \rho_2 j_2^\parallel = 0
  :label:

where :math:`\rho = \sigma^{-1}` is the electric resistivity.


Magnetic Field
^^^^^^^^^^^^^^

The interface condition for the tangential component of the magnetic field is derived from Eq. :eq:`AmpMaxInt`; i.e. the Ampere-Maxwell equation. Here, we can follow the exact same arguments used to obtain interface conditions for the electric field. In this case however, we must also address the integral term which contains the free current density such that:

.. math::
  I_f = \int_S \mathbf{j} \cdot d \mathbf{a}
  :label:

where :math:`I_f` is the total enclosed free current. By taking the limit :math:`h \rightarrow 0`, the Ampere-Maxwell equation applied to the Gaussian loop becomes:

.. math::
  \oint_C \mathbf{h}\cdot \mathbf{d}\mathbf{l} = h_{1}^\parallel \, l - h_{t}^\parallel \, l = I_f
  :label:

Like the right hand side of Eq. :eq:`eq_e_para_rectangle`, the flux term containing the electric displacement goes to zero as the area of the loop goes to zero. This however, is not the case for the enclosed free current. As :math:`h \rightarrow 0`, there is still free current which flows along the interface. The free surface current is the product of a surface current density :math:`K_f` and the width of the loop; assuming :math:`K_f` is constant along the interface. Thus:

.. math::
  h_{1}^\parallel \, l - h_{2}^\parallel \, l = K_f l
  :label:

Dividing the previous expression by the width of the loop, the interface condition for the tangential component of the magnetic field is given by:

.. math::
  h_{1}^\parallel - h_{t}^\parallel = K_f
  :label: interface_h_t

Therefore, the tangential component of the magnetic field is discontinuous at
the interface. Furthermore, the discontinuity of the magnetic field is related to a free surface current density which flows along the interface.

Magnetic Flux Density
^^^^^^^^^^^^^^^^^^^^^

To obtain the interface condition for tangential components of the magnetic flux density, we can combine Eqs. :eq:`BmuH` and :eq:`interface_h_t`. Thus:

.. math::
  \frac{b_{1}^\parallel}{\mu_1} - \frac{h_{t}^\parallel}{\mu_2} = K_f
  :label:


