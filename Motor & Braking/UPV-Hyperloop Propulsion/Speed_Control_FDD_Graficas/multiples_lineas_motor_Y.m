 %%% Main plotting area
    colors = ["#EE7623", "k", "#003B4D", "#8F8FA3", "#7398AD", "#C1C5C8"];
    
    set(groot,'defaultAxesTickLabelInterpreter','latex');  
    
    fig = figure(1);
    
    set(fig, 'Units', 'centimeters')
    pos = get(fig,'Position');
    set(fig,'PaperPositionMode','Auto','PaperUnits','centimeters','PaperSize',[pos(3), pos(4)])
    nLines=16;
    leyenda="";
    if ~ doubleAxisFlag
        for idx = 1:nLines
            
            plot(v_m(:,idx),ForceY(:,idx), 'Color',colors(mod(idx,6)+1), 'LineWidth', 1,'DisplayName',string(frecuencia(k))+'Hz')
            hold on
            leyenda=[leyenda, string(frecuencia(idx))+' [Hz]'];
        end

        hold off
        grid on
        %ylim([0 inf])
        ax = gca;
        ax.PlotBoxAspectRatio = [(1 + sqrt(5))/2, 1, 1];
        y_label='Lateral Force [N]';
        x_label='Mechanical Velocity [Km/h]';

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