from scipy.constants import epsilon_0
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from SimPEG.Utils import ndgrid, mkvc

# Plot options
ftsize_title = 18      #font size for titles
ftsize_axis  = 14      #font size for axis ticks
ftsize_label = 14      #font size for axis labels

# Radius function and useful sigma ratio
r  = lambda x,y,z: np.sqrt(x**2.+y**2.+z**2.)
sigf = lambda sig0,sig1: (sig1-sig0)/(sig1+2.*sig0)

def get_Setup(XYZ,sig0,sig1,R,E0,ax):
  
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    top = np.sqrt(R**2-xr[xr <R]**2)
    bot = -np.sqrt(R**2-xr[xr < R]**2)
    
    ax.plot(xr[xr <= R], top, xr[xr <= R], bot, color=[0.1,0.1,0.6],linewidth=1.5)
    ax.fill_between(xr,bot,top,color=[0.1,0.1,0.6],alpha=0.5 )
    ax.set_xlim([xr.min(),xr.max()])
    ax.set_ylim([yr.min(),yr.max()])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlabel('x',fontsize=12)
    ax.set_ylabel('y',fontsize=12)
    ax.arrow(0.,0.,np.sqrt(2.)*R/2.,np.sqrt(2.)*R/2.,head_width=10.,head_length=2.)
    ax.text(np.sqrt(R)/4.-1.,np.sqrt(R)/4.+10.,'$R$',fontsize=13)
    [ax.arrow(xr.min(),_,R,0.,head_width=10.,head_length=2.,color='k') for _ in np.linspace(-2*R,2*R,num=5)]
    ax.text(xr.min()+0.05, 0.1, '$\mathbf{E_0} = E_0 \mathbf{\hat{x}}$', fontsize=14)
    ax.patch.set_facecolor([0.4,0.7,0.4])
    ax.patch.set_alpha(0.2)
    ax.text(-1.,-np.sqrt(R)/2.-10.,'$\sigma_1$',fontsize=14)
    ax.text(-0.05,-R-10,'$\sigma_0$',fontsize=14)  
    ax.set_aspect('equal')
    
    return ax

def get_Conductivity(XYZ,sig0,sig1,R):
    '''
    Define the conductivity for each point of the space
    '''
    x,y,z = XYZ[:,0],XYZ[:,1],XYZ[:,2]
    r_view=r(x,y,z)
    
    ind0= (r_view>R)
    ind1= (r_view<=R)
    
    assert (ind0 + ind1).all(), 'Some indicies not included'
    
    Sigma = np.zeros_like(x)
    
    Sigma[ind0] = sig0
    Sigma[ind1] = sig1
    
    return Sigma


def get_Potential(XYZ,sig0,sig1,R,E0): 

    '''
    Function that returns the total, the primary and the secondary potentials, assumes an x-oriented inducing field and that the sphere is at the origin
    :input: grid, outer sigma, inner sigma, radius of the sphere, strength of the electric field
    '''
    
    x,y,z = XYZ[:,0],XYZ[:,1],XYZ[:,2]
    
    sig_cur = sigf(sig0,sig1)
    
    r_cur = r(x,y,z)  # current radius
    
    ind0 = (r_cur > R)
    ind1 = (r_cur <= R)
    
    assert (ind0 + ind1).all(), 'Some indicies not included'
    
    Vt = np.zeros_like(x)
    Vp = np.zeros_like(x)
    Vs = np.zeros_like(x)
    
    Vt[ind0] = -E0*x[ind0]*(1.-sig_cur*R**3./r_cur[ind0]**3.) # total potential outside the sphere
    Vt[ind1] = -E0*x[ind1]*3.*sig0/(sig1+2.*sig0)             # inside the sphere
    
    
    Vp = - E0*x  # primary potential
    
    Vs = Vt - Vp # secondary potential
    
    return Vt,Vp,Vs

def Plot_Primary_Potential(XYZ,sig0,sig1,R,E0,ax):
    
    Vt,Vp,Vs = get_Potential(XYZ,sig0,sig1,R,E0)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    
    xcirc = xr[np.abs(xr) <= R]
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    
    Pplot = ax.pcolor(xr,yr,Vp.reshape(xr.size,yr.size))
    ax.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax.set_title('Primary Potential',fontsize=ftsize_title)
    cb = plt.colorbar(Pplot,ax=ax)
    cb.set_label(label= 'Potential ($V$)',size=ftsize_label)
    cb.ax.tick_params(labelsize=ftsize_axis)
    ax.set_xlim([xr.min(),xr.max()])
    ax.set_ylim([yr.min(),yr.max()])
    ax.set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax.set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax.set_aspect('equal')
    ax.tick_params(labelsize=ftsize_axis)
    
    #fig.set_tight_layout(True)
    
    return ax

def Plot_Total_Potential(XYZ,sig0,sig1,R,E0,ax):
    
    Vt,Vp,Vs = get_Potential(XYZ,sig0,sig1,R,E0)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    
    xcirc = xr[np.abs(xr) <= R]
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    
    Pplot = ax.pcolor(xr,yr,Vt.reshape(xr.size,yr.size))
    ax.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax.set_title('Total Potential',fontsize=ftsize_title)
    cb = plt.colorbar(Pplot,ax=ax)
    cb.set_label(label= 'Potential ($V$)',size=ftsize_label)
    cb.ax.tick_params(labelsize=ftsize_axis)
    ax.set_xlim([xr.min(),xr.max()])
    ax.set_ylim([yr.min(),yr.max()])
    ax.set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax.set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax.set_aspect('equal')
    ax.tick_params(labelsize=ftsize_axis)
    
    #fig.set_tight_layout(True)
    
    return ax

def Plot_Secondary_Potential(XYZ,sig0,sig1,R,E0,ax):
    
    Vt,Vp,Vs = get_Potential(XYZ,sig0,sig1,R,E0)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    
    xcirc = xr[np.abs(xr) <= R]
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111)

    Pplot = ax.pcolor(xr,yr,Vs.reshape(xr.size,yr.size))
    ax.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax.set_title('Secondary Potential',fontsize=ftsize_title)
    cb = plt.colorbar(Pplot,ax=ax)
    cb.set_label(label= 'Potential ($V$)',size=ftsize_label)
    cb.ax.tick_params(labelsize=ftsize_axis)
    ax.set_xlim([xr.min(),xr.max()])
    ax.set_ylim([yr.min(),yr.max()])
    ax.set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax.set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax.set_aspect('equal')
    ax.tick_params(labelsize=ftsize_axis)

    #fig.set_tight_layout(True)
    
    return ax


def get_ElectricField(XYZ,sig0,sig1,R,E0):
    '''
    Function that returns the total, the primary and the secondary electric fields, 
    input: grid, outer sigma, inner sigma, radius of the sphere, strength of the electric field
    '''
    
    x,y,z= XYZ[:,0], XYZ[:,1], XYZ[:,2]
    
    r_cur=r(x,y,z)  # current radius
    
    ind0= (r_cur>R)
    ind1= (r_cur<=R)
    
    assert (ind0 + ind1).all(), 'Some indicies not included'
        
    Ep = np.zeros(shape=(len(x),3))
    Ep[:,0] = E0
    
    Et = np.zeros(shape=(len(x),3))
    
    Et[ind0,0] = E0 + E0*R**3./(r_cur[ind0]**5.)*sigf(sig0,sig1)*(2.*x[ind0]**2.-y[ind0]**2.-z[ind0]**2.);
    Et[ind0,1] = E0*R**3./(r_cur[ind0]**5.)*3.*x[ind0]*y[ind0]*sigf(sig0,sig1);
    Et[ind0,2] = E0*R**3./(r_cur[ind0]**5.)*3.*x[ind0]*z[ind0]*sigf(sig0,sig1);

    Et[ind1,0] = 3.*sig0/(sig1+2.*sig0)*E0;
    Et[ind1,1] = 0.;
    Et[ind1,2] = 0.;
    
    Es = Et - Ep
    
    return Et, Ep, Es

def Plot_Total_ElectricField(XYZ,sig0,sig1,R,E0,ax):
    
    Et, Ep, Es = get_ElectricField(XYZ,sig0,sig1,R,E0)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])

    xcirc = xr[np.abs(xr) <= R]

    EtXr = Et[:,0].reshape(xr.size, yr.size)
    EtYr = Et[:,1].reshape(xr.size, yr.size)
    EtAmp = np.sqrt(Et[:,0]**2+Et[:,1]**2 + Et[:,2]**2).reshape(xr.size, yr.size)
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    
    ax.set_xlim([xr.min(),xr.max()])
    ax.set_ylim([yr.min(),yr.max()])
    ax.set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax.set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax.tick_params(labelsize=ftsize_axis)
    ax.set_aspect('equal')
    
    Eplot = ax.pcolor(xr,yr,EtAmp)
    cb = plt.colorbar(Eplot,ax=ax)
    cb.set_label(label= 'Amplitude ($V/m$)',size=ftsize_label) #weight='bold')
    cb.ax.tick_params(labelsize=ftsize_axis)
    ax.streamplot(xr,yr,EtXr,EtYr,color='gray',linewidth=2.,density=0.75)#angles='xy',scale_units='xy',scale=0.05)
    ax.set_title('Total Field',fontsize=ftsize_title)
    
    #plt.tight_layout(True)
    
    return ax
    
    
def Plot_Secondary_ElectricField(XYZ,sig0,sig1,R,E0,ax):
    
    Et, Ep, Es = get_ElectricField(XYZ,sig0,sig1,R,E0)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])

    xcirc = xr[np.abs(xr) <= R]

    EsXr = Es[:,0].reshape(xr.size, yr.size)
    EsYr = Es[:,1].reshape(xr.size, yr.size)
    EsAmp = np.sqrt(Es[:,0]**2+Es[:,1]**2+Es[:,2]**2).reshape(xr.size, yr.size)
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    
    ax.set_xlim([xr.min(),xr.max()])
    ax.set_ylim([yr.min(),yr.max()])
    ax.set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax.set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax.tick_params(labelsize=ftsize_axis)
    ax.set_aspect('equal')
    
    Eplot = ax.pcolor(xr,yr,EsAmp)
    cb = plt.colorbar(Eplot,ax=ax)
    cb.set_label(label= 'Amplitude ($V/m$)',size=ftsize_label) #weight='bold')
    cb.ax.tick_params(labelsize=ftsize_axis)
    ax.streamplot(xr,yr,EsXr,EsYr,color='gray',linewidth=2.,density=0.75)#,angles='xy',scale_units='xy',scale=0.05)
    ax.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax.set_title('Secondary Field',fontsize=ftsize_title)
    
    #plt.tight_layout(True)
    
    return ax


def get_Current(XYZ,sig0,sig1,R,Et,Ep,Es):
    '''
    Function that returns the total, the primary and the secondary current densities, 
    :input: grid, outer sigma, inner sigma, radius of the sphere, total, the primary and the seconadry electric fields,
    '''
    
    x,y,z= XYZ[:,0], XYZ[:,1], XYZ[:,2]
    
    r_cur=r(x,y,z)
    
    ind0= (r_cur>R)
    ind1= (r_cur<=R)
    
    assert (ind0 + ind1).all(), 'Some indicies not included'
    
    Jt = np.zeros(shape=(len(x),3))
    J0 = np.zeros(shape=(len(x),3))
    Js = np.zeros(shape=(len(x),3))
    

    Jp = sig0*Ep
    
    Jt[ind0,:] = sig0*Et[ind0,:]   
    Jt[ind1,:] = sig1*Et[ind1,:]

    
    #Js[ind0,:] = sig0*Es[ind0,:]
    #Js[ind1,:] = sig1*Es[ind1,:]
    Js[ind0,:] = sig0*(Et[ind0,:]-Ep[ind0,:])
    Js[ind1,:] = sig1*Et[ind1,:]-sig0*Ep[ind1,:]
    
    return Jt,Jp,Js

def Plot_Total_Currents(XYZ,sig0,sig1,R,E0,ax):
    
    Et,Ep,Es = get_ElectricField(XYZ,sig0,sig1,R,E0)
    Jt,Jp,Js = get_Current(XYZ,sig0,sig1,R,Et,Ep,Es)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    xcirc = xr[np.abs(xr) <= R]

    JtXr = Jt[:,0].reshape(xr.size, yr.size)
    JtYr = Jt[:,1].reshape(xr.size, yr.size)
    JtAmp = np.sqrt(Jt[:,0]**2+Jt[:,1]**2+Jt[:,2]**2).reshape(xr.size, yr.size)
    
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    
    ax.set_xlim([xr.min(),xr.max()])
    ax.set_ylim([yr.min(),yr.max()])
    ax.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax.set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax.set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax.tick_params(labelsize=ftsize_axis)
    ax.set_aspect('equal')
    
    Jplot = ax.pcolor(xr,yr,JtAmp.reshape(xr.size,yr.size))
    cb = plt.colorbar(Jplot,ax=ax)
    cb.set_label(label= 'Current Density ($A/m^2$)',size=ftsize_label) #weight='bold')
    cb.ax.tick_params(labelsize=ftsize_axis)
    ax.streamplot(xr,yr,JtXr,JtYr,color='gray',linewidth=2.,density=0.75)#,angles='xy',scale_units='xy',scale=1)
    ax.set_title('Total Current Density',fontsize=ftsize_title)
    
    # plt.tight_layout(True)
    
    return ax
    
def Plot_Secondary_Currents(XYZ,sig0,sig1,R,E0,ax):
    
    Et,Ep,Es = get_ElectricField(XYZ,sig0,sig1,R,E0)
    Jt,Jp,Js = get_Current(XYZ,sig0,sig1,R,Et,Ep,Es)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    xcirc = xr[np.abs(xr) <= R]
        
    JsXr = Js[:,0].reshape(xr.size, yr.size)
    JsYr = Js[:,1].reshape(xr.size, yr.size)
    JsAmp = np.sqrt(Js[:,1]**2+Js[:,0]**2+Jt[:,2]**2).reshape(xr.size,yr.size)
    
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    
    ax.set_xlim([xr.min(),xr.max()])
    ax.set_ylim([yr.min(),yr.max()])
    ax.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax.set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax.set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax.tick_params(labelsize=ftsize_axis)
    ax.set_aspect('equal')
    
    Jplot = ax.pcolor(xr,yr,JsAmp.reshape(xr.size,yr.size))
    cb = plt.colorbar(Jplot,ax=ax)
    cb.set_label(label= 'Current Density ($A/m^2$)',size=ftsize_label) #weight='bold')
    cb.ax.tick_params(labelsize=ftsize_axis)
    ax.streamplot(xr,yr,JsXr,JsYr,color='gray',linewidth=2.,density=0.75)#,angles='xy',scale_units='xy',scale=1)
    ax.set_title('Secondary Current Density',fontsize=ftsize_title)
    
    # plt.tight_layout(True)
    
    return ax

def get_ChargesDensity(XYZ,sig0,sig1,R,Et,Ep):
    
    x,y,z= XYZ[:,0], XYZ[:,1], XYZ[:,2]
    
    dx = x[1]-x[0]
    
    r_cur=r(x,y,z)
    
    ind0 = (r_cur > R)
    ind1 = (r_cur < R)
    ind2 = ((r_cur < (R+dx/2)) & (r_cur > (R-dx/2)) )
    
    assert (ind0 + ind1 + ind2).all(), 'Some indicies not included'
    
    rho = np.zeros_like(x)
    
    rho[ind0] = 0
    rho[ind1] = 0
    rho[ind2] = epsilon_0*3.*Ep[ind2,0]*sigf(sig0,sig1)*x[ind2]/(np.sqrt(x[ind2]**2.+y[ind2]**2.))
    
    return rho

def Plot_ChargesDensity(XYZ,sig0,sig1,R,E0,ax):
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    xcirc = xr[np.abs(xr) <= R]
    
    Et, Ep, Es = get_ElectricField(XYZ,sig0,sig1,R,E0)
    rho = get_ChargesDensity(XYZ,sig0,sig1,R,Et,Ep)
    
    ax.set_xlim([xr.min(),xr.max()])
    ax.set_ylim([yr.min(),yr.max()])
    ax.set_aspect('equal')
    Cplot = ax.pcolor(xr,yr,rho.reshape(xr.size, yr.size))
    cb1 = plt.colorbar(Cplot,ax=ax)
    cb1.set_label(label= 'Charge Density ($C/m^2$)',size=ftsize_label) #weight='bold')
    cb1.ax.tick_params(labelsize=ftsize_axis)
    ax.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax.set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax.set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax.tick_params(labelsize=ftsize_axis)
    ax.set_title('Charges Density', fontsize=ftsize_title)
    
    return ax

def MN_Potential_total(sig0,sig1,R,E0,start,end,nbmp,mn):
    
    '''
    sig0: background conductivity
    sig1: sphere conductivity
    R: Sphere's radius
    E0: uniform E field value
    start: start point for the profile start.shape = (2,)
    end: end point for the profile end.shape = (2,)
    nbmp: number of dipoles
    mn: Space between the M and N electrodes
    '''

    #D: total distance from start to end
    D = np.sqrt((start[0]-end[0])**2.+(start[1]-end[1])**2.)
    
    #MP: dipoles'midpoint positions (x,y)
    MP = np.zeros(shape=(nbmp,2))                            
    MP[:,0] = np.linspace(start[0],end[0],nbmp)
    MP[:,1] = np.linspace(start[1],end[1],nbmp)
    
    #Dipoles'Electrodes positions around each midpoints
    EL = np.zeros(shape=(2*nbmp,2))                         
    for n in range(0,len(EL),2):
        EL[n,0]   = MP[n/2,0] - ((end[0]-start[0])/D)*mn/2.
        EL[n+1,0] = MP[n/2,0] + ((end[0]-start[0])/D)*mn/2.
        EL[n,1]   = MP[n/2,1] - ((end[1]-start[1])/D)*mn/2.
        EL[n+1,1] = MP[n/2,1] + ((end[1]-start[1])/D)*mn/2.
    
    VtEL = np.zeros(2*nbmp) #Total Potential (Vt-) at each electrode (-EL)
    VsEL = np.zeros(2*nbmp) #Secondary Potential (Vt-) at each electrode (-EL)
    dVtMP = np.zeros(nbmp)  #Diffence (d-) of Total Potential (Vt-) at each dipole (-MP)
    dVtMPn = np.zeros(nbmp) #Diffence (d-) of Total Potential (Vt-) at each dipole (-MP) normalized for the mn spacing (n)
    dVsMP = np.zeros(nbmp)  #Diffence (d-) of Secondaty Potential (Vt-) at each dipole (-MP)
    dVsMPn = np.zeros(nbmp) #Diffence (d-) of Secondary Potential (Vt-) at each dipole (-MP) normalized for the mn spacing (n)
    dVpMP = np.zeros(nbmp) #Diffence (d-) of Primary Potential (Vt-) at each dipole (-MP)
    dVpMPn = np.zeros(nbmp) #Diffence (d-) of Primary Potential (Vt-) at each dipole (-MP) normalized for the mn spacing (n)
    
    #Computing VtEL 
    for m in range(0,2*nbmp):
        if (r(EL[m,0],EL[m,1],0) > R):
            VtEL[m] = -E0*EL[m,0]*(1.-sigf(sig0,sig1)*R**3./r(EL[m,0],EL[m,1],0)**3.)
        else:
            VtEL[m] = -E0*EL[m,0]*3.*sig0/(sig1+2.*sig0)
    
    #Computing VsEL
    VsEL = VtEL + E0*EL[:,0]
    
    #Computing dVtMP, dVsMP
    for p in range(0,nbmp):
        dVtMP[p] = VtEL[2*p]-VtEL[2*p+1]
        dVtMPn[p] = dVtMP[p]/mn
        dVsMP[p] = VsEL[2*p]-VsEL[2*p+1]
        dVsMPn[p] = dVsMP[p]/mn
    
    return MP,EL,dVtMP,dVtMPn,dVsMP,dVsMPn

def plot_Potentials(XYZ,R,sig1,sig0,E0):
    
    Sigma    = get_Conductivity(XYZ,sig0,sig1,R)
    Vt,Vp,Vs = get_Potential(XYZ,sig0,sig1,R,E0)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])

    Ep = np.zeros(shape=(len(Sigma),3))
    Ep[:,0] = E0
    #Vp = get_Primary_Potential(XYZ,sig0,sig1,R,E0)

    xcirc = xr[np.abs(xr) <= R]

    fig,ax = plt.subplots(2,2,figsize=(10,8))
    ax=mkvc(ax)

    ax[0].pcolor(xr,yr,Sigma.reshape(xr.size, yr.size))
    cb0 = plt.colorbar(ax[0].pcolor(xr,yr,Sigma.reshape(xr.size, yr.size)),ax=ax[0])
    cb0.set_label(label= 'Conductivity ($S/m$)',size=ftsize_label) #weight='bold')
    cb0.ax.tick_params(labelsize=ftsize_axis)
    plt.tick_params(labelsize=ftsize_axis)
    ax[0].streamplot(xr,yr,Ep[:,0].reshape(xr.size,yr.size),Ep[:,1].reshape(xr.size,yr.size),color='gray'
                     ,density=0.5, linewidth=2.)
    ax[0].annotate('E0',(-80,80),xytext=(-80,80),fontsize=ftsize_title,color='gray',weight='bold')
    #ax[0].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[0].set_title('Configuration',fontsize=ftsize_title)
    ax[0].set_xlim([xr.min(),xr.max()])
    ax[0].set_ylim([yr.min(),yr.max()])
    ax[0].set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax[0].set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax[0].set_aspect('equal')
    ax[0].tick_params(labelsize=ftsize_axis)


    ax[1].pcolor(xr,yr,Vp.reshape(xr.size,yr.size))
    ax[1].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[1].set_title('Primary Potential',fontsize=ftsize_title)
    cb1 = plt.colorbar(ax[1].pcolor(xr,yr,Vp.reshape(xr.size, yr.size)),ax=ax[1])
    cb1.set_label(label= 'Potential ($V$)',size=ftsize_label)
    cb1.ax.tick_params(labelsize=ftsize_axis)
    ax[1].set_xlim([xr.min(),xr.max()])
    ax[1].set_ylim([yr.min(),yr.max()])
    ax[1].set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax[1].set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax[1].set_aspect('equal')
    ax[1].tick_params(labelsize=ftsize_axis)


    ax[2].pcolor(xr,yr,Vt.reshape(xr.size,yr.size))
    ax[2].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[2].set_title('Total Potential',fontsize=ftsize_title)
    cb2 = plt.colorbar(ax[2].pcolor(xr,yr,Vt.reshape(xr.size, yr.size)),ax=ax[2])
    cb2.set_label(label= 'Potential ($V$)',size=ftsize_label)
    cb2.ax.tick_params(labelsize=ftsize_axis)
    ax[2].set_xlim([xr.min(),xr.max()])
    ax[2].set_ylim([yr.min(),yr.max()])
    ax[2].set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax[2].set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax[2].set_aspect('equal')
    ax[2].tick_params(labelsize=ftsize_axis)

    ax[3].pcolor(xr,yr,Vs.reshape(xr.size,yr.size))
    ax[3].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[3].set_title('Secondary Potential',fontsize=ftsize_title)
    cb3 = plt.colorbar(ax[3].pcolor(xr,yr,Vs.reshape(xr.size, yr.size)),ax=ax[3])
    cb3.set_label(label= 'Potential ($V$)',size=ftsize_label)
    cb2.ax.tick_params(labelsize=ftsize_axis)
    ax[3].set_xlim([xr.min(),xr.max()])
    ax[3].set_ylim([yr.min(),yr.max()])
    ax[3].set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax[3].set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax[3].set_aspect('equal')
    ax[3].tick_params(labelsize=ftsize_axis)

    fig.set_tight_layout(True)
    return fig, ax

def plot_ElectricField(XYZ,R,sig1,sig0,E0,PlotOpt):
   
    Sigma = get_Conductivity(XYZ,sig0,sig1,R)
    Et, Ep, Es = get_ElectricField(XYZ,sig0,sig1,R,E0)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])

    xcirc = xr[np.abs(xr) <= R]
    
    EtXr = Et[:,0].reshape(xr.size, yr.size)
    EtYr = Et[:,1].reshape(xr.size, yr.size)
    EtAmp = np.sqrt(Et[:,0]**2+Et[:,1]**2 + Et[:,2]**2).reshape(xr.size, yr.size)
    
    EsXr = Es[:,0].reshape(xr.size, yr.size)
    EsYr = Es[:,1].reshape(xr.size, yr.size)
    EsAmp = np.sqrt(Es[:,0]**2+Es[:,1]**2+Es[:,2]**2).reshape(xr.size, yr.size)
    
    fig,ax = plt.subplots(2,2,figsize=(10,8))
    ax=mkvc(ax)

    ax[0].pcolor(xr,yr,Sigma.reshape(xr.size, yr.size))
    cb0 = plt.colorbar(ax[0].pcolor(xr,yr,Sigma.reshape(xr.size, yr.size)),ax=ax[0])
    cb0.set_label(label= 'Conductivity ($S/m$)',size=ftsize_label) #weight='bold')
    cb0.ax.tick_params(labelsize=ftsize_axis)
    #ax[0].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[0].streamplot(xr,yr,Ep[:,0].reshape(xr.size,yr.size),Ep[:,1].reshape(xr.size,yr.size),color='gray'
                     ,density=0.5, linewidth=2.)
    ax[0].set_title('Configuration',fontsize=ftsize_title)
    ax[0].annotate('E0',(-80,80),xytext=(-80,80),fontsize=ftsize_title,color='gray',weight='bold')
    ax[0].set_xlim([xr.min(),xr.max()])
    ax[0].set_ylim([yr.min(),yr.max()])
    ax[0].set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax[0].set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax[0].set_aspect('equal')
    ax[0].tick_params(labelsize=ftsize_axis)
    
    ax[2].set_xlim([xr.min(),xr.max()])
    ax[2].set_ylim([yr.min(),yr.max()])
    ax[2].set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax[2].set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax[2].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[2].tick_params(labelsize=ftsize_axis)
    ax[2].set_aspect('equal')

    ax[1].set_xlim([xr.min(),xr.max()])
    ax[1].set_ylim([yr.min(),yr.max()])
    ax[1].set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax[1].set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax[1].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[1].tick_params(labelsize=ftsize_axis)
    ax[1].set_aspect('equal')

    ax[3].set_xlim([xr.min(),xr.max()])
    ax[3].set_ylim([yr.min(),yr.max()])
    ax[3].set_ylabel('Y coordinate ($m$)',fontsize = ftsize_label)
    ax[3].set_xlabel('X coordinate ($m$)',fontsize = ftsize_label)
    ax[3].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[3].tick_params(labelsize=ftsize_axis)
    ax[3].set_aspect('equal')

    if PlotOpt == 'Total':
    
        ax[2].pcolor(xr,yr,EtAmp)
        cb2 = plt.colorbar(ax[2].pcolor(xr,yr,EtAmp),ax=ax[2])
        cb2.set_label(label= 'Amplitude ($V/m$)',size=ftsize_label) #weight='bold')
        cb2.ax.tick_params(labelsize=ftsize_axis)
        ax[2].streamplot(xr,yr,EtXr,EtYr,color='gray',linewidth=2.,density=0.75)#angles='xy',scale_units='xy',scale=0.05)
        ax[2].set_title('Total Field',fontsize=ftsize_title)

        ax[1].pcolor(xr,yr,EtXr)
        cb1 = plt.colorbar(ax[1].pcolor(xr,yr,EtXr),ax=ax[1])
        cb1.set_label(label= 'Amplitude ($V/m$)',size=ftsize_label) #weight='bold')
        cb1.ax.tick_params(labelsize=ftsize_axis)
        ax[1].set_title('Total Ex',fontsize=ftsize_title)
    
        ax[3].pcolor(xr,yr,EtYr)
        cb3 = plt.colorbar(ax[3].pcolor(xr,yr,EtYr),ax=ax[3])
        cb3.set_label(label= 'Amplitude ($V/m$)',size=ftsize_label) #weight='bold')
        cb3.ax.tick_params(labelsize=ftsize_axis)
        ax[3].set_title('Total Ey',fontsize=ftsize_title)
    
    
    elif PlotOpt is 'Secondary':

        ax[2].pcolor(xr,yr,EsAmp)
        cb2 = plt.colorbar(ax[2].pcolor(xr,yr,EsAmp),ax=ax[2])
        cb2.set_label(label= 'Amplitude ($V/m$)',size=ftsize_label) #weight='bold')
        cb2.ax.tick_params(labelsize=ftsize_axis)
        ax[2].streamplot(xr,yr,EsXr,EsYr,color='gray',linewidth=2.,density=0.75)#,angles='xy',scale_units='xy',scale=0.05)
        ax[2].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
        ax[2].set_title('Secondary Field',fontsize=ftsize_title)

        ax[1].pcolor(xr,yr,EsXr)
        cb1 = plt.colorbar(ax[1].pcolor(xr,yr,EsXr),ax=ax[1])
        cb1.set_label(label= 'Amplitude ($V/m$)',size=ftsize_label) #weight='bold')
        cb1.ax.tick_params(labelsize=ftsize_axis)
        ax[1].set_title('Secondary Ex',fontsize=ftsize_title)
    
        ax[3].pcolor(xr,yr,EsYr)
        cb3= plt.colorbar(ax[3].pcolor(xr,yr,EsYr),ax=ax[3])
        cb3.set_label(label= 'Amplitude ($V/m$)',size=ftsize_label) #weight='bold')
        cb3.ax.tick_params(labelsize=ftsize_axis)
        ax[3].set_title('Secondary Ey',fontsize=ftsize_title)
        
    else:

        print('Oups!')

    fig.set_tight_layout(True)
    return fig, ax

def plot_Currents(XYZ,R,sig1,sig0,E0,PlotOpt):
   
    Sigma = get_Conductivity(XYZ,sig0,sig1,R)
    Et, Ep, Es = get_ElectricField(XYZ,sig0,sig1,R,E0)
    Jt,Jp,Js = get_Current(XYZ,sig0,sig1,R,Et,Ep,Es)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])

    xcirc = xr[np.abs(xr) <= R]

    JtXr = Jt[:,0].reshape(xr.size, yr.size)
    JtYr = Jt[:,1].reshape(xr.size, yr.size)
    JtAmp = np.sqrt(Jt[:,0]**2+Jt[:,1]**2+Jt[:,2]**2).reshape(xr.size, yr.size)
    
    JsXr = Js[:,0].reshape(xr.size, yr.size)
    JsYr = Js[:,1].reshape(xr.size, yr.size)
    JsAmp = np.sqrt(Js[:,1]**2+Js[:,0]**2+Jt[:,2]**2).reshape(xr.size,yr.size)
    
    fig,ax = plt.subplots(2,2,figsize=(10,8))
    ax=mkvc(ax)

    ax[0].pcolor(xr,yr,Sigma.reshape(xr.size, yr.size))
    cb0 = plt.colorbar(ax[0].pcolor(xr,yr,Sigma.reshape(xr.size, yr.size)),ax=ax[0])
    cb0.set_label(label= 'Conductivity ($S/m$)',size=ftsize_label) #weight='bold')
    cb0.ax.tick_params(labelsize=ftsize_axis)
    ax[0].streamplot(xr,yr,Ep[:,0].reshape(xr.size,yr.size),Ep[:,1].reshape(xr.size,yr.size),color='gray'
                     ,linewidth=2.,density=0.5)
    #ax[0].quiver(np.zeros_like(xrr)-90,yrr,E0,0,angles='xy',scale_units='xy',scale=0.05,color='gray')
    #ax[0].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[0].set_title('Configuration',fontsize=ftsize_title)
    ax[0].annotate('E0',(-80,80),xytext=(-80,80),fontsize=ftsize_title,color='gray',weight='bold')
    ax[0].set_xlim([xr.min(),xr.max()])
    ax[0].set_ylim([yr.min(),yr.max()])
    ax[0].set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax[0].set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax[0].tick_params(labelsize=ftsize_axis)
    ax[0].set_aspect('equal')
    
    ax[1].set_xlim([xr.min(),xr.max()])
    ax[1].set_ylim([yr.min(),yr.max()])
    ax[1].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[1].set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax[1].set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax[1].tick_params(labelsize=ftsize_axis)
    ax[1].set_aspect('equal')
    
    ax[2].set_xlim([xr.min(),xr.max()])
    ax[2].set_ylim([yr.min(),yr.max()])
    ax[2].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[2].set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax[2].set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax[2].tick_params(labelsize=ftsize_axis)
    ax[2].set_aspect('equal')
    
    ax[3].set_xlim([xr.min(),xr.max()])
    ax[3].set_ylim([yr.min(),yr.max()])    
    ax[3].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[3].set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax[3].set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax[3].tick_params(labelsize=ftsize_axis)
    ax[3].set_aspect('equal')

    if PlotOpt == 'Total':
        
        ax[2].pcolor(xr,yr,JtAmp)
        cb2 = plt.colorbar(ax[2].pcolor(xr,yr,JtAmp),ax=ax[2])
        cb2.set_label(label= 'Current Density ($A/m^2$)',size=ftsize_label) #weight='bold')
        cb2.ax.tick_params(labelsize=ftsize_axis)
        ax[2].streamplot(xr,yr,JtXr,JtYr,color='gray',linewidth=2.,density=0.75)#,angles='xy',scale_units='xy',scale=1)
        ax[2].set_title('Total Current Density',fontsize=ftsize_title)

        ax[1].pcolor(xr,yr,JtXr)
        cb1 = plt.colorbar(ax[1].pcolor(xr,yr,JtXr),ax=ax[1])
        cb1.set_label(label= 'Current Density ($A/m^2$)',size=ftsize_label) #weight='bold')
        cb1.ax.tick_params(labelsize=ftsize_axis)
        ax[1].set_title('Total Jx',fontsize=ftsize_title)

        ax[3].pcolor(xr,yr,JtYr)
        cb3 = plt.colorbar(ax[3].pcolor(xr,yr,JtYr),ax=ax[3])
        cb3.set_label(label= 'Current Density ($A/m^2$)',size=ftsize_label) #weight='bold')
        cb3.ax.tick_params(labelsize=ftsize_axis)
        ax[3].set_title('Total Jy',fontsize=ftsize_title)

    elif PlotOpt == 'Secondary':
        
        ax[2].pcolor(xr,yr,JsAmp)
        cb2 = plt.colorbar(ax[2].pcolor(xr,yr,JsAmp),ax=ax[2])
        cb2.set_label(label= 'Current Density ($A/m^2$)',size=ftsize_label) #weight='bold')
        cb2.ax.tick_params(labelsize=ftsize_axis)
        ax[2].streamplot(xr,yr,JsXr,JsYr,color='gray',linewidth=2.)#angles='xy',scale_units='xy',scale=1)
        ax[2].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
        ax[2].set_xlim([xr.min(),xr.max()])
        ax[2].set_ylim([yr.min(),yr.max()])
        ax[2].set_title('secondary Current Density',fontsize=ftsize_title)
        
        ax[1].pcolor(xr,yr,JsXr)
        cb1 = plt.colorbar(ax[1].pcolor(xr,yr,JsXr),ax=ax[1])
        cb1.set_label(label= 'Current Density ($A/m^2$)',size=ftsize_label) #weight='bold')
        cb1.ax.tick_params(labelsize=ftsize_axis)
        ax[1].set_title('Secondary Jx',fontsize=ftsize_title)

        ax[3].pcolor(xr,yr,Js[:,1].reshape(xr.size,yr.size))
        cb3 = plt.colorbar(ax[3].pcolor(xr,yr,JsYr),ax=ax[3])
        cb3.set_label(label= 'Current Density ($A/m^2$)',size=ftsize_label) #weight='bold')
        cb3.ax.tick_params(labelsize=ftsize_axis)
        ax[3].set_title('Secondary Jy',fontsize=ftsize_title)
        
    else:
        print('Oups')
    
    fig.set_tight_layout(True)

    return fig,ax

def plot_Charges(XYZ,R,sig0,sig1,E0):
   
    Sigma = get_Conductivity(XYZ,sig0,sig1,R)
    Et, Ep, Es = get_ElectricField(XYZ,sig0,sig1,R,E0)
    rho = get_ChargesDensity(XYZ,sig0,sig1,R,Et,Ep)
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    xcirc = xr[np.abs(xr) <= R]
    
    fig,ax = plt.subplots(1,2,figsize=(10,4))

    ax[0].pcolor(xr,yr,Sigma.reshape(xr.size, yr.size))
    cb0 = plt.colorbar(ax[0].pcolor(xr,yr,Sigma.reshape(xr.size, yr.size)),ax=ax[0])
    cb0.set_label(label= 'Conductivity ($S/m$)',size=ftsize_label) #weight='bold')
    cb0.ax.tick_params(labelsize=ftsize_axis)
    ax[0].streamplot(xr,yr,Ep[:,0].reshape(xr.size,yr.size),Ep[:,1].reshape(xr.size,yr.size),color='gray'
                     ,density=0.5, linewidth=2.)
    #ax[0].quiver(np.zeros_like(xrr)-90,yrr,E0,0,angles='xy',scale_units='xy',scale=0.05,color='gray')
    #ax[0].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[0].set_title('Configuration',fontsize=ftsize_title)
    ax[0].annotate('E0',(-80,80),xytext=(-80,80),fontsize=ftsize_title,color='gray',weight='bold')
    ax[0].set_xlim([xr.min(),xr.max()])
    ax[0].set_ylim([yr.min(),yr.max()])
    ax[0].set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax[0].set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax[0].set_aspect('equal')
    ax[0].tick_params(labelsize=ftsize_axis)
    
    ax[1].set_xlim([xr.min(),xr.max()])
    ax[1].set_ylim([yr.min(),yr.max()])
    ax[1].set_aspect('equal')
    ax[1].pcolor(xr,yr,rho.reshape(xr.size, yr.size))
    cb1 = plt.colorbar(ax[1].pcolor(xr,yr,rho.reshape(xr.size, yr.size)),ax=ax[1])
    cb1.set_label(label= 'Charge Density ($C/m^2$)',size=ftsize_label) #weight='bold')
    cb1.ax.tick_params(labelsize=ftsize_axis)
    ax[1].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax[1].set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax[1].set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax[1].tick_params(labelsize=ftsize_axis)
    ax[1].set_title('Charges Density', fontsize=ftsize_title)
    

    fig.set_tight_layout(True)

    return fig, ax

def plot_PotentialDifferences(XYZ,R,sig0,sig1,E0,xstart,ystart,xend,yend,nb_dipole,electrode_spacing,PlotOpt):
    
    start = np.array([xstart,ystart])
    end = np.array([xend,yend])
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    
    Sigma    = get_Conductivity(XYZ,sig0,sig1,R)
    Vt,Vp,Vs = get_Potential(XYZ,sig0,sig1,R,E0)
    MP,EL,VtdMP,VtdMPn,VsdMP,VsdMPn = MN_Potential_total(sig0,sig1,R,E0,start,end,nb_dipole,electrode_spacing)
    
    Ep = np.zeros(shape=(len(Sigma),3))
    Ep[:,0] = E0

    xcirc = xr[np.abs(xr) <= R]

    #fig,ax = plt.subplots(1,3,figsize=(20,5))
    #ax=mkvc(ax)
    
    fig = plt.figure(figsize=(20,10))
    ax0 = plt.subplot2grid((10,12), (0, 0),colspan=6,rowspan=6)
    ax1 = plt.subplot2grid((10,12), (0, 6),colspan=6,rowspan=6)
    ax2 = plt.subplot2grid((10,12), (6, 2), colspan=9,rowspan=4)


    ax0.pcolor(xr,yr,Sigma.reshape(xr.size, yr.size))
    cb0 = plt.colorbar(ax0.pcolor(xr,yr,Sigma.reshape(xr.size, yr.size)),ax=ax0)
    cb0.set_label(label= 'Conductivity ($S/m$)',size=ftsize_label) #weight='bold')
    cb0.ax.tick_params(labelsize=ftsize_axis)
    ax0.streamplot(xr,yr,Ep[:,0].reshape(xr.size,yr.size),Ep[:,1].reshape(xr.size,yr.size),color='gray'
                    ,density=0.5,linewidth=2.)
    #ax[0].quiver(np.zeros_like(xrr)-90,yrr,E0,0,angles='xy',scale_units='xy',scale=0.05,color='gray')
    #ax[0].plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax0.set_title('Configuration',fontsize=ftsize_title)
    ax0.annotate('E0',(-80,80),xytext=(-80,80),fontsize=ftsize_title,color='gray',weight='bold')
    ax0.set_xlim([xr.min(),xr.max()])
    ax0.set_ylim([yr.min(),yr.max()])
    ax0.set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax0.set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax0.tick_params(labelsize=ftsize_axis)
    ax0.set_aspect('equal')
    
    ax1.set_xlim([xr.min(),xr.max()])
    ax1.set_ylim([yr.min(),yr.max()])
    ax1.plot(xcirc,np.sqrt(R**2-xcirc**2),'--k',xcirc,-np.sqrt(R**2-xcirc**2),'--k')
    ax1.set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax1.set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax1.tick_params(labelsize=ftsize_axis)
    ax1.set_aspect('equal')
    
    ax2.set_title('Potential Differences',fontsize=ftsize_title)
    ax2.set_ylabel('Potential difference ($V$)',fontsize=ftsize_label)
    ax2.set_xlabel('Distance from start point ($m$)',fontsize=ftsize_label)
    ax2.tick_params(labelsize=ftsize_axis)
    ax2.grid()

    if PlotOpt == 'Total':

        ax1.pcolor(xr,yr,Vt.reshape(xr.size,yr.size))
        cb1 = plt.colorbar(ax1.pcolor(xr,yr,Vt.reshape(xr.size, yr.size)),ax=ax1)
        cb1.set_label(label= 'Potential ($V$)',size=ftsize_label) #weight='bold')
        cb1.ax.tick_params(labelsize=ftsize_axis)
        ax1.set_title('Total Potential',fontsize=ftsize_title)
               
        ax2.plot(np.sqrt((MP[0,0]-MP[:,0])**2+(MP[:,1]-MP[0,1])**2),VtdMP)
        ax2.scatter(np.sqrt((MP[0,0]-MP[:,0])**2+(MP[:,1]-MP[0,1])**2),VtdMP)

    elif PlotOpt == 'Secondary':
               
        ax1.pcolor(xr,yr,Vs.reshape(xr.size,yr.size))
        ax1.set_title('Secondary Potential',fontsize=ftsize_title)
        cb1 = plt.colorbar(ax1.pcolor(xr,yr,Vs.reshape(xr.size, yr.size)),ax=ax1)
        cb1.set_label(label= 'Potential ($V$)',size=ftsize_label) #weight='bold')
        cb1.ax.tick_params(labelsize=ftsize_axis)

        ax2.plot(np.sqrt((MP[0,0]-MP[:,0])**2+(MP[:,1]-MP[0,1])**2),VsdMP)
        ax2.scatter(np.sqrt((MP[0,0]-MP[:,0])**2+(MP[:,1]-MP[0,1])**2),VsdMP)

    else:
        print('What dont you get? Total or Secondary?')
    
    ax1.plot(MP[:,0],MP[:,1],color='gray')           
    Dip_Midpoint = ax1.scatter(MP[:,0],MP[:,1],color='black')
    Electrodes = ax1.scatter(EL[:,0],EL[:,1],color='red')
    ax1.legend([Dip_Midpoint,Electrodes], ["Dipoles Midpoints", "Electrodes"],scatterpoints=1)
    
    plt.tight_layout(True)
    
    return fig

def inversion_uncertainty(XYZ,sig0,sig1,sig2,R0,R1,E0,xstart,ystart,xend,yend,nb_dipole,electrode_spacing,PlotOpt):
    
    xr,yr,zr = np.unique(XYZ[:,0]),np.unique(XYZ[:,1]),np.unique(XYZ[:,2])
    
#Defining the Profile
    start = np.array([xstart,ystart])
    end = np.array([xend,yend])
    
    #Calculating the differents fields
    Sigma0    = get_Conductivity(XYZ,sig0,sig1,R0)
    Sigma1    = get_Conductivity(XYZ,sig0,sig2,R1)
    Vt0,Vp0,Vs0 = get_Potential(XYZ,sig0,sig1,R0,E0)
    Vt1,Vp1,Vs1 = get_Potential(XYZ,sig0,sig2,R1,E0)
    MP0,EL0,VtdMP0,VtdMPn0,VsdMP0,VsdMPn0 = MN_Potential_total(sig0,sig1,R0,E0,start,end,nb_dipole,electrode_spacing)
    MP1,EL1,VtdMP1,VtdMPn1,VsdMP1,VsdMPn1 = MN_Potential_total(sig0,sig2,R1,E0,start,end,nb_dipole,electrode_spacing)
    
    #Primary Field
    Ep = np.zeros(shape=(len(Sigma0),3))
    Ep[:,0] = E0

    #Delineating the 2 differents circles
    xcirc0 = xr[np.abs(xr) <= R0]
    xcirc1 = xr[np.abs(xr) <= R1]

    # Initializing the figure
    fig = plt.figure(figsize=(20,20))
    ax0 = plt.subplot2grid((20,12), (0, 0),colspan=6,rowspan=6)
    ax1 = plt.subplot2grid((20,12), (0, 6),colspan=6,rowspan=6)
    ax2 = plt.subplot2grid((20,12), (16, 2), colspan=9,rowspan=4)
    ax3 = plt.subplot2grid((20,12), (8, 0),colspan=6,rowspan=6)
    ax4 = plt.subplot2grid((20,12), (8, 6),colspan=6,rowspan=6)

    #Plotting the Configuration 0
    cf0 = ax0.pcolor(xr,yr,Sigma0.reshape(xr.size, yr.size)
               ,norm=colors.LogNorm(vmin = min(sig0,sig1,sig2), vmax = max(sig0,sig1,sig2)))
    cb0=plt.colorbar(cf0,ax=ax0)
    cb0.set_clim(vmin = min(sig0,sig1,sig2), vmax = max(sig0,sig1,sig2))
    cb0.set_ticks(np.linspace(min(sig0,sig1,sig2),max(sig0,sig1,sig2),10))
    cb0.set_ticklabels(np.linspace(min(sig0,sig1,sig2),max(sig0,sig1,sig2),10))
    cb0.set_label(label= 'Conductivity ($S/m$)',size=ftsize_label) #weight='bold')
    cb0.ax.tick_params(labelsize=ftsize_axis)
    ax0.streamplot(xr,yr,Ep[:,0].reshape(xr.size,yr.size),Ep[:,1].reshape(xr.size,yr.size),color='gray'
                    ,density=0.5,linewidth=2.)
    ax0.plot(xcirc0,np.sqrt(R0**2-xcirc0**2),'--k',xcirc0,-np.sqrt(R0**2-xcirc0**2),'--k')
    ax0.set_title('Configuration 0',fontsize=ftsize_title)
    ax0.annotate('E0',(-80,80),xytext=(-80,80),fontsize=ftsize_title,color='gray',weight='bold')
    ax0.set_xlim([xr.min(),xr.max()])
    ax0.set_ylim([yr.min(),yr.max()])
    ax0.set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax0.set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax0.tick_params(labelsize=ftsize_axis)
    ax0.set_aspect('equal')
    
    #Plotting the Configuration 1
    cf1 = ax1.pcolor(xr,yr,Sigma1.reshape(xr.size, yr.size)
              ,norm=colors.LogNorm(vmin = min(sig0,sig1,sig2), vmax = max(sig0,sig1,sig2)))
    cb1 = plt.colorbar(cf1,ax=ax1)
    cb1.set_clim(vmin = min(sig0,sig1,sig2), vmax = max(sig0,sig1,sig2))
    cb1.set_ticks(np.linspace(min(sig0,sig1,sig2),max(sig0,sig1,sig2),10))
    cb1.set_ticklabels(np.linspace(min(sig0,sig1,sig2),max(sig0,sig1,sig2),10))
    cb1.set_label(label= 'Conductivity ($S/m$)',size=ftsize_label) #weight='bold')
    cb1.ax.tick_params(labelsize=ftsize_axis)
    ax1.streamplot(xr,yr,Ep[:,0].reshape(xr.size,yr.size),Ep[:,1].reshape(xr.size,yr.size),color='gray'
                    ,density=0.5,linewidth=2.)
    ax1.plot(xcirc1,np.sqrt(R1**2-xcirc1**2),'--k',xcirc1,-np.sqrt(R1**2-xcirc1**2),'--k')
    ax1.set_title('Configuration 1',fontsize=ftsize_title)
    ax1.annotate('E0',(-80,80),xytext=(-80,80),fontsize=ftsize_title,color='gray',weight='bold')
    ax1.set_xlim([xr.min(),xr.max()])
    ax1.set_ylim([yr.min(),yr.max()])
    ax1.set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax1.set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax1.tick_params(labelsize=ftsize_axis)
    ax1.set_aspect('equal')
    
    #Plotting the Fields (Part 1)
    ax3.set_xlim([xr.min(),xr.max()])
    ax3.set_ylim([yr.min(),yr.max()])
    ax3.plot(xcirc0,np.sqrt(R0**2-xcirc0**2),'--k',xcirc0,-np.sqrt(R0**2-xcirc0**2),'--k')
    ax3.set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax3.set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax3.tick_params(labelsize=ftsize_axis)
    ax3.set_aspect('equal')
    
    ax4.set_xlim([xr.min(),xr.max()])
    ax4.set_ylim([yr.min(),yr.max()])
    ax4.plot(xcirc1,np.sqrt(R1**2-xcirc1**2),'--k',xcirc1,-np.sqrt(R1**2-xcirc1**2),'--k')
    ax4.set_ylabel('Y coordinate ($m$)',fontsize=ftsize_label)
    ax4.set_xlabel('X coordinate ($m$)',fontsize=ftsize_label)
    ax4.tick_params(labelsize=ftsize_axis)
    ax4.set_aspect('equal')
    
    #Plotting the Graph (Part 1)
    ax2.set_title('Potential Differences',fontsize=ftsize_title)
    ax2.set_ylabel('Potential difference ($V$)',fontsize=ftsize_label)
    ax2.set_xlabel('Distance from start point ($m$)',fontsize=ftsize_label)
    ax2.tick_params(labelsize=ftsize_axis)
    ax2.grid()

    if PlotOpt == 'Total':
        
        #Plotting the Fields (Part 1)
        ax3.pcolor(xr,yr,Vt0.reshape(xr.size,yr.size))
        cb3 = plt.colorbar(ax3.pcolor(xr,yr,Vt0.reshape(xr.size, yr.size)),ax=ax3)
        cb3.set_label(label= 'Potential ($V$)',size=ftsize_label) #weight='bold')
        cb3.ax.tick_params(labelsize=ftsize_axis)
        ax3.set_title('Total Potential',fontsize=ftsize_title)
               
        gphy0 = ax2.plot(np.sqrt((MP0[0,0]-MP0[:,0])**2+(MP0[:,1]-MP0[0,1])**2),VtdMP0
                         ,marker='o',color='blue',linewidth=3.,label ='Left Model Response' )

        ax4.pcolor(xr,yr,Vt1.reshape(xr.size,yr.size))
        cb4 = plt.colorbar(ax4.pcolor(xr,yr,Vt1.reshape(xr.size, yr.size)),ax=ax4)
        cb4.set_label(label= 'Potential ($V$)',size=ftsize_label) #weight='bold')
        cb4.ax.tick_params(labelsize=ftsize_axis)
        ax4.set_title('Total Potential',fontsize=ftsize_title)
               
        #Plotting the Graph (Part 2)
        gphy1 = ax2.plot(np.sqrt((MP1[0,0]-MP1[:,0])**2+(MP1[:,1]-MP1[0,1])**2),VtdMP1
                ,marker='o',color='red',linewidth=2.,label ='Right Model Response' )
        ax2.legend(('Left Model Response','Right Model Response'),loc=4)

    elif PlotOpt == 'Secondary':
               
        #Plotting the Fields (Part 2)
        ax3.pcolor(xr,yr,Vs0.reshape(xr.size,yr.size))
        ax3.set_title('Secondary Potential',fontsize=ftsize_title)
        cb3 = plt.colorbar(ax3.pcolor(xr,yr,Vs0.reshape(xr.size, yr.size)),ax=ax3)
        cb3.set_label(label= 'Potential ($V$)',size=ftsize_label) #weight='bold')
        cb3.ax.tick_params(labelsize=ftsize_axis)

        gphy0 = ax2.plot(np.sqrt((MP0[0,0]-MP0[:,0])**2+(MP0[:,1]-MP0[0,1])**2),VsdMP0,color='blue'
                ,marker='o',linewidth=3.,label ='Left Model Response' )
        
        
        ax4.pcolor(xr,yr,Vs1.reshape(xr.size,yr.size))
        cb4 = plt.colorbar(ax4.pcolor(xr,yr,Vs1.reshape(xr.size, yr.size)),ax=ax4)
        cb4.set_label(label= 'Potential ($V$)',size=ftsize_label) #weight='bold')
        cb4.ax.tick_params(labelsize=ftsize_axis)
        ax4.set_title('Total Potential',fontsize=ftsize_title)
        
        #Plotting the Graph (Part 2)
        gphy1 = ax2.plot(np.sqrt((MP1[0,0]-MP1[:,0])**2+(MP1[:,1]-MP1[0,1])**2),VsdMP1
                 ,marker='o',color='red',linewidth=2.,label ='Right Model Response' )
        ax2.legend(('Left Model Response','Right Model Response'),loc=4 )
    else:
        print('What dont you get? Total or Secondary?')
    
    #Legends
    ax3.plot(MP0[:,0],MP0[:,1],color='gray')           
    Dip_Midpoint0 = ax3.scatter(MP0[:,0],MP0[:,1],color='black')
    Electrodes0 = ax3.scatter(EL0[:,0],EL0[:,1],color='red')
    ax3.legend([Dip_Midpoint0,Electrodes0], ["Dipole Midpoint", "Electrodes"],scatterpoints=1)
    
    ax4.plot(MP1[:,0],MP1[:,1],color='gray')           
    Dip_Midpoint1 = ax4.scatter(MP1[:,0],MP1[:,1],color='black')
    Electrodes1 = ax4.scatter(EL1[:,0],EL1[:,1],color='red')
    ax4.legend([Dip_Midpoint1,Electrodes1], ["Dipole Midpoint", "Electrodes"],scatterpoints=1)
    
    plt.tight_layout(True)
    
    return fig


if __name__ == '__main__':
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

    fig, ax = plt.subplots(1,2)
    ax[0] = Plot_Total_Currents(XYZ,sig0,sig1,R,E0,ax[0])
    ax[1] = Plot_Secondary_Currents(XYZ,sig0,sig1,R,E0,ax[1])

    
    plt.tight_layout()
    plt.show()

    # example = 'Charges' # ElectricFields, Currents, Charges

    # if example is 'Potentials':
    #     fig, ax = plot_Potentials(XYZ, R, sig1, sig0, E0)
    # elif example is 'ElectricFields':
    #     fig, ax = plot_ElectricField(XYZ, R, sig1, sig0 , E0, PlotOpt)
    # elif example is 'Currents':
    #     fig, ax = plot_Currents(XYZ, R, sig1, sig0, E0, PlotOpt)
    # elif example is 'Charges':
    #     fig, ax = plot_Charges(XYZ,R,sig0,sig1,E0)

