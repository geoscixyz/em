.. _uxo_pratical_considerations:

.. purpose::

	Here

Practical Considerations
========================

Geological responses and clutter items make UXO classification difficult because they mask the responses from targets and distort anomalies. Before attempting to locate and classify UXOs within a new area, work must be done to ensure the survey will produce successful results. In practice this is accomplished by:

	- Accurately characterizing the background response due to local geology and clutter.
	- Performing test surveys over seeded items to validate location and classification algorithms.

Characterizing the Background Response
--------------------------------------

An important aspect of UXO surveys is accurate characterization of the background response. By measuring the local background response, we can determine the nature and amplitude of signals which may mask responses from UXOs. In the case of geological responses, it may be possible to remove the background response and isolate the UXO's response. In the case of clutter items, characterization of the background response can be used to infer survey limitations; for example, the maximum depth at which a particular ordnance item can be classified with 100% certainty (detection assurance level).

Below, we show the background response due to clutter items and the responses over two identical UXOs a different depths. The shallow UXO produces a much higher amplitude anomaly than the deeply buried UXO. In the latter case, the amplitude of the background response is significant and distorts the TEM anomaly. 


.. figure:: images/data_practical_clutter.png
	:align: center
	:figwidth: 100%
	:name: fig_clutter_uxo

	Distortion of TEM anomalies due to clutter items at t = :math:`10^{-3}` s. (left) Background response. (center) Response over shallow UXO; z = -1 m. (right) Response over deep UXO; z = -2 m.

Test Survey over Seeded Items
-----------------------------







Once an instrument has been chosen and the survey designed, it may be beneficial to perform a test survey. During the test survey, a known ordnance item is buried within a test site. The proposed survey design is then used to locate and accurately classify the ordnance.

Test surveys are used to determine whether:

	1) the line and station spacings are sufficient.
	2) the detection assurance level is accurate.
	3) the current survey parameters can be used to accurately locate and classify ordnance items.




**If you want to get fancy, show that you were able to recover polarizations but not for the object at significant depth**.


.. figure:: images/practical_recovery.png
	:align: center
	:figwidth: 80%
	:name: fig_uxo_practical_recovery

	Successful (left) and unsuccessful (right) classification of seeded items. :math:`L1` is the true primary polarization, :math:`L2 = L3` are the true secondary polarizations and :math:`Lx, \; Ly` and :math:`Lz` are recovered polarizations.










From Laurens
------------

An important step in UXO data processing is visual quality control (QC) of the fit to each target. The example in Figure 4 represents the ideal case: a near-perfect fit to the data and an excellent correspondence between the estimated polarizabilities and expected values for the target’s class. However, feature estimation is often complicated by neighbouring target anomalies or low signal strength from small or deep (> 30 cm) targets. In these cases, the fit to the observed data will be affected by noise and recovered polarizabilities may be unreliable. Careful inspection of all fits by expert data analysts is essential to ensure that the field data for each target anomaly can support classification decisions. When data quality is poor for individual targets, the data may be reacquired or, in the worst case, the target must be dug as a precaution. With newer sensor data and careful field practices, the number of anomalies that cannot be analyzed is usually negligible (less than 1 % of the total).

