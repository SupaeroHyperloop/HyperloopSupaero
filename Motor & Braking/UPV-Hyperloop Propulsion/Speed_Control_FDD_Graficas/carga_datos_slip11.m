clear all

datos=readtable("20230207_Barrido_DLIM_Resultados.xlsx");

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


FuerzaX=[];
FuerzaY=[];
Flujo=[];


for i=1:max(size(slip))
    for j=1:max(size(Ipeak))
        for k=1:max(size(frecuencia))
           FuerzaX(i,j,k)=AuxX(max(size(slip))+1-i,j,k);
           FuerzaY(i,j,k)=AuxY(max(size(slip))+1-i,j,k);
           Flujo(i,j,k)=AuxFlujo(max(size(slip))+1-i,j,k);
        end 
    end
end

slipFuerza=(-1:0.1:1);
FuerzaXslip=[-AuxX(1:end-1,:,:);FuerzaX(1:end,:,:)];

%% Graficas vel-fuerza
v_m=[];
Force=[];
maxForce=[];
indicesSlip=[];



figure
hold on
grid
for k=1:max(size(frecuencia))
   v_ref=7.2*0.114*frecuencia(k);
    for i=1:max(size(slip))
        v_m(i,k)=v_ref-slip(i)*v_ref;
        Force(i,k)=FuerzaX(i,max(size(Ipeak)),k);
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
freq_motor_max_f=[];
for m=1:max(size(v_motor))
    [maximo,indice]=max(newy(:,m));
    vel_motor_max_f(m)=v_motor(m);
    frec_max_f(m)=frecuencia(indice);
end

figure
hold on
plot(vel_motor_max_f,frec_max_f,'.', 'markersize', 8)
hold off



% miny = min(newy);                                       % Minimum Of All Curves
% maxy = max(newy);                                       % Maximum Of All Curves
% miny = miny(~isnan(miny));
% maxy = maxy(~isnan(maxy));
% [~,nsc] = find(~isnan(newy),1);
% [~,nec] = find(~isnan(newy),1,'last');
% patch([v_motor(nsc:nec), fliplr(v_motor(nsc:nec))], [miny fliplr(maxy)], [0.7 0.8 0.9], 'EdgeColor','none')
% 
% for k1 = 1:numel(hL)
%     plot(plotvalue(k1).XData, plotvalue(k1).YData)                    % Re-Plot Original Curves
% end
% 
% 
% 
% figure




%%


addpath('plots')
addpath('lib')

current         = Ipeak;
L = zeros((length(current)-2), length(slip),length(frecuencia));        % Inductance [H]
figure()
for k=1:max(size(frecuencia))



magnetic_flux   = Flujo(:,:,k);

[AG_map, I_map] = meshgrid(slip, current);

%% Discretization 



for AG_i = 1:length(slip)
    L(:, AG_i,k) = FDM(magnetic_flux(AG_i, :), current);  
end

[AG_reduced_map, I_reduced_map] = meshgrid(slip, current(2:(end-1)));

% plotL(AG_reduced_map, I_reduced_map, L)

surf(AG_reduced_map, I_reduced_map, L(:,:,k))
end

surf(AG_reduced_map, I_reduced_map, L(:,:,5))

