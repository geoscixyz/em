.. _dcr_index:

Direct Current Resistivity
==========================

- Intro:
	- brief overview of the experiment
	- applications
	- links to case-histories

 .. figure:: images/DCR_Intro.png
    :align: right
    :scale: 80% 
    :figwidth: 50%
    :name: DCR_intro

    Direct-Current Resisitivity (DCR)
    experiment showing current path and
    charge built up near a (a) conductive 
    and (b) resitive anomaly.


In a DC resistivity  (DCR) experiment a generator is used to inject current
into the earth. The path of the currents depends upon the variation of
resistivity{link}  or equivalently, its reciprocal, the electrical
conductivity {link}. Currents are channeled into good conductors and flow
around poor conductors. Electrical charges are built up on interfaces that
separate units of  different conductivity and these charges generate an
electric potential.  Data are acquired at the surface by measuring the
potential difference between two electrodes.  A generic  survey involving two
current and two potential electrodes is shown in :numref:`DCR_intro` for the case
of (a) a conductive and (b) a resistive unit in a uniform half-space.



The measured voltage depends upon the positions of the current and potential
electrodes with respect to the target as well as on the earth’s conductivity.
Obtaining information at the conductivity in lateral and vertical directions
requires many different locations for the electrodes and different geometries
are given different names. :numref:`DCR_TwoSpheres`. For visualization purposes, the observed
voltages are usually converted to apparent resistivities.{link} and data are
plotted in a  pseudosection format :numref:`DCR_AppRes`.  A typical pseudosection is
provided below.

 .. figure:: images/TwoSphere_model.png
    :align: center
    :scale: 80% 
    :name: DCR_TwoSpheres

    Two-spheres model with dipole-dipole configuration.

 .. figure:: images/TwoSphere_AppRes.png
    :align: center
    :scale: 80% 
    :name: DCR_AppRes

    Pseudo-section of apparent resistivity (log10).

Pseudosections are a valuable way to present data, especially if data have
been acquired along a single line, but extracting information about the
conductivity requires that the observations be inverted. {link}. The cross-
section below shows the 2D conductivity obtained by inverting the data shown
in :numref:`DCR_Inv2D`.

 .. figure:: images/TwoSphere_Inv2D.png
    :align: center
    :scale: 80% 
    :name: DCR_Inv2D

    Inverted 2D model.

.. toctree::
    :maxdepth: 1

    governing_equations
    field_acquisition
    data
    survey_design
    interpretation
    practical_considerations
    