.. _wave_propagation_details:

Details
=======

.. todo:: Here are the details! Derivations, in-between steps, all the pieces. Each sub-heading has an anchor so that you can reference to this in previous pages

.. _wave_propagation_in_free_space_details: 

Derivation of wave euqations for homogeneous media
--------------------------------------------------

To derive the wave equations in time-domain, we begin with :ref:`Faraday <faraday>` and :ref:`Ampere-Maxwell <ampere_maxwell>` equations:

.. include:: ../../../../equation_bank/faraday_time.rst

.. include:: ../../../../equation_bank/ampere_maxwell_time.rst

and the three constitutive relations:

.. include:: ../../../../equation_bank/ohms_law_time.rst

.. math:: \mathbf{d} = \epsilon \mathbf{e}
        :name: depse

.. math:: \mathbf{b} = \mu \mathbf{h}
        :name: bmuh

The derivations will be done for  first :math:`\mathbf{e}` and then for :math:`\mathbf{h}`. 

Derivation for electric field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To derive the wave equation which uses only :math:`\mathbf{e}`, we first take the curl of Faraday's Law, shown in equation :eq:`faraday_time`:

.. math:: \boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{e}) = - \boldsymbol{\nabla} \times \frac{\partial \mathbf{b}}{\partial t}
        :name: hme1

The appropriate constitutive relations can be substituted into Equation :eq:`hme1` to get the following expressions in terms of only the fields :math:`\mathbf{e}` and :math:`\mathbf{h}` instead of fields and fluxes:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \boldsymbol{\nabla} \times \left (  \frac{\partial}{\partial t} (\mu \mathbf{h}) \right )
        :name: hme2

Because we assume a homogenous space, the physical properties :math:`\mu`, :math:`\epsilon`, and :math:`\sigma` can be moved out front of the derivative terms. Thi simplifies the above expressions, which only contains :math:`\mu`.

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \boldsymbol{\nabla} \times \frac{\partial \mathbf{h}}{\partial t}
        :name: hme3

If we further assume that we can take the first and second derivatives of :math:`\mathbf{e}`, we can either take the spatial derivatives first or the time derivatives. Equation :eq:`hme3` can then also be written as:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \boldsymbol{\nabla} \times \mathbf{h} \right )
        :name: hme4

This expression is now solely in terms of :math:`\boldsymbol{\nabla} \times \mathbf{e}` and :math:`\boldsymbol{\nabla} \times \mathbf{h}`. Thus, we can use Equation :eq:`ampere_maxwell_time` to generate an equation with only :math:`\mathbf{e}`. We substitute in Equation :eq:`ampere_maxwell_time` into Equation :eq:`hme4` and simplify using the constitutive relations in Equations :eq:`ohms_law_time` and :eq:`depse`:

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t} \right )

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \sigma \mathbf{e} + \frac{\partial (\epsilon \mathbf{e})}{\partial t} \right )

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}
        :name: hme5

Additionally, we can simplify the first term of this expression by using the vector identity :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{x} = \boldsymbol{\nabla} \boldsymbol{\nabla} \cdot \mathbf{x} - \boldsymbol{\nabla}^2 \mathbf{x}`. Recalling that both :math:`\boldsymbol{\nabla} \cdot \mathbf{e}` and :math:`\boldsymbol{\nabla} \cdot \mathbf{h}` are zero in a homogenous space, the vector identity simply becomes :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{x} = - \boldsymbol{\nabla}^2 \mathbf{x}`. If we now substitute that into :eq:`hme5`, we get the following expression:

.. math::  \boldsymbol{\nabla}^2 \mathbf{e}  - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} = 0
        :name: hme6

This is the wave equation for the electric field in the time-domain.


Derivation for magnetic field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To derive the wave equation for :math:`\mathbf{h}`, we repeat the above derivation but now start with taking the curl of Ampere's Law, shown in equation :eq:`ampere_maxwell_time`:

.. math:: \boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{h}) = \boldsymbol{\nabla} \times \mathbf{j} + \boldsymbol{\nabla} \times \frac{\partial \mathbf{d}}{\partial t}
        :name: hmh1

The constitutive relations can be substituted into Equation :eq:`hmh1` to get the following expressions in terms of only :math:`\mathbf{e}` and :math:`\mathbf{h}`:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \boldsymbol{\nabla} \times (\sigma \mathbf{e}) + \boldsymbol{\nabla} \times \left (  \frac{\partial}{\partial t} (\epsilon \mathbf{e}) \right )
        :name: hmh2

We simplify the expression just like we did before for the electric field.

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \sigma \boldsymbol{\nabla} \times \mathbf{e} + \epsilon \boldsymbol{\nabla} \times \frac{\partial \mathbf{e}}{\partial t}
        :name: hmh3

We can assume that we can take the first and second derivatives of :math:`\mathbf{e}` and :math:`\mathbf{h}` and can either take the spatial derivatives or time derivatives first. Equation :eq:`hmh3` can then also be written as:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \sigma \boldsymbol{\nabla} \times \mathbf{e} + \epsilon \frac{\partial}{\partial t} \left ( \boldsymbol{\nabla} \times \mathbf{e} \right )
        :name: hmh4

These expressions are now in terms of :math:`\boldsymbol{\nabla} \times \mathbf{e}` and :math:`\boldsymbol{\nabla} \times \mathbf{h}`. Thus, we can use Equation :eq:`faraday_time` to generate an equation with only :math:`\mathbf{h}`. We then again use the vector identity :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{x} = \boldsymbol{\nabla} \boldsymbol{\nabla} \cdot \mathbf{x} - \boldsymbol{\nabla}^2 \mathbf{x}` and the fact that :math:`\boldsymbol{\nabla} \cdot \mathbf{h}` is zero in a homogenous space to simplify the vector identity to :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{x} = - \boldsymbol{\nabla}^2 \mathbf{x}`. This is then substituted into the wave equation. The following shows these derivations.

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \frac{\partial \mathbf{b}}{\partial t} - \epsilon \frac{\partial}{\partial t} \left (\frac{\partial \mathbf{b}}{\partial t} \right )

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \frac{\partial (\mu \mathbf{h}) }{\partial t} - \epsilon \frac{\partial}{\partial t} \left (\frac{\partial (\mu \mathbf{h})}{\partial t} \right )

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2}

.. math:: - \boldsymbol{\nabla}^2 \mathbf{h} = - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2}

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2} - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} = 0
        :name: hmh6

Equation :eq:`hmh6` is then the wave equation for the magnetic field in the time-domain.

Summary
^^^^^^^

We now have two wave equations or second-order differential equations; one for the electric field and one for the magnetic field, summarized in Equations :eq:`hme7` and :eq:`hmh7`.

.. math::  \boldsymbol{\nabla}^2 \mathbf{e} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}  = 0
        :name: hme7

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \mu \sigma \frac{\partial \mathbf{h}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}  = 0
        :name: hmh7

.. _speed_light_details: 

Solving the wave equation when :math:`\sigma=0`
----------------------------------------------

.. todo:: already have most of this. maybe remove or just add to the other material?

In the case where :math:`\sigma` is zero, Equations :eq:`hme7` and :eq:`hmh7` become:

.. math::  \boldsymbol{\nabla}^2 \mathbf{e} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}  = 0
        :name: hme13

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}  = 0
        :name: hmh14

The following derivation will be the same for both the magnetic and electric fields. Let's use the magnetic field for this analysis. In 1D, Equation :eq:`hmh14` is now written as:

.. math:: \frac{\partial^2 \mathbf{h}}{\partial z^2} = \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2},
        :name: hmh15

for which there is a solution of the form:

.. math:: \mathbf{h} = \mathbf{h}_0 \cos \left ( 2\pi \frac{z-vt}{\lambda} \right ),
        :name: slwave

where :math:`v` is the speed of the sinosoidal wave and :math:`\lambda` is its wavelength. We can check this solution by taking the derivatives with respect to :math:`z` and :math:`t` to see if we get back to Equation :eq:`hmh15`.

.. math:: \frac{\partial^2 \mathbf{h}}{\partial z^2} = \frac{\partial}{\partial z} \left [ - \mathbf{h}_0 \sin \left(  2\pi \frac{z-vt}{\lambda} \right) \left( \frac{2\pi}{\lambda}\right) \right ] = - \mathbf{h}_0 \cos \left(  2\pi \frac{z-vt}{\lambda} \right) \left( \frac{2\pi}{\lambda}\right)^2

.. math:: \frac{\partial^2 \mathbf{h}}{\partial t^2} =\frac{\partial}{\partial t} \left [ - \mathbf{h}_0 \sin \left ( 2\pi \frac{z-vt}{\lambda} \right ) \left ( \frac{-2\pi v}{\lambda} \right) \right ] = - \mathbf{h}_0 \cos \left ( 2\pi \frac{z-vt}{\lambda} \right ) \left ( \frac{-2\pi v}{\lambda} \right)^2

We now plug these solutions into Equation :eq:`hmh15` and simplify:

.. math:: \left (\frac{2\pi}{\lambda} \right)^2 = \epsilon \mu \left (\frac{-2\pi v}{\lambda} \right)^2

.. math:: 1 = \epsilon \mu v^2

.. math:: v = \sqrt{\frac{1}{\epsilon \mu}}
        :name: v

This shows that the solution to Equation :eq:`hmh15` is a wave of the form given in Equation :eq:`slwave` if Equation :eq:`v` holds true. In free space, we can quickly evaluate Equation :eq:`v`, knowing that :math:`\mu = 4\pi \times 10^{-7} \frac{T \cdot m}{A}` and :math:`\epsilon = 8.85 \times 10^{-12} \frac{F}{m}`:

.. math:: v = \sqrt{\frac{1}{( 4\pi \times 10^{-7})(8.85 \times 10^{-12})}} = 3 \times 10^8

The units of :math:`v` work out as following:

.. math:: \sqrt{ \frac{1}{\left[\frac{T \cdot m}{A} \right] \left [ \frac{F}{m} \right ]} } = \left ( \frac{A}{T \cdot F} \right) ^ {1/2} = \left ( \frac{\frac{C}{s}}{\frac{V\cdot s}{m^2} \cdot F} \right) ^ {1/2} = 

.. math:: \left ( \frac{\frac{F \cdot V}{s}}{\frac{V\cdot s}{m^2} \cdot F} \right) ^ {1/2} = \left ( \frac{F\cdot V}{s} \frac{m^2}{V \cdot F \cdot s} \right ) ^{1/2} = \frac{m}{s}

Thus, the velocity of the wave is :math:`3 \times 10^8 \frac{m}{s}`, which is the speed of light! The same derivation can be done using the electric field.


