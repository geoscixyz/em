import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 12
tau = [1e-1, 1e-1/5, 1e-1/10]
fig = plt.figure(figsize=(10, 3))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
axs = [ax1, ax2]

t = np.linspace(-0.2, 1, 300)
current_TD = np.ones_like(t)
current_TD[t>0.] = 0.
omega = 5*np.pi*2
current_FD = np.cos(t*omega)

ax1.plot(t, current_FD, "k",lw=3)
ax2.plot(t, current_TD, "k", lw=3)

for ax in axs:
    ax.grid(True)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Current (A)")
ax1.set_ylim(-1.2, 1.2)
ax2.set_ylim(-.2, 1.2)

ax1.set_title("Sinusoidal current (5Hz)")
ax2.set_title("Step-off current")
plt.tight_layout()
plt.show()