TS=1;
ORDER=4;
PHIS=0;
SIGTH=0.01;
SIGR=100;
VT=3000;
VTERR=50;
GAMDEG=45;
GAMDEGERR=0;
VTNOM=VT+VTERR;
GAMDEGNOM=GAMDEG+GAMDEGERR;
G=32.2;
XT=0;
YT=0;
XTD=VT*cos(GAMDEG/57.3);
YTD=VT*sin(GAMDEG/57.3);
XTNOM=XT;
YTNOM=YT;
XTDNOM=VTNOM*cos(GAMDEGNOM/57.3);
YTDNOM=VTNOM*sin(GAMDEGNOM/57.3);
XR=100000;
YR=0;
T=0;
S=0;
H=0.001;
XH(1,1)=XT-XTNOM;
XH(2,1)=XTD-XTDNOM;
XH(3,1)=YT-YTNOM;
XH(4,1)=YTD-YTDNOM;
count=0;
PHI=zeros(ORDER,ORDER);
P=zeros(ORDER,ORDER);
Q=zeros(ORDER,ORDER);
IDNP=zeros(ORDER,ORDER);
IDNP(1,1)=1;
IDNP(2,2)=1;
IDNP(3,3)=1;
IDNP(4,4)=1;
P(1,1)=1000^2;
P(2,2)=100^2;
P(3,3)=1000^2;
P(4,4)=100^2;
RMAT(1,1)=SIGTH^2;
RMAT(1,2)=0;
RMAT(2,1)=0;
RMAT(2,2)=SIGR^2;
PHI(1,1)=1;
PHI(1,2)=TS;
PHI(2,2)=1;
PHI(3,3)=1;
PHI(3,4)=TS;
PHI(4,4)=1;
Q(1,1)=PHIS*TS^3/3;
Q(1,2)=PHIS*TS^2/2;
Q(2,1)=Q(1,2);
Q(2,2)=PHIS*TS;
Q(3,3)=Q(1,1);
Q(3,4)=Q(1,2);
Q(4,3)=Q(3,4);
Q(4,4)=Q(2,2);
while YT>=0
    XTOLD=XT;
    XTDOLD=XTD;
    YTOLD=YT;
    YTDOLD=YTD;
    XTNOMOLD=XTNOM;
    XTDNOMOLD=XTDNOM;
    YTNOMOLD=YTNOM;
    YTDNOMOLD=YTDNOM;
    XTDD=0;
    YTDD=-G;
    XTDDNOM=0;
    YTDDNOM=-G;
    XT=XT+H*XTD;
    XTD=XTD+H*XTDD;
    YT=YT+H*YTD;
    YTD=YTD+H*YTDD;
    XTNOM=XTNOM+H*XTDNOM;
    XTDNOM=XTDNOM+H*XTDDNOM;
    YTNOM=YTNOM+H*YTDNOM;
    YTDNOM=YTDNOM+H*YTDDNOM;
    T=T+H;
    XTDD=0;
    YTDD=-G;
    XTDDNOM=0;
    YTDDNOM=-G;
    XT=0.5*(XTOLD+XT+H*XTD);
    XTD=0.5 *(XTDOLD+XTD+H*XTDD);
    YT=0.5*(YTOLD+YT+H*YTD);
    YTD=0.5*(YTDOLD+YTD+H*YTDD);
    XTNOM=0.5*(XTNOMOLD+XTNOM+H*XTDNOM);
    XTDNOM=0.5*(XTDNOMOLD+XTDNOM+H*XTDDNOM);
    YTNOM=0.5*(YTNOMOLD+YTNOM+H*YTDNOM);
    YTDNOM=0.5*(YTDNOMOLD+YTDNOM+H*YTDDNOM);
    S=S+H;
    if S>=TS
        S=0;
        RTNOM=sqrt((XTNOM-XR)^2+(YTNOM-YR)^2);
        HMAT(1,1)=-(YTNOM-YR)/RTNOM^2;
        HMAT(1,2)=0;
        HMAT(1,3)=(XTNOM-YR)/RTNOM^2;
        HMAT(1,4)=0;
        HMAT(2,1)=(XTNOM-XR)/RTNOM;
        HMAT(2,2)=0;
        HMAT(2,3)=(YTNOM-YT)/RTNOM;
        HMAT(2,4)=0;
        HT = HMAT';
        PHIT=PHI';
        PHIP=PHI*P;
        PHIPPHIT=PHIP*PHIT;
        M=PHIPPHIT+Q;
        HM=HMAT*M;
        HMHT=HM*HT;
        HMHTR=HMHT+RMAT;
        HMHTRINV=inv(HMHTR);
        MHT=M*HT;
        K=MHT*HMHTRINV;
        KH=K*HMAT;
        IKH=IDNP-KH;
        P=IKH*M;
        THETNOISE=SIGTH*randn;
        RTNOISE=SIGR*randn;
        THET=atan2((YT-YR),(XT-XR));
        RT=sqrt((XT-XR)^2+(YT-YR)^2);
        THETNOM=atan2((YTNOM-YR),(XTNOM-XR));
        RTNOM=sqrt((XTNOM-XR)^2+(YTNOM-YR)^2);
        DELTHET=THET-THETNOM;
        DELTR=RT-RTNOM;
        MEAS(1,1)=DELTHET+THETNOISE;
        MEAS(2,1)=DELTR+RTNOISE;
        PHIXH=PHI*XH;
        HPHIXH=HMAT*PHIXH;
        RES=MEAS-HPHIXH;
        KRES=K*RES;
        XH=PHIXH+KRES;
        XTH=XTNOM+XH(1,1);
        XTDH=XTDNOM+XH(2,1);
        YTH=YTNOM+XH(3,1);
        YTDH=YTDNOM+XH(4,1);
        ERRX=XT-XTH;
        SP11=sqrt(P(1,1));
        ERRXD=XTD-XTDH;
        SP22=sqrt(P(2,2));
        ERRY=YT-YTH;
        SP33=sqrt(P(3,3));
        ERRYD=YTD-YTDH;
        SP44=sqrt(P(4,4));
        SP11P=-SP11;
        SP22P=-SP22;
        SP33P=-SP33;
        SP44P=-SP44;
        
        count=count+1;
        ArrayT(count)=T;
        ArrayERRX(count)=ERRX;
        ArrayERRXD(count)=ERRXD;
        ArrayERRY(count)=ERRY;
        ArrayERRYD(count)=ERRYD;
        ArraySP11(count)=SP11;
        ArraySP11P(count)=SP11P;
        ArraySP22(count)=SP22;
        ArraySP22P(count)=SP22P;
        ArraySP33(count)=SP33;
        ArraySP33P(count)=SP33P;
        ArraySP44(count)=SP44;
        ArraySP44P(count)=SP44P;
    end
end

plot(ArrayT,ArrayERRX)
hold on;
plot(ArrayT,ArraySP11,'--')
plot(ArrayT,ArraySP11P,'--')
hold off;
grid on;
xlabel('Time (Sec)');
ylabel('Error in Estimate of x (Ft)');
axis([0 140 -200 200]);

plot(ArrayT,ArrayERRXD)
hold on;
plot(ArrayT,ArraySP22,'--')
plot(ArrayT,ArraySP22P,'--')
hold off;
grid on;
xlabel('Time (Sec)');
ylabel('Error in Estimate of x dot (Ft/Sec)');
axis([0 140 -20 20]);

plot(ArrayT,ArrayERRY)
hold on;
plot(ArrayT,ArraySP33,'--')
plot(ArrayT,ArraySP33P,'--')
hold off;
grid on;
xlabel('Time (Sec)');
ylabel('Error in Estimate of y (Ft)');
axis([0 140 -700 700]);

plot(ArrayT,ArrayERRYD)
hold on;
plot(ArrayT,ArraySP44,'--')
plot(ArrayT,ArraySP44P,'--')
hold off;
grid on;
xlabel('Time (Sec)');
ylabel('Error in Estimate of y dot (Ft/Sec)');
axis([0 140 -20 20]);
