

[current_a_u,time_u]=sensor_data_convert('motor_a_current_u.csv',1);
[current_a_v,time_u]=sensor_data_convert('motor_a_current_v.csv',1);
[current_a_w,time_u]=sensor_data_convert('motor_a_current_w.csv',1);

[current_b_u,time_u]=sensor_data_convert('motor_b_current_u.csv',1);
[current_b_v,time_u]=sensor_data_convert('motor_b_current_v.csv',1);
[current_b_w,time_u]=sensor_data_convert('motor_b_current_w.csv',1);

[peak_current,time_u]=sensor_data_convert('peak_current.csv',1);
[pos,time_pos]=sensor_data_convert('position.csv',1);
[vel,time_pos]=sensor_data_convert('speed.csv',1);
[frequency,time_frequency]=sensor_data_convert('target_frequency.csv',1);

[target_voltage,time_voltage]=sensor_data_convert('target_voltage.csv',1);
[target_current,time_current]=sensor_data_convert('target_current.csv',1);
%plot(seconds(time_u),current_a_v)

[duty_u,time_u]=sensor_data_convert('duty_u.csv',1);
[duty_v,time_v]=sensor_data_convert('duty_v.csv',1);
[duty_w,time_w]=sensor_data_convert('duty_w.csv',1);

for k = 1:numel(vel)
    if abs(vel(k)) > 50
        vel(k)=vel(k-1);
    end
end

aux=0;
for k = 2:numel(pos)
     pos(k)=pos(k)+aux;
    if abs(pos(k)-pos(k-1)) > 100
        aux=pos(k-1)+aux;
        pos(k)=pos(k-1);
        disp(aux);
    end
end

time_ppu=[];
for k=1:numel(time_u)
    time_ppu(1,k)=0.001*k;
end
time_encoder=[];
for k=1:numel(time_pos)
    time_encoder(k)=0.001*k;
end

%%
figure()
plot(time_encoder,vel)
xlabel('Time (s)')
ylabel('vel (km/h)')

figure()
plot(pos-pos(1),vel)
xlabel('Pos (m)')
ylabel('vel (km/h)')


figure()
hold on
plot(time_ppu,peak_current,'DisplayName','Corriente Pico')
plot(time_ppu,target_current,'DisplayName','Corriente Referencia PI')
plot(time_ppu,target_voltage,'DisplayName','Referencia Voltaje PI')
plot(time_ppu,frequency,'DisplayName','Frecuencia')
xlabel('Time (s)')


figure()
hold on
plot(peak_current,'DisplayName','Corriente Pico')
plot(target_current,'DisplayName','Corriente Referencia PI')
plot(target_voltage,'DisplayName','Referencia Voltaje PI')
plot(time_ppu,frequency,'DisplayName','Frecuencia')
xlabel('Time (s)')


% figure();
% hold on
% plot(duty_u)
% plot(duty_v)
% plot(duty_w)
% plot(peak_current)
% 
% 
f1=figure();
hold on
plot(time_ppu,peak_current,'DisplayName','Corriente Pico')
plot(time_ppu,current_a_u,'DisplayName','Corriente UA')
plot(time_ppu,current_a_v,'DisplayName','Corriente VA')
plot(time_ppu,current_a_w,'DisplayName','Corriente WA')

% 
% f2=figure()
% hold on
plot(time_ppu,current_b_u,'DisplayName','Corriente UB')
plot(time_ppu,current_b_v,'DisplayName','Corriente VB')
plot(time_ppu,current_b_w,'DisplayName','Corriente WB')
% plot(peak_current)
% 
% figure
% plot(pos)
% 
% figure
% plot(vel)