% This function plots some given data with the corporative layout for the
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

%%% Program initialization

clc;
close all;
f = [];
leyenda = ["legend"];

fprintf('\n')
fprintf('╔═══════════════════════════════════════════════════════════════════════╗\n')
fprintf('║───────────────╔╗─╔╗───────────╔╗──────────╔╗─╔╦═══╦╗──╔╗──────────────║\n')
fprintf('║───────────────║║─║║───────────║║──────────║║─║║╔═╗║╚╗╔╝║──────────────║\n')
fprintf('║───────────────║╚═╝╠╗─╔╦══╦══╦═╣║╔══╦══╦══╗║║─║║╚═╝╠╗║║╔╝──────────────║\n')
fprintf('║───────────────║╔═╗║║─║║╔╗║║═╣╔╣║║╔╗║╔╗║╔╗║║║─║║╔══╝║╚╝║───────────────║\n')
fprintf('║───────────────║║─║║╚═╝║╚╝║║═╣║║╚╣╚╝║╚╝║╚╝║║╚═╝║║───╚╗╔╝───────────────║\n')
fprintf('║───────────────╚╝─╚╩═╗╔╣╔═╩══╩╝╚═╩══╩══╣╔═╝╚═══╩╝────╚╝────────────────║\n')
fprintf('║───────────────────╔═╝║║║──────────────║║──────────────────────────────║\n')
fprintf('║───────────────────╚══╝╚╝──────────────╚╝──────────────────────────────║\n')
fprintf('╚═══════════════════════════════════════════════════════════════════════╝\n \n')

fprintf('¡Hola! Bienvenido a la plataforma de gráficos 2D de H7. Por favor, responde a las siguientes preguntas: \n'); 

%%% Check if we want an special plot
especialPlotFlag = input('\n¿Quieres plotear un gráfico especial (barras, pie chart o 3D)? Si = 1, No = 0: ');

if especialPlotFlag
    barPlotFlag = input('¿Gráfico de barras? Si = 1, No = 0: ');

    if barPlotFlag 
        nLevels = input('\n¿Cuantos niveles hay por columna? ');
        
        x      = input('\n¡Genial! Por favor, indica el nombre de la variable que contiene los datos del eje X: ');
        
        for i = 1:nLevels
            f(i,:) = (input(sprintf('\nIndica la variable que contiene los datos de la parte numero %s. Recuerda que debe estar definida en un vector 1D columna: ', num2str(i)))).';
            if nLevels > 1 
                    leyenda(i) = convertCharsToStrings(input('Indica el nombre (se acepta codigo LaTeX) que quieres que aparezca en la leyenda para los anteriores datos: ', 's'));
            end  
        end
        
        y_label = input('\nIndica el nombre del eje y (sin comillas, y recuerda las unidades entre corchetes): ', 's');
        
        %%% Main plotting area
        set(groot,'defaultAxesTickLabelInterpreter','latex');  
            
        fig = figure(1);
        set(fig, 'Units', 'centimeters')
        pos = get(fig,'Position');
        set(fig,'PaperPositionMode','Auto','PaperUnits','centimeters','PaperSize',[pos(3), pos(4)])
        
        colors = ["#EE7623", "#003B4D", "k",  "#7398AD", "#8F8FA3", "#C1C5C8"];
        
        b = bar(x, f, 'stacked');
        
        for i = 1:nLevels
            b(i).FaceColor = colors(i);
            b(i).EdgeColor = 'k';
        end
        grid on
        
        pbaspect([(1 + sqrt(5))/2, 1, 1])
        
        ylabel(y_label, 'Interpreter','latex')
        ylim([0, 1.2*max(sum(f))])
        xtickangle(45)

        shg
            
        %%% Handling legend
        if nLevels > 1 
            legendPos_1 = lower(input('\nViendo la figura, ¿quieres la leyenda arriba o abajo? ', 's'));
            legendPos_2 = lower(input('Y, ¿a la izquierda o a la derecha? ', 's'));
        
            switch legendPos_1
                case 'arriba'
                    position = 'north';
                case 'abajo'
                    position = 'south';
            end
        
            switch legendPos_2
                case 'izquierda'
                    position = strcat(position, 'west');
                case 'derecha'
                    position = strcat(position, 'east');
            end
        
            legend(leyenda, 'Interpreter','latex', 'Location',position)
        
        end
        
        saveFlag = input('\n¿Estas contento con la figura y la quieres guardar? No = 0, Si = 1: ');
        
        if saveFlag
            nombre_archivo = input('¿Que nombre quieres que tenga el pdf? (sin comillas y todo junto): ','s');
            print(fig, nombre_archivo ,'-dpdf','-r0')
        else
            fprintf('¡No pasa nada! Repitamos')
            pause(2)
            run plotH7.m
        end

    else
        fprintf('Contacta con Amparo (outreach) o Ferran (Dynamics).')
    end

else
    %%% Take number of functions to be plotted
    nLines = input('\nDe acuerdo. ¿Cuantas funciones distintas (líneas) quieres plotear en un mismo gráfico? ');
    
    if nLines > 1
        doubleAxisFlag = (input('¿Quieres que el gráfico tenga 1 eje Y o 2? ') - 1);
    else
        doubleAxisFlag = 0;
    end
    
    %%% Take XY data
    x      = input('\n¡Genial! Por favor, indica el nombre de la variable que contiene los datos del eje X: ');
    
    for idx_nLines = 1:nLines
       f(:,idx_nLines) = input(sprintf('\nIndica la variable que contiene los datos de la función numero %s. Recuerda que debe estar definida en un vector 1D columna: ', num2str(idx_nLines)));
       if nLines > 1 && doubleAxisFlag == 0
            leyenda(idx_nLines) = convertCharsToStrings(input('Indica el nombre (se acepta codigo LaTeX) que quieres que aparezca en la leyenda para la anterior función: ', 's'));
       end
    end
    
    %%% Name axis
    x_label = input('\nIndica el nombre del eje x (sin comillas, y recuerda las unidades entre corchetes): ', 's');
    
    if ~ doubleAxisFlag
        y_label = input('\nIndica el nombre del eje y (sin comillas, y recuerda las unidades entre corchetes): ', 's');
    else
        y_label_1 = input('\nIndica el nombre del eje y izquierdo (sin comillas, y recuerda las unidades entre corchetes): ', 's');
        y_label_2 = input('\nIndica el nombre del eje y derecho (sin comillas, y recuerda las unidades entre corchetes): ', 's');
    end
    
    %%% Main plotting area
    colors = ["#EE7623", "k", "#003B4D", "#8F8FA3", "#7398AD", "#C1C5C8"];
    
    set(groot,'defaultAxesTickLabelInterpreter','latex');  
    
    fig = figure(1);
    
    set(fig, 'Units', 'centimeters')
    pos = get(fig,'Position');
    set(fig,'PaperPositionMode','Auto','PaperUnits','centimeters','PaperSize',[pos(3), pos(4)])
    
    if ~ doubleAxisFlag
        for idx = 1:nLines
            plot(x, f(:,idx), 'Color',colors(idx), 'LineWidth', 1)
            hold on
        end
        hold off
        grid on
    
        ax = gca;
        ax.PlotBoxAspectRatio = [(1 + sqrt(5))/2, 1, 1];
        
        xlabel(x_label, 'Interpreter','latex')
        ylabel(y_label, 'Interpreter','latex')
    else
       yyaxis left
       plot(x, f(:,1), 'Color', colors(1), 'LineWidth', 1.2)
       xlabel(x_label, 'Interpreter','latex')
       ylabel(y_label_1, 'Interpreter','latex')
        
       yyaxis right
       plot(x, f(:,2), 'Color', colors(3), 'LineWidth', 1.2)
       ylabel(y_label_2, 'Interpreter','latex')
       grid on
    
       ax                    = gca;
       ax.YAxis(1).Color     = colors(1);
       ax.YAxis(2).Color     = colors(3);
       ax.PlotBoxAspectRatio = [(1 + sqrt(5))/2, 1, 1];
    end
    
    shg
    
    %%% Handling legend
    if nLines > 1 && doubleAxisFlag == 0
        legendPos_1 = lower(input('Viendo la figura, ¿quieres la leyenda arriba o abajo? ', 's'));
        legendPos_2 = lower(input('Y, ¿a la izquierda o a la derecha? ', 's'));
    
        switch legendPos_1
            case 'arriba'
                position = 'north';
            case 'abajo'
                position = 'south';
        end
    
        switch legendPos_2
            case 'izquierda'
                position = strcat(position, 'west');
            case 'derecha'
                position = strcat(position, 'east');
        end
    
        legend(leyenda, 'Interpreter','latex', 'Location',position)
    
    end
    
    
    saveFlag = input('¿Estas contento con la figura y la quieres guardar? No = 0, Si = 1: ');
    
    if saveFlag
        nombre_archivo = input('¿Que nombre quieres que tenga el pdf? (sin comillas y todo junto): ','s');
        print(fig, nombre_archivo ,'-dpdf','-r0')
    else
        fprintf('¡No pasa nada! Repitamos')
        pause(2)
        run plotH7.m
    end
end



