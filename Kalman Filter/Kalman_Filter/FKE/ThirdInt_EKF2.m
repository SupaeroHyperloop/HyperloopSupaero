i = 1;
while i<=5
SIGNOISE = 25;
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
HMAT = [1 0];
P = [SIGNOISE^2 0; 0 150*150];
I = [1 0;0 1];
Q = zeros(2,2);
HT = HMAT';
RMAT = SIGNOISE^2;
count = 0;

while T<=TF
    XOLD = X;
    XDOLD = XD;
    XDD = 0.0034*32.2*XD^2*exp(-X/22000)/(2*BETA)-32.2;
    XD = XD+H*XDD;
    X = X+H*XD;
    T = T+H;
    XDD = 0.0034*32.2*XD^2*exp(-X/22000)/(2*BETA)-32.2;
    XD = 0.5*(XDOLD+XD+H*XDD);
    X = 0.5*(XOLD+X+H*XD);
    S = S+H;
    if S>=TS
        S = 0;
        RHOH = 0.0034*exp(-XH/22000);
        F21 = -32.2*RHOH*XDH^2/(44000*BETA);
        F22 = RHOH*32.3*XDH^2/(44000*BETA);
        PHI = [1 TS;F21*TS 1+F22*TS];
        PHIT = PHI';
        Q = PHIS*[TS^3/3 TS^2/2+TS^3/3;TS^2/2+TS^3/3 TS+F22*TS^2+F22^2*TS^3/3];

        M = PHI*P*PHIT+Q;
        K = M*HT/(HMAT*M*HT+RMAT);
        P = (I-K*HMAT)*M;

        XNOISE = SIGNOISE*randn;
        [XB,XDB,XDDB] = project(T,TS,XH,XDH,BETA);
        RES = X+XNOISE-XB;
        XH = XB+K(1,1)*RES;
        XDH = XDB+K(2,1)*RES;
        ERRX = X-XH;
        ERRXD = XD-XDH;
        SP11 = sqrt(P(1,1));
        SP11P = -SP11;
        SP22 = sqrt(P(2,2));
        SP22P = -SP22;
        count = count+1;
        ArrayT(count) = T;
        ArrayERRX(count) = ERRX;
        ArrayERRXD(count) = ERRXD;
        ArraySP11(count) = SP11;
        ArraySP11P(count) = SP11P;
        ArraySP22(count) = SP22;
        ArraySP22P(count) = SP22P;
        ArrayRES(count) = RES;
    end
end 

plot(ArrayT,ArrayERRX,'--')
hold on;
plot(ArrayT,ArraySP11)
plot(ArrayT,ArraySP11P)
grid on;
xlabel('Time (sec)');
ylabel('Error in Estimate of Altitude (Ft)');
axis([0 30 -30 30]);

% plot(ArrayT,ArrayERRXD,'--')
% hold on;
% plot(ArrayT,ArraySP22)
% plot(ArrayT,ArraySP22P)
% grid on;
% xlabel('Time (sec)');
% ylabel('Error in Estimate of Velocity (Ft/sec)');
% axis([0 30 -50 50]);

i = i+1;
end



% plot(ArrayT,ArrayRES)
% grid on;
% xlabel('Time (sec)');
% ylabel('Residual (Ft)');
% axis([0 30 -60 80]);
% legend('SIGNOISE = 25 FT PHIS = 0 H = 0.001 S');

function [XH,XDH,XDDH] = project(TP,TS,XP,XDP,BETA)
T = 0;
X = XP;
XD = XDP;
H = 0.001;
while T<=TS
    XDD = 0.0034*32.2*XD^2*exp(-X/22000)/(2*BETA)-32.2;
    XD = XD+H*XDD;
    X = X+H*XD;
    T = T+H;
end
XH = X;
XDH = XD;
XDDH = XDD;
end
