load('Fuerzas_primeros_resultados.mat');

% Fuerza en X
figure 
subplot(2,2,1)
for i = 1:1:19
    plot(caso(1).time(1:34,1), caso(1).f_x(1:34,i))
    hold on

end
hold off
title("Desviación 0 mm: Id = 0, Iq = 86")
xlabel("Tiempo (s)")
ylabel("Fuerza X (N)")


subplot(2,2,2)
for i = 1:1:19
    plot(caso(3).time(1:34,1), caso(3).f_x(1:34,i))
    hold on

end
hold off
title("Desviación 0 mm: Id = 86, Iq = 0")
xlabel("Tiempo (s)")
ylabel("Fuerza X (N)")

subplot(2,2,3)
for i = 1:1:19
    plot(caso(2).time(1:34,1), caso(2).f_x(1:34,i))
    hold on

end
hold off
title("Desviación 5 mm: Id = 0, Iq = 86")
xlabel("Tiempo (s)")
ylabel("Fuerza X (N)")

subplot(2,2,4)
for i = 1:1:19
    plot(caso(4).time(1:34,1), caso(4).f_x(1:34,i))
    hold on

end
hold off
title("Desviación 5 mm: Id = 86, Iq = 0")
xlabel("Tiempo (s)")
ylabel("Fuerza X (N)")


% legend({'Diente 1', 'Diente 2', 'Diente 3', 'Diente 4'...
%     'Diente 5', 'Diente 6', 'Diente 7', 'Diente 8', 'Diente 9', 'Diente 10'...
%     'Diente 11', 'Diente 12', 'Diente 13', 'Diente 14', 'Diente 15', 'Diente 16'...
%     'Diente 17', 'Diente 18', 'Diente 19'})

% Fuerza en Y
figure 
subplot(2,2,1)
for i = 1:1:19
    plot(caso(1).time(1:34,1), caso(1).f_y(1:34,i))
    hold on

end
hold off
title("Desviación 0 mm: Id = 0, Iq = 86")
xlabel("Tiempo (s)")
ylabel("Fuerza Y (N)")


subplot(2,2,2)
for i = 1:1:19
    plot(caso(3).time(1:34,1), caso(3).f_y(1:34,i))
    hold on

end
hold off
title("Desviación 0 mm: Id = 86, Iq = 0")
xlabel("Tiempo (s)")
ylabel("Fuerza Y (N)")

subplot(2,2,3)
for i = 1:1:19
    plot(caso(2).time(1:34,1), caso(2).f_y(1:34,i))
    hold on

end
hold off
title("Desviación 5 mm: Id = 0, Iq = 86")
xlabel("Tiempo (s)")
ylabel("Fuerza Y (N)")

subplot(2,2,4)
for i = 1:1:19
    plot(caso(4).time(1:34,1), caso(4).f_y(1:34,i))
    hold on

end
hold off
title("Desviación 5 mm: Id = 86, Iq = 0")
xlabel("Tiempo (s)")
ylabel("Fuerza Y (N)")


% legend({'Diente 1', 'Diente 2', 'Diente 3', 'Diente 4'...
%     'Diente 5', 'Diente 6', 'Diente 7', 'Diente 8', 'Diente 9', 'Diente 10'...
%     'Diente 11', 'Diente 12', 'Diente 13', 'Diente 14', 'Diente 15', 'Diente 16'...
%     'Diente 17', 'Diente 18', 'Diente 19'})


