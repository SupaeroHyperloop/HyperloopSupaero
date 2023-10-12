function plotL(AG_map, I_map, inductance)
% Creates a plot of the minductance as a funtion of airgap and intensity
% ═════════════════════════════════════════════════════════════════════════
% Created by:       Ferran de Andres 
% Last updated by:  Ferran de Andres 
% ═════════════════════════════════════════════════════════════════════════
% Last updated: 12.01.2022
% ═════════════════════════════════════════════════════════════════════════

set(groot,'defaultAxesTickLabelInterpreter','latex');  

f = figure();
s = surf(AG_map, I_map, inductance);
s.EdgeColor = 'white';
s.EdgeAlpha = 0.25;

title('\textbf{Inductance \textit{megabarrido}}','Interpreter','latex')
xlabel('Air gap [mm]','Interpreter','latex')
ylabel('Current [A]','Interpreter','latex')
zlabel('Inductance [H]','Interpreter','latex')

colormap copper

exportgraphics(f,'inductance.png','Resolution',660)

end

