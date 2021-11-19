.. _apps_index:

Apps
====

To augment the content in EM GeoSci, a number of `Jupyter
Notebook <http://jupyter.org>`_ apps have been developed.
There are two categories of notebooks

- :ref:`EM Apps <em-apps>`
    - **Purpose:** To provide an interactive way to explore fundamentals of EM geophysics

- :ref:`Simulation Notebooks <simulation_notebooks>`
    - **Purpose:** To be a starting point for getting up and running with the EM Module of SimPEG for performing numerical simulations and inversions

If you run into any issues, please let us know at: http://github.com/geoscixyz/em-apps.


.. _em-apps:

EM Apps
-------

.. image:: https://mybinder.org/badge.svg
    :target: https://mybinder.org/v2/gh/geoscixyz/em-apps/main?filepath=index.ipynb
    :alt: Binder

.. image:: images/DC_LayeredEarth_notebook.png
    :width: 45%
    :alt: dc-layered-earth-app
    :align: right

There are a few ways you can run the notebooks. We provide instructions using:

- :ref:`Binder <binder>` (free, no login required)

Alternatively, they can be downloaded from GitHub and run locally.
Please see instructions at: https://github.com/geoscixyz/em-apps



.. _jupyter_notebooks:

Jupyter Notebooks
^^^^^^^^^^^^^^^^^

Within the Jupyter Notebook environment, you can use :code:`shift + enter` to run
each cell of code, or from the menu, select :code:`cell, run all`

.. image:: images/run_all_cells.png


.. _binder:

Binder
^^^^^^

.. image:: https://mybinder.org/badge.svg
    :target: https://mybinder.org/v2/gh/geoscixyz/em-apps/main?filepath=index.ipynb
    :alt: Binder


1. Launch the binder by clicking on the badge above or going to: https://mybinder.org/v2/gh/geoscixyz/em-apps/main?filepath=index.ipynb.
   This can sometimes take a couple minutes, so be patient...

2. Select the notebook of interest from the contents

3. :ref:`Run the Jupyter notebook <jupyter_notebooks>`

.. image:: images/binder-steps.png
    :alt: binder-steps
    :width: 100%
    :align: center




.. _simulation_notebooks:

Simulation Notebooks
--------------------


.. image:: ./images/FDEM_sounding_over_sphere.png
    :width: 45%
    :alt: dc-layered-earth-app
    :align: right

.. image:: https://mybinder.org/badge.svg
    :target: https://mybinder.org/v2/gh/simpeg/em-notebooks/master?filepath=index.ipynb
    :alt: Binder

These notebooks walk through forward simulations of both frequency domain
electromagnetics and time domain electromagnetics using `SimPEG <http://simpeg.xyz>`_.

See the above instructions to run the notebooks from Binder.

- :ref:`Binder <binder>` (free, no login required): https://mybinder.org/v2/gh/simpeg/em-notebooks/master?filepath=index.ipynb

Alternatively, they can be downloaded from GitHub and run locally.
Please see instructions at: https://github.com/simpeg/em-notebooks

Further examples and documentation are available at http://simpeg.xyz.
