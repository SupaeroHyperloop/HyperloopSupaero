datos=readtable("20230227_DLIM_H8_Freno_v3.xlsx");

frecuencia_freno=-48:3:-3;

vel_motor_freno=1.368:1.368:10.944;
vel_motor_freno=vel_motor_freno*3.6;

FuerzaX_freno=[];
FuerzaY_freno=[];
Flujo_freno=[];
valor=1;

for i=1:max(size(vel_motor_freno))
    for j=1:max(size(frecuencia_freno))
           AuxFuerzaX_freno(i,j)=-datos{valor,6};
           AuxFuerzaY_freno(i,j)=datos{valor,7};
           AuxslipCalculado(i,j)=datos{valor,5};
           valor=valor+1;
    end
end

for j=1:max(size(frecuencia_freno))
           FuerzaX_freno(:,j)=AuxFuerzaX_freno(:,1-j+max(size(frecuencia_freno)));
           FuerzaY_freno(:,j)=AuxFuerzaY_freno(:,1-j+max(size(frecuencia_freno)));
           slipCalculado(:,j)=AuxslipCalculado(:,1-j+max(size(frecuencia_freno)));
end


figure
hold on
grid
for i=1:max(size(frecuencia_freno))
    plotvalue_freno(i)=plot(vel_motor_freno,FuerzaX_freno(:,i),'DisplayName',string(frecuencia_freno(i))+'Hz');
end

legend
xlabel('Vel motor(Km/h)')
ylabel('F (N)')
hold off
figure
hold on
grid

for i=1:max(size(frecuencia_freno))
    plotvalue_freno(i)=plot(slipCalculado(:,i),FuerzaX_freno(:,i),'DisplayName',string(frecuencia_freno(i))+'Hz');
end

legend
xlabel('Slip')
ylabel('F (N)')
hold off






