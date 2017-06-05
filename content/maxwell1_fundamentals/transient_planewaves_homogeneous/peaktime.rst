.. _transient_planewaves_homogeneous_peaktime:

Peak Time
=========

The peak time is the time at which the maximum signal amplitude is observed at a particular location. The peak time observed in :numref:`fig_planewaves_peaktime` (a) can be dervied by setting the time derivative of the analytic solution for :math:`E_x` to zero. Where:

.. math::
	e_x(t>0)  = E_{x,0}^- \frac{\big (\mu\sigma)^{1/2} z}{2\pi^{1/2} t^{3/2}} \, e^{-\mu\sigma z^2/4t}

is the quasi-static analytic solution, the peak time is given by:

.. math::
    t_{max} = \frac{\mu\sigma z^2}{6}
    :label: tmax

For an impulse excitation, the peak time is proportional to the square of the distance traveled.

.. figure:: images/Ward1988Fig1_2.png
   :align: center
   :scale: 40%
   :name: fig_planewaves_peaktime

   Electric field as a function of time 100 m from a 1D impulse in the field in a 0.01 S/m whole space (a). Electric field at t = 0.03 ms as a function of distance (Modifed from :cite:`ward1988`) (b).
