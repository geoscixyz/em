.. _frequency_domain_magnetic_dipole_analytic_solution:

Analytic Solution
=================

.. topic:: Purpose

    Here, Maxwell's equations are solved for a harmonic magnetic dipole source.
    This is accomplished by using the method of Schelkunoff potentials, as shown in Ward and Hohmann (:cite:`ward1988`).
    Analytic expressions for the electric field, the magnetic field and the corresponding vector potential are provided.
    



For a magnetic source (:math:`\mathbf{J_m^s}`), Maxwell's equations in the frequency domain are given by:


.. math::
	\nabla \times \mathbf{E_m} + i\omega \mu \mathbf{H_m} = - \mathbf{J_m^s} 
	:label: Faraday_m
.. math::
	\nabla \times \mathbf{H_m} - (\sigma + i\omega \epsilon) \mathbf{E_m} = 0
	:label: Ampere_m

where the subscripts :math:`_m` remind us that we are using a magnetic source.
For a magnetic source (:math:`\mathbf{J_m^s}`), the electric and magnetic fields can be expressed in terms of the Schelkunoff vector potential, where:

.. math::
	\mathbf{H}_m = -(\sigma + i \omega \epsilon) \mathbf{F} + \frac{1}{(i \omega \mu)} \nabla (\nabla \cdot \mathbf{F})
	:label: H_F_potential


and

.. math::
	\mathbf{E}_m = - \nabla \times \mathbf{F}
	:label: E_F_potential


Eq. :eq:`E_F_potential` can be obtained simply by taking the divergence of Eq. :eq:`Ampere_m`.
Eq. :eq:`H_F_potential` is obtained by manipulating Eqs. :eq:`Faraday_m`, :eq:`Ampere_m` and :eq:`E_F_potential`, and choosing an appropriate Gauge.
We can see from Eqs. :eq:`H_F_potential` and :eq:`E_F_potential` that :math:`\mathbf{F}` contains all the information corresponding to the electric and magnetic fields.
Therefore, Maxwell's equations will be manipulated to solve for :math:`\mathbf{F}`; which can then be used to obtain :math:`\mathbf{E_m}` and :math:`\mathbf{H_m}`. 

By manipulating Eqs. :eq:`Faraday_m`, :eq:`Ampere_m` and :eq:`E_F_potential` and choosing an appropriate Gauge, we find that :math:`\mathbf{F}` can be expressed using the Helmholtz equation:


.. math::
	\nabla^2 \mathbf{F} + k^2 \mathbf{F} = - \mathbf{J}_m^s, \  \  \  \  \text{where} \  \  k^2 = \omega^2\mu\epsilon -i\omega\mu\sigma
	:label: Helmholtz_F 

The Helmholtz equation with boundary conditions can be solved to generate :math:`\mathbf{F}`. 
For infinite media, the boundary condition is such that :math:`\mathbf{F} \rightarrow 0` as :math:`r \rightarrow \infty`.
From the Helmholtz equation, we can see that :math:`\mathbf{F}` will only have a component along the direction of :math:`\mathbf{J_m^s}`.
The scalar Green's function for the Helmholtz equation is:


.. math::
	G(r) = \frac{e^{-ikr}}{4\pi r}.
	:label: GreensFncFullSpace

and hence the vector potential for an arbitrary magnetic source isL

.. math::
	\mathbf{F}(\mathbf{r}) = \int_v \frac{e^{-ik|\mathbf{r}-\mathbf{r}'|}}{4\pi |\mathbf{r}-\mathbf{r}'|} \mathbf{J}_m(\mathbf{r}') dv
	:label: F_Potential

For a magnetic dipole oriented in the :math:`\hat{x}` direction, the source term is given by:


.. math::
	\mathbf{J}_m(\mathbf{r}) = i \omega \mu I S \delta(x) \delta(y) \delta(z) \hat{x}
	:label: Jm_x


and the solution to Eq. :eq:`F_Potential` is:

.. math::
	\mathbf{F}(\mathbf{r}) = \frac{i \omega \mu m}{4\pi r} e^{-ikr} \hat{x}
	:label: F_Potential_for_Jm_x


Recall the :math:`\mathbf{F}` can be used to obtain the electric and magnetic field according to Eqs. :eq:`H_F_potential` and :eq:`E_F_potential`.
Thus the electric field for an electrical current dipole in the :math:`\hat x` direction is:

.. math::
	\mathbf{E}_m = \frac{i \omega \mu m}{4 \pi r^2} \left( ikr + 1 \right) e^{-ikr} \left( -\frac{z}{r} \hat{y} + \frac{y}{r} \hat{z} \right).
	:label: Em_Cartesian


While the magnetic field is given by:

.. math::
	\mathbf{H}_m = \frac{m}{4 \pi r^3} e^{-ikr} \left[ \left(\frac{x^2}{r^2} \hat{x} + \frac{xy}{r^2} \hat{y} + \frac{xz}{r^2} \hat{z} \right) \left(-k^2 r^2 + 3ikr +3 \right) + \left(k^2 r^2 - ikr -1 \right) \hat{x} \right].
	:label: Hm_Cartesian

On the following page, we show how Eqs. :eq:`Em_Cartesian` and :eq:`Hm_Cartesian` can be simplified for various cases.




