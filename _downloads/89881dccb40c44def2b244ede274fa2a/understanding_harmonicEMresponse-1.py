from scipy.constants import mu_0
L = 1.
R = 2000.
xc = 0.
yc = 0.
zc = 2.
incl = 0.
decl = 90.
S = 4.
ht = 0.
f = 10000.
xmin = -10.
xmax = 10.
dx = 0.25
xp = np.linspace(xmin, xmax, 101)
yp = xp.copy()
zp = np.r_[-ht]
xyz_profile = np.c_[xp, np.zeros_like(xp), np.ones_like(xp)*ht]
tx_loc = xyz_profile - [S/2, 0, 0]
rx_loc = xyz_profile + [S/2, 0, 0]

def Mij(loc_i, loc_j, dir_i, dir_j, area_i=1, area_j=1):
    di=dir_i[0]*np.pi/180
    dd=dir_i[1]*np.pi/180

    m_i = area_i * np.array([
        np.cos(di)*np.cos(dd),
        np.cos(di)*np.sin(dd),
        np.sin(di)
    ])

    ai=dir_j[0]*np.pi/180
    ad=dir_j[1]*np.pi/180

    m_j = area_j * np.array([
        np.cos(ai)*np.cos(ad),
        np.cos(ai)*np.sin(ad),
        np.sin(ai)
    ])

    dr = loc_i - loc_j
    r = np.linalg.norm(dr, axis=-1)[:, None]
    B = mu_0 / (4*np.pi) * (3 * dr * dr.dot(m_i)[:, None] / r**5 - m_i/r**3)
    return B.dot(m_j)

M13 = Mij(tx_loc, rx_loc, (90, 0), (90, 0))
M12 = Mij(tx_loc, [xc, yc, zc], (90, 0), (incl, decl), area_j=3.0)
M23 = Mij([xc, yc, zc], rx_loc, (incl, decl), (90, 0), area_i=3.0)
C = -M12*M23/(M13*L)


fig = plt.figure(figsize=(5,3))
plt.plot(xp, C, 'k', lw=2)
plt.plot(xp, np.zeros_like(xp), 'k--', lw=1)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Mid point between Tx and Rx (m)")
plt.ylabel("Coupling Coefficient")
plt.grid()
plt.tight_layout()
plt.show()