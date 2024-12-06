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

Jt1, Jp1, Js1 = sphere1.current_density((X, Y, Z), field='all')
Jt2, Jp2, Js2 = sphere2.current_density((X, Y, Z), field='all')

fig, axs = plt.subplots(2,2,figsize=(18,12))
Js = [Jt1, Jt2, Js1, Js2]
titles = [
    'Conductive Sphere: \n Total Current Density',
    'Resistive Sphere: \n Total Current Density',
    'Conductive Sphere: \n Secondary Current Density',
    'Resistive Sphere: \n Secondary Current Density',
]
for ax, J, title in zip(axs.flatten(), Js, titles):
    J_amp = np.linalg.norm(J, axis=-1)
    im = ax.pcolor(X, Y, J_amp, shading='auto')
    cb = plt.colorbar(im, ax=ax)
    cb.set_label(label='Current Density ($A/m^2$)')
    ax.streamplot(X, Y, J[..., 0], J[..., 1], color='gray', linewidth=2., density=0.75)
    ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

    ax.set_ylabel('Y coordinate ($m$)')
    ax.set_xlabel('X coordinate ($m$)')
    ax.set_aspect('equal')
    ax.set_title(title)

plt.tight_layout()
plt.show()