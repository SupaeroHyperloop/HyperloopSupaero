ORDER = 2;
PHIS = 10000;
TS = 0.1;
A0 = 400000;
A1 = -6000;
A2 = -16.1;
XH = 0;
XDH = 0;
SIGNOISE = 1000;
PHI = [1 TS ; 0 1];
P = [99999999 0; 0 99999999];
IDNP = eye(ORDER);
I = [1 0; 0 1];
H = [1 0];
HT = H';
R = SIGNOISE^2;
PHIT = PHI';
count = 0;
Q = [(PHIS*TS^3)/3 (PHIS*TS^2)/2;(PHIS*TS^2)/2 PHIS*TS];

for T=0:TS:30
    M = PHI*P*PHIT+Q;
    K = M*HT*inv(H*M*HT+R);
    P = (I-K*H)*M;
    XNOISE = SIGNOISE*randn;
    X = A0+A1*T+A2*T^2;
    XD = A1+2*A2*T;
    XS = X+XNOISE;
    RES = XS-XH-TS*XDH;
    XH = XH+XDH*TS+K(1,1)*RES;
    XDH = XDH+K(2,1)*RES;
    SP11 = sqrt(P(1,1));
    SP22 = sqrt(P(2,2));
    XHERR = X-XH;
    XDHERR = XD-XDH;
    SP11P = -sqrt(P(1,1));
    SP22P = -sqrt(P(2,2));

    count = count+1;
    ArrayT(count) = T;
    ArrayX(count) = X;
    ArrayXH(count) = XH;
    ArrayXD(count) = XD;
    ArrayXDH(count) = XDH;
    ArrayXHERR(count) = XHERR;
    ArraySP11(count) = SP11;
    ArraySP11P(count) = SP11P;
    ArrayXDHERR(count) = XDHERR;
    ArraySP22(count) = SP22;
    ArraySP22P(count) = SP22P;
end

plot(ArrayT,ArrayX,'--')
hold on
plot(ArrayT,ArrayXH)
hold off
grid on;
xlabel('Time(Sec)');
ylabel('Altitude (Ft)');
axis([0 30 0 400000]);

plot(ArrayT,ArrayXD,'--')
hold on
plot(ArrayT,ArrayXDH)
hold off
grid on;
xlabel('Time(Sec)');
ylabel('Velocity (Ft/sec)');
axis([0 30 -10000 0]);

plot(ArrayT,ArrayXHERR)
hold on
plot(ArrayT,ArraySP11,'--')
plot(ArrayT,ArraySP11P,'--')
hold off
grid on;
xlabel('Time(Sec)');
ylabel('Error in Estimate of Altitude (Ft)');
axis([0 30 -1500 1500]);

plot(ArrayT,ArrayXDHERR)
hold on
plot(ArrayT,ArraySP22,'--')
plot(ArrayT,ArraySP22P,'--')
hold off
grid on;
xlabel('Time(Sec)');
ylabel('Error in Estimate of Velocity (Ft/sec)');
axis([0 30 -500 500]);