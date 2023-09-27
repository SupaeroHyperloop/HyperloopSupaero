clc
clear all

%% LIM variables
%PAPER
Llx = 0.0225; %Primary leakage inductance
Lly = 0.0065; %Secondary leakage inductance
Lm = 0.0376; % Lm=1.5*Lm0 ; Lm0 = magnetizing inductance at 0 speed 
Ly = Lm+Lly; %Primary self inductance
Lx = Lm+Llx; %Secondary self inductance
Rx = 1.2; %Primary Resistance (Ohm)
Ry = 2.7; %Secondary Resistance (Ohm)
P = 4400; % Motor Power (W)
l = 0.308; %motor lenght (m)
tau = 0.066; %Pole pitch
we = 314.16; %electrical angular velocity (50 Hz)
Ty = Ly/Ry; %Time constant of secondary circuit
m = 10; %POD mass (kg)

% % V = 150
%   I = 160
% omega_e = 80*2*pi;
% l = 1;
% m = 230;
% Rx = 0.42;
%   


%% CONTROL

%Velocity Control
kp_speed = 2;
ki_speed = 1;

%Force Control
kp_force = 0.015;
ki_force =15;

%Current Control
kp_iedx = 0.2;
ki_iedx = 0.5;
kp_ieqx = 0.2;
ki_ieqx = 0.5;

%Induction Control

kp_lambda = 2;
ki_lambda = 10;


