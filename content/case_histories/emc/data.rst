.. _emc_data:

Data
====

The Z-axis tipper electromagnetic technique (ZTEM) is a natural source geophysical method. It is similar to the magnetotelluric method (MT) but only the magnetic fields are measured :cite:`lo08`. The vertical component of the magnetic field is recorded along flight lines while the horizontal field components are measured at a fixed reference station on the surface. Transfer functions relate the vertical components to the horizontal component as shown in Equation :eq:`emceq1`:

.. math:: \mathbf{H}_z (\mathbf{r}) = T_{zx} (\mathbf{r},\mathbf{r}_0) \mathbf{H}_x(\mathbf{r}) +  T_{zy} (\mathbf{r},\mathbf{r}_0) \mathbf{H}_y(\mathbf{r})
        :name: emceq1

Each tipper has an in-phase and a quadrature component. The data were collected by Geotech Ltd. in 2011 using a helicopter-based ZTEM and aeromagnetic system. The survey consisted of 200 line kilometers with 200 m spacing over a 38 square km area about 45 km east of Fallon, Nevada. There are approximately 20,000 data locations. The flight lines are shown in :numref:`emc2`. The in-phase and quadrature components of the tipper transfer functions are calculated from raw field data for siz frequencies ranging from 20 to 720 Hz. Preliminary processing such spike removal, attitude corrections, and filtering were applied to the data by Geotech.

Data were collected for six frequencies: 30, 45, 90, 180, 360, and 720 Hz. When comparing data maps between frequencies, the images are similar but smaller details change. :numref:`emc3` shoes the in-phase (real) and quadrature (imaginary) components of :math:`T_{zx}` and :math:`T_{zy}` for hte 30 Hz frequency in a local grid.

.. figure:: ./images/FIGURE_3.png
        :name: emc3
        :figwidth: 100%
        :align: left

        The four components of the lowest (30 Hz) frequency data are shown in (a)-(d).

First-hand ideas about the conductivity structures can be obtained by evaluating the data. ZTEM data over a conductive block will show a high and low anomaly while data over a halfspace or a layered earth will be zero. Therefore, we can expect little to no 3D conductivity structures in the eastern portion of the survey area as the tipper data is roughly zero to the east of 6000 m. In the western portion of the area, the real and imaginary component of :math:`T_{zx}` show a north-west trending anomaly while in the :math:`T_{zy}` components show anomalies of different shapes in the area. This shows the difference between the two tippers and the different magnetic field components they take use.

Despite getting a few initial ideas from the data, the data remain hard to interpret. The next page delves into :ref:`processing and inverting <emc_processing>` the data to better understand the conductivity.
