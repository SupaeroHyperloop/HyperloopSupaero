ITERM = 4;
SIGNOISE = 25;
X = 200000;
XD = -6000;
BETA = 500;
XH = 200025;
XDH = -6150;
ORDER = 2;
TS = 0.1;
TF = 30;
PHIS = 0;
T = 0;
S = 0;
H = 0.001;
PHI = zeros(2,2);
P = [SIGNOISE^2 0; 0 20000];
I = [1 0;0 1];
Q = zeros(2,2);
HMAT = [1 0];
HT = HMAT';
RMAT = SIGNOISE^2;
count = 0;

while T<=TF
    XOLD = X;
    XDOLD = XD;
    XDD = 0.0034*32.2*XD^2*exp(-X/22000)/(2*BETA)-32.2;
    X = X+H*XD;
    XD = XD+H*XDD;
    T = T+H;
    XDD = 0.0034*32.2*XD^2*exp(-X/22000)/(2*BETA)-32.2;
    X = 0.5*(XOLD+X+H*XD);
    XD = 0.5*(XDOLD+XD+H*XDD);
    S = S+H;
    if S>=TS
        S = 0;
        RHOH = 0.0034*exp(-XH/22000);
        F21 = -32.2*RHOH*XDH^2/(44000*BETA);
        F22 = RHOH*32.2*XDH/BETA;
        if ITERM==2
            PHI = [1 TS; F21*TS 1+F22*TS];
        elseif ITERM==3
            PHI(1,1) = 1+0.5*TS^2*F21;
            PHI(1,2) = TS+0.5*TS^2*F22;
            PHI(2,1) = F21*TS+0.5*F22*F21*TS^2;
            PHI(2,2) = 1+F22*TS+0.5*TS^2*(F21+F22^2);
        else
            PHI(1,1) = 1+0.5*TS^2*F21+(F22*F21*TS^3)/6;
            PHI(1,2) = TS+0.5*TS^2*F22+(TS^3*(F21+F22^2))/6;
            PHI(2,1) = F21*TS+0.5*F22*F21*TS^2+((F21^2+F22^2*F21)*TS^3)/6;
            PHI(2,2) = 1+F22*TS+0.5*TS^2*(F21+F22^2)+((2*F22*F21+F22^3)*TS^3)/6;
        end

        PHIT = PHI';
        Q(1,1) = PHIS*TS^3/3;
        Q(1,2) = PHIS*(TS^2/2+F22*TS^3/3);
        Q(2,1) = PHIS*(TS^2/2+F22*TS^3/3);
        Q(2,2) = PHIS*(TS+F22*TS^2+F22^2*TS^3/3);

        M = PHI*P*PHIT+Q;
        K = M*HT/(HMAT*M*HT+RMAT);
        P = (I-K*HMAT)*M;

        XNOISE = SIGNOISE*randn;
        XDDB = 0.0034*32.2*XDH^2*exp(-XH/22000)/(2*BETA)-32.2;
        XDB = XDH+XDDB*TS;
        XB = XH+TS*XDB;
        RES = X+XNOISE-XB;
        XH = XB+K(1,1)*RES;
        ERRX = X-XH;
        SP11 = sqrt(P(1,1));
        SP11P = -SP11;
        XDH = XDB+K(2,1)*RES;
        ERRXD = XD-XDH;
        SP22 = sqrt(P(2,2));
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
        ArraySP22(count) = SP22;
        ArraySP11P(count) = SP11P;
        ArraySP22P(count) = SP22P;
    end
end

plot(ArrayT,ArrayERRX)
hold on;
plot(ArrayT,ArraySP11,'--')
plot(ArrayT,ArraySP11P,'--')
hold off;
grid on;
xlabel('Time (sec)');
ylabel('Error in Estimate of Altitude (Ft)');
axis([0 30 -40 20]);

plot(ArrayT,ArrayERRXD)
hold on;
plot(ArrayT,ArraySP22,'--')
plot(ArrayT,ArraySP22P,'--')
hold off;
grid on;
xlabel('Time (sec)');
ylabel('Error in Estimate of Velocity (Ft/Sec)');
axis([0 30 -40 20]);