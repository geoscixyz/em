.. _electrostatic_sphere:

Conducting sphere in a uniform electric field
=============================================

A sphere in a whole-space provides a simple geometry to examine a variety of
questions and can provide powerful physical insights into a variety of
problems. Here we examine the case of a conducting sphere in a uniform
electrostatic field. This scenario gives us a setting to examine aspects of
the DC resistivity experiment, including the behavior of electric fields,
current density and the build up of charges at interfaces. This work follows
the derivation in [1]_ and is supported by apps developed in a `Jupyter
Notebook`_.

.. _Jupyter Notebook: https://github.com/ubcgif/em/blob/AmpereMaxwell/examples/sphere/ElectrostaticSphere.ipynb

Setup
-----

The problem setup is shown in the figure below, where we have

- a uniform electric fields oriented in the \\(x\\)-direction: \\(\\mathbf{E_0} = E_0 \\mathbf{\\hat{x}}\\)
- a whole-space background with conductivity \\(\\sigma_0\\)
- a sphere with radius \\(R\\) and conductivity \\(\\sigma_1\\)

.. plot::

    import matplotlib.pyplot as plt
    import numpy as np

    R = 0.5 
    x = np.linspace(-R,R,500)
    top = np.sqrt(R**2-x**2)
    bot = -np.sqrt(R**2-x**2)
    axlim = 3*R

    fig, ax = plt.subplots(1,1,figsize=(6,6))
    ax.plot(x, top, x, bot, color=[0.1,0.1,0.6],linewidth=1.5)
    ax.fill_between(x,bot,top,color=[0.1,0.1,0.6],alpha=0.5 )
    ax.set_xlim([-axlim,axlim])
    ax.set_ylim([-axlim,axlim])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlabel('x',fontsize=12)
    ax.set_ylabel('y',fontsize=12)
    ax.arrow(0.,0.,np.sqrt(R)/2.,np.sqrt(R)/2.,head_width=0.05,head_length=0.0)
    ax.text(np.sqrt(R)/4.-0.15,np.sqrt(R)/4.,'$R$',fontsize=13)
    [ax.arrow(-axlim,_,R,0.,head_width=0.05,head_length=0.05,color='k') for _ in np.linspace(-2*R,2*R,num=5)]
    ax.text(-axlim+0.05, 0.1, '$\mathbf{E_0} = E_0 \mathbf{\hat{x}}$', fontsize=14)
    ax.patch.set_facecolor([0.4,0.7,0.4])
    ax.patch.set_alpha(0.2)
    ax.text(-0.05,-np.sqrt(R)/2.,'$\sigma_1$',fontsize=14)
    ax.text(-0.05,-R-0.2,'$\sigma_0$',fontsize=14)  


Governing Equations
-------------------

The governing equation for DC resistivity problem can be obtained from Maxwell's equations (appropriate links) if 
we consider a zero-frequency case

.. math::
	\nabla \times \mathbf{e} = 0
	:label: Faraday_DC
	
.. math::
	\nabla \times \mathbf{h} = \sigma \cdot \mathbf{e}
	:label: Ampere_DC

According to :eq:`Faraday_DC`, We can define a scalar potential so that the primary electric field can be described as
the negative gradient of the primary potential

.. math::
	\mathbf{E}_p = -\nabla V_p
	:label: DC_Potential
	
A couple things we want to highlight:

- behavior for a resistive v. conductive sphere
- total v. secondary

Potentials 
----------
Assuming a x-directed uniform electric field and zero potential at infinity, by integration to :eq:`DC_Potential`, we obtain

.. math::
	V_p = - E_0 x = -E_0 r \cos\theta
	:label: Primary_Potential

The total potential outside the sphere \\(r > R\\) is

.. math::
	V_1 = -E_0 (1 - \frac{R^3}{r^3}\frac{\sigma_1 - \sigma_0}{\sigma_1 + 2\sigma_0}) r \cos\theta
	:label: totalP_outside

and inside the sphere \\(r < R\\)

.. math::
	V_2 = -E_0 \frac{3\sigma_0}{\sigma_1+2\sigma_0}r \cos\theta
	:label: totalP_inside

Solution, discussion, explain some intuition, questions. 

.. plot::
    
    import matplotlib.pyplot as plt
    from examples.sphere import *

    sig0 = 10.          # conductivity of the wholespace
    sig1 = 100.         # conductivity of the sphere
    R    = 50.          # radius of the sphere
    E0   = 1.           # inducing field strength
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition
    PlotOpt = 'Total'

    plot_Potentials(XYZ, R, sig1, sig0, E0)


Electric Field
--------------

The secondary electric field builds up to oppose the primary field. 
It’s strongly discontinuous making the total electric field discontinuous.

By taking the gradient of potentials, we can obtain electric fields outside the sphere \\(r>R\\)

.. math::
	E_1 = E_0\hat{x} + E_0\frac{\sigma_1-\sigma_0}{\sigma_1+2\sigma_0}\frac{R^3}{r^5}[(2x^2 - y^2 - z^2)\hat{x} + (3xy)\hat{y} + (3xz)\hat{z}]
	:label: eField_outside
	
and inside the sphere \\(r<R\\) is

.. math::
	E_2 = E_0\frac{3\sigma_0}{\sigma_1+2\sigma_0}\hat{x}
	:label: eField_inside
	
How do we get from potentials to electric field

.. plot::
    
    import matplotlib.pyplot as plt
    from examples.sphere import *

    sig0 = 10.          # conductivity of the wholespace
    sig1 = 100.         # conductivity of the sphere
    R    = 50.          # radius of the sphere
    E0   = 1.           # inducing field strength
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition
    PlotOpt = 'Total'

    plot_ElectricField(XYZ,R,sig1,sig0,E0,PlotOpt)

Current Density
---------------

According to Ohm’s law there is a linear correlation between the current density and the electric field at that location:  \\(\\mathbf{J} = \\sigma \\mathbf{E}\\). 
This can be applied when computing both the total and the primary current densities, but not to the secondary. 
The secondary current density needs to be thought as a difference between two other densities.   


.. plot::
    
    import matplotlib.pyplot as plt
    from examples.sphere import *

    sig0 = 10.          # conductivity of the wholespace
    sig1 = 100.         # conductivity of the sphere
    R    = 50.          # radius of the sphere
    E0   = 1.           # inducing field strength
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition
    PlotOpt = 'Total'

    plot_Currents(XYZ,R,sig1,sig0,E0,PlotOpt)

Charge Accumulation
-------------------

Where are the negative charges, where are the positive charges? for a resistive and conductive sphere

.. plot::
    
    import matplotlib.pyplot as plt
    from examples.sphere import *

    sig0 = 10.          # conductivity of the wholespace
    sig1 = 100.         # conductivity of the sphere
    R    = 50.          # radius of the sphere
    E0   = 1.           # inducing field strength
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition
    PlotOpt = 'Total'

    plot_Charges(XYZ,R,sig0,sig1,E0)

Questions
^^^^^^^^^

- now that you have all of the pieces, do they make sense when you put them together. 


Data
----

During a DC survey, we measure the difference of potentials between two electrodes,generally along a profile.

Therefore, as it is displayed on the figure below, we do not see the background potential as a linear function but as a constant, whose value will depend of the orientation of the survey line (as long as the spacing between the electrodes is constant).

We also notice that, as for the background, the differences measured inside the sphere are equal to a constant.

For a conductive sphere, the potential differences measured in the area of influence of the sphere are smaller. This can be anticipated using Ohm's law. This is the reverse for a resistive sphere.

.. plot::
    
    import matplotlib.pyplot as plt
    from examples.sphere import *

    sig0 = 10.          # conductivity of the wholespace
    sig1 = 100.         # conductivity of the sphere
    R    = 50.          # radius of the sphere
    E0   = 1.           # inducing field strength
    n = 100             #level of discretisation
    xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
    yr = xr.copy()      # Y-axis discretization
    dx = xr[1]-xr[0]       # mesh spacing
    dy = yr[1]-yr[0]       # mesh spacing
    zr = np.r_[0]          # identical to saying `zr = np.array([0])`
    XYZ = ndgrid(xr,yr,zr) # Space Definition
    PlotOpt = 'Total'

    xstart=-100.
    ystart=-100.
    xend=100.
    yend=100.
    nb_dipole=11
    electrode_spacing=20

    plot_PotentialDifferences(XYZ,R,sig0,sig1,E0,xstart,ystart,xend,yend,nb_dipole,electrode_spacing,PlotOpt)

Building some Intuition for DC problem
--------------------------------------

In real life, we do not know the underground configuration. We only see the data and we are trying to model the underground based from them. There are several set of parameters that can fit perfectly the data. Even in the simple case presented here, where we know it is a sphere, and whose response can be calculated analytically, we can find several configuration that can produce the same data along the same profile.

Here is an example: 

.. plot::

    import matplotlib.pyplot as plt
    from examples.sphere import *

    sig0 = 10.         
    sig1 = 100.         
    sig2 = 13.10344828
    R0    = 10.          
    R1 = 20.
    E0   = 1.           
    n = 100             
    xr = np.linspace(-100, 100, n) 
    yr = xr.copy()      
    zr = np.r_[0]          
    XYZ = ndgrid(xr,yr,zr)
    xstart = -100.
    ystart = 50.
    xend = 100.
    yend = 50.
    nb_dipole = 11
    electrode_spacing = 20.
    PlotOpt = 'Total'
    
    inversion_uncertainty(XYZ,sig0,sig1,sig2,R0,R1,E0,xstart,ystart,xend,yend,nb_dipole,electrode_spacing,PlotOpt)



.. [1] Ward, S. H., & Hohmann, W. (1988). *Electromagnetic Theory for Geophysical Applications Applications.* In Electromagnetic methods in applied geophysics (1st ed., pp. 130–311). Society of Exploration Geophysicists.
