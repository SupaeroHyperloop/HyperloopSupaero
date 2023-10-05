n=1;
while n<=4
TS=1;
VT=3000;
if n==1
    VTERR=0;
elseif n==2
    VTERR=50;
elseif n==3
    VTERR=100;
else
    VTERR=200;
end
GAMDEG=45;
GAMDEGERR=0;
VTNOM=VT+VTERR;
GAMDEGNOM=GAMDEG+GAMDEGERR;
G=32.2;
XT=0;
YT=0;
XTD = VT*cosd(GAMDEG);
YTD = VT*sind(GAMDEG);
XTNOM=XT;
YTNOM=YT;
XTDNOM = VTNOM*cosd(GAMDEGNOM);
YTDNOM = VTNOM*sind(GAMDEGNOM);
XR=100000;
YR=0;
T=0;
S=0;
H=0.001;
count=0;
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
    XT=0.5 *(XTOLD+XT+H*XTD);
    XTD=0.5*(XTDOLD+XTD+H*XTDD);
    YT=0.5 *(YTOLD+YT+H* YTD);
    YTD=0.5*(YTDOLD+YTD+H*YTDD);
    XTNOM=0.5*(XTNOMOLD+XTNOM+H*XTDNOM);
    XTDNOM=0.5*(XTDNOMOLD+XTDNOM+H*XTDDNOM);
    YTNOM=0.5*(YTNOMOLD+YTNOM+H*YTDNOM);
    YTDNOM=0.5*(YTDNOMOLD+YTDNOM+H*YTDDNOM);
    S=S+H;
    if S>=TS
        S=0.;
        RTNOM=sqrt((XTNOM-XR)^2+(YTNOM-YR)^2);
        THET=atan2((YT-YR),(XT-XR));
        RT=sqrt((XT-XR)^2+(YT-YR)^2);
        THETNOM=atan2((YTNOM-YR),(XTNOM-XR));
        DELTHET=57.3*(THET-THETNOM);
        DELRT=RT-RTNOM;
        DELXT=XT-XTNOM;
        DELXTD=XTD-XTDNOM;
        DELYT=YT-YTNOM;
        DELYTD=YTD-YTDNOM;
        count=count+1;
        ArrayT(count)=T;
        ArrayDELXT(count)=DELXT;
        ArrayDELTHET(count)=DELTHET;
        ArrayDELRT(count)=DELRT;
    end
end

plot(ArrayT,ArrayDELXT,'--')
hold on;
grid on;
xlabel('Time (Sec)');
ylabel('Error in x (Ft)');
axis([0 140 -20000 5000]);

plot(ArrayT,ArrayDELTHET,'--')
hold on;
grid on;
xlabel('Time (Sec)');
ylabel('Error in θ (Ft)');
axis([0 140 -7 7]);

plot(ArrayT,ArrayDELRT,'--')
hold on;
grid on;
xlabel('Time (Sec)');
ylabel('Error in R_T (Ft)');
axis([0 140 -20000 5000]);

n=n+1;
end