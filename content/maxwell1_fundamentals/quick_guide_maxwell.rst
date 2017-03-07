.. _quick_guide_maxwell:

Maxwell's Equations in Various Forms
====================================

.. purpose::
	
	Having provided the set of :ref:`formative laws<formative_laws_index>` for electromagnetics, we present four common representations of Maxwell's equations. This page is meant to serve as a quick guide. For specific problems, it may be beneficial to begin from less common forms of Maxwell's equations. Please note however, that all forms can be derived from the expressions presented here.

Maxwell's equations are comprised of the first four :ref:`formative laws<formative_laws_index>`; i.e. :ref:`Gauss's law for electric fields<gauss_electric>`, :ref:`Gauss's law for magnetic fields<gauss_magnetic>`, :ref:`Faraday's law<faraday>` and the :ref:`Ampere-Maxwell law<ampere_maxwell>`. Although we tend to state Gauss's law's for electric and magnetic fields explicitly, it should be noted that all other formative laws may be derived from Farday's law and the Ampere-Maxwell equation.

In this section, we will provide four forms for representing Maxwell's equations:

(a) :ref:`differential_equations_time`
(b) :ref:`differential_equations_frequency`
(c) :ref:`integral_equations_time`
(d) :ref:`integral_equations_frequency`

This page is designed to be a quick access to the relevant equations with proper
:ref:`notation<introduction_notation>` and units.

Variables and Units
-------------------

The variables and units for relevant quantities in Maxwell's equations are given here.

.. include:: maxwell_variables.rst


.. _differential_equations_time:

Differential Form in the Time Domain
------------------------------------

Here, we present differential forms for :ref:`Gauss's law for electric fields<gauss_electric>`, :ref:`Gauss's law for magnetic fields<gauss_magnetic>`, :ref:`Faraday's law<faraday>` and the :ref:`Ampere-Maxwell equation<ampere_maxwell>` in the time domain.

.. math::
	\begin{align}
	                            & \textbf{In a Vacuum}                              & & \textbf{In Matter} \\
	\textbf{Gauss for E-field:}\;\;  & \nabla\cdot\mathbf{e}=\dfrac{\rho}{\varepsilon_0} & &\nabla\cdot\mathbf{d}=\rho_f \\
	\textbf{Gauss for B-field:}\;\;  & \nabla\cdot\mathbf{b}=0                           & &\nabla\cdot\mathbf{b}=0 \\
	\textbf{Faraday:}          \;\;  & \nabla\times\mathbf{e}=-\dfrac{\partial \mathbf{b}}{\partial t} & &\nabla\times\mathbf{e}=-\dfrac{\partial \mathbf{b}}{\partial t} \\
	\textbf{Ampere-Maxwell:}   \;\;  & \nabla\times\mathbf{b}=\mu_0\varepsilon_0 \dfrac{\partial \mathbf{e}}{\partial t} & &\nabla\times\mathbf{h}=\mathbf{j_f} + \dfrac{\partial \mathbf{d}}{\partial t}
	\end{align}

where the following :ref:`constitutive relationships<physical_properties_index>` can be used to replace fields and fluxes:

.. math::
	\begin{align}
	\mathbf{j} &= \sigma \mathbf{e}\\
	\mathbf{b} &= \mu \mathbf{h}\\
	\mathbf{d} &= \varepsilon \mathbf{e}
	\end{align}

.. _differential_equations_frequency:

Differential Form in the Frequency Domain
-----------------------------------------

Here, we present differential forms for :ref:`Gauss's law for electric fields<gauss_electric>`, :ref:`Gauss's law for magnetic fields<gauss_magnetic>`, :ref:`Faraday's law<faraday>` and the :ref:`Ampere-Maxwell equation<ampere_maxwell>` in the frequency domain:

.. math::
	\begin{align}
	                                 & \textbf{In a Vacuum}                              & & \textbf{In Matter} \\
	\textbf{Gauss for E-field:} \;\; & \nabla\cdot\mathbf{E}=\dfrac{\rho}{\varepsilon_0} & &\nabla\cdot\mathbf{D}=\rho_f \\
	\textbf{Gauss for B-field:} \;\; & \nabla\cdot\mathbf{B}=0                           & &\nabla\cdot\mathbf{B}=0 \\
	\textbf{Faraday:}           \;\; & \nabla\times\mathbf{E}=-i\omega\mathbf{B}         & &\nabla\times\mathbf{E}=-i\omega\mathbf{B} \\
	\textbf{Ampere-Maxwell:}    \;\; & \nabla\times\mathbf{B}=i\omega\mu_0\varepsilon_0\mathbf{E} & &\nabla\times\mathbf{H}=\mathbf{J_f} + i\omega \mathbf{D}
	\end{align}

where the following :ref:`constitutive relationships<physical_properties_index>` can be used to replace fields and fluxes:

.. math::
	\begin{align}
	\mathbf{J} &= \sigma \mathbf{E}\\
	\mathbf{B} &= \mu \mathbf{H}\\
	\mathbf{D} &= \varepsilon \mathbf{E}
	\end{align}

.. _integral_equations_time:

Integral Form in the Time Domain
--------------------------------

Here, we present integral forms for :ref:`Gauss's law for electric fields<gauss_electric>`, :ref:`Gauss's law for magnetic fields<gauss_magnetic>`, :ref:`Faraday's law<faraday>` and the :ref:`Ampere-Maxwell equation<ampere_maxwell>` in the time domain.

.. math::
	\begin{align}
	                            & \;\;\;\;\;\;\;\;\; \textbf{In a Vacuum}                              & & \;\;\;\;\;\;\;\;\; \textbf{In Matter} \\
	\textbf{Gauss for E-field:} \; & \int_V\nabla\cdot\mathbf{e}\; dV \! =\!\oint_S\mathbf{e}\cdot d \mathbf{a} \!=\! \dfrac{Q}{\varepsilon_0} & & \int_V\nabla\cdot\mathbf{d}\; dV \! =\!\oint_S\mathbf{d}\cdot d\mathbf{a} \! = \! Q_f \\
	\textbf{Gauss for B-field:} \; & \oint_S \mathbf{b} \cdot  d\mathbf{a}=0                          & & \oint_S \mathbf{b} \cdot d \mathbf{a}=0 \\
	\textbf{Faraday:}           \; & \oint_C \mathbf{e}\cdot d\mathbf{l}=-\int_S\dfrac{\partial \mathbf{b}}{\partial t}\cdot d\mathbf{a} & & \oint_C \mathbf{e}\cdot d\mathbf{l}=-\int_S\dfrac{\partial \mathbf{b}}{\partial t}\cdot d\mathbf{a} \\
	\textbf{Ampere-Maxwell:}    \; & \oint_C \mathbf{b} \cdot d\mathbf{l} = \mu_0\varepsilon_0 \int_S \dfrac{\partial \mathbf{e}}{\partial t} \!\cdot d\mathbf{a} & & \oint_C \!\mathbf{h} \cdot  d\mathbf{l} = \! \int_S \!\Big ( \mathbf{j_f} \!+\! \dfrac{\partial \mathbf{d}}{\partial t} \Big ) \!\cdot d\mathbf{a}
	\end{align}

where the following :ref:`constitutive relationships<physical_properties_index>` can be used to replace fields and fluxes:

.. math::
	\begin{align}
	\mathbf{j} &= \sigma \mathbf{e}\\
	\mathbf{b} &= \mu \mathbf{h}\\
	\mathbf{d} &= \varepsilon \mathbf{e}
	\end{align}


.. _integral_equations_frequency:

Integral Form in the Frequency Domain
-------------------------------------

Here, we present integral forms for :ref:`Gauss's law for electric fields<gauss_electric>`, :ref:`Gauss's law for magnetic fields<gauss_magnetic>`, :ref:`Faraday's law<faraday>` and the :ref:`Ampere-Maxwell equation<ampere_maxwell>` in the frequency domain.

.. math::
	\begin{align}
	                            & \;\;\;\;\;\;\;\;\; \textbf{In a Vacuum}                              & & \;\;\;\;\;\;\;\;\; \textbf{In Matter} \\
	\textbf{Gauss for E-field:} \; & \int_V\nabla\cdot\mathbf{E}\; dV \! = \!\oint_S\mathbf{E}\cdot d\mathbf{a} \! =\!\dfrac{Q}{\varepsilon_0} & &\int_V\nabla\cdot\mathbf{D}\; dV=\oint_S\mathbf{D}\cdot d \mathbf{a} \! =\! Q_f \\
	\textbf{Gauss for B-field:} \; & \oint_S \mathbf{B} \cdot d\mathbf{a}=0           & &\oint_S \mathbf{B} \cdot d\mathbf{a}=0 \\
	\textbf{Faraday:}           \; & \oint_C \mathbf{E}\cdot d\mathbf{l}=-i\omega\int_S\mathbf{B}\cdot d\mathbf{a} & &\oint_C \mathbf{E}\cdot d\mathbf{l}=-i\omega\int_S\mathbf{B}\cdot d\mathbf{a} \\
	\textbf{Ampere-Maxwell:}    \; & \oint_C \mathbf{B} \cdot d\mathbf{l} = i\omega\mu_0\varepsilon_0 \int_S \mathbf{E} \cdot d\mathbf{a} & & \oint_C \!\mathbf{H} \cdot  d\mathbf{l} = \! \int_S \!\big ( \mathbf{J_f} \!+\! i\omega \mathbf{D} \big ) \!\cdot d\mathbf{a}
	\end{align}

where the following :ref:`constitutive relationships<physical_properties_index>` can be used to replace fields and fluxes:

.. math::
	\begin{align}
	\mathbf{J} &= \sigma \mathbf{E}\\
	\mathbf{B} &= \mu \mathbf{H}\\
	\mathbf{D} &= \varepsilon \mathbf{E}
	\end{align}












