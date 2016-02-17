.. _fundamental_laws_details:

Details
=======


.. _gauss_electric_equivalence_to_coulombs_law:

Equivalence of Gauss' Law for Electric Fields to Coulomb's Law
**************************************************************
 
 .. figure:: images/CoulombsLaw.png
    :align: right
    :scale: 75% 
    :name: CoulombsLaw

    Electric force

Coulomb's law is often one of the first quantitative laws encountered by
students of electromagnetism. It describes the force between two point
electric charges. It turns out that it is equivalent to Gauss's law. Coulomb's
law states that the force between two static point electric charges is
proportional to the inverse square of the distance between them, acting in the
direction of a line connecting them. If the charges are of opposite sign, the
force is attractive and if the charges are of the same sign, the force is
repulsive. Mathematically, Coulomb's law is written as


.. math::
  \mathbf{F} = \frac{qQ}{4\pi \varepsilon_0 |\mathbf{r} - \mathbf{r'}|^2}~\mathbf{\hat{\underline{r}}} \;,
  :label: Coulomb_q

where :math:`\mathbf{F}` is the force between the two charges :math:`q` and :math:`Q`, :math:`|\mathbf{r} - \mathbf{r'}|` is the distance between the charges and :math:`\mathbf{\hat{\underline{r}}}` is a unit vector in the direction of the line separating the two charges.

Having defined Coulomb's law, one might next naturally ask the question how
would a standard reference charge behave in the presence of any distribution
of electric charge we might dream up? Answering this question brings us to the
concept of the electric field. We follow the presentation of :cite:`griffiths1999`. We can
define the electric field of an arbitrary charge :math:`Q` as the force
experienced by a unit charge :math:`q` due to :math:`Q`

.. math::
       \mathbf{e} = \frac{\mathbf{F}}{q}.
       :label: Force_per_q

Dividing both sides of Coulomb's law by :math:`q` and substituting the
definition of :math:`\mathbf{e}`, we get that the electric field of a point
charge :math:`Q` is

.. math::
      \mathbf{e}(\mathbf{r}) = \frac{Q}{4\pi\varepsilon_0 |\mathbf{r} - \mathbf{r'}|^2}~\mathbf{\hat{\underline{r}}}\;.
      :label: e_charge_q

It is important to note here that the electric field obeys the principle of
superposition, meaning that the electric field of an arbitrary collection of
point charges is equal to the sum of the electric fields due to each
individual charge.

.. math::
   \mathbf{e}\left(\sum_{k=1,n} Q_i\right) = \sum_{k=1,n} \mathbf{e}(Q_i)
   :label:

If we consider the the electric field due to a spatially extended body with
charge density :math:`\rho`, the sum becomes an integral over infinitesimal
volume elements of the body

.. math::
  \mathbf{e} = \frac{1}{4\pi\varepsilon_0}\int_V \frac{\rho}{|\mathbf{r} - \mathbf{r'}|^2}\;~\mathbf{\hat{\underline{r}}}\;\mathrm{d}v,
  :label: e_charge_den

where :math:`|\mathbf{r} - \mathbf{r'}|` is now the distance from a point in
the charged body to the point at which the electric field is to be evaluated.
The integral is over the charged body.

We can show that :eq:`e_charge_den` is equivalent to Gauss's Law directly from
the definition of divergence,

.. math::
  \boldsymbol{\nabla} \cdot \mathbf{e} = \underset{\Delta V \rightarrow 0}{lim} ~\frac{1}{\Delta V} \oint_{S} \mathbf{e}~da,
  
where the integral is over :math:`S`, the closed surface bounding the volume
:math:`\Delta V`. Applying this definition to the electric field of a point
charge :math:`q` at the origin gives

.. math::
   \boldsymbol{\nabla} \cdot \mathbf{e} = \underset{\Delta V \rightarrow 0}{lim} \left[ \frac{1}{\Delta V}\frac{q}{4\pi\varepsilon_0 |\mathbf{r} - \mathbf{r'}|^2} \oint_{S} ~da \right].

Taking :math:`\Delta V` as a closed sphere of radius :math:`|\mathbf{r} -
\mathbf{r'}|` centered at the origin, we can easily evaluate the integral,
giving
   
.. math::
  \boldsymbol{\nabla} \cdot \mathbf{e} &=  \underset{\Delta V \rightarrow 0}{lim} \left[ \frac{1}{\Delta V} \frac{4 \pi |\mathbf{r} - \mathbf{r'}|^2\;q }{4\pi\varepsilon_0 |\mathbf{r} - \mathbf{r'}|^2} \right ] 
  
  ~ &=  \underset{\Delta V \rightarrow 0}{lim} \left[ \frac{1}{\Delta V} \frac{q}{\varepsilon_0} \right ]. 

In the limit :math:`\Delta V \rightarrow 0`, :math:`\frac{q}{\Delta V}` is
simply the charge density :math:`\rho`. This establishes the desired result

.. math::
   \boldsymbol{\nabla} \cdot \mathbf{e} = \frac{\rho}{\varepsilon_0}.

For a more detailed discussion, see page 36 of :cite:`fleisch2008`. For an alternate
derivation and discussion, see pages 65-70 of :cite:`griffiths1999`.