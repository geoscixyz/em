
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

Snell's law determines angular relationship between incident, refelcted, and refracted plane waves at an interface separating two medium having different electrical properties. Required information to derive Snell's law are:

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
        :label: snellslaw_1

    .. math::
        k_i \text{sin} \ \theta_i = k_t \text{sin} \ \theta_t

    or

    .. math::
        k_1 \text{sin} \ \theta_i = k_2 \text{sin} \ \theta_t
        :label: snellslaw_2

where :math:`k_i=k_r=k_1` and  :math:`k_t=k_2` are the complex scalar wave numbers in medium 1 and 2, respectively.

The first equation explain incident and reflection angles are same, and the second equation describe how transmission angle is determined due to different electrical properties merged in :math:`k_1` and :math:`k_2`.

.. question::

    - At an air-earth interface, consider incident angle :math:`\theta_i` of 45 :math:`^{\circ}` and 5 :math:`^{\circ}`, and compute amplitude of transmission angle :math:`|\theta_t|`. Here we let :math:`\epsilon_1=\epsilon_2=\epsilon_0`, :math:`\mu_1=\mu_2=\mu_0`, and :math:`\sigma_1=0` and :math:`\sigma_2=0.01` S/m

    - What can you infer from computed :math:`|\theta_t|`?


.. _fresnel_equations:

Fresnel equations
-----------------

We turn our attention to the Fresnel equations which interrelate the amplitudes of the :math:`\mathbf{E}` and :math:`\mathbf{H}`. As before, we consider reflection and refraction of uniform plane wave at an inteface :math:`S` as described in :numref:`snellslaw_setup`.

Two different modes will be considered: a) :math:`\mathbf{E}_i` normal to the plane of incidence and b) :math:`\mathbf{E}_i` in the plane of incidence. :numref:`fresnel_setup_TE` and :numref:`fresnel_setup_TM` correspondingly show each mode.

.. note::

    Each mode is often called a) Transverse Electric (TE or TE :sub:`z`) and b) Tranverse Magnetic (TM or TM  :sub:`z`) because either electric or magnetic field is transverse to :math:`z`-direction.

We exploit either electric or magnetic field transverse to :math:`z` to derive Fresnel equations for each mode. This feature makes a simplified situtuation for instance in the case a), we only have tangential component of electric field. For b), similarly, we only have have tangential component of magnetic field. This principal difference will make different reflection and refraction features for a) and b).

:math:`\mathbf{E}_i` normal to the plane of incidence (TE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/fresnel_setup_TE.png
   :align: center
   :scale: 30%
   :name: fresnel_setup_TE

   the relative orientations of the :math:`\mathbf{E}`, :math:`\mathbf{H}`, and :math:`\mathbf{k}` vectors for relflection at a plane interface when :math:`\mathbf{E}_i` is normal to the plane of incidence.

We want to derive relflection and trasnmission coefficents of the electric fields for TE mode (:numref:`fresnel_setup_TE`):

.. math::
    r_{TE} = \frac{\mathbf{E}_r}{\mathbf{E}_i}

.. math::
    t_{TE} = \frac{\mathbf{E}_t}{\mathbf{E}_i}


Required information to derive amplitude relationship between :math:`\mathbf{E}_i`, :math:`\mathbf{E}_r` and :math:`\mathbf{E}_t` are:

- Transverse electric field to :math:`z` (:math:`\hat{\mathbf{n}}`):

.. math::
    \hat{\mathbf{n}} \cdot \mathbf{E}_i = \mathbf{k}_i \cdot \mathbf{E}_i = 0

and

.. math::
    \hat{\mathbf{n}} \cdot \mathbf{E}_t = \hat{\mathbf{n}} \cdot \mathbf{E}_r = 0

- Tangential electric field is continuous at :math:`S`

- Snell's Law shown in Eqs. :eq:`snellslaw_1` and :eq:`snellslaw_2`

From above relationships, we can derive below equations:

.. math::
    \mathbf{E}_i + \mathbf{E}_r = \mathbf{E}_t
    :label: TE_fresnel1

.. math::
    \text{cos} \theta_i \mathbf{E}_i - \text{cos} \theta_r \mathbf{E}_r
    = \frac{\mu_1 k_2}{\mu_2 k_1} \text{cos} \theta_t \mathbf{E}_t
    :label: TE_fresnel2

Rearranging Eqs. :eq:`TE_fresnel1` and :eq:`TE_fresnel2` yields

.. math::
    \mathbf{E}_r = \frac{\mu_2 k_1 \text{cos} \theta_i - \mu_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}}
    {\mu_2 k_1 \text{cos} \theta_i + \mu_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}} \mathbf{E}_i
    :label: TE_EiandEr

.. math::
    \mathbf{E}_t = \frac{2\mu_2 k_1 \text{cos} \theta_i}
    {\mu_2 k_1 \text{cos} \theta_i + \mu_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}} \mathbf{E}_t
    :label: TE_EiandEt

where

.. math::
    \text{cos}^2 \theta_t  = 1 - \text{sin}^2 \theta_t = 1-\Big(\frac{k_1}{k_2}\Big) \text{sin}^2 \theta_i

Reflection and transmission coefficients for TE mode can be written as

.. math::
    r_{TE} = \frac{\mathbf{E}_r}{\mathbf{E}_i}
           = \frac{\mu_2 k_1 \text{cos} \theta_i - \mu_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}}
    {\mu_2 k_1 \text{cos} \theta_i + \mu_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}}
    :label: rTE_theta

.. math::
    t_{TE} = \frac{\mathbf{E}_t}{\mathbf{E}_i}
           = \frac{2\mu_2 k_1 \text{cos} \theta_i}
    {\mu_2 k_1 \text{cos} \theta_i + \mu_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}}
    :label: tTE_theta

Subsitituting

.. math::
    u_1 = k_1 \text{cos} \theta_i
    :label: u1

.. math::
    u_2 = (k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}
    :label: u2

then :math:`r_{TE}` and :math:`t_{TE}` can be written

.. math::
    r_{TE} = \frac{\mu_2 u_1 - \mu_1 u_2}
    {\mu_2 u_1 + \mu_1 u_2}
    :label: rTE_u

.. math::
    t_{TE} = \frac{2\mu_2 u_1}
    {\mu_2 u_1 + \mu_1 u_2}
    :label: tTE_u

.. note::

    In the final form of :math:`r_{TE}` and :math:`t_{TE}` shown in Eqs :eq:`rTE_u` and :eq:`tTE_u`, angular information is merged into :math:`u_1` and :math:`u_2`, which are scalar wavenumbers in :math:`z`-direction. Namely, horizontal component of the wavenumber do not make any impact to determine :math:`r_{TE}` and :math:`t_{TE}`, and this is driven by transverse electic field to :math:`z`-direction.


:math:`\mathbf{E}_i` is in the plane of incidence (TM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/fresnel_setup_TM.png
   :align: center
   :scale: 30%
   :name: fresnel_setup_TM

   the relative orientations of the :math:`\mathbf{E}`, :math:`\mathbf{H}`, and :math:`\mathbf{k}` vectors for relflection at a plane interface when :math:`\mathbf{E}_i` is in the plane of incidence.

Similarly, we want to derive relflection and trasnmission coefficents of the electric fields for TM mode (:numref:`fresnel_setup_TM`):

.. math::
    r_{TM} = \frac{\hat{\mathbf{n}}\times \mathbf{E}_r}{\hat{\mathbf{n}}\times \mathbf{E}_i}
    :label: rTM

.. math::
    t_{TM} = \frac{\hat{\mathbf{n}}\times \mathbf{E}_t}{\hat{\mathbf{n}}\times \mathbf{E}_i}
    :label: tTM


Required information to derive amplitude relationship between :math:`\mathbf{H}_i`, :math:`\mathbf{H}_r` and :math:`\mathbf{H}_t` are:

- Transverse magnetic field to :math:`z` (:math:`\hat{\mathbf{n}}`):

.. math::
    \hat{\mathbf{n}} \cdot \mathbf{H}_i = \mathbf{k}_i \cdot \mathbf{H}_i = 0

and

.. math::
    \hat{\mathbf{n}} \cdot \mathbf{H}_t = \hat{\mathbf{n}} \cdot \mathbf{H}_r = 0

- Tangential magnetic field is continuous at :math:`S`

- Snell's Law shown in Eqs. :eq:`snellslaw_1` and :eq:`snellslaw_2`

From above relationships, we can derive below equations:

.. math::
    \mathbf{H}_i + \mathbf{H}_r = \mathbf{H}_t
    :label: TM_fresnel1

.. math::
    \text{cos} \theta_i \mathbf{H}_i - \text{cos} \theta_r \mathbf{H}_r
    = \frac{\mu_1 k_2}{\mu_2 k_1} \text{cos} \theta_t \mathbf{H}_t
    :label: TM_fresnel2

Rearranging Eqs :eq:`TE_fresnel1` and :eq:`TE_fresnel2` yields

.. math::
    \mathbf{H}_r = -\frac{\mu_2 k_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}  - \mu_1k_2^2 \text{cos} \theta_i}
    {\mu_2 k_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}  + \mu_1k_2^2 \text{cos} \theta_i} \mathbf{H}_i
    :label: TM_HiandHr

.. math::
    \mathbf{H}_t = \frac{2 \mu_1k_2^2 \text{cos} \theta_i}
    {\mu_2 k_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}  + \mu_1k_2^2 \text{cos} \theta_i} \mathbf{H}_i
    :label: TM_HiandHt

where

.. math::
    \text{cos}^2 \theta_t  = 1 - \text{sin}^2 \theta_t = 1-\Big(\frac{k_1}{k_2}\Big) \text{sin}^2 \theta_i

Reflection and transmission coefficients for TM mode can be written as

.. math::
    r_{TM} = \frac{\hat{\mathbf{n}}\times \mathbf{E}_t}{\hat{\mathbf{n}}\times \mathbf{E}_i}
           = - \frac{\mathbf{H}_r}{\mathbf{H}_i}
           = \frac{\mu_2 k_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}  - \mu_1k_2^2 \text{cos} \theta_i}{\mu_2 k_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}  + \mu_1k_2^2 \text{cos} \theta_i}
    :label: rTM_theta

.. math::
    t_{TM} = \frac{\hat{\mathbf{n}}\times \mathbf{E}_t}{\hat{\mathbf{n}}\times \mathbf{E}_i}
           = \frac{\mathbf{H}_t}{\mathbf{H}_i}
           = \frac{2 \mu_1k_2^2 \text{cos} \theta_i}{\mu_2 k_1(k_2^2-k_1^2 \text{sin}^2 \theta_i)^{1/2}  + \mu_1k_2^2 \text{cos} \theta_i}
    :label: tTM_theta

Subsitituting these with Eqs. :eq:`u1` and :eq:`u2` yields

.. math::
    r_{TM} = \frac{\mu_2 u_2 k_1^2 - \mu_1 u_1 k_2^2}
    {\mu_2 u_2 k_1^2 + \mu_1 u_1 k_2^2}
    :label: rTM_u

.. math::
    t_{TM} = \frac{2\mu_1 u_1 k_2^2}
    {\mu_2 u_2 k_1^2 + \mu_1 u_1 k_2^2}
    :label: tTM_u

.. question::

   -  We defined reflection coefficient of TM mode :math:`r_{TM}` as ratio between tangential electric field of incidence and reflection as shown in Eq. :eq:`rTM`. However, we derived ratio of :math:`\mathbf{H}_i` and :math:`\mathbf{H}_r` then multipy -1 to obtain :math:`r_{TM}`, why is that? (Hint: See direction of :math:`\mathbf{E}` and :math:`\mathbf{H}` in :numref:`fresnel_setup_TM`)

Normal incidence
^^^^^^^^^^^^^^^^

When incidence is normal (:math:`\theta_i` =0), Eqs. :eq:`rTE_u` and :eq:`rTM_u` can be reduced to

.. math::

    r_{TE} = r_{TM} = \frac{\mu_2 k_1 - \mu_1 k_2} {\mu_2 k_1 + \mu_1 k_2}

