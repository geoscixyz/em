.. _em_index:

em.geosci
=========

..ToDo::
   Our front-cover image for em.geosci

**Purpose:** To facilitate the understanding and use of
electromagnetics in solving exploration, geotechnical and environmental
problems.

Society today faces many challenges in which geophysical remote sensing can play an important, and sometimes crucial, role. Problems might fall into categories of - Finding resources
- Natural hazards
- Geotechnical engineering
- Environmental problems
- Surface or underground storage 

..todo::
   use the images in the DL talk (and perhaps others, related to magnetic permeability and dielectric constant). Write a couple of sentences regarding what the problem is. Link these with the categories above. 


The usefulness of geophysics requires that the sought target or geologic structure has different physical properties than its surrounding host material. For many  of the problems listed above, the electromagnetic properties of earth materials can be diagnostic or at least they can provide a useful component of information. In reality, all of the problems are complicated and multi-disciplinary, and their solution will require a team of geoscientists and engineers to interact and meaningfully converse. Electromagnetics, in itself, should not be expected to provide a complete solution, but it can often play a significant role. An important goal of em.geosci is to help foster communication and elevate the state-of-practise of EM geophysics. By understanding the principles of electromagnetics and associated geophysical surveys, by linking that with informative case histories, incorporating interactive tools to explore the underlying physics, and connecting mathematics to numerical computations for forward modelling and inversion, we hope to increase the effectiveness of EM geophysics. By adopting an open-source approach we hope to capitalize on the experience and knowledge of practising geoscientists so that this resource can grow and benefit the community at large. 

Our emphasis is on fundamentals and applications and correspondingly `Case
Histories`_ play an essential role. These provide the motivation for using
electromagnetics and show the success, or not, of their application in making
an impact upon the problem at hand.

.. _Case Histories: http://case-histories.geosci.xyz

For the most part, rigorous analytic solutions of the EM
problems with specific transmitting fields and earth models is left to
existing books and research papers. Also, this resource does not concentrate
upon the scientific computing aspects to numerically solve Maxwell’s
equations. We do however, make much use of software that can perform those
functions. Rather, our emphasis is on using analytic and numerical solutions
to understand electromagnetic  fields and fluxes obtained from various types
of transmitters in different geological environments.





How to use this resource
------------------------

There are multiple ways to use em.geosci. It might be to ask a question like "what is :ref:`Faraday's law<faraday>`?" or "How does an electromagnetic wave decay as it propagates?". Or, perhaps information about a geophysical survey (instrumentation, data acquisition, processing) is sought; or it might be a desire to find a  :ref:`Case Histories<case_histories_index>` about the use of geophysics in solving applied problems. 

These objectives are interconnected and the sequence in which the questions
are asked will depend upon the problem. The advantage of a digital resource is
that essential elements can be linked; so starting at a :ref:`Case History<case_histories_index>` for
mineral exploration might lead to querying what a time domain survey is and
this might bring the reader back to :ref:`Faraday's law<faraday>`. Alternatively, in the
presentation of Faraday's Law, there are links to time domain surveys and also
links to case history examples.The exact organizational structure of the menu is therefore inconsequential. Nevertheless, we have attempted to organize topics into self-contained groups. Each section begins with on overview that can help
guide the reader.

A major component of learning is the ability to interact with material, that
is, to engage with the concepts that are being presented. Throughout the
resource we have embedded python notebooks that will allow the user to observe
results after changing parameters. In addition, through Examples, the user
will be able to interface with SimPEG_, our open-source modelling and
simulation package, so that he/she can generate their own codes and test
results or carry out further exploration of a topic.
Examples are available through `Jupyter Notebooks`_ and can be run through Binders_

.. image:: http://mybinder.org/badge.svg 
   :target: http://mybinder.org/repo/ubcgif/em_examples
   :align: center

.. _Jupyter Notebooks: http://github.com/ubcgif/em_examples
.. _Binders: http://mybinder.org/repo/ubcgif/em_examples

This resource is Open Source and while currently being developed by brilliant
and enthusiastic graduate students and faculty at UBC, the vision is to have
experts, worldwide, contribute. Join the development on github_.

.. _github: https://github.com/ubcgif/em


.. _SimPEG : http://simpeg.xyz






Contributors:
-------------

.. include:: AUTHORS.rst


Contents:
---------

.. toctree::
   :maxdepth: 6
   :name: `EM GeoSci`

   content/introduction/index
   content/physical_properties/index
   content/maxwell1_fundamentals/index
   content/maxwell2_dc/index
   content/maxwell3_fdem/index
   content/maxwell4_tdem/index
   content/geophysical_surveys/index
   content/case_histories/index
   content/equation_bank
   content/references





