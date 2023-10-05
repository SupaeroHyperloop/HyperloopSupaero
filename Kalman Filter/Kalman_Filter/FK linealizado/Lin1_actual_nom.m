n=1;
while n<=4
X=200000.;
XD=-6000.;
BETA=500.;
XNOM=200000.;
XDNOM=-6000.;
if n==1
BETANOM=500.;
elseif n==2
   BETANOM=600.;
elseif n==3
    BETANOM=800.;
else
    BETANOM =1100,
end
TS=0.1;
T=0.;
S=0.;
H=0.001;
count = 0;
while(X>=0.);
XOLD=X;
XDOLD=XD;
XNOMOLD=XNOM;
XDNOMOLD=XDNOM;
XDD=.0034*32.2*XD*XD*exp(-X/22000.)/(2.*BETA)-32.2;
XDDNOM=.0034*32.2*XDNOM*XDNOM*exp(-XNOM/22000.)/(2.*BETANOM)-32.2;
X=X+H*XD;
XD=XD+H*XDD;
XNOM=XNOM+H*XDNOM;
XDNOM=XDNOM+H*XDDNOM;
T=T+H;
XDD=0.0034*32.2*XD*XD*exp(-X/22000.)/(2.*BETA)-32.2;
XDDNOM=0.0034*32.2*XDNOM*XDNOM*exp(-XNOM/22000.)/(2.*BETANOM)-32.2;
X=0.5*(XOLD+X+H*XD);
XD=0.5*(XDOLD+XD+H*XDD);
XNOM=0.5*(XNOMOLD+XNOM+H*XDNOM);
XDNOM=0.5*(XDNOMOLD+XDNOM+H*XDDNOM);
S=S+H;
if(S>=(TS-.00001))
S=0.;
DELXH=X-XNOM;
DELXDH=XD-XDNOM;
DELBETAH=BETA-BETANOM;
XH=XNOM+DELXH;
XDH=XDNOM+DELXDH;
BETAH=BETANOM+DELBETAH;
count = count+1;
ArrayT(count) = T;
ArrayERRX(count) = DELXH;
ArrayERRXD(count) = DELXDH;
end
end

% plot(ArrayT,ArrayERRX,'--')
% hold on;
% grid on;
% xlabel('Time (Sec)');
% ylabel('Error in Altitude (Ft)');
% axis([0 45 -100 14000]);

plot(ArrayT,ArrayERRXD,'--')
hold on;
grid on;
xlabel('Time (Sec)');
ylabel('Error in Velocity (Ft/Sec)');
axis([0 45 -100 1000]);


n = n+1;
end