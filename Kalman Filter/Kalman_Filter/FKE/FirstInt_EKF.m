SIGNOISE = 25;
G = 32.2;
PHIS = 100;
X = 200000;
XD = -6000;
BETA = 500;
XH = 200025;
XDH = -6150;
TS = 0.1;
TF = 30;
T = 0; 
S = 0;
H = 0.001;
PHI = zeros(2,2);
P = [SIGNOISE^2 0; 0 20000];
I = [1 0;0 1];
Q = zeros(2,2);
HMAT = [1 0];
HT = HMAT';
R = SIGNOISE^2;
count = 0;
while T<=TF
    XOLD = X;
    XDOLD = XD;
    XDD = (0.0034*G*XD^2*exp(-X/22000))/(2*BETA)-G;
    X = X+H*XD;
    XD = XD+H*XDD;
    T = T+H;
    XDD = (0.0034*G*XD^2*exp(-X/22000))/(2*BETA)-G;
    X = 0.5*(XOLD+X+H*XD);
    XD = 0.5*(XDOLD+XD+H*XDD);
    S = S+H;
    if S>=TS
        S = 0;
        RHOH = 0.0034*exp(-XH/22000);
        F21 = -G*RHOH*XDH^2/(44000*BETA);
        F22 = RHOH*G*XDH/BETA;
        PHI = [1 TS;F21*TS 1+F22*TS];
        PHIT = PHI';
        Q = PHIS*[TS^3/3 TS^2/2+F22*TS^3/3; TS^2/2+F22*TS^3/3 TS+F22*TS^2+F22^2*TS^3/3];
        M = PHI*P*PHIT+Q;
        K = M*HT*inv(HMAT*M*HT+R);
        P = (I-K*HMAT)*M;
        XNOISE = SIGNOISE*randn;
        XDDB = (0.0034*G*XDH^2*exp(-XH/22000))/(2*BETA)-G;
        XDB = XDH+XDDB*TS;
        XB = XH+TS*XDB;
        RES = X+XNOISE-XB;
        XH = XB+K(1,1)*RES;
        XDH = XDB+K(2,1)*RES;
        ERRX = X-XH;
        SP11 = sqrt(P(1,1));
        ERRXD = XD-XDH;
        SP22 = sqrt(P(2,2));
        SP11P = -SP11;
        SP22P = -SP22;

        count = count+1;
        ArrayT(count) = T;
        ArrayX(count) = X;
        ArrayXH(count) = XH;
        ArrayERRX(count) = ERRX;
        ArrayXD(count) = XD;
        ArrayXDH(count) = XDH;
        ArrayERRXD(count) = ERRXD;
        ArraySP11(count) = SP11;
        ArraySP11P(count) = SP11P;
        ArraySP22(count) = SP22;
        ArraySP22P(count) = SP22P;
        ArrayRES(count) = RES;
        ArrayK1(count) = K(1,1);
        ArrayK2(count) = K(2,1);
    end
end

plot(ArrayT,ArrayERRX)
hold on
plot(ArrayT,ArraySP11,'--')
plot(ArrayT,ArraySP11P,'--')
hold off
grid on;
xlabel('Time(Sec)');
ylabel('Error in Estimate of Altitude (Ft)');
axis([0 30 -30 30]);

plot(ArrayT,ArrayERRXD)
hold on
plot(ArrayT,ArraySP22,'--')
plot(ArrayT,ArraySP22P,'--')
hold off
grid on;
xlabel('Time(Sec)');
ylabel('Error in Estimate of Velocity (Ft/sec)');
axis([0 30 -50 50]);

% %% Residual
% plot(ArrayT,ArrayRES)
% grid on;
% xlabel('Time(Sec)');
% ylabel('Residual (Ft)');
% axis([0 30 -80 80]);
% 
% %% Kalman Gains
% plot(ArrayT,ArrayK1)
% hold on
% plot(ArrayT,ArrayK2)
% hold off
% grid on;
% xlabel('Time(Sec)');
% ylabel('Kalman Gains');
% axis([0 30 0 0.5]);
% legend('K1','K2');
