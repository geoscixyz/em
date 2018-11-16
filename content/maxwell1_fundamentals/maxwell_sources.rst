.. _maxwell_fundamentals_sources:

Maxwell's Equations with Electromagnetic Sources
================================================

.. purpose::
	
	Here, we show how Maxwell's equations are altered in the presence of electromagnetic sources. The two principle types of electromagnetic sources are discussed.

In many cases, the fields and fluxes within a region result from the presence of an electromagnetic source. Because Maxwell's equations fully characterize all electromagnetic interactions, they must also accommodate the existence of electromagnetic sources. There are two principle types of electromagnetic sources: electrical sources (:math:`\mathbf{j_e^s}`) and magnetic sources (:math:`\mathbf{j_m^s}`).

Electrical Sources
------------------

In Maxwell's equations, electrical sources are represented using a current density (:math:`\mathbf{j_e^s}`). Thus they have units [A/m :math:`\! ^2`]. Electrical sources may correspond to an :ref:`electrical current dipole<definition_electric_dipole_index>` or a current-carrying loop of wire. 

According to the :ref:`Ampere-Maxwell<ampere_maxwell>` equation, electrical currents are responsible for generating magnetic fluxes. By accounting for the electrical source term, the Ampere-Maxwell equation becomes:

.. math::
	 \nabla\times \mathbf{h} - \mathbf{j_f} - \frac{\partial \mathbf{d}}{\partial t} = \mathbf{j_e^s}

where :math:`\mathbf{j_f}` is now the free current density not accounted for by the source term. The total current density within the region can be treated as the sum of the source current density and the remaining free current density (i.e. :math:`\mathbf{j_{tot} = j_e^s + j_f}`). In the frequency domain, the Ampere-Maxwell equation becomes:

.. math::
	\nabla\times \mathbf{H} - \mathbf{J_f} - i\omega \mathbf{D} = \mathbf{J_e^s}

where the electrical source term is given by :math:`\mathbf{J_e^s}` and the remaining free current density is given by :math:`\mathbf{J_f}`.

Magnetic Sources
----------------

In Maxwell's equations, the magnetic source is a magnetic flux density (:math:`\mathbf{b_m^s}`); which has units [T]. One example of a magnetic source is the :ref:`magnetic dipole<definition_magnetic_dipole_index>`. 

According to :ref:`Faraday's law<faraday>`, time-varying magnetic fluxes induce rotational electric fields. Note however, that dimensional analysis of Faraday's law shows the right hand side has units [T/s]. As a result, the magnetic source term is commonly defined as :math:`\mathbf{j_m^s}`, where:

.. math::
	\mathbf{j_m^s} = - \frac{\partial \mathbf{b_m^s}}{\partial t}

By this convention, the magnetic source term can be thought of as a magnetic current density. In the presence of a magnetic source term, Faraday's law becomes:

.. math::
	\nabla \times \mathbf{e} + \frac{\partial \mathbf{b}}{\partial t} = \mathbf{j_m^s}

where :math:`\mathbf{b}` is the magnetic flux density not accounted for within the source term. The total density of magnetic flux within the region can be treated as the sum of the source flux density and the remaining flux density (i.e. :math:`\mathbf{b_{tot} = b_m^s + b}`). In the frequency domain, the source magnetic flux density is given by :math:`\mathbf{B_m^s}`. The corresponding source term is therefore defined as:

.. math::
	\mathbf{J_m^s} = -i\omega\mathbf{B_m^s}

and Faraday's law is give by:

.. math::
	\nabla\times \mathbf{E} + i\omega\mathbf{B} = \mathbf{J_m^s}


Restating Maxwell's Equations
-----------------------------

The existence of electrical and magnetic sources results in alterations for the Maxwell-Ampere equation and Faraday's law, respectively. Let us now restate Maxwell's equations in differential form in the presence of electromagnetic sources.

Differential Form in the Time Domain
************************************

Here, we present differential forms for :ref:`Gauss's law for electric fields<gauss_electric>`, :ref:`Gauss's law for magnetic fields<gauss_magnetic>`, :ref:`Faraday's law<faraday>` and the :ref:`Ampere-Maxwell equation<ampere_maxwell>` in the time domain.

.. math::
	\begin{align}
	\textbf{Gauss for E-field:}\;\;  &\nabla\cdot\mathbf{d}=\rho_f \\
	\textbf{Gauss for B-field:}\;\;  &\nabla\cdot\mathbf{b}=0 \\
	\textbf{Faraday:}          \;\;  &\nabla\times\mathbf{e} + \dfrac{\partial \mathbf{b}}{\partial t} = \mathbf{j_m^s} \\
	\textbf{Ampere-Maxwell:}   \;\;  &\nabla\times\mathbf{h} - \mathbf{j_f} - \dfrac{\partial \mathbf{d}}{\partial t} = \mathbf{j_e^s}
	\end{align}

where the following :ref:`constitutive relationships<physical_properties_index>` can be used to replace fields and fluxes:

.. math::
	\begin{align}
	\mathbf{j} &= \sigma \mathbf{e}\\
	\mathbf{b} &= \mu \mathbf{h}\\
	\mathbf{d} &= \varepsilon \mathbf{e}
	\end{align}

If we consider a **homogeneous medium** and combined the Maxwell-Ampere equation and Faraday's law to obtain the wave equation, we see that for an **electrical source**:

.. math::
	\nabla^2 \mathbf{e} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \varepsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} = \mu \frac{\partial \mathbf{j_e^s}}{\partial t}

As we can see, the forcing term in the above wave equation depends on the time-derivative of an electric current density. For a **magnetic source**:

.. math::
	\nabla^2 \mathbf{h} - \mu\sigma \frac{\partial \mathbf{h}}{\partial t} - \mu \varepsilon \frac{\partial^2 \mathbf{h}}{\partial t^2} = - \sigma \mathbf{j_m^s} - \mu \frac{\partial \mathbf{j_m^s}}{\partial t}

where the forcing term contains both first and second order time-derivatives.

Differential Form in the Frequency Domain
*****************************************

Here, we present differential forms for :ref:`Gauss's law for electric fields<gauss_electric>`, :ref:`Gauss's law for magnetic fields<gauss_magnetic>`, :ref:`Faraday's law<faraday>` and the :ref:`Ampere-Maxwell equation<ampere_maxwell>` in the frequency domain:

.. math::
	\begin{align}
	\textbf{Gauss for E-field:} \;\; &\nabla\cdot\mathbf{D}=\rho_f \\
	\textbf{Gauss for B-field:} \;\; &\nabla\cdot\mathbf{B}=0 \\
	\textbf{Faraday:}           \;\; &\nabla\times\mathbf{E} + i\omega\mathbf{B} = \mathbf{J_m^s} \\
	\textbf{Ampere-Maxwell:}    \;\; &\nabla\times\mathbf{H} - \mathbf{J_f} - i\omega \mathbf{D} = \mathbf{J_e^s}
	\end{align}

where the following :ref:`constitutive relationships<physical_properties_index>` can be used to replace fields and fluxes:

.. math::
	\begin{align}
	\mathbf{J} &= \sigma \mathbf{E}\\
	\mathbf{B} &= \mu \mathbf{H}\\
	\mathbf{D} &= \varepsilon \mathbf{E}
	\end{align}

If we consider a **homogeneous medium** and combined the Maxwell-Ampere equation and Faraday's law to obtain the Helmholtz equation, we see that for an **electrical source**:

.. math::
	\nabla^2 \mathbf{E} + k^2 \mathbf{E} = i\omega\mu \mathbf{J_e^s}

where the magnitude of the forcing term increases linearly with respect to the angular frequency. For a **magnetic source**:

.. math::
	\nabla^2 \mathbf{H} + k^2 \mathbf{H} = - \big ( \sigma + i\omega\varepsilon \big ) \mathbf{J_m^s}

where the right-hand side depends on both the conductive and dielectric properties of the medium. Recall that the :ref:`wavenumber<harmonic_planewaves_homogeneous_wavenumber>` is given by:

.. math::
	k = \sqrt{\omega^2 \mu \varepsilon - i\omega \mu\sigma}


