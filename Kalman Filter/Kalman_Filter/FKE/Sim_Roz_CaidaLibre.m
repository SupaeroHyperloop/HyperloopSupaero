G1 = 32.2;
X1 = 200000;
XD1 = -6000;
BETA1 = 500;
TS1 = 0.1;
TF1 = 30;
T1 = 0;
S1 = 0;
H1 = 0.001;
count1 = 0;
while T1<=TF1
    XOLD1 = X1;
    XDOLD1 = XD1;
    XDD1 = (0.0034*G1*XD1^2*exp(-X1/22000))/(2*BETA1)-G1;
    X1 = X1+H1*XD1;
    T1 = T1+H1;
    XDD1 = (0.0034*G1*XD1^2*exp(-X1/22000))/(2*BETA1)-G1;
    X1 = 0.5*(XOLD1+X1+H1*XD1);
    XD1 = 0.5*(XDOLD1+XD1+H1*XDD1);
    S1 = S1+H1;
    if S1>=TS1
        S1 = 0;
        count1 = count1+1;
        ArrayT1(count1) = T1;
        ArrayX1(count1) = X1;
        ArrayXD1(count1) = XD1;
        ArrayXDD1(count1) = XDD1;
    end
end

G2 = 32.2;
X2 = 200000;
XD2 = -6000;
BETA2 = 1000;
TS2 = 0.1;
TF2 = 30;
T2 = 0;
S2 = 0;
H2 = 0.001;
count2 = 0;
while T2<=TF2
    XOLD2 = X2;
    XDOLD2 = XD2;
    XDD2 = (0.0034*G2*XD2^2*exp(-X2/22000))/(2*BETA2)-G2;
    X2 = X2+H2*XD2;
    T2 = T2+H2;
    XDD2 = (0.0034*G2*XD2^2*exp(-X2/22000))/(2*BETA2)-G2;
    X2 = 0.5*(XOLD2+X2+H2*XD2);
    XD2 = 0.5*(XDOLD2+XD2+H2*XDD2);
    S2 = S2+H2;
    if S2>=TS2
        S2 = 0;
        count2 = count2+1;
        ArrayT2(count2) = T2;
        ArrayX2(count2) = X2;
        ArrayXD2(count2) = XD2;
        ArrayXDD2(count2) = XDD2;
    end
end

G3 = 32.2;
X3 = 200000;
XD3 = -6000;
BETA3 = 2000;
TS3 = 0.1;
TF3 = 30;
T3 = 0;
S3 = 0;
H3 = 0.001;
count3 = 0;
while T3<=TF3
    XOLD3 = X3;
    XDOLD3 = XD3;
    XDD3 = (0.0034*G3*XD3^2*exp(-X3/22000))/(2*BETA3)-G3;
    X3 = X3+H3*XD3;
    T3 = T3+H3;
    XDD3 = (0.0034*G3*XD3^2*exp(-X3/22000))/(2*BETA3)-G3;
    X3 = 0.5*(XOLD3+X3+H3*XD3);
    XD3 = 0.5*(XDOLD3+XD3+H3*XDD3);
    S3 = S3+H3;
    if S3>=TS3
        S3 = 0;
        count3 = count3+1;
        ArrayT3(count3) = T3;
        ArrayX3(count3) = X3;
        ArrayXD3(count3) = XD3;
        ArrayXDD3(count3) = XDD3;
    end
end

G4 = 32.2;
X4 = 200000;
XD4 = -6000;
BETA4 = 99999999999999999999999;
TS4 = 0.1;
TF4 = 30;
T4 = 0;
S4 = 0;
H4 = 0.001;
count4 = 0;
while T4<=TF4
    XOLD4 = X4;
    XDOLD4 = XD4;
    XDD4 = (0.0034*G4*XD4^2*exp(-X4/22000))/(2*BETA4)-G4;
    X4 = X4+H4*XD4;
    T4 = T4+H4;
    XDD4 = (0.0034*G4*XD4^2*exp(-X4/22000))/(2*BETA4)-G4;
    X4 = 0.5*(XOLD4+X4+H4*XD4);
    XD4 = 0.5*(XDOLD4+XD4+H4*XDD4);
    S4 = S4+H4;
    if S4>=TS4
        S4 = 0;
        count4 = count4+1;
        ArrayT4(count4) = T4;
        ArrayX4(count4) = X4;
        ArrayXD4(count4) = XD4;
        ArrayXDD4(count4) = XDD4;
    end
end

% plot(ArrayT1,ArrayX1)
% hold on
% plot(ArrayT2,ArrayX2,'--')
% plot(ArrayT3,ArrayX3,'--')
% plot(ArrayT4,ArrayX4,'--')
% hold off
% grid on;
% xlabel('Time(Sec)');
% ylabel('Altitude (Ft)');
% axis([0 30 0 200000]);
% legend('BETA=500','BETA=1000','BETA=2000','BETA=Inf')

% plot(ArrayT1,ArrayXD1)
% hold on
% plot(ArrayT2,ArrayXD2,'--')
% plot(ArrayT3,ArrayXD3,'--')
% plot(ArrayT4,ArrayXD4,'--')
% hold off
% grid on;
% xlabel('Time(Sec)');
% ylabel('Velocity (Ft)');
% axis([0 30 -7000 -3000]);
% legend('BETA=500','BETA=1000','BETA=2000','BETA=Inf')

plot(ArrayT1,ArrayXDD1)
hold on
plot(ArrayT2,ArrayXDD2,'--')
plot(ArrayT3,ArrayXDD3,'--')
plot(ArrayT4,ArrayXDD4,'--')
hold off
grid on;
xlabel('Time(Sec)');
ylabel('Acceleration (Ft)');
axis([0 30 -100 400]);
legend('BETA=500','BETA=1000','BETA=2000','BETA=Inf')