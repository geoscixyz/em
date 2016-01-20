.. _interface_conditions:

Interface Conditions
====================

It's important to understand how the electromagnetic fields and fluxes change
at boundaries between media of differing material properties. In this section,
we derive these interface conditions from Maxwell's equations in time domain
integral form. To recap, the equations are

.. math::
  \oint_S \mathbf{d}\cdot \hat{\mathbf{n}}\,da = Q_{\text{enc}},
  :label: GaussEint
  
.. math::
  \oint_S \mathbf{b}\cdot \hat{\mathbf{n}}\,da = 0,
  :label: GaussMint
  
.. include:: ../../equation_bank/faradays_law_int_time.rst

.. math::
   \oint_C \mathbf{h} \cdot \mathbf{dl} = I_{\text{enc}} + \int_S \frac{\partial\mathbf{d}}{\partial t} \cdot \hat{\mathbf{n}} \, da.
  :label: AmpMaxInt


Recall also that :math:`\mathbf{d}` and :math:`\mathbf{h}` are related to
:math:`\mathbf{e}` and :math:`\mathbf{b}`, respectively, through constitutive
relations. Assuming linear isotropic media, the constitutive relations are

.. math::
	\mathbf{d} = \varepsilon \mathbf{e},
	:label: DepsE

.. math::
	\mathbf{b} = \mu \mathbf{h},
	:label: BmuH

where :math:`\varepsilon` denotes the dielectric permittivity and :math:`\mu` denotes the magnetic permeability.

In the following derivations, we consider a two layer medium where each layer
has its corresponding physical properties. In this page, the subindices 1 and
2 denote dependency on layer 1 and layer 2, respectively. This is illustrated
in :numref:`twoLayerMedium`. Our derivations follow those presented by
Griffiths (c.f.  :cite:`griffiths1999`).

.. figure:: images/twoLayerMedium.png
    :align: center
    :name: twoLayerMedium

    Two layered medium. 


.. [#f1]_ comment out footnote to patch pdf



Normal Component of Electric Displacement
-----------------------------------------

.. figure:: images/pillbox.png
    :align: right
    :scale: 70% 
    :name: pillbox

    Gaussian pillbox. 

.. [#f1]_ comment out footnote to patch pdf


Consider an extremely small Gaussian pillbox of height :math:`h` and cross-
sectional area :math:`S_{\text{top}} = \pi r_{\text{top}}^2`. The pillbox is
shown in :numref:`pillbox`. To derive the interface condition on the normal
component of the electric displacement, denoted as :math:`d_{n}`, we apply
Gauss's law formulated in terms of electric displacement :eq:`GaussEint` to
the pillbox, yielding to


.. math::
  \int_0^{2\pi}\int_0^{r_{\text{top}}} d_{1n} ~drd\theta - \int_0^{2\pi}\int_0^{r_{\text{top}}} d_{2n} ~ dr d \theta + \int\limits_{-h/2}^{h/2}\int\limits_0^{2\pi} d_r~ d \theta dz = Q_{\text{enc}},

where :math:`d_{1n}` and :math:`d_{2n}` are the components of the electric
displacement normal to the top and bottom of the pillbox, respectively, and
:math:`d_r` is the radial component. Since the pillbox is extremely small, we
can assume :math:`d_{1n}` and :math:`d_{2n}` to be constant over the top and
bottom of the pillbox, respectively. Thus, evaluating the first two integrals
in the last equation yields

.. math::
  d_{1n} S_{\text{top}} - d_{2n} S_{\text{top}} + \int\limits_{-h/2}^{h/2}\int\limits_0^{2\pi} d_r~ d \theta dz = Q_{\text{enc}}.

In the limit, when :math:`h` approaches 0 while :math:`S_{\text{top}}` remains
constant, the integral remaining on the left hand side vanishes and the charge
enclosed (i.e. :math:`Q_{\text{enc}}`) can be represented by the free surface
charge density :math:`\tau_f` (assumed constant over the pillbox) times the
area of the top of the pillbox. This gives the expression

.. math::
  d_{1n} S_{\text{top}} - d_{2n} S_{\text{top}} = \tau_f S_{\text{top}},

which yields the interface condition on the normal component of
:math:`\mathbf{d}`

.. math::
  d_{1n} - d_{2n} = \tau_f.
  
That is, the normal component the electric displacement is discontinuous at
the interface.  If the medium is linear and isotropic, the condition can be
written in terms of the electric field as

.. math::
  \varepsilon_1 e_{1n} -\varepsilon_2 e_{2n} = \tau_f.

Normal Component of Magnetic Flux
-----------------------------------------

The interface condition on the normal component of the magnetic flux, denoted
as :math:`b_{n}`, is derived from the integral form of Gauss's law for the
magnetic flux :eq:`GaussMint`. We follow the exact argument as for the
electric displacement, see previous section. However, since the right hand
side of :ref:`Gauss's law<gauss_magnetic>` is always zero, the interface
condition on the normal magnetic flux is given by

.. math::
  b_{1n} - b_{2n} = 0.
  

That is, the normal component of the magnetic flux is continuous at the
interface.

Tangential Component of the Electric Field
------------------------------------------

.. figure:: images/rectangle.png
    :align: right
    :scale: 70% 
    :name: rectangle

    Gaussian rectangle. 

.. [#f1]_ comment out footnote to patch pdf

The interface condition on the tangential component of the electric field,
denoted as :math:`e_{t}`, is derived from :ref:`Faraday's law<faraday>` in
integral form :eq:`faradays_law_int_time`. Consider Faraday's law applied to
the extremely small rectangle of height :math:`h`, width :math:`l` and area
:math:`A` shown in :numref:`rectangle`, with surface normal parallel to the
interface. As with the Gaussian pillbox in the electric displacement
derivation, we assume the rectangle to be small enough that the tangential
electric field is constant on both horizontal edges. This allows us to
evaluate the components of the contour integral on the top and bottom edges of
the rectangle, giving

.. math::
  \oint_C \mathbf{e}\cdot \mathbf {d}\mathbf{l} = e_{1t}l - e_{2t}l + \int_{-h/2}^{h/2} e_n(x=-l/2) ~dz - \int_{-h/2}^{h/2} e_n(x=+l/2) ~dz = -\int_A \frac{\partial \mathbf{b}}{\partial t}\cdot \hat{\mathbf{n}}\,da,

where :math:`e_{1t}` and :math:`e_{2t}` are the tangential components of the
electric field on the top and bottom edges of the Gaussian rectangle,
respectively, and :math:`e_n` is the normal component of :math:`\mathbf{e}`.

In the limit as :math:`h` approaches 0 while holding :math:`l` constant, the
remaining integral terms vanish, leaving

.. math::
   e_{1t}l - e_{2t}l = 0.

Dividing by :math:`l` the previous expression yields the interface condition

.. math::
  e_{1t} - e_{2t} = 0.


That is, the tangential component of the electric field is continuous at the
interface.

Tangential Component of the Magnetic Field
------------------------------------------

The interface condition on the tangential component of the magnetic field,
denoted as :math:`h_t`, is derived from the integral form of the :ref:`Ampere-
Maxwell equation<ampere_maxwell>` :eq:`AmpMaxInt` applied to the same Gaussian
rectangle as for the tangential electric field (:numref:`rectangle`). Using
the same reasoning as for the tangential electric field (see previous
section), we have

.. math::
  \oint_C \mathbf{h}\cdot \mathbf{d}\mathbf{l} = h_{1t}l - h_{2t}l = I_{\text{enclosed}}.

In the limit, when the height of the Gaussian rectangle approaches zero, the
current enclosed by the rectangle, :math:`I_{\text{enclosed}}`, can be
represented as a surface current density on the interface
:math:`j_{\text{surf}}` times the width of the rectangle :math:`l`. This gives

.. math::
  h_{1t}l - h_{2t}l = j_{\text{surf}} l.

The above expression yields the interface condition on the tangential
component of the magnetic field

.. math::
  h_{1t}- h_{2t} = j_{\text{surf}}.
  
That is, the tangential component of the magnetic field is discontinuous at
the interface.


.. .. rubric:: Footnotes
.. .. [#f1] Figures were created by `Luz`_ and are licenced under `CC BY 2.0`_

.. note::
  Figures were created by `Luz`_ and are licenced under `CC BY 2.0`_

.. _Luz: https://luzcaudillo.wordpress.com/

.. _CC BY 2.0: http://creativecommons.org/licenses/by/2.0/


