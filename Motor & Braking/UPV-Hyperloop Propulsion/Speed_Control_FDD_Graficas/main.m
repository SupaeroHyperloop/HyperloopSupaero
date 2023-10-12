% This script plots some given data with the corporative layout for the
% Hyperloop UPV's Final Demonstration Documentation. It takes no input nor
% generates outputs explicitly, but guides the user through the process.
% 
% If there's any issue with the implementation or you need special
% characteristics in your plot (like other LineStyles or text), contact
% Ferran de Andrés. 
% ═════════════════════════════════════════════════════════════════════════
% Created by:       Hyperloop UPV Team (Dynamics H7)
% Last updated:     31.01.2022
% ═════════════════════════════════════════════════════════════════════════
% Version log: 
%       * 1.0. First implementation for 2D lines with 1 and 2 axis, with a
%       maximum of 5 different lines in the same plot
% ═════════════════════════════════════════════════════════════════════════

%% Usa esta sección para ordenar tus datos: 
%clear; clc; close all;

%%% Data for third plot
%x = categorical({'Mechanical', 'Propulsion', 'Sense and control', 'Marketing', 'Workspace'});
%x = reordercats(x, {'Mechanical', 'Propulsion', 'Sense and control', 'Marketing', 'Workspace'});

%sponsored = [8954;  22456; 28976; 2089; 560];
%totalCost = [65009; 42333; 32334; 6508; 2000];




%% ¡A dibujar!
%  Esta versión de la función solo admite gráficos de línea, para otros
%  tipos de gráfico como barras o pie charts, ponte en contacto con
%  Outreach. Para gráficas 3D mira la siguiente sección.

run plotH8.m

%% Gráficas 3D

% Descomenta el código de abajo
% Guarda en x y z tus variables
% Recuerda cambiar los nombres del titulo y los ejes!

% set(groot,'defaultAxesTickLabelInterpreter','latex');  
% 
% f = figure();
% s = surf(x, y, z);
% s.EdgeColor = 'white';
% s.EdgeAlpha = 0.25;
% 
% title('\textbf{Nombre de la gráfica}','Interpreter','latex')
% xlabel('Titulo Eje X [unidades]','Interpreter','latex')
% ylabel('Titulo Eje Y [unidades]','Interpreter','latex')
% zlabel('Titulo Eje Z [unidades]','Interpreter','latex')
% 
% colormap copper
% 
% exportgraphics(f,'Grafica3D.png','Resolution',660)



