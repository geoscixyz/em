% Sphere Problem - Electrostatic case
%
% In this program, we investigate the case of a conductive sphere in a 
% wholespace, subject to a uniform electrostatic field.
%
% We assume that the sphere has radius R, and conductivity sig2. The
% background has conductivity sig1. We assume that the permittivity is a
% constant, and equal to that of free space in the entire domain. 
%
% The inducing field is constant and oriented in the x-direction. 
%
% Naming convention
%    1: outside the sphere
%    2: inside the sphere
% 
% The origin of our coordinate system is at the center of the sphere
%
% To set up the problem, we start with Maxwell's equations:
%    CURL E = 0
%    CURL H = J
%         J = sig E
%
% Since CURL E = 0, we can define
%         E = - GRAD V
%
% with the interface conditions at r = R
%      J1_n = J2_n  (normal component of flux continuous)
%        V1 = V2    (the potential is continuous) 


clear all 
close all
clc

%% Parameters

sig1 = 1e-1        % conductivity of the wholespace
sig2 = 2           % conductivity of the sphere
R    = 50          % radivs of tee sphere
E0   = 1           % inducing field strength
d    = 2;         % mesh spacing
e0   = 8.85*10^-12; % permittivity of free space

% usefvl simplifications
sigf = @(sig1,sig2) (sig2-sig1)/(sig2+2*sig1);
xr = [-R:d:R];
r  = @(x,y,z) sqrt(x.^2+y.^2+z.^2);

%% Define the fields and potentials
% potential ovtside the sphere
V1 = @(x,y,z,sig1,sig2) -E0*x.*(1-sigf(sig1,sig2)*R^3./r(x,y,z).^3);

% potential inside the sphere
V2 = @(x,y,z,sig1,sig2) -E0*x.*3*sig1/(sig2+2*sig1);

V  = @(x,y,z,sig1,sig2) (r(x,y,z) > R).*V1(x,y,z,sig1,sig2) + (r(x,y,z) <= R).*V2(x,y,z,sig1,sig2);
Vp = @(x,y,z,sig1,sig2) - E0.*x;

% electric field outside the sphere
E1x = @(x,y,z,sig1,sig2) E0 + E0*R^3./r(x,y,z).^5.*sigf(sig1,sig2).*(2*x.^2-y.^2-z.^2);
E1y = @(x,y,z,sig1,sig2) E0*R^3./r(x,y,z).^5.*3.*x.*y*sigf(sig1,sig2);
E1z = @(x,y,z,sig1,sig2) E0*R^3./r(x,y,z).^5.*3.*x.*z*sigf(sig1,sig2);

E2x = @(x,y,z,sig1,sig2) 3*sig1/(sig2+2*sig1)*ones(size(x));
E2y = @(x,y,z,sig1,sig2) 0*ones(size(x));
E2z = @(x,y,z,sig1,sig2) 0*ones(size(x));

Ex = @(x,y,z,sig1,sig2) (r(x,y,z) > R).*E1x(x,y,z,sig1,sig2) + (r(x,y,z) <= R).*E2x(x,y,z,sig1,sig2);
Ey = @(x,y,z,sig1,sig2) (r(x,y,z) > R).*E1y(x,y,z,sig1,sig2) + (r(x,y,z) <= R).*E2y(x,y,z,sig1,sig2); 
Ez = @(x,y,z,sig1,sig2) (r(x,y,z) > R).*E1z(x,y,z,sig1,sig2) + (r(x,y,z) <= R).*E2z(x,y,z,sig1,sig2);

Exp = @(x,y,z,sig1,sig2) E0.*ones(size(x));

x = [-3*R:d:3*R];
y = 0;
z = [-3*R:d:3*R];

[xg,zg] = meshgrid(x,z);

%% compute potential & fields
% In this section, we compute the primary and secondary potentials, as well
% as the components of the electric field and plot them. 
%  Figure 1: A plot of the primary and secondary potential in the domain
%  Figure 2: A plot of the x and z - components of the electric field. We
%  show both the 
% compute the potential
v  = V(xg,y,zg,sig1,sig2);
vp = Vp(xg,y,zg,sig1,sig2);

figure(1)
subplot(121)
pcolor(x,z,v); shading flat; colorbar
axis('square');
title('Potential');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

subplot(122)
pcolor(x,z,v-vp); shading flat; colorbar
title('Secondary Potential');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

% compute the fields
ex  = Ex(xg,y,zg,sig1,sig2);
exp = Exp(xg,y,zg,sig1,sig2);

figure(2)
subplot(221)
pcolor(x,z,ex); shading flat; colorbar
title('Ex');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

subplot(222)
pcolor(x,z,ex-exp); shading flat; colorbar
title('Ex Secondary');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

ez = Ez(xg,y,zg,sig1,sig2);
subplot(2,2,3.5)
pcolor(x,z,ez); shading flat; colorbar
title('Ez');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

figure(3)
ix = (x == 5*round(x./5));
iz = (z == 5*round(z./5));

subplot(121)
quiver(x(ix),z(iz),ex(ix,iz),ez(ix,iz)); axis('tight')
title('Full Field');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

subplot(122)
quiver(x(ix),z(iz),ex(ix,iz)-exp(ix,iz),ez(ix,iz)); axis('tight')
axis('square');
title('Secondary Field');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

%% Current Density

Jx = @(x,y,z,sig1,sig2) ((r(x,y,z) > R).*sig1 + (r(x,y,z) <= R).*sig2).*(Ex(x,y,z,sig1,sig2));
Jy = @(x,y,z,sig1,sig2) ((r(x,y,z) > R).*sig1 + (r(x,y,z) <= R).*sig2).*(Ey(x,y,z,sig1,sig2));
Jz = @(x,y,z,sig1,sig2) ((r(x,y,z) > R).*sig1 + (r(x,y,z) <= R).*sig2).*(Ez(x,y,z,sig1,sig2));

jx = Jx(xg,y,zg,sig1,sig2);
jy = Jy(xg,y,zg,sig1,sig2);
jz = Jz(xg,y,zg,sig1,sig2);


figure(4)

subplot(221)
pcolor(x,z,jx); shading flat; colorbar
title('Jx');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

subplot(222)
pcolor(x,z,jz); shading flat; colorbar
title('Jz');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

ix = (x == 5*round(x./5));
iz = (z == 5*round(z./5));
subplot(2,2,3.5)
quiver(x(ix),z(iz),jx(ix,iz),jz(ix,iz)); axis('tight')
title('J');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off
xlabel('x'); ylabel('z');

%% Magnitude of electric dipole moment
Sig = logspace(-5,2);
p   = 4*pi*R.^3*E0*e0*(Sig-1)./(Sig+2);

figure(5)
plot(Sig,p);
title('Electric Dipole moment');
xlabel('\sigma_2 / \sigma_1'); ylabel('dipole moment');

%% Plot Ex Ez along the x-axis at y = 0, z = 75m for various sig2/sig1
Sig = logspace(-3,3,5);
y = 0;
z = 75;

exf = zeros(numel(x),numel(Sig));
ezf = zeros(numel(x),numel(Sig));
leg = cell(numel(Sig),1);

for i = 1:numel(Sig)
    sig2 = Sig(i)*sig1;
    exf(:,i) = Ex(x,y,z,sig1,sig2);
    ezf(:,i) = Ez(x,y,z,sig1,sig2);
    leg{i} = sprintf('s2/s1 = %1.0e',Sig(i));
end

figure(6)
subplot(121)
plot(x,exf);
title('Ex with varying \sigma_2/\sigma_1');
xlabel('x'); ylabel('Ex');
legend(leg); xlim([min(x),max(x)]);

subplot(122)
plot(x,ezf);
title('Ez with varying \sigma_2/\sigma_1')
xlabel('x'); ylabel('Ez');
legend(leg); xlim([min(x),max(x)]);

