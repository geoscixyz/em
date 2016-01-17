.. _introduction_notation:

Notation and Conventions
========================

We choose the notation set forth in :cite:`Ward1988`. Their chapter has
been the foundation of many research papers, is used by geophysicists world-
wide, and it is clean and unambiguous.

Vectors
-------

- vectors are bold:                          
    * ie. :math:`\mathbf{v}`, :math:`\boldsymbol{\nabla\cdot}`                       
- tensors are bold and underlined:           
    * ie. :math:`\mathbf{\underline{v}}`, :math:`\boldsymbol{\underline{\sigma}}`   
- time domain variable are lower case:       
    * ie. :math:`\mathbf{e}`, :math:`\mathbf{j}`, :math:`\mathbf{h}`, :math:`\mathbf{b}` 
- frequency domain variables are upper case: 
    * ie. :math:`\mathbf{E}`, :math:`\mathbf{J}`, :math:`\mathbf{H}`, :math:`\mathbf{B}`

Integrals
---------

- Integrating a scalar function over a volume:
    .. math::
        \int_V f ~dv

   or over a closed volume
    .. math::
        \oint_V f ~dv

- Integrating a vector function over a surface:
    .. math::
        \int_S \mathbf{f} \cdot \mathbf{da} = \int_S \mathbf{f} \cdot \mathbf{\hat{n}} ~da

   or over a closed surface:
    .. math::
        \oint_S \mathbf{f} \cdot \mathbf{da} = \oint_S \mathbf{f} \cdot \mathbf{\hat{n}} ~da

- Integrating a vector function over a line: 
    .. math::
        \int_C \mathbf{f} \cdot \mathbf{dl} = \int_C \mathbf{f} \cdot \mathbf{\hat{n}} ~dl

   or over a closed surface:
    .. math::
        \oint_C \mathbf{f} \cdot \mathbf{dl} = \oint_C \mathbf{f} \cdot \mathbf{\hat{n}} ~dl


.. _fourier_transform_convention: 

Fourier Transform Convention
----------------------------

We also adopt their choice of sign in the Fourier Transform: :math:`e^{i\omega t}` time dependence. 

 .. math::
    F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t} dt
    :name: fourier_transform_convention

.. math::
    f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega
    :name: inv_fourier_transform_convention



**References** 

 .. bibliography:: ../references.bib
    :style: alpha
    :encoding: latex+latin
    :filter: docname in docnames
