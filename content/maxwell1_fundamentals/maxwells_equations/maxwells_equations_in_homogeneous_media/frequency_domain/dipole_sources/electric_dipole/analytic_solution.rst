.. _frequency_domain_electric_dipole_analytic_solution:

Analytic Solution
=================

.. topic:: Purpose

    Purpose here


The electric current dipole is an elementary length of current flowing in a single direction. It is convenient to solve the problem in terms of Schelkunoff potentials as done in :cite:`ward1988`. To summarize, for an electric current source (:math:`\mathbf{J_e^s}`), Maxwell's equations in frequency are

.. math::
	\nabla \times \mathbf{E_e} + i\omega \mu \mathbf{H_e} = 0 
	:label: Faraday_e
.. math::
	\nabla \times \mathbf{H_e} - (\sigma + i\omega \epsilon) \mathbf{E_e} = \mathbf{J}_e^s 
	:label: Ampere_e

where the subscripts :math:`_e` remind us that we are using an electric source. Taking the curl of :eq:`Faraday_e` allows us to define :math:`\mathbf{H_e}` as the curl of a vector potential (:math:`\mathbf{A}`). 

.. math::
	\mathbf{H_e} \equiv \nabla \times \mathbf{A} 
	:label: A_def

After some manipulation of :eq:`Ampere_e` we obtain the Helmholtz equation for :math:`\mathbf{A}`.

.. math::
	\nabla^2 \mathbf{A} + k^2 \mathbf{A} = - \mathbf{J}_e^s, \  \  \  \  \text{where} \  \  k^2 = \omega^2\mu\epsilon -i\omega\mu\sigma
	:label: Helmholtz_A 

The equation with boundary conditions , is solved to generate :math:`\mathbf{A}`. For infinite media, the boundary condition is that :math:`\mathbf{A} \rightarrow 0` as :math:`r \rightarrow \infty`.

If :math:`\mathbf{J_e^s}` has only a single component, the :math:`\mathbf{A}` only has a component in that direction. The scalar Green's function for :eq:`Helmholtz_A` is

.. math::
	G(r) = \frac{e^{-ikr}}{4\pi r}.
	:label: GreensFncFullSpace

and hence the vector potential for an arbitrary electric current source is 

.. math::
	\mathbf{A}(\mathbf{r}) = \int_v \frac{e^{-ik|\mathbf{r}-\mathbf{r}'|}}{4\pi |\mathbf{r}-\mathbf{r}'|} \mathbf{J}_e(\mathbf{r}') dv
	:label: A_Potential

For an electric current dipole oriented in the :math:`\hat{x}` direction

.. math::
	\mathbf{J}_e(\mathbf{r}) = \hat{x} I ds \delta(x) \delta(y) \delta(z)
	:label: Je_x

and 

.. math::
	\mathbf{A}(\mathbf{r}) = \frac{I ds}{4\pi r} e^{-ikr} \hat{x}
	:label: A_Potential_for_Je_x


The electric and magnetic fields expressed in terms of :math:`\mathbf{A}` are

.. math::
	\mathbf{E}_e = -i\omega\mu\mathbf{A} + \frac{1}{(\sigma + i\omega\epsilon)} \nabla (\nabla \cdot \mathbf{A})
	:label: Fields_fncA

	\mathbf{H}_e = \nabla \times \mathbf{A}
	
In component form the electric field is given by

.. math::
	\mathbf{E}_e = \frac{I ds}{4 \pi \sigma} \left[ \left( k^2 + \frac{\partial^2}{\partial x^2} \right) \hat{x} + \frac{\partial^2}{\partial x \partial y} \hat{y} + \frac{\partial^2}{\partial x \partial z} \hat{z} \right] \frac{e^{-ikr}}{r}

which becomes

.. math::
	\mathbf{E}_e = \frac{I ds}{4 \pi \sigma r^3} e^{-ikr} \left[ \left(\frac{x^2}{r^2} \hat{x} + \frac{xy}{r^2} \hat{y} + \frac{xz}{r^2} \hat{z} \right) \left(-k^2 r^2 + 3ikr +3 \right) + \left(k^2 r^2 - ikr -1 \right) \hat{x} \right].
	:label: E_Cartesian

While the magnetic field is equal to

.. math::
	\mathbf{H}_e = \frac{I ds}{4 \pi} \left[ \frac{\partial}{\partial z} \hat{y} - \frac{\partial}{\partial y} \hat{z} \right] \frac{e^{-ikr}}{r}

which becomes

.. math::
	\mathbf{H}_e = \frac{I ds}{4 \pi r^2} \left( ikr + 1 \right) e^{-ikr} \left( -\frac{z}{r} \hat{y} + \frac{y}{r} \hat{z} \right).
	:label: H_Cartesian

