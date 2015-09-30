.. _introduction_notation:

Notation and Conventions
========================

We choose the notation set forth in [Ward_and_Hohmann]_; it is clean and unambiguous. Their chapter has
been the foundation of many research papers and is used by geophysicists world-
wide. 


- vectors and operators are bold:                          
    * e.g. \\(\\mathbf{v}\\), \\(\\mathbf{r}\\), \\(\\boldsymbol{\\nabla\\cdot}\\), \\(\\boldsymbol{\\nabla\\times}\\)                       
- time domain vector functions are lower case:       
	* i.e. \\(\\mathbf{b}\\), \\(\\mathbf{d}\\), \\(\\mathbf{e}\\), \\(\\mathbf{h}\\), \\(\\mathbf{j}\\) 
- frequency domain vector functions are upper case: 
	* i.e. \\(\\mathbf{B}\\), \\(\\mathbf{D}\\), \\(\\mathbf{E}\\), \\(\\mathbf{H}\\), \\(\\mathbf{J}\\) 
- tensors are lower case, bold and underlined:           
    * e.g. \\(\\mathbf{\\underline{\\mu}}\\), \\(\\boldsymbol{\\underline{\\sigma}}\\), \\(\\mathbf{\\underline{\\epsilon}}\\)
- scalar variables are lowercase:
	* e.g. \\(\\mu\\), \\(\\sigma\\), \\(\\epsilon\\), \\(\\omega\\), \\(t\\)  

We also adopt their choice of sign in the Fourier Transform: \\(e^{i\\omega t}\\) time dependence. 

 .. math::
    F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t} dt

    f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega




**References** 

.. [Ward_and_Hohmann] Ward, S. H., & Hohmann, W. (1988). *Electromagnetic Theory for Geophysical Applications Applications.* In Electromagnetic methods in applied geophysics (1st ed., pp. 130–311). Society of Exploration Geophysicists.
