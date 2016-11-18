.. _frequency_domain_electric_dipole_analytic_solution:

Analytic Solution
=================

.. Purpose::

    Here, Maxwell's equations are solved for a harmonic electrical current dipole source.
    This is accomplished by using the method of Schelkunoff potentials, as shown in Ward and Hohmann (:cite:`ward1988`).
    Analytic expressions for the electric field, the magnetic field and the corresponding vector potential are provided.
    :ref:`Numerical modeling tools<frequency_domain_electric_dipole_fields>` for visualizing the fields are provided after the :ref:`asymptotics<frequency_domain_electric_dipole_asymptotics>` section.



For an electrical current source (:math:`\mathbf{J_e^s}`), Maxwell's equations in the frequency domain are given by:

.. math::
	\nabla \times \mathbf{E_e} + i\omega \mu \mathbf{H_e} = 0 
	:label: Faraday_e
.. math::
	\nabla \times \mathbf{H_e} - (\sigma + i\omega \varepsilon) \mathbf{E_e} = \mathbf{J}_e^s 
	:label: Ampere_e

where subscripts :math:`_e` remind us that we are considering an electric source. 
For an electrical current source (:math:`\mathbf{J_e^s}`), the electric and magnetic fields can be expressed in terms of the Schelkunoff vector potential (:math:`\mathbf{A}`), where:
	
.. math::
	\mathbf{H_e} \equiv \nabla \times \mathbf{A} 
	:label: H_A_potential

and

.. math::
	\mathbf{E}_e = -i\omega\mu\mathbf{A} + \frac{1}{(\sigma + i\omega\varepsilon)} \nabla (\nabla \cdot \mathbf{A})
	:label: E_A_potential


Eq. :eq:`H_A_potential` can be obtained simply by taking the divergence of Eq. :eq:`Faraday_e`.
Eq. :eq:`E_A_potential` is obtained by manipulating Eqs. :eq:`Faraday_e`, :eq:`Ampere_e` and :eq:`H_A_potential`, and choosing an appropriate Gauge.
We can see from Eqs. :eq:`H_A_potential` and :eq:`E_A_potential` that :math:`\mathbf{A}` contains all the information corresponding to the electric and magnetic fields.
Therefore, Maxwell's equations will be manipulated to solve for :math:`\mathbf{A}`; which can then be used to obtain :math:`\mathbf{E_e}` and :math:`\mathbf{H_e}`. 

By manipulating Eqs. :eq:`Faraday_e`, :eq:`Ampere_e` and :eq:`H_A_potential` and choosing an appropriate Gauge, we find that :math:`\mathbf{A}` can be expressed using the Helmholtz equation:

.. math::
	\nabla^2 \mathbf{A} + k^2 \mathbf{A} = - \mathbf{J}_e^s, \  \  \  \  \text{where} \  \  k^2 = \omega^2\mu\epsilon -i\omega\mu\sigma
	:label: Helmholtz_A 

The Helmholtz equation with boundary conditions can be solved to generate :math:`\mathbf{A}`. 
For infinite media, the boundary condition is such that :math:`\mathbf{A} \rightarrow 0` as :math:`r \rightarrow \infty`.
From the Helmholtz equation, we can see that :math:`\mathbf{A}` will only have a component along the direction of :math:`\mathbf{J_e^s}`.
The scalar Green's function for the Helmholtz equation is:

.. math::
	G(r) = \frac{e^{-ikr}}{4\pi r}.
	:label: GreensFncFullSpace

and hence the vector potential for an arbitrary electric current source is:

.. math::
	\mathbf{A}(\mathbf{r}) = \int_v \frac{e^{-ik|\mathbf{r}-\mathbf{r}'|}}{4\pi |\mathbf{r}-\mathbf{r}'|} \mathbf{J_e^s}(\mathbf{r}') dv
	:label: A_Potential

where :math:`\mathbf{r}` is the observation location and :math:`\mathbf{r^\prime}` refers to locations within the source region.
For an electric current dipole oriented in the :math:`\hat{x}` direction, the source term is given by:

.. math::
	\mathbf{J_e^s} = \hat{x} I ds \delta(x) \delta(y) \delta(z)
	:label: Je_x

and the solution to Eq. :eq:`A_Potential` is:

.. math::
	\mathbf{A (r)} = \frac{I ds}{4\pi r} e^{-ikr} \hat{x}
	:label: A_Potential_for_Je_x


Recall the :math:`\mathbf{A}` can be used to obtain the electric and magnetic field according to Eqs. :eq:`H_A_potential` and :eq:`E_A_potential`.
Thus the electric field for an electrical current dipole in the :math:`\hat x` direction is:

.. math::
	\mathbf{E_e (r)} = \frac{I ds}{4 \pi (\sigma + i \omega \varepsilon)} \left[ \left( k^2 + \frac{\partial^2}{\partial x^2} \right) \hat{x} + \frac{\partial^2}{\partial x \partial y} \hat{y} + \frac{\partial^2}{\partial x \partial z} \hat{z} \right] \frac{e^{-ikr}}{r}

which is equal to:

.. math::
	\begin{split}
	\mathbf{E_e (r)} = \frac{I ds}{4 \pi (\sigma + i \omega \varepsilon) r^3} e^{-ikr} \Bigg [ \Bigg ( \frac{x^2}{r^2} \hat{x} + & \frac{xy}{r^2} \hat{y} + \frac{xz}{r^2} \hat{z} \Bigg ) ... \\
	&\big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 - ikr -1 \big ) \hat{x} \Bigg ] .
	\end{split}
	:label: E_Cartesian

The magnetic field is:

.. math::
	\mathbf{H_e (r)} = \frac{I ds}{4 \pi} \left[ \frac{\partial}{\partial z} \hat{y} - \frac{\partial}{\partial y} \hat{z} \right] \frac{e^{-ikr}}{r}

which is equal to:

.. math::
	\mathbf{H_e (r)} = \frac{I ds}{4 \pi r^2} \left( ikr + 1 \right) e^{-ikr} \left( -\frac{z}{r} \hat{y} + \frac{y}{r} \hat{z} \right) .
	:label: H_Cartesian


On the following page, we show how Eqs. :eq:`E_Cartesian` and :eq:`H_Cartesian` can be simplified for various cases.


