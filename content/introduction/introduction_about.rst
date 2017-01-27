:orphan:


.. _introduction_about:

Why em.geosci?
==============



What is em.geosci?
------------------

em.geosci is a conglomeration of pieces of information, stored on the cloud
using Github_, and currently organized through `Read-the-docs`_. It uses ( `Juypter
notebooks <https://github.com/geoscixyz/em_apps>`_). It is an out-growth of the EM group at UBC-GIF
with a goal to capture our historic EM achievements and knowledge, make it
available to members of the group, expand its reach to individuals and groups
outside UBC and obtain participation from outside UBC.  It interfaces with our
other open-source software (`gpg.geosci.xyz <http://gpg.geosci.xyz>`_
which  provides an introduction to the
use of geophysics for geoscientists; and SimPEG_ which is an open-source
forward simulation and parameter estimation resource).

.. _SimPEG: http://simpeg.xyz

.. _Read-the-docs: https://docs.readthedocs.io/en/latest/index.html

How is it organized?
--------------------

The motivation for the structure of em.geosci follows from
:ref:`introduction_basic_electromagnetic_experiments`. The goal is to identify
topics that are logically self-contained and then use links to connect them.
At the large scale we have the following items.

- :ref:`introduction_index`:
  Provides motivational examples, outlines the site, takes care of housekeeping
  items like notation

- :ref:`physical_properties_index`:
  Is the "go-to" location for information about what the properties are, how
  they are measured, typical values etc.

- :ref:`maxwell1_fundamentals_index`:
  This contains items that relate to the general understanding of Maxwell's
  equations and how they are solved. Topics are general and not survey specific.
  (eg  the basic equations, interface conditions, concepts of fields and fluxes,
  plane waves in homogeous media, fields from electric and magnetic dipoles etc.
  )

- :ref:`maxwell2_static_index`:
  This section pertains to the understanding the steady-state Maxwell's and its
  applications. Foundations for DC resistivity (DCR); Magnetometric resistivity
  (MMR), and magnetic surveys are found here.

- :ref:`maxwell3_fdem_index`:
  This section pertains to understanding Maxwell's equations in the frequency
  domain. Foundations for galvanic, inductive and natural source surveys in
  frequency are presented.

- :ref:`maxwell4_tdem_index`:
  This section pertains to understanding Maxwell's equations in the time domain.

- :ref:`geophysical_surveys_index`:
  Self-contained folders for individual geophysical surveys are provided. For
  example DCR provides a comprehensive overview about the DC resistivity survey
  as well as links to case histories. Each Survey is linked to relevant sections
  in other portions of em.geosci so that comprehensive knowledge can be
  accessed.

- :ref:`inversion`:
  This provides basic tutorial information about inversion that is applicable to
  all em surveys.

- :ref:`case_histories_index`:
  These form the cornerstones of our site. They motivate the use of EM
  geophysics and they also dictate what material needs to be developed in the
  background sections. Each case history is presented with a Seven-Step
  Framework.

- `Examples`_:
  These notebooks or script-codes are provided so that the user can experiment
  with parameters and ask "what if" questions. For instance, in DCR, with a
  grounded source, it is of interest to see how the earth currents flow in the
  presence of a conductive or resistive body. To keep material organized, most
  of the code in the examples, is stored on SimPEG_.

.. _Examples: http://mybinder.org/repo/geoscixyz/em_apps

.. _Github: https://github.com/geoscixyz/em
.. _SimPEG: http://simpeg.xyz

How to contribute?
------------------

We are still developing the site and are making it available on an "as-is"
basis. You are free to download and use anything on the site subject to
appropriate attributions. Everything is developed  under `Creative Commons
Attribution 4.0 International License`_. We welcome feedback about the
useability of the site and the technical details.

.. _Creative Commons Attribution 4.0 International License: https://creativecommons.org/licenses/by/4.0/


