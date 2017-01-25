.. _ztem_data:

Data
====

ZTEM data consists of the vertical magnetic field :math:`\mathbf{H}_z` collected along survey lines with an airborne system. The horizontal magnetic fields :math:`\mathbf{H}_x` and :math:`\mathbf{H}_y` are measured at a referecen station on the ground. Generally, the reference station is placed in a location where the earth structure is 1D.

Similar to the :ref:`measured MT data <mt_data>`, the ZTEM system records a time-series of the magnetic field. The data are then binned and processed to generate transfer functions in the frequency domain :cite:`holtham2010`. For more information about converting the time-series into frequency domain, see the :ref:`MT data page <mt_data>`.

Similar to MT which uses the impedance, ZTEM data or tipper data are transfer functions. For this method, the transfer functions are calculated from relating the vertical magnetic field at locations :math:`\mathbf{r}` and the horizontal magnetic fields at the base station located at :math:`\mathbf{r}_0`. :

.. math:: \mathbf{H}_z (\mathbf{r}) = T_{zx}(\mathbf{r},\mathbf{r}_0) \mathbf{H}_x (\mathbf{r}_0) + T_{zy}(\mathbf{r},\mathbf{r}_0) \mathbf{H}_y (\mathbf{r}_0)
        :name: eqn_ztem_tipper

By taking the ratios of the vertical and horizontal fields, the influence of the unknown source field is removed (similar to the :ref:`MT method <mt_data>`). 

In order to solve Equation :eq:`eqn_ztem_tipper`, two independent polarizations are required:

.. math:: \mathbf{H}_{z1} (\mathbf{r}) = T_{zx} \mathbf{H}_{x1} + T_{zy} \mathbf{H}_{y1}

.. math:: \mathbf{H}_{z2} (\mathbf{r}) = T_{zx} \mathbf{H}_{x2} + T_{zy} \mathbf{H}_{y2}

The transfer functions are then solved for as following:

.. math:: T_{zx} = \frac{\mathbf{H}_{y2} \mathbf{H}_{z1} - \mathbf{H}_{y1} \mathbf{H}_{z2}}{\mathbf{H}_{x1}\mathbf{H}_{y2} - \mathbf{H}_{x2}\mathbf{H}_{y1}}

.. math:: T_{zy} = \frac{-\mathbf{H}_{x2} \mathbf{H}_{z1} + \mathbf{H}_{x1} \mathbf{H}_{z2}}{\mathbf{H}_{x1}\mathbf{H}_{y2} - \mathbf{H}_{x2}\mathbf{H}_{y1}}

The transfer functions are complex and thus have both a real and an imaginary component.

Consider the example below where a conductive block is buried in a uniform halfspace. The tipper data are forward modelled and the real and imaginary components of :math:`T_{zx}` and :math:`T_{zy}` are shown in Figure :numref:`img_ztem_data`. In each case, the data contain a high and low peak over the conductive block and the orientation of the anomaly depends on which transfer function is plotted.

.. figure:: images/ztem_data.png
        :name: img_ztem_data
        :align: center
        :figwidth: 80%

        Real and imaginary components of tipper data for a conductive block in a halfspace.

.. todo:: explain that data are zero over a halfspace/1D earth


