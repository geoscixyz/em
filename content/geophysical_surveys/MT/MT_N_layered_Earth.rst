.. _MT_N_layered_Earth:

Response of a layered Earth to a plane wave
===========================================

.. _Jupyter Notebook:

Introduction
------------

The problem setup is shown in the figure below, where we have

| -a layered Earth, each layer with its own physical properties \\(\\sigma, \\varepsilon, \\mu \\) 

| -a plane wave coming from air, perpendicular to the Earth's surface, traveling along the axis Z (oriented downward), with an electric field \\(\\mathbf{E_x}\\) and a magnetic field \\(\\mathbf{H_y}\\)

| - the origin of coordinate system coincides with the Earth's surface


.. plot::

    from examples.MT_N_Layered_Earth import *

    z=np.arange(-200,500,10) #Space Definition
    thick5=np.array([1.2*10.**5., 50.,100.,75.,50.]) #Define the Thickness of 5 layers

    fig,ax = plt.subplots(1,1,figsize=(10,10))
    ax = PlotLayer(thick5,ax,1.,z)

    plt.show()



Governing Equations
-------------------

The governing equation for DC resistivity problem can be obtained from
:ref:`Maxwell's equations <maxwell1_fundamentals_index>`. We start by
considering the zero-frequency case, in which case, Maxwell's equations are

.. math::
	\nabla \times \mathbf{E_x} = - i \omega \mu \mathbf{H_y}
	:label: Faraday
	
.. math::
	\nabla \times \mathbf{H_y} = (\sigma + i \omega \varepsilon) \mathbf{E_x}
    :label: Ampere

Knowing that the divergent of \textbf{E} and \textbf{H} are equal to 0 here (no free charge)
according to :eq:`gauss_electric_frequency` and :eq: `gauss_magnetic_frequency`, we can combine the equations to write the Helmhotz (wave propagation) equation for both \textbf{E} and \textbf{B} field:

.. math::
    \nabla ^2  \mathbf{E_x} + k^2 \mathbf{E_x} = 0
    :label: E_wave_propagation_equation

.. math::
    \nabla ^2 \mathbf{H_y} + k^2 \mathbf{H_y} = 0
    :label: H_wave_propagation_equation

with k the wavenumber:

.. math::
    k = \sqrt{\omega ^2 \mu \epsilon - i \omega \mu \sigma }
    :label: kwavenumber


Taking the problem from the point of view of the electric field, we know the :ref:E_wave_propagation_equation has a solution in the form of:

.. math::
    E_x (z) = U e^{i k z} + D e^{-i k z}
    
.. math::
    H_y (z) = \frac{(\nabla \times \mathbf{E_x})_y}{- i \omega \mu} = \frac{k}{ \omega \mu} (U e^{i k z} -D e^{-i k z} ) = \frac{1}{Z} (U e^{i k z} -D e^{-i k z} )

with U and D are the complex amplitudes of the Up and Down components of the field and Z the intrinsic impedance of the space.

Writing the solution in the j-th layer, we got:

.. math::
    E_{x,j} (z) = U_j e^{i k (z-z_{j-1})} + D_j e^{-i k (z-z_{j-1})}
    
.. math::
    H_{y,j} (z) = \frac{1}{Z_j} (D_j e^{-i k (z-z_{j-1})} - U_j e^{i k (z-z_{j-1})})

Which can be rewrite as:

.. math::
    \left(\begin{matrix} E_{x,j} \\ H_{y,j} \end{matrix} \right) = \left(\begin{matrix} 1 & 1 \\ -\frac{1}{Z_j} & \frac{1}{Z_j} \end{matrix} \right) \left(\begin{matrix} U_j \\ D_j \end{matrix} \right) 
    = P_j \left(\begin{matrix} U_j \\ D_j \end{matrix} \right) 


The transition of the Up and Down component inside a layer can then be 

.. figure:: images/InsideLayer.png
    :align: center
    :scale: 100% 
    :name: InsideLayer

.. math::
    \left(\begin{matrix} U_j' \\ D_j' \end{matrix} \right)  = \left(\begin{matrix} e^{i k h_j} & 0 \\ 0 & e^{-i k h_j} \end{matrix} \right) \left(\begin{matrix} U_j \\ D_j \end{matrix} \right) 
    = T_j \left(\begin{matrix} U_j \\ D_j \end{matrix} \right) 

Using the continuity of the tangential \\(\\mathbf{E_x}\\) and \\(\\mathbf{H_y}\\) field at the interfaces, we find an iterative relation between the fields in consecutive layer:

.. math::
    \left(\begin{matrix} E_{x,j} \\ H_{y,j} \end{matrix} \right) = P_j T_j P^{-1}_J \left(\begin{matrix} E_{x,j+1} \\ H_{y,j+1} \end{matrix} \right)

We are now only missing a Boundary Condition to be able to compute our MT forward modeling. A reasonable one is to set the Down Amplitude to 1 and the Up Amplitude to 0 in the last layer, as there is no reflection from an other interface below.

.. math::
    \left(\begin{matrix} U_n \\ D_n \end{matrix} \right)  = \left(\begin{matrix} 0 \\ 1 \end{matrix} \right) 


Field Acquisition
-----------------

In MT, the source is unknown but we are avoiding the problem by measuring the ratio of the fields. usually at the surface. We define an apparent impedance

.. math::
    \hat{Z_{xy}} = \frac{E_x}{H_y}

Notice this is a complex number, with a norm and an angle.

Data
----

Apparent Resistivity
********************

.. math::
    \rho_{app} = \frac{1}{\mu_0 \omega} |\hat{Z_{xy}}|

Phase
*****

.. math::
    \Theta =tan^{-1} \frac{Im(\hat{Z_{xy}})}{Re(\hat{Z_{xy}})} 


Survey Design
-------------

Interpretation
--------------

Pratical Consideration
----------------------

Building some Intuition for MT problem
--------------------------------------

.. raw:: html
  :file: ./images/movieMT_time.html




.. [1] Ward, S. H., & Hohmann, W. *Electromagnetic Theory for Geophysical Applications Applications.* In Electromagnetic methods in applied geophysics (1st ed., pp. 130–311). Society of Exploration Geophysicists. 1988.
