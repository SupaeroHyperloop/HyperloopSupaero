%% Carga datos motor

datos=readtable("20230208_Barrido_DLIM_Resultados.xlsx");

frecuencia=(3:3:48);
%No puede ser vector hacia abajo
slip=(0:0.1:1);
Ipeak=(10:10:100);
 
AuxX=[];
AuxY=[];
AuxFlujo=[];
valor=1;

mass=200;
%Resistencia
r=0.384;
pole_length=0.114;

for i=1:max(size(slip))
    for j=1:max(size(Ipeak))
        for k=1:max(size(frecuencia))
           AuxX(i,j,k)=datos{valor,6};
           AuxY(i,j,k)=datos{valor,7};
           AuxFlujo(i,j,k)=double(datos{valor,8});
           valor=valor+1;
        end 
    end
end


FuerzaX_acel=[];
FuerzaY_acel=[];
Flujo_acel=[];

%Girar el vector para slip
for i=1:max(size(slip))
    for j=1:max(size(Ipeak))
        for k=1:max(size(frecuencia))
           FuerzaX_acel(i,j,k)=AuxX(max(size(slip))+1-i,j,k);
           FuerzaY_acel(i,j,k)=AuxY(max(size(slip))+1-i,j,k);
           Flujo_acel(i,j,k)=AuxFlujo(max(size(slip))+1-i,j,k);
        end 
    end
end



%% Graficas vel-fuerza
v_m=[];
Force=[];
maxForce=[];

 figure
 hold on
 grid




for k=1:max(size(frecuencia))
   v_ref=7.2*0.114*frecuencia(k);
    for i=1:max(size(slip))
        v_m(i,k)=v_ref-slip(i)*v_ref;
        Force(i,k)=FuerzaX_acel(i,max(size(Ipeak)),k);
        ForceY(i,k)=FuerzaY_acel(i,max(size(Ipeak)),k);
    end
    
    plotvalue(k)=plot(v_m(:,k),Force(:,k),'DisplayName',string(frecuencia(k))+'Hz');
end
legend
xlabel('Vel motor(Km/h)')
ylabel('F (N)')
hold off

v_motor=linspace(0,35,max(size(slip)));
td = get(plotvalue, 'XData');
tdm = cell2mat(td); 
yd=get(plotvalue,'YData');
ydm = cell2mat(yd);
newy = zeros(size(tdm,1), numel(v_motor));

for k1 = 1:size(tdm,1)
    newy(k1,:) = interp1(tdm(k1,:), ydm(k1,:), v_motor);   % Map Individual Curve Independent Variables To ‘allt’
end

vel_motor_max_f=[];
frec_motor_max_f=[];
for m=1:max(size(v_motor))
    [maximo,indice]=max(newy(:,m));
    vel_motor_max_f(m)=v_motor(m);
    frec_motor_max_f(m)=frecuencia(indice);
end

figure
hold on
plot(vel_motor_max_f,frec_motor_max_f,'.', 'markersize', 8)

%Curve Fitter obtener parametros
p1=1.3;
p2=8.4;

datos_f_lineal=p2+p1*vel_motor_max_f;

plot(vel_motor_max_f,datos_f_lineal,'.', 'markersize', 8)


%% Calculo inductancia


addpath('plots')
addpath('lib')

current         = Ipeak;

L = zeros((length(current)-2), length(slip),length(frecuencia)); 
% Inductance [H]
figure()
for k=1:max(size(frecuencia))

    magnetic_flux   = Flujo_acel(:,:,k);
    [AG_map, I_map] = meshgrid(slip, current);

    % Discretization 

    for AG_i = 1:length(slip)
        L(:, AG_i,k) = FDM(magnetic_flux(AG_i, :), current);  
    end

    [AG_reduced_map, I_reduced_map] = meshgrid(slip, current(2:(end-1)));

    % plotL(AG_reduced_map, I_reduced_map, L)

     surf(AG_reduced_map, I_reduced_map, L(:,:,k))
end

 surf(AG_reduced_map, I_reduced_map, L(:,:,5))




