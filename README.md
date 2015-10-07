# GeoSci.xyz EM

[![Build Status](https://travis-ci.org/ubcgif/em.svg?branch=master)](https://travis-ci.org/ubcgif/em)

http://em.geosci.xyz

A resource for electromagnetic geophysics

**Resources for Contributors:**

Link for anaconda (python package manager):
- https://www.continuum.io/downloads

Here are a couple resources on sphinx and reStructured Text:

- http://sphinx-doc.org/markup/
- http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

and an overview of using GitHub:
- https://guides.github.com/activities/hello-world/

**Best practices for attribution:**

- https://wiki.creativecommons.org/wiki/Best_practices_for_attribution


**Notation:**

We choose the notation set forth  in Ward and Hohmann. Their chapter has been the foundation of many research papers, is used by geophysicists world-wide, and it is clean and unambiguous. 
 
- vectors are bold : 

    ```
    .. math:: 
        \mathbf{v}
    ```
  or for a symbol
    ```
    .. math::
        \boldsymbol{\nabla\cdot}
    ```
  
- tensors are bold and underlined :

    ```
    .. math::
        \mathbf{\underline{v}}
    ```
  or for a symbol
    ```
    .. math::
        \boldsymbol{\underline{\sigma}}
    ```
  
- time domain variable are lower case
- frequency domain variables are upper case
