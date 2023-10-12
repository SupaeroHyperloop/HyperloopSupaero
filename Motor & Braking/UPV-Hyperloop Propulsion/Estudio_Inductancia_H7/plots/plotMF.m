function plotMF(AG_map, I_map, magnetic_flux)
% Creates a plot of the magnetic flux as a funtion of airgap and intensity
% ═════════════════════════════════════════════════════════════════════════
% Created by:       Ferran de Andres 
% Last updated by:  Ferran de Andres 
% ═════════════════════════════════════════════════════════════════════════
% Last updated: 12.01.2022
% ═════════════════════════════════════════════════════════════════════════

set(groot,'defaultAxesTickLabelInterpreter','latex');  

f = figure();
s = surf(AG_map, I_map, magnetic_flux');
s.EdgeColor = 'white';
s.EdgeAlpha = 0.25;

title('\textbf{Magnetic flux \textit{megabarrido}}','Interpreter','latex')
xlabel('Air gap [mm]','Interpreter','latex')
ylabel('Current [A]','Interpreter','latex')
zlabel('Magnetic Flux [Mx]','Interpreter','latex')

colormap copper

exportgraphics(f,'MF.png','Resolution',660)

end

