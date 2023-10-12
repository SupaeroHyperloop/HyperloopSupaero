function plotModels(r, Lmodel, Lstep)
% Creates a plot of the inductance models
% ═════════════════════════════════════════════════════════════════════════
% Created by:       Ferran de Andres 
% Last updated by:  Ferran de Andres 
% ═════════════════════════════════════════════════════════════════════════
% Last updated: 12.01.2022
% ═════════════════════════════════════════════════════════════════════════

plot(r.current(2:(end-1)), r.inductance(:,1),...
    'LineWidth',1.5, 'Color', 'k', 'LineStyle',  '--')
hold on
plot(r.current(2:(end-1)), r.inductance(:,end),...
    'LineWidth',1.5, 'Color', '#AA4E2F', 'LineStyle',  '--')
hold on

plot(r.current, Lstep(:,1),...
    'LineWidth',1.5, 'Color','#474875', 'LineStyle',  '-')

plot(r.current, Lmodel(:,1),...
    'LineWidth',1.8, 'Color','r', 'LineStyle',  '-')

xlabel('Current [A]','Interpreter','latex')
ylabel('Inductance [H]', 'Interpreter','latex')

ylim([0 0.024])

legend('HF data (ag = 11 mm)', 'HF data (ag = 23 mm)',...
    ' step model ($\varepsilon = 0.089$)', ' sigmoid model ($\varepsilon = 0.038$)',...
    'Interpreter', 'latex',...
    'location','southwest')
grid on
