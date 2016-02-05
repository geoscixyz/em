.. _wave_propagation_in_free_space:

Wave Propagation in Free Space
==============================

In this section, we combine the first-order partial :ref:`differential equations <differential_equations_time>` into second-order equations for :math:`\mathbf{e}` or :math:`\mathbf{h}` and show how EM fields propagate in homogenous media. The plane wave solutions have propogation and attenuating components and the relative balance of these is determined by the complex wave number. When electrical conductivity :math:`\sigma` is zero, the electromagnetic waves propagate without attenuation. When :math:`\sigma` is large, as it is with most earth rocks, the EM waves are diffusive and attenuate rapidly within one or two wavelengths. In many problems, the wave propagation portion of the equation (or effectively, the displacement current), can be neglected and quasi-static Maxwell's equations can be solved. The following content parallels that offered in many EM resources :cite:`ward1988,griffiths1999,stratton1941`. We first generate the second-order differential equations in the time-domain and then use Fourier transforms to get the frequency-domain counterparts.

Wave equations in time-domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We begin with :ref:`Faraday <faraday>` and :ref:`Ampere-Maxwell <ampere_maxwell>` equations in the time-domain:

.. include:: ../../../equation_bank/faraday_time.rst

.. include:: ../../../equation_bank/ampere_maxwell_time.rst

and the three constitutive relations:

.. include:: ../../../equation_bank/ohms_law_time.rst

.. math:: \mathbf{d} = \epsilon \mathbf{e}
        :name: depse

.. math:: \mathbf{b} = \mu \mathbf{h}
        :name: bmuh

The goal is to combine these equations to obtain a single equation that involves :math:`\mathbf{e}` or :math:`\mathbf{h}`. For instance, to develop an equation for :math:`\mathbf{e}`, we take the curl of :eq:`faraday_time` and then substitute in Equations :eq:`ohms_law_time` and :eq:`depse`. Because all of the physical properties are assumed to be constant in space and time, they are not affected by curl operators or time derivatives. Thus the equation for :math:`\mathbf{e}` becomes Equation :eq:`hme7`. 

.. math::  \boldsymbol{\nabla}^2 \mathbf{e} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}  = 0
        :name: hme7

A similar procedure can be used to obtain an equation that involves only :math:`\mathbf{e}`, starting from Equation :eq:`ampere_maxwell_time` and using Equation :eq:`bmuh`:

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \mu \sigma \frac{\partial \mathbf{h}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}  = 0
        :name: hmh7

Check out :ref:`this page <wave_propagation_in_free_space_details>` for the detailed derivation of Equations :eq:`hme7` and :eq:`hmh7`.

The equations for :math:`\mathbf{e}` and :math:`\mathbf{h}` are identical in form. The first term is the Laplacian, the second term involves a first derivative in time, and the third term has a second order time derivative. This is the general form taken by a propagating and attenuating wave. If :math:`\sigma` = 0, the second term vanishes and the equations become a pure wave equation so that the energy propagates without loss. Alternatively, if the third term were zero, the equations reduce to the heat equation and the field is diffusive. This becomes clearer when the equations are transformed to the frequency-domain.

Wave equations in frequency-domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To get the frequency-domain wave equations, we use the Fourier transform using an :math:`e^{i\omega t}` time dependence. If we look at the derivative of :math:`e^{i\omega t}` with respect to time, we see that it is :math:`i\omega e^{i\omega t}`. Thus, we can easily convert Equations :eq:`hme7` and :eq:`hmh7` to the frequency-domain by replacing :math:`\partial/\partial t` with :math:`i \omega` and  :math:`\partial^2/\partial t^2` with :math:`-\omega^2`. The frequency-domain equations are then expressed as:

.. math::  \boldsymbol{\nabla}^2 \mathbf{E} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{E}  = 0
        :name: hme8

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{H}  = 0
        :name: hmh8

Equations :eq:`hme8` and :eq:`hmh8` can be be written in a simpler form:

.. math:: \boldsymbol{\nabla}^2 \mathbf{E} - k^2 \mathbf{E}  = 0

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} - k^2 \mathbf{H}  = 0

where :math:`k` is the wave number defined by

.. math:: k^2 = \mu \epsilon \omega^2 - i \mu \sigma \omega. 
        :name: ksquared

The behaviour of electromagnetic waves is governed by the relative values of the two terms that make up :math:`k^2`. If :math:`\sigma` = 0, the electromagnetic energy propagates as unattenuating waves in the medium. If the imaginary term dominates, then the waves diffuse as they propagate. The behaviour thus depends upon the ratio:

.. math:: \frac{ \mu \epsilon \omega^2}{\mu \sigma \omega} = \frac{\epsilon \omega}{\sigma} = \frac{2\pi \epsilon f}{\sigma}
        :name: kcomp

In many of the problems in geophysics, we deal with relatively low frequencies, :math:`f \lt 10^5` Hz. If the electric permittivity is that of free space, :math:`\epsilon = 8.85 \times 10^{-12}` F/m, and even if the electrical conductivity is small (:math:`10^{-4}` S/m), then this ratio becomes

.. math:: \frac{\mu \epsilon \omega^2}{\mu \sigma \omega} \approx \frac{(6.28)(8.85 \times 10^{-12})(10^{5})}{10^{-4}} = 0.06

This shows that even for quite high frequencies, the first part of :math:`k^2` will be substantially smaller for realistic earth conductivities. Thus, :math:`\mu \epsilon \omega^2 \lt\lt \mu \sigma \omega`. This means that displacement currents can be neglected and the wave equations can be simplified:

.. math::  \boldsymbol{\nabla}^2 \mathbf{E} - i \mu \sigma \omega \mathbf{E}  = 0
        :name: hme9

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} - i \mu \sigma \omega \mathbf{H}  = 0
        :name: hmh9

In time-domain, these equations become:

.. math::  \boldsymbol{\nabla}^2 \mathbf{e} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t}  = 0
        :name: hme10

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \mu \sigma \frac{\partial \mathbf{h}}{\partial t}  = 0
        :name: hmh10

Wave equation solution in 1D
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Equations :eq:`hme10` and :eq:`hmh10` are written in 1D as following:

.. math:: \frac{\partial^2 \mathbf{e}}{\partial z^2} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} = 0
        :name: hme11

.. math:: \frac{\partial^2 \mathbf{h}}{\partial z^2} - \mu \sigma \frac{\partial \mathbf{h}}{\partial t} = 0
        :name: hmh11

These are second-order linear differential equations which we can analytically solve for a solution. The solutions have a sinusoidal time-dependence :math:`e^{i\omega t}` and have two parts to decribe the up-going wave and the down-going wave. As this equations for the electric and magnetic field are identical, we will only carry through with the expression for the electric field. The same analysis can be done for the magnetic field.

The solution to Equation :eq:`hme11` is written as:

.. math:: \mathbf{e} = \mathbf{e}_p e^{-i(kz-\omega t)} + \mathbf{e}_n e^{i(kz-\omega t)}

Recall that the wavenumber is expressed as:

.. math:: k = \sqrt{\mu\epsilon\omega^2 - i\mu\sigma\omega}

which can be divided into a real and an imaginary component:

.. math:: k = \alpha - i\beta

According to :cite:`stratton1941`, :math:`\alpha` and :math:`\beta` are:

.. math:: \alpha = \omega \left ( \frac{\mu \epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right )^{1/2} + 1 \right ] \right )^{1/2}

.. math:: \beta = \omega \left ( \frac{\mu\epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right)^{1/2} - 1 \right ] \right ) ^{1/2}

However, when we ignore displacements currents, :math:`\alpha` and :math:`\beta` become identical, simple values.

.. math:: \alpha = \beta = \sqrt{\frac{\omega \mu \sigma}{2}}
        :name: ab

Taking a closer look at the wave going in the positive z-direction and using :math:`\alpha` and :math:`\beta` , we write:

.. math:: \mathbf{e} = \mathbf{e}_p e^{-i(kz-\omega t)}

.. math:: \mathbf{e} = \mathbf{e}_p e^{-ikz} e^{i\omega t}

.. math:: \mathbf{e} = \mathbf{e}_p e^{-i\alpha z} e^{i^2\beta z}  e^{i\omega t}

.. math:: \mathbf{e} = \mathbf{e}_p e^{-i\alpha z} e^{-\beta z}  e^{i\omega t}

From this final expression, a few conclusions can be made. Additionally, the analysis can be repeated for the magnetic field so that the final equations for both the electric and magnetic field are:

.. math:: \mathbf{e} = \mathbf{e}_p e^{-i\alpha z} e^{-\beta z}  e^{i\omega t}
        :name: hme12

.. math:: \mathbf{h} = \mathbf{h}_p e^{-i\alpha z} e^{-\beta z}  e^{i\omega t}
        :name: hmh12

First, the term :math:`e^{-\beta z}` decreases as :math:`z` increases because :math:`\beta` is real. This means that the wave attenuates as :math:`z` gets larger. This leads to the idea of skin depth, which is the depth where the amplitude of the electromagnetic wave has decreased by :math:`1/e`:

.. math:: \delta = \frac{1}{\beta} = \frac{1}{ \sqrt{\frac{\omega \mu \sigma}{2}}} = \sqrt{\frac{2}{\omega \mu \sigma}}

Knowing that :math:`\mu = 4\pi \times 10^{-7}` and :math:`\omega = 2\pi f`, we get the following expression for skin depth:

.. math:: \delta \approx 500 \sqrt{\frac{1}{f\sigma}} = 500 \sqrt{\frac{\rho}{f}},

where :math:`\rho` is the resistivity. Secondly, we can write:

.. math:: e^{-i\alpha z} = \cos{\alpha z} - i \sin{\alpha z},

which shows that the wave indeed varies sinusoidally in the :math:`z`-direction. The same thing can be done for :math:`e^{i\omega t}`, showing that the wave also varies sinusoidally with time.

Speed of light
^^^^^^^^^^^^^^

So far, we considered that :math:`\mu\epsilon\omega^2 \lt \lt \mu \sigma \omega` and ignored the displacements currents. However, in the case where :math:`\mu\epsilon\omega^2 \gt \gt \mu \sigma \omega`, Equations :eq:`hme7` and :eq:`hmh7` (or :eq:`hme8` and :eq:`hmh8` for the frequency-domain) become:

.. math::  \boldsymbol{\nabla}^2 \mathbf{e} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}  = 0
        :name: hme13

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}  = 0
        :name: hmh14

The following derivation will be the same for both the magnetic and electric fields. Let's use the magnetic field for this analysis. In 1D, Equation :eq:`hmh14` is now written as:

.. math:: \frac{\partial^2 \mathbf{h}}{\partial z^2} = \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2},
        :name: hmh15

for which there is a solution of the form:

.. math:: \mathbf{h} = \mathbf{h}_0 \sin \left ( 2\pi \frac{z-vt}{\lambda} \right ),
        :name: slwave

where :math:`v` is the speed of the sinosoidal wave and :math:`\lambda` is its wavelength. We can check this solution by taking the derivatives with respect to :math:`z` and :math:`t` to see if we get back to Equation :eq:`hmh15`.

.. math:: \frac{\partial^2 \mathbf{h}}{\partial z^2} = \frac{\partial}{\partial z} \left [ \mathbf{h}_0 \cos \left(  2\pi \frac{z-vt}{\lambda} \right) \left( \frac{2\pi}{\lambda}\right) \right ] = - \mathbf{h}_0 \sin \left(  2\pi \frac{z-vt}{\lambda} \right) \left( \frac{2\pi}{\lambda}\right)^2

.. math:: \frac{\partial^2 \mathbf{h}}{\partial t^2} =\frac{\partial}{\partial t} \left [ \mathbf{h}_0 \cos \left ( 2\pi \frac{z-vt}{\lambda} \right ) \left ( \frac{-2\pi v}{\lambda} \right) \right ] = - \mathbf{h}_0 \sin \left ( 2\pi \frac{z-vt}{\lambda} \right ) \left ( \frac{-2\pi v}{\lambda} \right)^2

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
