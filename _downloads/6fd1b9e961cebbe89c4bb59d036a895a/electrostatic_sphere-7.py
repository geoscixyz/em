from matplotlib import patches
from geoana.em.static import ElectrostaticSphere

sig0 = 10.**-3.          # conductivity of the whole-space in S/m
sig1 = 10.**-1.         # conductivity of the sphere in S/m
sig2 = 10.**-5.         # conductivity of the sphere in S/m
R    = 50.          # radius of the sphere in m
E0   = 1.           # inducing field strength in V/m

sphere1 = ElectrostaticSphere(R, sig1, sig0, E0) # create the sphere object
sphere2 = ElectrostaticSphere(R, sig2, sig0, E0) # create the sphere object

n = 31             #level of discretization
xr = np.linspace(-100, 100, n) # X-axis dipole midpoints
yr = xr.copy()      # Y-axis dipole midpoints
X, Y = np.meshgrid(xr, yr)
Z = np.zeros_like(X)

Dx = np.linspace(-100, 100, n)
Dy = np.linspace(-100, 100, n)
Dz = np.zeros(n)
electrode_spacing = 10

Mx = Dx - 0.5 * electrode_spacing/np.sqrt(2)
My = Dy - 0.5 * electrode_spacing/np.sqrt(2)
Mz = Dz
Nx = Dx + 0.5 * electrode_spacing/np.sqrt(2)
Ny = Dy + 0.5 * electrode_spacing/np.sqrt(2)
Nz = Dz

fig = plt.figure(figsize=(20, 20))
ax0 = plt.subplot2grid((20, 12), (0, 0), colspan=6, rowspan=6)
ax1 = plt.subplot2grid((20, 12), (0, 6), colspan=6, rowspan=6)
ax2 = plt.subplot2grid((20, 12), (8, 0), colspan=6, rowspan=6)
ax3 = plt.subplot2grid((20, 12), (8, 6), colspan=6, rowspan=6)
ax4 = plt.subplot2grid((20, 12), (16, 2), colspan=9, rowspan=4)

for ax, color, sig_circ in zip([ax0, ax1], [[0.6, 0.1, 0.1], [0.1, 0.1, 0.6]], [sig1, sig2]):
    circle = patches.Circle([0,0],radius=R, alpha=0.4, color=color, linewidth=1.5)
    ax.add_patch(circle)
    ax.arrow(0., 0., np.sqrt(2.)*R/2., np.sqrt(2.)*R/2., head_width=0., head_length=0.)

    for y in np.linspace(-2 * R, 2 * R, 10):
        ax.arrow(-2*R, y, 0.3*R, 0.0, head_width=5., head_length=2., color='k')

    ax.text(0, -R/2., f'$\sigma_1$={sig_circ*1000:3.3f} mS/m')
    ax.text(0, -1.5*R, f'$\sigma_0$={sig0*1000:3.3f} mS/m')
    ax.text(0.5*np.cos(np.pi/6)*R, 0.5*np.sin(np.pi/6)*R, f'R={R:1.0f} m')
    ax.text(-1.8*R, 1.3*R, f'$\mathbf{{E_0}} = {E0:1.0f} \mathbf{{\hat{{x}}}}$ V/m')

    ax.set_facecolor([0.4, 0.7, 0.4, 0.3])
    ax.set_xlim([-2 * R, 2 * R])
    ax.set_ylim([-2 * R, 2 * R])
    ax.set_ylabel('Y coordinate ($m$)')
    ax.set_xlabel('X coordinate ($m$)')
    ax.set_aspect('equal')

Vt1 = sphere1.potential((X, Y, Z), field='total')
Vt2 = sphere2.potential((X, Y, Z), field='total')
titles = [
        'Conductive Sphere: \n Total Potential',
        'Resistive Sphere: \n Total Potential',
    ]

for ax, V, title in zip([ax2, ax3], [Vt1, Vt2], titles):
    im = ax.pcolor(X, Y, V, shading='auto')
    cb = plt.colorbar(im, ax=ax)
    cb.set_label(label='Potential ($V$)')
    ax.add_patch(patches.Circle([0,0], R, fill=False, linestyle='--'))

    ax.set_title(title)
    ax.set_ylabel('Y coordinate ($m$)')
    ax.set_xlabel('X coordinate ($m$)')
    ax.set_aspect('equal')

    ax.plot(Dx, Dy, color='gray')
    ax.scatter(Dx, Dx, color='black', label="Dipole Midpoint")
    ax.scatter(np.r_[Mx, Nx], np.r_[My, Ny], color='red', label="Electrodes")
    ax.legend(loc='best')

VM1 = sphere1.potential((Mx, My, Mz), field='total')
VN1 = sphere1.potential((Nx, Ny, Nz), field='total')

VM2 = sphere2.potential((Mx, My, Mz), field='total')
VN2 = sphere2.potential((Nx, Ny, Nz), field='total')

#Plot the Data (from Configuration 0)
ax4.plot(np.sqrt(2)*np.linspace(-100, 100, n), VM1-VN1,
         marker='o', color='red', linewidth=3., label='Left Model Response' )
ax4.plot(np.sqrt(2)*np.linspace(-100, 100, n), VM2-VN2,
         marker='o', color='blue', linewidth=3., label='Right Model Response' )
ax4.set_xlabel('Profile Distance ($m$)')
ax4.set_ylabel('Potential Difference ($V$)')
ax4.legend(loc='best')

plt.show()