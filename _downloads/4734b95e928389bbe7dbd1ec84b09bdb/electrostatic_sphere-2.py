from matplotlib import patches
from geoana.em.static import ElectrostaticSphere

sig0 = 10.**-3.         # conductivity of the whole-space in S/m
sig1 = 10.**-1.         # conductivity of the sphere in S/m
R    = 50.          # radius of the sphere in m
E0   = 1.           # inducing field strength in V/m

sphere = ElectrostaticSphere(R, sig1, sig0, E0) # create the sphere object

n = 50             #level of discretization
xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
yr = xr.copy()      # Y-axis discretization
X, Y = np.meshgrid(xr, yr)
Z = np.zeros_like(X)

potentials = sphere.potential((X, Y, Z), field='primary')

fig, ax = plt.subplots(1,1, figsize = (8,6))
im = ax.pcolor(X, Y, potentials, shading='auto')
cb = plt.colorbar(im)
cb.set_label(label='Potential ($V$)')
ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

ax.set_title('Primary Potential')
ax.set_ylabel('Y coordinate ($m$)')
ax.set_xlabel('X coordinate ($m$)')
ax.set_aspect('equal')