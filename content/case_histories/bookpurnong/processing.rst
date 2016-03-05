.. _bookpurnong_processing:

Processing
==========

The primary goal of processing the raw data is to prepare the delivered data. The procedures usually involve considerations on the instrumentation and field operation. Examples are de-noising, leveling, smoothing, filtering, stacking, spatial and temporal corrections, convolution/deconvolution, transfer function estimation, etc. The readers are suggest to refer to the survey report or the field crew for more information.

From an interpreter's point of view, data processing is a step to examine and edit the data so it can be reliably interpreted in the next step. There are several major reasons why processing is necessary:

(1) Quality control. Data without quality or uncertainty assessment mean nothing. So it is important to know the overall quality of a data set. A data set may be deemed not suitable for interpretation if the noise level is too high. For most data sets, preliminary QC is carried out during acquisition. So the delivered data can still show useful signals in decent quality. But we still have to identify the "bad data". 

(2) Uncertainty analysis. Uncertainty is a quantitative way of assessing the data qiality. Data with greater noise may be assigned larger uncertainty. Most inversion programs need this information to decide how well the inversion wants to fit a particular datum.

(3) Data simplification. A data set can be difficult to interpret because of its size and noise. For example, the numerical modeling time is roughly proportional to the number of measurements in an airborne survey that has significant data redundancy. So it may be desired to down-sample the data set without losing information. And high-frequency noise associated with non-geologic objects can be effectively removed by low-pass filtering and other smoothing methods.

(4) Model parameterization. Any interpretation is based on models. By processing the data, we may choose more proper models. For example, negative transients in a central loop TEM survey indicate the existance of induced polarization. So we know at some places a real and time-independent conductivity model is not enough to explain the data. Another example is the variation of data in space may indicate the scale of EM induction, which helps the design of discretization for numerical modeling.


Processing of RESOLVE data
--------------------------


.. figure:: ./images/booky-resolveqc.jpg
    :align: left
    :scale: 80% 
    :name: booky-resolveqc


Processing of SkyTEM data
--------------------------

.. figure:: ./images/booky-skytemqc.jpg
    :align: left
    :scale: 80% 
    :name: booky-skytemqc


