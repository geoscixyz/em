L = 1.
R = 2000.
alpha = np.logspace(-3, 3, 100)
Q = (alpha ** 2 + 1j * alpha) / (1 + alpha ** 2)
fig = plt.figure(figsize=(5, 3))
ax1 = plt.subplot(111)
ax1.semilogx(alpha, Q.real, 'k', lw=3)
ax1.semilogx(alpha, Q.imag, 'r', lw=3)
ax1.grid(True)
ax1.legend(("Real","Imaginary"), loc=2)
ax1.set_xlabel("Induction number ($\\alpha$)")
ax1.set_ylabel("Response function (Q)")
plt.tight_layout()
plt.show()