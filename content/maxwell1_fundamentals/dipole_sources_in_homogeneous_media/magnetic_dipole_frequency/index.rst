.. _frequency_domain_magnetic_dipole_index:

Harmonic Magnetic Dipole
========================

.. topic:: Purpose

    Here, we provide a physical description for the harmonic magnetic dipole.
    This is used to develop a mathematical expression which can be used to replace the magnetic source term in Maxwell's equations.





An magnetic dipole is an infinitesimal loop of wire of area :math:`S` carrying a current :math:`I`. The strength of the dipole is given by the magnetic dipole moment (:math:`m`)

.. math::
	m = IS

The magnetizaton vector is given by, for a loop laying in the yz plane:

.. math::
	\mathbf{M} = m \mathbf{u_x} \delta(x) \delta(y) \delta(z)

.. _notebook: https://github.com/geoscixyz/em_apps/blob/master/notebooks/maxwell1_fundamentals/HarmonicDipoleWidget_MD.ipynb

**Contents**

.. toctree::
    :maxdepth: 2

    analytic_solution
    asymptotics
    fields
