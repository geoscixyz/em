
Snell's law and Fresnel equatoins
=================================

.. purpose::

    EM waves are reflected and refracted at a plane interface. Two essential items to understand them are: a) angular relationship and b) amplitude of plane waves at each media. a) Snell's Law and b) Fresnel equations respectively provide those information hence we introduce them, and understand. 

Set up
------

At the out set we shall treat reflection of a uniform, linearly polarized, homogeneous, plane wave. :numref:`snellslaw_setup` shows two media of electrical parameters, :math:`\sigma_1`, :math:`\mu _1`, :math:`\epsilon_1` and :math:`\sigma_2`, :math:`\mu _2`, :math:`\epsilon_2` are in contact at an infinite plane surface :math:`S`. A uniform, homogeneous plane wave is propagated in the incident dirction denoted by the vector wavenumber :math:`\mathbf{k}_i` or by the angle of incidence :math:`\theta_i`. The vector :math:`\mathbf{k}_i` is confined to :math:`x\text{-}z` plane. The wave is reflected in the direction denoted by :math:`\mathbf{k}_r` or by the angle :math:`\theta_r`; it is also transmitted into the second medium in the direction denoted by :math:`\mathbf{k}_t` or :math:`\theta_t`.

For a uniform, homogenous, plane wave, :math:`\mathbf{E}`, :math:`\mathbf{H}`, and the direction of propagation are orthogonal to one another such that :math:`\mathbf{E} \times \mathbf{H} = \mathbf{k}`.


.. figure:: images/snellslaw_setup.png
   :align: center
   :scale: 40%
   :name: snellslaw_setup

   Incident :math:`\mathbf{k}_i`, reflected :math:`\mathbf{k}_r`, and transmitted :math:`\mathbf{k}_t` wave vectors at a plane interface S. the angles of incidence, relfection, and trasnmission are :math:`\theta_i`, :math:`\theta_r`, and :math:`\theta_t`, respectively. The unit normal to the surface :math:`S`, separating medium from the medium is denoted by :math:`\hat{\mathbf{n}}`. Modified from citeWH Figure 3.1.

The unit vector :math:`\hat{\mathbf{n}}` in :numref:`snellslaw_setup` is normal to the plane :math:`S`. If :math:`\mathbf{r}` is a position vector drawn from the origin :math:`O` to anyh point in either medium 1 and 2, then for any point in the plane S, 

.. math::

    \hat{\mathbf{n}} \cdot \mathbf{r} = 0.

In followings, rather than developing details of both Snell's law ans Fresnel equations, we provide required items to derive both of them, then directly introduce final form of equations and discuss them. 

.. _snells_law:

Snell's law
-----------

Snell's law determines 
Required information to derive Snell's law are:

- General solution of EM fields for plane wave, for instance for the incident electic field:

.. math::
    ^i\mathbf{E} = \mathbf{E}_i e^{-\imath \mathbf{k}_i \cdot \mathbf{r}} 

- Continuity of tangental :math:`\mathbf{E}` and :math:`\mathbf{H}` at the plane, :math:`S`:

.. math::
    \hat{\mathbf{n}} \times (^i\mathbf{E}+^r\mathbf{E}) = \hat{\mathbf{n}} \times ^t\mathbf{E}

- Relationship between :math:`\mathbf{E}` and :math:`\mathbf{H}` for plane waves:

.. math::
    \mathbf{E} \times \mathbf{H} = \mathbf{k}

.. note::

    Using above three items, we can derive Snell's law of reflection and refraction, respectively:

    .. math::
        \text{sin} \ \theta_i = \text{sin} \ \theta_r

    .. math::
        k_i \text{sin} \ \theta_i = k_t \text{sin} \ \theta_t

    or 

    .. math::
        k_1 \text{sin} \ \theta_i = k_2 \text{sin} \ \theta_t

where :math:`k_i=k_r=k_1` and  :math:`k_t=k_2` are the complex scalar wave numbers in medium 1 and 2, respectively. 

The first equation explain incident and reflection angles are same, and the second equation describe how transmission angle is determined due to different electrical properties merged in :math:`k_1` and :math:`k_2`. 

.. note::

    At an air-earth interface, consider incident angle :math:`\theta_i` of 45 :math:`^{\circ}` and 5 :math:`^{\circ}`, and compute transmission angle. Here we let :math:`\epsilon_1=\epsilon_2=\epsilon_0`, :math:`\mu_1=\mu_2=\mu_0`, and :math:`\sigma_1=0` and :math:`\sigma_2=0.01` S/m

    What did you identify? See XXX for the answers.



.. _fresnel_equations:

Fresnel equations
-----------------
    
