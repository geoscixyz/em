import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 12
# Time constant
tau = [0.1, 0.05, 0.01]
fig = plt.figure(figsize=(10, 3))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
axs = [ax1, ax2]
color = ["k", "b", "r"]
t = np.logspace(-3, 0, 61)
for i in range(3):
    resp = 1./tau[i] * np.exp(-t/tau[i])
    ax1.loglog(t, resp, color[i], lw=3)
    ax2.semilogy(t, resp, color[i], lw=3)
for ax in axs:
    ax.grid(True)
    ax.set_ylim(1e-2, 1e2)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Secondary voltage (V)")
ax2.legend(("$\\tau=0.1$","$\\tau=0.05$", "$\\tau=0.01$"), loc=1)
ax1.set_title("Log-Log scale")
ax2.set_title("Lin-Log scale")
plt.tight_layout()
plt.show()