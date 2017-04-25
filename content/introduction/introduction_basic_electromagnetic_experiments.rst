.. _introduction_basic_electromagnetic_experiments:

Basic Electromagnetic Experiments
=================================

In :ref:`Case Histories <case_histories_index>` we present a number of problems of
relevance to today's society. In most of those problems there is a requirement
to determine what is beneath the surface without direct sampling. This is the
realm of geophysics. In a generic geophysical survey, as shown in Figure XXXX, 
energy is input to the
ground. This energy propagates through the subsurface and signals are
recorded. We briefly discuss each of the elements involved in a generic geophysical survey below.

:ref:`Physical properties<physical_properties_index>` : Earth materials can be characterized in terms of their physical properties.
The properties of relevance to electromagnetics are:

- :ref:`electrical conductivity <electrical_conductivity_index>`
- :ref:`magnetic permeability <magnetic_permeability_index>`
- :ref:`dielectric permittivity <dielectric_permittivity_index>`

The success of a geophysical survey depends upon how the physical properties
of a sought target or geologic structure differ from the background host
material. If difference exist, then a particular geophysical survey that is
sensitive to that physical property can be selected. In :ref:`Case Histories
<case_histories_index>` the reader is invited to view each of the problems and
determine which of the above properties, or any, might be useful. Making this
connection is the most crucial element in the successful use of geophysics.

**Source:** A source  provides initial energy that will excite the earth. We are
interested only in sources for electromagnetic energy. Man-made sources
involve electrical currents that are either injected into the earth or flow in
a wire-loop. "Natural" sources refer to the energy fields that arise from the
earth and its environment. For example, the solar wind and its interation with
our magnetosphere, or the generation of magnetic fields due to the geomagnetic
dynamo in the Earth's core.  The input signals to the earth can be harmonic or
transient. Correspondingly the equations that propagate the energy through the
earth are FDEM (Frequency Domain ElectroMagnetic) or TDEM (Time Domain
ElectroMagnetic). The way in which this energy propagates depends upon how the
physical properties vary inside the earth.

**Data:** The electromagnetic fields at the earth's surface are recorded by
"electromagnetic sensors" or "receivers". The receivers can be in the air, on
the surface or undergound. The data, which are components of the magnetic or
electric fields, contain information about the physical properties through
which they travelled.


 .. figure:: images/geophysics.png
    :scale: 40%
    :align: center
    :name: basic_geophysics

    Sources provide energy to excite the earth. Responses depend upon the physical properties and contrasts in the subsurface. We measure responses at the surface to generate data.

Although the data contain information about the subsurface, subsequent
processing and inversion are required to extract meaningful information. This
is conceptualized in :numref:`basic_inversion`. The item "Forward" refers to
predicting the electromagnetic responses from the survey when the physical properties are
known. The item "Inverse" refers to the procedure for generating a physical
property distribution that explains the observations.


 .. figure:: images/inversionclouds.png
    :scale: 40%
    :align: center
    :name: basic_inversion


    Forward problems predict data given a model, and inverse problems aim to find a model given data.


