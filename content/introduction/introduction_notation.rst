.. _introduction_notation:

Notation and Conventions
========================

We choose the notation set forth in [Ward_and_Hohmann]_. Their chapter has
been the foundation of many research papers, is used by geophysicists world-
wide, and it is clean and unambiguous.


- vectors are bold:                          
    * ie. \\(\\mathbf{v}\\), \\(\\boldsymbol{\\nabla\\cdot}\\)                       
- tensors are bold and underlined:           
    * ie. \\(\\mathbf{\\underline{v}}\\), \\(\\boldsymbol{\\underline{\\sigma}}\\)   
- time domain variable are lower case:       
    * ie. \\(\\mathbf{e}\\), \\(\\mathbf{j}\\), \\(\\mathbf{h}\\), \\(\\mathbf{b}\\) 
- frequency domain variables are upper case: 
    * ie. \\(\\mathbf{E}\\), \\(\\mathbf{J}\\), \\(\\mathbf{H}\\), \\(\\mathbf{B}\\)


We also adopt their choice of sign in the Fourier Transform: \\(e^{i\\omega t}\\) time dependence. 

 .. math::
    F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t} dt

    f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega




**References** 

.. [Ward_and_Hohmann] Ward, S. H., & Hohmann, W. (1988). *Electromagnetic Theory for Geophysical Applications Applications.* In Electromagnetic methods in applied geophysics (1st ed., pp. 130–311). Society of Exploration Geophysicists.
