%% Carga datos motor
datos=readtable("20230208_Barrido_DLIM_Resultados.xlsx");

frecuencia=(3:3:48);
slip=(1:-0.1:0);
Ipeak=(10:10:100);
 
AuxX=[];
AuxY=[];
AuxFlujo=[];
valor=1;


FuerzaX_acel=[];
FuerzaY_acel=[];

for i=1:max(size(slip))
    for j=1:max(size(Ipeak))
        for k=1:max(size(frecuencia))
           FuerzaX_acel(i,j,k)=datos{valor,6};
           FuerzaY_acel(i,j,k)=datos{valor,7};
           valor=valor+1;
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
    plot(v_m(:,k),Force(:,k),'DisplayName',string(frecuencia(k))+'Hz');
end

legend
xlabel('Vel motor(Km/h)')
ylabel('F (N)')
hold off


plot(vel_motor_max_f,datos_f_lineal,'.', 'markersize', 8)
