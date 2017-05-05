import numpy as np
import matplotlib.pyplot as plt
import em_examples.dipole_figures_homogeneous_medium_functions as fcnFields

p = 1.
L0 = 0.001
Emax = 1e3

m = 1.          
Hmax = 1e3

xmin, xmax, dx = -1., 1., 0.025
ymin, ymax, dy = -1., 1., 0.025
x,y = np.mgrid[xmin:xmax+dx:dx, ymin:ymax+dy:dy]
x = np.transpose(x)
y = np.transpose(y)

Ex0, Ey0, Eabs0 = fcnFields.fcnE_ShortWireX(x,y,p,L0,Emax)
Hx0, Hy0, Habs0 = fcnFields.fcnH_DipoleY(x,y,m,Hmax)
FS = 30
dL = 0.495

fig1 = plt.figure(1,figsize=(29,10))

ax1 = plt.subplot(121)
cplot1 = ax1.contourf(x,y,np.log10(Eabs0),40,cmap='gist_heat_r')
ax1.streamplot(x,y,Ex0,Ey0,color=(0.2,0.2,0.2),linewidth=3.5)
ax1.arrow( -0.25*dL, 0, 0.3*dL, 0, fc="y", ec="k",head_width=0.2, head_length=0.2,width=0.08 )
cbar1 = fig1.colorbar(cplot1)
cbar1.set_label('log10($\mathbf{|J|}$)', rotation=270, labelpad = 20, size=FS)
cbar1.ax.tick_params(labelsize=FS)
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.xticks(fontsize=FS)
plt.yticks(fontsize=FS)
plt.xlabel('X [m]',fontsize=FS+4)
plt.ylabel('Y [m]',fontsize=FS+4)
plt.title('Electrical Current Dipole',fontsize=FS+8)
plt.text(-0.04,-0.25,'$\mathbf{p}$',fontsize=FS+32)     # Definition

ax2 = plt.subplot(122)
cplot2 = ax2.contourf(x,y,np.log10(Habs0),40,cmap='ocean_r')       # Seogi used viridis
ax2.streamplot(x,y,Hx0,Hy0,color=(0.2,0.2,0.2),linewidth=3.5)
ax2.arrow( 0, -0.125, 0, 0.15, fc=((0.7,0,0.7)), ec="k",head_width=0.2, head_length=0.2,width=0.08 )
cbar2 = fig1.colorbar(cplot2)
cbar2.set_label('log10($\mathbf{|H|}$)', rotation=270, labelpad = 20, size=FS)     # labelpad moves label left-right
cbar2.ax.tick_params(labelsize=FS)
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.xticks(fontsize=FS)
plt.yticks(fontsize=FS)
plt.xlabel('X [m]',fontsize=FS+4)
plt.ylabel('Y [m]',fontsize=FS+4)
plt.title('Magnetic Dipole',fontsize=FS+8)
plt.text(-0.35,-0.05,'$\mathbf{m}$',fontsize=FS+32)

plt.show()