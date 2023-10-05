X=200000;
XD=-6000;
BETA=500;
XNOM=200000;
XDNOM=-6000;
BETANOM=800;
ORDER=3;
TS=0.1;
TF=30;
Q33=300^2/TF;
T=0;
S=0;
H=0.001;
SIGNOISE=25;
XH(1,1)=X-XNOM;
XH(2,1)=XD-XDNOM;
XH(3,1)=-300;
count=0;
PHI=zeros(ORDER,ORDER);
P=zeros(ORDER,ORDER);
Q=zeros(ORDER,ORDER);
IDNP=zeros(ORDER,ORDER);
IDNP(1,1)=1;
IDNP(2,2)=1;
IDNP(3,3)=1;
P(1,1)=SIGNOISE*SIGNOISE;
P(2,2)=20000;
P(3,3)=300^2;
HMAT=[1 0 0];
RMAT(1,1)=SIGNOISE^2;
HT=HMAT';
while X>=0
XOLD=X;
XDOLD=XD;
XNOMOLD=XNOM;
XDNOMOLD=XDNOM;
XDD=0.0034*32.2*XD*XD*exp(-X/22000)/(2*BETA)-32.2;
XDDNOM=0.0034*32.2*XDNOM*XDNOM*exp(-XNOM/22000)/(2*BETANOM)-32.2;
X=X+H*XD;
XD=XD+H*XDD;
XNOM=XNOM+H*XDNOM;
XDNOM=XDNOM+H*XDDNOM;
T=T+H;
XDD=0.0034*32.2*XD*XD*exp(-X/22000)/(2.*BETA)-32.2;
XDDNOM=0.0034*32.2*XDNOM*XDNOM*exp(-XNOM/22000)/(2*BETANOM)-32.2;
X=0.5*(XOLD+X+H*XD);
XD=0.5*(XDOLD+XD+H*XDD);
XNOM=0.5*(XNOMOLD+XNOM+H*XDNOM);
XDNOM=0.5*(XDNOMOLD+XDNOM+H*XDDNOM);
S=S+H;
if S>=TS
    S=0;
    RHONOM=0.0034*exp(-XNOM/22000);
    F21=-32.2*RHONOM*XDNOM*XDNOM/(2*22000*BETANOM);
    F22=RHONOM*32.2*XDNOM/BETANOM;
    F23=-RHONOM*32.2*XDNOM*XDNOM/(2*BETANOM*BETANOM);
    PHI(1,1)=1;
    PHI(1,2)=TS;
    PHI(2,1)=F21*TS;
    PHI(2,2)=1.+F22*TS;
    PHI(2,3)=F23*TS;
    PHI(3,3)=1;
    Q(2,2)=F23*F23*Q33*TS*TS*TS/3;
    Q(2,3)=F23*Q33*TS*TS/2;
    Q(3,2)=Q(2,3);
    Q(3,3)=Q33*TS;
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
    XNOISE=SIGNOISE*randn;
    DELX=X-XNOM;
    MEAS(1,1)=DELX+XNOISE;
    PHIXH=PHI*XH;
    HPHIXH=HMAT*PHIXH;
    RES=MEAS-HPHIXH;
    KRES=K*RES;
    XH=PHIXH+KRES;
    DELXH=XH(1,1);
    DELXDH=XH(2,1);
    DELBETAH=XH(3,1);
    XHH=XNOM+DELXH;
    XDH=XDNOM+DELXDH;
    BETAH=BETANOM+DELBETAH;
    ERRX=X-XHH;  
    SP11=sqrt(P(1,1));  
    ERRXD=XD-XDH;  
    SP22=sqrt(P(2,2));  
    ERRBETA=BETA-BETAH;  
    SP33=sqrt(P(3,3));  
    SP11P=-SP11;  
    SP22P=-SP22;  
    SP33P=-SP33;

    count=count+1;  
    ArrayT(count)=T;
    ArrayBETA(count)=BETA;
    ArrayBETAH(count)=BETAH;
    ArrayERRBETA(count)=ERRBETA;
    ArraySP33(count)=SP33;
    ArraySP33P(count)=SP33P;

end
end
    
plot(ArrayT,ArrayBETAH)
hold on;
plot(ArrayT,ArrayBETA,'--')
hold off;
grid on;
xlabel('Time (Sec)');
ylabel('Ballistic coefficient (Lb/Ft^2)');
axis([0 45 0 800]);

plot(ArrayT,ArrayERRBETA)
hold on;
plot(ArrayT,ArraySP33,'--')
plot(ArrayT,ArraySP33P,'--')
hold off;
grid on;
xlabel('Time (Sec)');
ylabel('Error of β (Lb/Ft^2)');
axis([0 45 -400 400]);

