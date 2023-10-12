% ╔═══════════════════════════════════════════════════════════════════════╗
% ║───────────────╔╗─╔╗───────────╔╗──────────╔╗─╔╦═══╦╗──╔╗──────────────║
% ║───────────────║║─║║───────────║║──────────║║─║║╔═╗║╚╗╔╝║──────────────║
% ║───────────────║╚═╝╠╗─╔╦══╦══╦═╣║╔══╦══╦══╗║║─║║╚═╝╠╗║║╔╝──────────────║
% ║───────────────║╔═╗║║─║║╔╗║║═╣╔╣║║╔╗║╔╗║╔╗║║║─║║╔══╝║╚╝║───────────────║
% ║───────────────║║─║║╚═╝║╚╝║║═╣║║╚╣╚╝║╚╝║╚╝║║╚═╝║║───╚╗╔╝───────────────║
% ║───────────────╚╝─╚╩═╗╔╣╔═╩══╩╝╚═╩══╩══╣╔═╝╚═══╩╝────╚╝────────────────║
% ║───────────────────╔═╝║║║──────────────║║──────────────────────────────║
% ║───────────────────╚══╝╚╝──────────────╚╝──────────────────────────────║
% ╚═══════════════════════════════════════════════════════════════════════╝
%% Script initialization
clear
clc
close all

%cd C:\FERRAN\2_Hyperloop_2022\1_dynamics_H7\3_Estudio_Inductancia
addpath('plots')
addpath('lib')

% H7
load("data.mat")

air_gap         = r.air_gap;
current         = r.current;
force           = r.force;
magnetic_flux   = r.magnetic_flux;

[AG_map, I_map] = meshgrid(air_gap, current);

% plotMF(AG_map, I_map, magnetic_flux)

% % H8
% load("hems.mat")
% 
% air_gap         = hems.Airgap;
% current         = hems.Current;
% force           = hems.Force_Vertical;
% magnetic_flux   = hems.Flux;
% 
% [AG_map, I_map] = meshgrid(air_gap, current);
% 
% %plotMF(AG_map, I_map, magnetic_flux)
% surf(AG_map, I_map, magnetic_flux)

%% Discretization 

L = zeros((length(current)-2), length(air_gap));        % Inductance [H]

for AG_i = 1:length(air_gap)
    L(:, AG_i) = FDM(magnetic_flux(AG_i, :), current);  
end

[AG_reduced_map, I_reduced_map] = meshgrid(air_gap, current(2:(end-1)));

% plotL(AG_reduced_map, I_reduced_map, L)
surf(AG_reduced_map, I_reduced_map, L)

%% Data collection - Lookup table

hems.inductance              = L;
save("hems.mat", "hems")

%% Data collection - Regression model 

points    = zeros(numel(hems.inductance),3);
current_L = current(2:(end-1));
it        = 1;

for i = 1:size(hems.Airgap,2)
    for j = 1:size(current_L,2)
        points(it,:) = [hems.Airgap(i), current_L(j), hems.inductance(j,i)];
        it = it+1;
    end
end

x = points(1:2:end,1);
y = points(1:2:end,2);
z = points(1:2:end,3);

%%% 3D curve fitting tool
cftool 

%% Sigmoid/tanh model:

% f(x,y) = a * tanh(b *y - c)+ d*x + e
% Coefficients (with 95% confidence bounds):
%        a =   -0.008752  (-0.008818, -0.008685)
%        b =      0.1609  (0.1551, 0.1668)
%        c =       1.389  (1.336, 1.442)
%        d =   6.277e-07  (-1.387e-05, 1.512e-05)
%        e =     0.01042  (0.01017, 0.01068)

plotLmodel(AG_reduced_map, I_reduced_map, points)


%% Step model:

Lstep = zeros(size(Lmodel));

for i = 1:20
    Lstep(i,:) = 0.019 * ones(1,size(Lmodel,2));
end
for i = 21:33
    Lstep(i,:) = 0.0018 * ones(1,size(Lmodel,2));
end

%% Error computation

err_sigmoid = quadError(Lmodel(2:(end-1),:), r.inductance);
err_step    = quadError(Lstep(2:(end-1),:),  r.inductance);

%% Plot max difference

plotModels(r, Lmodel, Lstep)














