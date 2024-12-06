from matplotlib import patches
from geoana.em.static import ElectrostaticSphere

sig0 = 10.**-3.          # conductivity of the whole-space in S/m
sig1 = 10.**-1.         # conductivity of the sphere in S/m
sig2 = 10.**-5.         # conductivity of the sphere in S/m
R    = 50.          # radius of the sphere in m
E0   = 1.           # inducing field strength in V/m

sphere1 = ElectrostaticSphere(R, sig1, sig0, E0) # create the sphere object
sphere2 = ElectrostaticSphere(R, sig2, sig0, E0) # create the sphere object

n = 50             #level of discretization
xr = np.linspace(-2.*R, 2.*R, n) # X-axis discretization
yr = xr.copy()      # Y-axis discretization
X, Y = np.meshgrid(xr, yr)
Z = np.zeros_like(X)

q1 = sphere1.charge_density((X, Y, Z), dr=xr[1]-xr[0])
q2 = sphere2.charge_density((X, Y, Z), dr=xr[1]-xr[0])

fig, axs = plt.subplots(1,2,figsize=(18,6))
qs = [q1, q2]
titles = ['Conductive Sphere: \n Charge Accumulation', 'Resistive Sphere: \n Charge Accumulation']

for ax, q, title in zip(axs, qs, titles):
    im = ax.pcolor(X, Y, q, shading='auto')
    cb1 = plt.colorbar(im, ax=ax)
    cb1.set_label(label= 'Charge Density ($C/m^2$)')
    ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

    ax.set_ylabel('Y coordinate ($m$)')
    ax.set_xlabel('X coordinate ($m$)')
    ax.set_title(title)
    ax.set_aspect('equal')

plt.tight_layout()
plt.show()