import numpy as np
from scipy import special

deg2rad  = lambda deg: deg/180.*np.pi
rad2deg  = lambda rad: rad*180./np.pi

def AnBnfun(n, radius, x0, rho, rho1, I=1.):
    const = I*rho/(4*np.pi)
    bunmo = n*rho + (n+1)*rho1
    An = const * radius**(2*n+1) / x0 ** (n+1.) * n * \
        (rho1-rho) / bunmo
    Bn = const * 1. / x0 ** (n+1.) * (2*n+1) * (rho1) / bunmo
    return An, Bn

def DCSpherePointCurrent(txloc, rxloc, xc, radius, rho, rho1, \
                 flag = "sec", order=12):
# def DCSpherePointCurrent(txloc, rxloc, xc, radius, rho, rho1, \
#                  flag = "sec", order=12):    
    """

        Parameters:

            - txloc (array) : current electrode location (x,y,z)                              
            - xc (float)    : x center of depressed sphere
            - rxloc (array) : electrode locations 
                              (Nx3 array, # of electrodes)                         
            - radius (float): radius of the sphere (m)
            - rho (float)   : resistivity of the background (ohm-m)
            - rho1 (float)  : resistivity of the sphere
            - flag (string) : "sec", "total", "prim" 
                              (default="sec")
                              "sec": secondary potential only due to sphere
                              "prim": primary potential from the point source
                              "total": "sec"+"prim"
            - order (float) : maximum order of Legendre polynomial 
                              (default=12)

        Written by Seogi Kang (skang@eos.ubc.ca)
        Ph.D. student of University of British Columbia, Canada

    """

    Pleg = []
    for i in range(order):
        Pleg.append(special.legendre(i, monic=0))            
            
    # Center of the sphere should be aligned in txloc in y-direction
    yc = txloc[1]
    xyz = np.c_[rxloc[:,0]-xc, rxloc[:,1]-yc, rxloc[:,2]]
    r = np.sqrt( (xyz**2).sum(axis=1) )
    
    x0 = abs(txloc[0]-xc)
    
    costheta = xyz[:,0]/r * (txloc[0]-xc)/x0
    phi = np.zeros_like(r)
    R = (r**2+x0**2.-2.*r*x0*costheta)**0.5    
    # primary potential in a whole space 
    prim = rho*1./(4*np.pi*R)

    if flag =="prim":
        return prim
    
    sphind = r < radius
    out = np.zeros_like(r)    
    for n in range(order):
        An, Bn = AnBnfun(n, radius, x0, rho, rho1)
        dumout = An*r[~sphind]**(-n-1.)*Pleg[n](costheta[~sphind])
        out[~sphind] += dumout
        dumin = Bn*r[sphind]**(n)*Pleg[n](costheta[sphind])    
        out[sphind] += dumin

    out[~sphind] += prim[~sphind]
    
    if flag == "sec":
        return out-prim                
    elif flag == "total":              
        return out    

if __name__ == '__main__':
    #TODO add an exmple run
    
    