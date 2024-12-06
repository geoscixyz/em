from matplotlib import patches

R = 50  # Define the radius of the sphere

fig, ax = plt.subplots(1,1, figsize = (6,6))

circle = patches.Circle([0,0],radius=R, alpha=0.4, color='blue', linewidth=1.5)
ax.add_patch(circle)
ax.arrow(0., 0., np.sqrt(2.)*R/2., np.sqrt(2.)*R/2., head_width=0., head_length=0.)

for y in np.linspace(-2 * R, 2 * R, 10):
    ax.arrow(-2*R, y, 0.3*R, 0.0, head_width=5., head_length=2., color='k')

ax.text(-1., -np.sqrt(R)/2.-10., '$\sigma_1$')
ax.text(-0.05, -R-10, '$\sigma_0$')
ax.text(0.5*np.cos(np.pi/6)*R, 0.5*np.sin(np.pi/6)*R, 'R')
ax.text(-1.8*R, 1.3*R, '$\mathbf{E_0} = E_0 \mathbf{\hat{x}}$ V/m')

ax.set_facecolor([0.4, 0.7, 0.4, 0.3])
ax.set_xlim([-2 * R, 2 * R])
ax.set_ylim([-2 * R, 2 * R])
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()