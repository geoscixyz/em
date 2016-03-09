.. _bookpurnong_data:

Data
====

Here we make distinction bewteen "raw data" and "delivered data". Raw data are usually direct dump from the instruments, and may contain repeated measurements at the same location. For EM, the raw data are generally in the form of time series at a certain sampling rate. Then the raw data are processed by stacking, averaging, transforming, filtering, etc. The delivered data are usually in a reduced format of smaller size and higher signal noise ratio. In our framework, we consider "data" as "delivered data".

An important task in this particular step is to visualize the data. Data visualization serves several purposes:

(1) Understanding the underlying physics.

(2) Data quality control.

(3) Quanlitative interpretation.

(4) Quality control for advanced interpretation, e.g. predicted data in inversion.

Every datum point in an airborne EM survey can be specified using three parameters: the horizontal sounding location (easting and northing) and the time(t)/frequency(f). Using easting and northing as x and y respectively and time/frequency as z, a 3D data volume can be formed. So there are three ways of plotting data for airbrone EM survey:

(1) Map: contouring a particular time/freq as a function of the horizontal location. Slice the data volume horizontally. Spotting interesting area.

(2) Profile: plotting all or select time/freq along a flight line as a function of one horizontal dimension. Slice the data volume vertically. Compare time/freq along a transverse.

(3) Sounding: plotting data at a particular location as a function of time/freq. Drill the data volume vertically. 

The RESOLVE and SkyTEM data are presented in those three formats below.


RESOLVE
-------

The figure below is a map view of the RESOLVE data in ppm. The real and imaginary parts of 382 and 7970 Hz are shown. We can identify the area with relatively high responses (warm color) that are potentially associated with the saline water and low responses (cold color) for the fresher water. The strips are from the variation of flight height. 

.. figure:: ./images/booky-resolve1.jpg
    :align: left
    :scale: 80% 
    :name: booky-resolve1
    
One of the flight lines is chosen for the profile view below. We identify the location where high conductivity may exist. We note the 35920 and 130100 Hz data are very close, indicating the inductive limit was achieved. 

.. figure:: ./images/booky-resolve2.jpg
    :align: left
    :scale: 80% 
    :name: booky-resolve2

The sounding below is taken from a location on the floodplain. As the frequency increases, the imaginary part decreases and the real part increase. This is consistent with the typical response curve in the 3-loop tutorial. 

.. figure:: ./images/booky-resolve3.jpg
    :align: left
    :scale: 80% 
    :name: booky-resolve3


SkyTEM(HM)
----------

In a similar manner, we show the data on a map from four time channels. The high responses are likely to be associated with the salinization, compatible with the RESOLVE data map. The last time channel is very noisy, but we are still able to see a long-wavelength trend.

.. figure:: ./images/booky-skytem1.jpg
    :align: left
    :scale: 80% 
    :name: booky-skytem1

We also present multiple time channels along a flight line. The data set has relatively high overall quality, except some late times are a bit noisy. This plot help us find the appropriate noise floor.

.. figure:: ./images/booky-skytem2.jpg
    :align: left
    :scale: 80% 
    :name: booky-skytem2

A clean time transient decay is provided below. The variation of the decay rate in time indicates the Earth may contain a more conductive layer under the surface layer.

.. figure:: ./images/booky-skytem3.jpg
    :align: left
    :scale: 80% 
    :name: booky-skytem3
    
SkyTEM(LM)
----------    
    
TBD


