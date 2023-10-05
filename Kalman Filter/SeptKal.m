function [A, w, dw, cg, g] = fcn

A= [ ones(25,1) , zeros(25,2)]
w= zeros(25,3) 
dw = zeros(25,3) 
cg =  zeros(25,3)
g = [ zeros(25,2),9.8*ones(25,1) ]

end 

function xdot = Kalman_Filter(IMU,GPS,pos_ref,v_ref,acc_ref)

Hz = 100; 
GPSHz = 10; 
% dt = 0.02;
dt = 1/Hz;
t=(0:dt:9)';
n = numel(t);

%Reference Values, x coordinate
% acc_ref = acc_ref(:,1); 
% v_ref = v_ref(:,1); 
% pos_ref = pos_ref(:,1); 

pos_GPS = GPS(:,1); 
% acc_IMU = IMU (:,1); 
acc_IMU = IMU; 

acc_std = 42 *10^-6 *9.8/sqrt(Hz); 
pos_std = 1.6; 

%%


% state matrix (position, velocity, acceleration)
X = zeros(3,1);

% covariance matrix
P = diag([0, 0,1]);

% system noise
Q = diag([1, 0.5, 0.02]);

% transition matrix
F = [1, dt, 0.5*dt^2; 
     0,  1,     dt  ;
     0,  0,     1   ]; 

% observation matrix 
H1 = [0 0 1]; %Accel
H2 = [1 0 0]; %Pos 

% measurement noise 
R = 0; % will be set depending on sensor A or B

% kalman filter output through the whole time
X_arr = zeros(n, 3);

gps_mes = 0; 

for i = 1:n
    y1 = acc_IMU(i);
    R1 = acc_std^2; %set varaince of Sensor A as measurement noise

    
%     R2 = accB_std(i)^2; %set varaince of Sensor B as measurement noise
    R2 = pos_std^2;

    if (i == 1)
        [X] = init_kalman(X, y1); % initialize the state using the 1st sensor
    elseif mod(i,Hz/GPSHz)==0
        gps_mes = gps_mes + 1; 
        y2 = pos_GPS(gps_mes);

        [X, P] = prediction(X, P, Q, F);

        [X, P] = update(X, P, y1, R1, H1); %Update for Sensor A
        [X, P] = update(X, P, y2, R2, H2); %Update for Sensor B
    else 
        [X, P] = prediction(X, P, Q, F);
        [X, P] = update(X, P, y1, R1, H1); %Update for Sensor A
    end

    X_arr(i, :) = X;
end  

%%
% figure(1);
% plot(t, acc_ref, 'LineWidth', 2);
% hold on;
% plot(t, accA, 'LineWidth', 1);
% plot(t, posB, 'LineWidth', 1);
% plot(t, X_arr(:, 1), 'LineWidth', 1);
% plot(t, X_arr(:, 2), 'LineWidth', 2);
% hold off;
% grid on;
% legend('Acceleration Ground Truth', 'SensorAcc', 'SensorPosB', 'Estimation_Position','Estimation_Velocity');
% 
% figure(2);
% plot(t, pos_ref, 'LineWidth', 2);
% hold on;
% % plot(t, accA, 'LineWidth', 1);
% % plot(t, posB, 'LineWidth', 1);
% plot(t, X_arr(:, 1), 'LineWidth', 1);
% % plot(t, X_arr(:, 2), 'LineWidth', 2);
% % plot(t, X_arr(:, 3), 'LineWidth', 1);
% hold off;
% grid on;
% legend('Position Ground Truth', 'SensorPosB', 'Estimation_Position');
% 
% figure(3);
% plot(t, acc_ref, 'LineWidth', 2);
% hold on;
% plot(t, accA, 'LineWidth', 1);
% % plot(t, posB, 'LineWidth', 1);
% % plot(t, X_arr(:, 1), 'LineWidth', 1);
% % plot(t, X_arr(:, 2), 'LineWidth', 2);
% plot(t, X_arr(:, 3), 'LineWidth', 1);
% hold off;
% grid on;
% legend('Acceleratio Ground Truth', 'SensorAcc', 'Estimation Acc');
% 
% figure(4);
% plot(t, v_ref, 'LineWidth', 2);
% hold on;
% %plot(t, accA, 'LineWidth', 1);
% % plot(t, posB, 'LineWidth', 1);
% % plot(t, X_arr(:, 1), 'LineWidth', 1);
% plot(t, X_arr(:, 2), 'LineWidth', 2);
% % plot(t, X_arr(:, 3), 'LineWidth', 1);
% hold off;
% grid on;
% legend('Velocity Ground Truth','Estimation Velocity');
% 
% 
% figure(5)
% plot(t, pos_ref - X_arr(:, 1), 'LineWidth', 1);
% %plot(t, v_ref, 'LineWidth', 2);
% hold on;
% plot(t, v_ref - X_arr(:, 2), 'LineWidth', 1);
% plot(t, acc_ref - X_arr(:, 3), 'LineWidth', 1);
% %plot(t, accA, 'LineWidth', 1);
% % plot(t, posB, 'LineWidth', 1);
% % plot(t, pos_ref - X_arr(:, 1), 'LineWidth', 1);
% %plot(t, X_arr(:, 2), 'LineWidth', 2);
% % plot(t, X_arr(:, 3), 'LineWidth', 1);
% hold off;
% grid on;
% legend('P Error', 'V Error', 'A error');


function [X] = init_kalman(X, y)
X(1) = 0;
X(2) = 0; 
X(3) = y;
end

function [X, P] = prediction(X, P, Q, F)
X = F*X;
P = F*P*F' + Q;
end

function [X, P] = update(X, P, y, R, H)
Inn = y - H*X;
S = H*P*H' + R;
K = P*H'/S;

X = X + K*Inn;
P = P - K*H*P;
end


xdot = zeros(2,1); 
xdot(1) = X(2); 
xdot(2) = -2*k*q^2*(1/(d+X(1))^3 + 1/(d-X(1))^3); 
end 

