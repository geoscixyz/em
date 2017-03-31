.. _maxwell1_fundamentals_interface_conditions_index:

Interface Conditions
====================

.. purpose::

    Here, we define the interface conditions for fields :math:`\mathbf{e}` and :math:`\mathbf{h}` as well as for fluxes :math:`\mathbf{j}`, :math:`\mathbf{d}` and :math:`\mathbf{b}` according to Griffiths (:cite:`griffiths1999`). As we will show, the interface conditions in each case can be derived directly from Maxwell's equations in :ref:`integral form<integral_equations_time>`.

.. figure:: images/twoLayerMedium.png
    :align: right
    :figwidth: 50%
    :name: interface_cond_index

    Fields across an horizontal physical property interface. 

Electromagnetic fields and fluxes differ across physical property interfaces. As we will show, the relationships between fields or fluxes on either side of an interface can be expressed in terms of the physical properties on either side of the interface. Before solving Maxwell's equations for general cases, we must derive appropriate interface conditions for :math:`\mathbf{e}`, :math:`\mathbf{h}`, :math:`\mathbf{j}`, :math:`\mathbf{d}` and :math:`\mathbf{b}`. 

|
|
|
|
|
|

+------------------+------------------------------------------------------------+---------------------------------------------------------------+
|Property          | Normal Component                                           | Tangential Component                                          |
+==================+============================================================+===============================================================+
|:math:`\mathbf{e}`|:math:`\varepsilon_1e_1^\perp-\varepsilon_2e_2^\perp=\tau_f`|:math:`e_1^\parallel-e_2^\parallel=0`                          |
+------------------+------------------------------------------------------------+---------------------------------------------------------------+
|:math:`\mathbf{d}`| :math:`d_1^\perp-d_2^\perp=\tau_f`                         |:math:`\varepsilon_2d_1^\parallel-\varepsilon_1d_2^\parallel=0`|
+------------------+------------------------------------------------------------+---------------------------------------------------------------+
|:math:`\mathbf{h}`|:math:`\mu_1h_1^\perp-\mu_2h_2^\perp=\tau_f`                |:math:`h_1^\parallel-h_2^\parallel=0`                          |
+------------------+------------------------------------------------------------+---------------------------------------------------------------+
|:math:`\mathbf{b}`| :math:`b_1^\perp-b_2^\perp=0`                              |:math:`\mu_2b_1^\perp-\mu_1b_2^\perp=0`                        |
+------------------+------------------------------------------------------------+---------------------------------------------------------------+






This can be accomplished by using Maxwell's equations in integral form in the time-domain, where:

.. math::
  \oint_S \mathbf{d} \cdot d \mathbf{a} = Q_f
  :label: GaussEint
  
.. math::
  \oint_S \mathbf{b}\cdot d \mathbf{a} = 0
  :label: GaussMint
  
.. math::
  \oint_C \mathbf{e} \cdot d\mathbf{l} = - \int_S \frac{\partial \mathbf{b}}{\partial t} \cdot d\mathbf{a}
  :label:

.. math::
  \oint_C \mathbf{h} \cdot d\mathbf{l} = \int_S \bigg ( \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t} \bigg ) \cdot d\mathbf{a}
  :label: AmpMaxInt


Recall that :math:`Q_f` and :math:`\mathbf{j}` are the total enclosed free charge and free current density, respectively. The fields and fluxes are related through the following constitutive relationships:

.. math::
  \mathbf{j} = \sigma \mathbf{e},
  :label: JsigE

.. math::
  \mathbf{d} = \varepsilon \mathbf{e},
  :label: DepsE

.. math::
  \mathbf{b} = \mu \mathbf{h},
  :label: BmuH

where :math:`\sigma` denotes the electric conductivity, :math:`\varepsilon` denotes the dielectric permittivity and :math:`\mu` denotes the magnetic permeability.

**Organization**

The subsequent content has been organized into two parts. First, we define the interface conditions for the electric field, free current density and displacement current. Next, we define the interface conditions for the magnetic field and magnetic flux density.


**Contents**

.. toctree::
    :maxdepth: 3

    derivation
    


