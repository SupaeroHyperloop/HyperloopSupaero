%% Carga datos Drag

datos=readtable("Estudio drag 3D.xlsx");

vel_drag=0:5:35;
airgap_drag=8:5:23;
valor=1;
Force_drag=[];

for i=1:max(size(vel_drag))
    for j=1:max(size(airgap_drag))
        Force_drag(i,j)=datos{valor,2};
        valor=valor+1;
    end
end
plot(vel_drag,Force_drag(:,1))