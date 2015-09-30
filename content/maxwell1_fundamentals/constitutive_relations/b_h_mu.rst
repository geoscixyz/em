(B,H):  mu
==========
This law is one of the three constitutive equations used to couple the fields and fluxes in Maxwell's equations.  It is an empirical law that describes the relationship between the magnetic flux and the magnetic field. 

In the frequency domain, the law is written as

.. include:: ../../equation_bank/cons_eq_mu_freq.rst

where :math:`\mathbf{B}` denote the complex magnetic flux, :math:`\mathbf{H}` denotes the complex magnetic field, and :math:`\mu` denotes the `magnetic permeability`_, which is defined as the degree of magnetization that a media obtains in response to an applied magnetic field.  For anisotropic media :math:`\mu` is a complex tensor and for isotropic media :math:`\mu` is a scalar value.  Most of the discussion of electromagnetic earth problems presented in [Ward_and_Hohmann]_ assumes that :math:`\mu` is independent of frequency and is a real quantity.   

.. _magnetic permeability: ../../physical_properties/physical_properties_magnetic_permeability.rst

For elementary electromagnetic earth problems it can be assumed that :math:`\mu` takes its free space value, that is (:math:`4\pi \times 10^{-7}` H\m).

The law can also be written in the time-domain as

.. include:: ../../equation_bank/cons_eq_mu_time.rst

where :math:`\mathbf{b}` denotes the real magnetic flux, :math:`\mathbf{h}` denotes the real magnetic field, and and :math:`\mu` denotes the real magnetic permeability.

In the SI_ the units of the magnetic permeability are henries_ per meter [:math:`H/m`], the unites of the magnetic flux are weber_ per meter square [:math:`Wb/m^2`], and the units of the magnetic field are amperes_ per meter [:math:`A/m`].

.. _SI: https://en.wikipedia.org/wiki/International_System_of_Units
.. _henries: https://en.wikipedia.org/wiki/Henry_(unit)
.. _weber: https://en.wikipedia.org/wiki/Weber_(unit)
.. _amperes: https://en.wikipedia.org/wiki/Ampere

        