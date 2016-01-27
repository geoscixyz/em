.. _waveNumber:

Wave Number
==========

.. :math:`\Phi_{\mathbf{B}}`

.. math::
    \nabla \times {\bf E} = - \, i \omega \mu {\bf H}
    :label: faradays_law_diff_freq

.. math::
    \nabla \times {\bf H} = \sigma {\bf E} + i \omega \epsilon {\bf E} \\
    = \left(\sigma + i \omega \epsilon\right){\bf E} \\
    = \hat{\sigma} {\bf E} 
    :label: Amperes_law_diff_freq_freqDepSigma   

:math:`\hat{\sigma}` is the complex conductivity

Source free region, neglecting derivative of displacement current.


.. math::
    \frac{1}{\hat{\sigma}} \nabla \times {\bf H} =  {\bf E} 

Taking the curl of both sides

.. math::
    \nabla \times \frac{1}{\hat{\sigma}} \nabla \times {\bf H} =  \nabla \times {\bf E} \\
    = - \, i \omega \mu {\bf H}

In a region with constant constant physical properties :math:`\hat{\sigma}` and :math:`\mu`

.. math::
    \nabla \times  \nabla \times {\bf H} = - \, i \omega \mu \hat{\sigma} {\bf H}

Using the vector identity :math:`\nabla \times \left( \nabla \times {\bf A} \right) = \nabla \left( \nabla \cdot {\bf A} \right) - \nabla^2 {\bf A}` 

.. math::
    \nabla \times \left( \nabla \times {\bf H} \right) = \nabla \left( \nabla \cdot {\bf H} \right) - \nabla^2 {\bf H} \\
    :label: curl_ampere

Since :math:`\nabla \cdot {\bf B} = 0`, and :math:`\nabla \cdot \mu {\bf H} = \mu \cdot {\bf H} = 0`.

Then equation :eq:`curl_ampere` simplifies to,

.. math::
    \nabla^2 {\bf H} - i \omega \mu \hat{\sigma} {\bf H} = 0

This can be written in the form of a Helmholtz Equation

.. math::
    \nabla^2 {\bf H} + k^2 {\bf H} = 0

where the wave number (:math:`k`) has the following form.

.. math:: 
    k = \left( \omega^2 \mu \epsilon - i \omega \mu \sigma \right)^{1/2}



In free space (or in air where :math:`\sigma \approx 0` S/m) 

.. math::
    k_o = \sqrt{\omega^2 \mu_o \epsilon_o}

The wave number can be related to the speed of light (:math:`c`) in free space. Since :math:`c^2 = \frac{1}{\mu_o \epsilon_o}`

.. math::
    k_o = \frac{\omega}{c}


In earth materials :math:`\omega^2 \mu \epsilon` is typically much smaller than :math:`i \omega \mu \sigma`. 
Under these circumstances :math:`k` can be approximated by

.. math::
    k \approx \sqrt{- \, i \omega \mu \sigma}







