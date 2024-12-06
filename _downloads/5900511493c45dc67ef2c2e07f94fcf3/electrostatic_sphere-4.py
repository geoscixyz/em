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

Et1, Ep1, Es1 = sphere1.electric_field((X, Y, Z), field='all')
Et2, Ep2, Es2 = sphere2.electric_field((X, Y, Z), field='all')

fig, axs = plt.subplots(2,2,figsize=(18,12))
Es = [Et1, Et2, Es1, Es2]
titles = [
    'Conductive Sphere: \n Total Electric Field',
    'Resistive Sphere: \n Total Electric Field',
    'Conductive Sphere: \n Secondary Electric Field',
    'Resistive Sphere: \n Secondary Electric Field',
]
for ax, E, title in zip(axs.flatten(), Es, titles):
    E_amp = np.linalg.norm(E, axis=-1)
    im = ax.pcolor(X, Y, E_amp, shading='auto')
    cb = plt.colorbar(im, ax=ax)
    cb.set_label(label= 'Amplitude ($V/m$)')
    ax.streamplot(X, Y, E[..., 0], E[..., 1], color='gray', linewidth=2., density=0.75)
    ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

    ax.set_ylabel('Y coordinate ($m$)')
    ax.set_xlabel('X coordinate ($m$)')
    ax.set_aspect('equal')
    ax.set_title(title)

plt.tight_layout()
plt.show()