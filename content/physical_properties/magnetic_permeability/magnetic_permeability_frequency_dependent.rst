.. _magnetic_permeability_frequency_dependent:

Frequency-Dependent Magnetic Permeability
=========================================

In response to changes in an applied magnetic field, the induced magnetization within most rocks may be considered an instantaneous process.
For some lateritic soils and rapidly cooled basalts however, a portion of the induced magnetization will instead undergo a relaxation process.
This relaxation process has been attributed to the presence of superparamagnetic iron-oxide nanoparticles, and is commonly refered to as: viscous remanent magnetization, magnetic viscosity, or magnetic after-effect.

Mathematical Relationships
--------------------------

As a result of their magnetic viscosity, lateritic soils and rapidly cooled basalts are characterized by frequency-dependent magnetic permeabilities, where:

.. math::
	{\bf B}(\omega) = \mu (\omega) \, {\bf H}(\omega)
	:label: FreqConstRel

The magnetic viscosity can also be represented using a frequency-dependent magnetic susceptibility :math:`\chi (\omega)`, where:

.. math::
	\mu (\omega) = \mu_0 \big [ 1 + \chi (\omega) \, \big ]



.. math::
	\chi(\omega) = \chi_0 - \frac{\chi_0 - \chi_\infty}{ln (\tau_2/\tau_1)} ln \Bigg ( \frac{1 + i\omega\tau_2}{1 + i\omega\tau_1} \Bigg )
	


.. math::
	\chi(\omega) = \chi_\infty + \frac{\chi_0 - \chi_\infty}{1 + (i \omega \tau)^C}




.. figure:: ./figures/figChiOmegaDistr.png
	:align: center
        :scale: 40%
















