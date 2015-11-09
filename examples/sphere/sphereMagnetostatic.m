% Sphere Problem - Magnetostatic case
%
% Assume we have a permeable sphere in a uniform wholespace. The inducing
% field is constant and in the x-direction with magnitude H0. 

clear all 
close all
clc

%% Parameters

mu1 = 4e-7*pi; % permeability of the wholespace
mu2 = 10*mu1;  % permeability of the sphere
R   = 3;       % radius of the sphere
H0  = 1;       % inducing field strength
d   = 0.1;     % mesh spacing

% useful simplifications
muf = (mu2-mu1)/(mu2+2*mu1);
xr = [-R:d:R];


r  = @(x,y,z) sqrt(x.^2+y.^2+z.^2);

% potential outside the sphere
U1 = @(x,y,z) -H0*x.*(1-muf*R^3./r(x,y,z).^3);

% potential inside the sphere
U2 = @(x,y,z) -H0*x.*3*mu1/(mu2+2*mu1);

U  = @(x,y,z) (r(x,y,z) > R).*U1(x,y,z) + (r(x,y,z) <= R).*U2(x,y,z);
Up = @(x,y,z) - H0.*x;

% magnetic field outside the sphere
H1x = @(x,y,z) H0 + H0*R^3./r(x,y,z).^5.*muf.*(2*x.^2-y.^2-z.^2);
H1y = @(x,y,z) H0*muf.*R^3./r(x,y,z).^5.*3.*x.*y;
H1z = @(x,y,z) H0*muf.*R^3./r(x,y,z).^5.*3.*x.*z;

H2x = @(x,y,z) 3*mu1/(mu2+2*mu1)*ones(size(x));
H2y = @(x,y,z) 0*ones(size(x));
H2z = @(x,y,z) 0*ones(size(x));

Hx = @(x,y,z) (r(x,y,z) > R).*H1x(x,y,z) + (r(x,y,z) <= R).*H2x(x,y,z);
Hy = @(x,y,z) (r(x,y,z) > R).*H1y(x,y,z) + (r(x,y,z) <= R).*H2y(x,y,z); 
Hz = @(x,y,z) (r(x,y,z) > R).*H1z(x,y,z) + (r(x,y,z) <= R).*H2z(x,y,z);

Hxp = @(x,y,z) H0.*ones(size(x));

% plot
x = [-10:d:10];
y = 0;
z = [-10:d:10];

[xg,zg] = meshgrid(x,z);

%% compute potential & fields

% compute the potential
u  = U(xg,y,zg);
up = Up(xg,y,zg);

figure(1)
subplot(121)
pcolor(x,z,u); shading flat; colorbar
axis('square');
title('Potential');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off

subplot(122)
pcolor(x,z,u-up); shading flat; colorbar
title('Secondary Potential');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off


% compute the fields
hx  = Hx(xg,y,zg);
hxp = Hxp(xg,y,zg);
figure(2)
subplot(221)
pcolor(x,z,hx); shading flat; colorbar
title('Hx');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off

subplot(222)
pcolor(x,z,hx-hxp); shading flat; colorbar
title('Hx Secondary');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off

hz = Hz(xg,y,zg);
subplot(2,2,3.5)
pcolor(x,z,hz); shading flat; colorbar
title('Hz');
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off

figure(3)
ix = (x == round(x));
iz = (z == round(z));
subplot(121)
quiver(x(ix),z(iz),hx(ix,iz),hz(ix,iz)); axis('tight')
axis('square');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off

subplot(122)
quiver(x(ix),z(iz),hx(ix,iz)-hxp(ix,iz),hz(ix,iz)); axis('tight')
axis('square');
title('Secondary Field');
hold on
plot(xr,sqrt(R^2-xr.^2),'--k',xr,-sqrt(R^2-xr.^2),'--k');
hold off

%% Effective Susceptibility

% Plot H2/H0 and keff as functions of k2

H2oH0 = @(k2) (3./(k2+3));
keff  = @(k2) (k2./(1+k2/3));

k2 = logspace(0,2.5,100);

figure(4)
subplot(211)
plot(k2,H2oH0(k2)); xlabel('k_2'); ylabel('H_2/H_0');
title('H_2/H_0 as a function of k_2');

subplot(212)
plot(k2,keff(k2)); xlabel('k_2'); ylabel('k_{eff}');
title('k_{eff} as a function of k_2');


%% Equivalent Dipole Moment

% plot the magnitude of the dipole moment as a fct of R for k2 valies of 1,
% 10, 100, 1000, 10000. 

m = @(k2,R) 4/3*pi*R.^3.*keff(k2).*H0;

k2  = 10.^(0:4);
nk2 = numel(k2);
mag = cell(nk2,1);
leg = cell(nk2,1);
R   = (0:d:2);
col = lines(nk2);

figure(5)
hold on
for i = 1:numel(k2)
    mag{i} = m(k2(i),R);
    plot(R,mag{i},'col',col(i,:));
    leg{i} = sprintf('k = %i',k2(i));
end
legend(leg,'location','Northwest');
xlabel('R'); ylabel('m');
title('Dipole Moment magnitude as a function of Radius');
hold off




