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

Vt1, Vp1, Vs1 = sphere1.potential((X, Y, Z), field='all')
Vt2, Vp2, Vs2 = sphere2.potential((X, Y, Z), field='all')

fig, axs = plt.subplots(2,2,figsize=(18,12))
for ax, V, title in zip(
    axs.flatten(),
    [Vt1, Vt2, Vs1, Vs2],
    [
        'Conductive Sphere: \n Total Potential',
        'Resistive Sphere: \n Total Potential',
        'Conductive Sphere: \n Secondary Potential',
        'Resistive Sphere: \n Secondary Potential',
    ]
):
    im = ax.pcolor(X, Y, V, shading='auto')
    cb = plt.colorbar(im, ax=ax)
    cb.set_label(label='Potential ($V$)')
    ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

    ax.set_title(title)
    ax.set_ylabel('Y coordinate ($m$)')
    ax.set_xlabel('X coordinate ($m$)')
    ax.set_aspect('equal')

plt.tight_layout()
plt.show()