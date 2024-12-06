import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 12
tau = [0.1, 0.05, 0.01]
fig = plt.figure(figsize=(10, 3))
ax1 = plt.subplot(131)
ax2 = plt.subplot(132)
ax3 = plt.subplot(133)
axs = [ax1, ax2, ax3]

t = np.linspace(-0.2, 1, 300)
oncurrent = np.ones_like(t)
oncurrent[t<0.] = 0.

offcurrent = np.zeros_like(t)
offcurrent[t<0.] = 1.

omega = 5*np.pi*2
current_FD = np.cos(t*omega)

ax1.plot(t, oncurrent, "k", lw=3)
ax2.plot(t, offcurrent, "k", lw=3)
ax3.arrow(0, 0, 0, 0.9, width=0.003, facecolor="k")

for ax in axs:
    ax.plot(t, np.zeros_like(t), "k:", lw=1)
    ax.plot(np.zeros_like(t), np.linspace(-0.2, 1.2, t.size), "k:", lw=1)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Current (A)")
    ax.set_ylim(-.2, 1.2)

ax1.set_title("Step-on current")
ax2.set_title("Step-off current")
ax3.set_title("Impulse current")
plt.tight_layout()
plt.show()