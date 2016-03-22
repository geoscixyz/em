.. _MT_N_layered_Earth:

Response of a layered Earth to a plane wave
===========================================

Introduction
------------

We present here a 1D modelisation of the MagnetoTelluric waves and the associated geophysical data to build better representation of the different physical phenomenons and better understanding of the resulting data. This work follows the derivation presented in :cite:`ward1988` and is supported by interactive apps developed in a `binder`_.

 .. image:: http://mybinder.org/badge.svg 
    :target: http://mybinder.org/repo/ubcgif/em_examples/notebooks/geophysical_surveys/MT_N_Layered_Earth/MT_n_layered_earth_example.ipynb
    :align: center

.. _binder: http://mybinder.org/repo/ubcgif/em_examples/notebooks/geophysical_surveys/MT_N_Layered_Earth/MT_n_layered_earth_example.ipynb

MagnetoTelluric is a widely used method, especially for imaging geothermal structures. Its ability to image deep structure, up to kilometers depth is unique in EM geophysics. It is a passive method that use waves generated mostly in the Earth's Atmosphere. High frequencies are mainly produced by lightning strikes all around the globe, travelling through the Earth's Ionosphere that acts as a waveguide. Low Frequencies source waves are produced through the interaction of the Earth's Ionosphere with solar wind and Earth's magnetic field.

In MagnetoTellurics problem, the key diagnosed physical property is :ref:`electrical conductivity<electrical_conductivity_index>` :math:`\sigma`, as we expect the contrasts of the others physical properties to be negligible. 



Setup
-----

An example of a 1D MagnetoTelluric modelisation, with a 2-layers Earth, is shown in the movie below, where we have:

 - a layered Earth, each layer with its own physical properties :math:`\sigma, \varepsilon, \mu`

 - a plane wave traveling along the axis Z coming from air, composed of an electric field :math:`\mathbf{E_x}` and a magnetic field :math:`\mathbf{H_y}`. These are the fields we will be measuring with our geophysical instruments to obtain information from the underground


 .. raw:: html
  :file: ./images/movieMT_time.html


We can see that several phenomenons are occuring. Just to mention few of them:

 - the incoming wave (down component) is reflected at the surface

 - once in the ground we observe a diffusive effect of the Earth on the wave that will regulate the depth of investigation and the resolution of the survey. The decay is more important in the second layer with a higher conductivity

 - :math:`\mathbf{E_x}` and  :math:`\mathbf{H_y}` are continuous and phased compared to each other


Governing Equations
-------------------

The governing equation for MagnetoTellurics problem can be obtained from
:ref:`Maxwell's equations <maxwell1_fundamentals_index>`. We start by
considering the zero-frequency case, in which case, Maxwell's equations are

.. math::
	\nabla \times \mathbf{E_x} = - i \omega \mu \mathbf{H_y}
	:label: Faraday
	
.. math::
	\nabla \times \mathbf{H_y} = (\sigma + i \omega \varepsilon) \mathbf{E_x}
    :label: Ampere

Knowing that the divergent of **E** and **H** are equal to 0 here (no free charge)
according to :ref:`Gauss's Law for Electric Fields<gauss_electric>` and :ref:`Gauss's Law for Magnetic Fields<gauss_magnetic_frequency>`, we can combine the equations to write the Helmhotz (wave propagation) equation for both **E** and **B** field:

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


We usually assume that the displacement current is negligible, which means \\(\\sigma >> \\omega \\varepsilon\\). In this case 

.. math::
    k \simeq (1-j) \sqrt{ \frac{\omega \mu \sigma}{2} }
    :label: kwavenumber_steadystate

Taking the problem from the point of view of the electric field, we know the :eq:`E_wave_propagation_equation` has a solution in the form of:

.. math::
    E_x (z) = U e^{i k z} + D e^{-i k z}
    
.. math::
    H_y (z) = \frac{(\nabla \times \mathbf{E_x})_y}{- i \omega \mu} = \frac{k}{ \omega \mu} (U e^{i k z} -D e^{-i k z} ) = \frac{1}{Z} (U e^{i k z} -D e^{-i k z} )

with :math:`\mathbf{E_x} = E_x \mathbf{\hat{x}}`  and U and D are the complex amplitudes of the Up and Down components of the field and Z the intrinsic impedance of the space.

Writing the solution in the j-th layer (See :numref:`MTlayeredEarth`), we got:

 .. math::
    E_{x,j} (z) = U_j e^{i k (z-z_{j-1})} + D_j e^{-i k (z-z_{j-1})}
    
 .. math::
    H_{y,j} (z) = \frac{1}{Z_j} (D_j e^{-i k (z-z_{j-1})} - U_j e^{i k (z-z_{j-1})})


 .. figure:: images/MT_N_layered_Earth-1.hires.png
    :align: center
    :scale: 20% 
    :name: MTlayeredEarth

    1D general Earth Model Configuration

Which can be rewrite as:

 .. math::
    \left(\begin{matrix} E_{x,j} \\ H_{y,j} \end{matrix} \right) = \left(\begin{matrix} 1 & 1 \\ -\frac{1}{Z_j} & \frac{1}{Z_j} \end{matrix} \right) \left(\begin{matrix} U_j \\ D_j \end{matrix} \right) 
    = P_j \left(\begin{matrix} U_j \\ D_j \end{matrix} \right) 

The transition of the Up and Down component inside a layer can then be write as such

 .. figure:: images/InsideLayer.png
    :align: center
    :scale: 100% 
    :name: InsideLayer

    Transition inside a layer, variables definition.


.. math::
    \left(\begin{matrix} U_j' \\ D_j' \end{matrix} \right)  = \left(\begin{matrix} e^{i k h_j} & 0 \\ 0 & e^{-i k h_j} \end{matrix} \right) \left(\begin{matrix} U_j \\ D_j \end{matrix} \right) 
    = T_j \left(\begin{matrix} U_j \\ D_j \end{matrix} \right) 

With the variables U, D, U' and D' define as in (:numref:`InsideLayer`)

Using the continuity of the tangential \\(\\mathbf{E_x}\\) and \\(\\mathbf{H_y}\\) field at the interfaces, we find an iterative relation between the fields in consecutive layers:

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

For a half-space, \\(\\rho_{app} = \\rho_{earth}\\).

For a unhomogeneous earth, \\(\\rho_{app}\\) at a particular frequency is an average of the conductivity of the earth on about a sphere with a radius equal to the skin depth.

Phase
*****

.. math::
    \Theta =tan^{-1} \frac{Im(\hat{Z_{xy}})}{Re(\hat{Z_{xy}})}

for a half-space,

.. math::
    \Theta = tan^{-1} \frac{Im({Z_{xy}})}{Re({Z_{xy}})} 
    = tan^{-1} \frac{\omega \mu}{(1-j) \sqrt{\frac{\omega \mu \sigma}{2}}} 
    = \frac{\pi}{4}


If \\(\\sigma \\) **increases** at depth, then \\(\\Theta \\) **increases** before returning to 45°


If \\(\\sigma \\) **decreases** at depth, then \\(\\Theta \\) **decreases** before returning to 45°


Survey Design
-------------

Interpretation
--------------

Pratical Consideration
----------------------





.. [1] Ward, S. H., & Hohmann, W. *Electromagnetic Theory for Geophysical Applications Applications.* In Electromagnetic methods in applied geophysics (1st ed., pp. 130–311). Society of Exploration Geophysicists. 1988.
