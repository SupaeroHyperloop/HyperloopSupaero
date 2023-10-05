X = 200000;
XD = -6000;
BETA = 500;
XH = X;
XDH = XD;
TS = 0.1;
TF = 30;
T = 0;
S = 0;
H = 0.001;
HP = 0.001;
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
        [XB,XDB,XDDB] = project(T,TS,XH,XDH,BETA,HP);
        XH = XB;
        XDH = XDB;
        ERRX = X-XH;
        ERRXD = XD-XDH;
        count = count+1;
        ArrayT(count) = T;
        ArrayERRX(count) = ERRX;
        ArrayERRXD(count) = ERRXD;
    end
end 

% X1 = 200000;
% XD1 = -6000;
% BETA1 = 500;
% XH1 = X1;
% XDH1 = XD1;
% TS1 = 0.1;
% TF1 = 30;
% T1 = 0;
% S1 = 0;
% H1 = 0.001;
% HP1 = 0.01;
% count1 = 0;
% 
% while T1<=TF1
%     XOLD1 = X1;
%     XDOLD1 = XD1;
%     XDD1 = 0.0034*32.2*XD1^2*exp(-X1/22000)/(2*BETA1)-32.2;
%     XD1 = XD1+H1*XDD1;
%     X1 = X1+H1*XD1;
%     T1 = T1+H1;
%     XDD1 = 0.0034*32.2*XD1^2*exp(-X1/22000)/(2*BETA1)-32.2;
%     XD1 = 0.5*(XDOLD1+XD1+H1*XDD1);
%     X1 = 0.5*(XOLD1+X1+H1*XD1);
%     S1 = S1+H1;
%     if S1>=TS1
%         S1 = 0;
%         [XB1,XDB1,XDDB1] = project(T1,TS1,XH1,XDH1,BETA1,HP1);
%         XH1 = XB1;
%         XDH1 = XDB1;
%         ERRX1 = X1-XH1;
%         ERRXD1 = XD1-XDH1;
%         count1 = count1+1;
%         ArrayT1(count1) = T1;
%         ArrayERRX1(count1) = ERRX1;
%         ArrayERRXD1(count1) = ERRXD1;
%     end
% end 
% 
% X2 = 200000;
% XD2 = -6000;
% BETA2 = 500;
% XH2 = X2;
% XDH2 = XD2;
% TS2 = 0.1;
% TF2 = 30;
% T2 = 0;
% S2 = 0;
% H2 = 0.001;
% HP2 = 0.001;
% count2 = 0;
% 
% while T2<=TF2
%     XOLD2 = X2;
%     XDOLD2 = XD2;
%     XDD2 = 0.0034*32.2*XD2^2*exp(-X2/22000)/(2*BETA2)-32.2;
%     XD2 = XD2+H2*XDD2;
%     X2 = X1+H2*XD2;
%     T2 = T2+H2;
%     XDD2 = 0.0034*32.2*XD2^2*exp(-X2/22000)/(2*BETA2)-32.2;
%     XD2 = 0.5*(XDOLD2+XD2+H2*XDD2);
%     X2 = 0.5*(XOLD2+X2+H2*XD2);
%     S2 = S2+H2;
%     if S2>=TS2
%         S2 = 0;
%         [XB2,XDB2,XDDB2] = project(T2,TS2,XH2,XDH2,BETA2,HP2);
%         XH2 = XB2;
%         XDH2 = XDB2;
%         ERRX2 = X2-XH2;
%         ERRXD2 = XD2-XDH2;
%         count2 = count2+1;
%         ArrayT2(count2) = T2;
%         ArrayERRX2(count2) = ERRX2;
%         ArrayERRXD2(count2) = ERRXD2;
%     end
% end 

% plot(ArrayT,ArrayERRX)
% % hold on;
% % plot(ArrayT1,ArrayERRX1,'--')
% % plot(ArrayT2,ArrayERRX2,'--')
% % hold off;
% grid on;
% xlabel('Time (sec)');
% ylabel('Error in Estimate of Altitude (Ft)');
% axis([0 30 -30 30]);
% legend('Euler integration H=0.1 S');

plot(ArrayT,ArrayERRXD)
% hold on;
% plot(ArrayT1,ArrayERRX1,'--')
% plot(ArrayT2,ArrayERRX2,'--')
% hold off;
grid on;
xlabel('Time (sec)');
ylabel('Error in Estimate of Velocity (Ft/sec)');
axis([0 30 -2 12]);
legend('Euler integration H=0.1 S');


function [XH,XDH,XDDH] = project(TP,TS,XP,XDP,BETA,HP)
T = 0;
X = XP;
XD = XDP;
H = HP;
while T<TS
    XDD = 0.0034*32.2*XD^2*exp(-X/22000)/(2*BETA)-32.2;
    XD = XD+H*XDD;
    X = X+H*XD;
    T = T+H;
end
XH = X;
XDH = XD;
XDDH = XDD;
end
