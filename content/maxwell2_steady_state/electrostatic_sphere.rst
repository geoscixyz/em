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

Here we state the equations needed to derive everything, Gauss' law, boundary conditions, (appropriate links)


A couple things we want to highlight:

- behavior for a resistive v. conductive sphere
- total v. secondary

Potentials 
----------

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

Potential differences along a profile.

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

.. [1] Ward, S. H., & Hohmann, W. (1988). *Electromagnetic Theory for Geophysical Applications Applications.* In Electromagnetic methods in applied geophysics (1st ed., pp. 130–311). Society of Exploration Geophysicists.
