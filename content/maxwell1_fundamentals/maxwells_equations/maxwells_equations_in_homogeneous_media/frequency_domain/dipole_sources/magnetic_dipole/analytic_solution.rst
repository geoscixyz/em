.. _frequency_domain_magnetic_dipole_analytic_solution:

Analytic Solution
=================

.. topic:: Purpose

    Purpose here


The magnetic dipole is a current flowing in a infinitesimal loop. It is convenient to solve the problem in terms of Schelkunoff potentials as done in :cite:`ward1988`. To summarize, for an magnetic current source (:math:`\mathbf{J_m^s}`), Maxwell's equations in frequency are

.. math::
	\nabla \times \mathbf{E_m} + i\omega \mu \mathbf{H_m} + \mathbf{J_m^s} = 0 
	:label: Faraday_m
.. math::
	\nabla \times \mathbf{H_m} - (\sigma + i\omega \epsilon) \mathbf{E_m} = 0
	:label: Ampere_m

where the subscripts :math:`_m` remind us that we are using a magnetic source. Taking the divergence of :eq:`Ampere_m` allows us to define :math:`\mathbf{E_m}` as the curl of a vector potential (:math:`\mathbf{F}`). 

.. math::
	\mathbf{E_m} \equiv - \nabla \times \mathbf{F} 
	:label: F_def

After some manipulation of :eq:`Faraday_m` using Lorentz conditions, we obtain the Helmholtz equation for :math:`\mathbf{F}`.

.. math::
	\nabla^2 \mathbf{F} + k^2 \mathbf{F} = - \mathbf{J}_m^s, \  \  \  \  \text{where} \  \  k^2 = \omega^2\mu\epsilon -i\omega\mu\sigma
	:label: Helmholtz_F 

The equation with boundary conditions , is solved to generate :math:`\mathbf{F}`. For infinite media, the boundary condition is that :math:`\mathbf{F} \rightarrow 0` as :math:`r \rightarrow \infty`.

If :math:`\mathbf{J_m^s}` has only a single component, the field :math:`\mathbf{F}` only has a component in that direction. The scalar Green's function for :eq:`Helmholtz_F` is

.. math::
	G(r) = \frac{e^{-ikr}}{4\pi r}.
	:label: GreensFncFullSpace

and hence the vector potential for an arbitrary magnetic current source is 

.. math::
	\mathbf{F}(\mathbf{r}) = \int_v \frac{e^{-ik|\mathbf{r}-\mathbf{r}'|}}{4\pi |\mathbf{r}-\mathbf{r}'|} \mathbf{J}_m(\mathbf{r}') dv
	:label: F_Potential

For an magnetic current dipole oriented in the :math:`\hat{x}` direction

.. math::
	\mathbf{J}_m(\mathbf{r}) = i \omega \mu I S \delta(x) \delta(y) \delta(z) \hat{x}
	:label: Jm_x

and 

.. math::
	\mathbf{F}(\mathbf{r}) = \frac{i \omega \mu m}{4\pi r} e^{-ikr} \hat{x}
	:label: F_Potential_for_Jm_x


The magnetic and electric fields expressed in terms of :math:`\mathbf{F}` are

.. math::
	\mathbf{H}_m = -(\sigma + i \omega \epsilon) \mathbf{F} + \frac{1}{(i \omega \mu)} \nabla (\nabla \cdot \mathbf{F})
	:label: Fields_fncF

	\mathbf{E}_m = - \nabla \times \mathbf{F}
	
In component form the magnetic field is given by

.. math::
	\mathbf{H}_m = \frac{m}{4 \pi r^3} e^{-ikr} \left[ \left(\frac{x^2}{r^2} \hat{x} + \frac{xy}{r^2} \hat{y} + \frac{xz}{r^2} \hat{z} \right) \left(-k^2 r^2 + 3ikr +3 \right) + \left(k^2 r^2 - ikr -1 \right) \hat{x} \right].
	:label: Hm_Cartesian

While the electric field is equal to

.. math::
	\mathbf{E}_m = \frac{i \omega \mu m}{4 \pi r^2} \left( ikr + 1 \right) e^{-ikr} \left( -\frac{z}{r} \hat{y} + \frac{y}{r} \hat{z} \right).
	:label: Em_Cartesian

