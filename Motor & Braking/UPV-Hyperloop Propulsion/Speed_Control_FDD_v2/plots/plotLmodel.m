function plotLmodel(AG_map, I_map, points)
% Creates a plot of the inductance model regression
% ═════════════════════════════════════════════════════════════════════════
% Created by:       Ferran de Andres 
% Last updated by:  Ferran de Andres 
% ═════════════════════════════════════════════════════════════════════════
% Last updated: 12.01.2022
% ═════════════════════════════════════════════════════════════════════════

set(groot,'defaultAxesTickLabelInterpreter','latex');  

a =   -0.008752;
b =      0.1609;
c =       1.389;
d =           0;
e =     0.01042;

Lmodel = a .* tanh(b.*I_map - c)+ d.*AG_map + e;

f = figure();
s = surf(AG_map, I_map, Lmodel);
hold on

scatter3(points(1:2:end,1),points(1:2:end,2),points(1:2:end,3),10, ...
         'k','filled','MarkerFaceAlpha',0.75)

s.EdgeColor = 'white';
s.EdgeAlpha = 0.25;

title('\textbf{Inductance non-linear model}','Interpreter','latex')
xlabel('Air gap [mm]','Interpreter','latex')
ylabel('Current [A]','Interpreter','latex')
zlabel('Inductance [H]','Interpreter','latex')

colormap copper

exportgraphics(f,'inductance_model.png','Resolution',660)

end

