X=0;
Y=0;
XR1=1000000;
YR1=20000*3280;
XR2=500000;
YR2=20000*3280;
TS=1;
TF=100;
T=0;
S=0;
H=0.01;
count=0;
while(T<=TF)
    XR1OLD=XR1;
    XR2OLD=XR2;
    XR1D=-14600;
    XR2D=-14600;
    XR1=XR1+H*XR1D;
    XR2=XR2+H*XR2D;
    T=T+H;
    XR1D=-14600;
    XR2D=-14600;
    XR1=0.5*(XR1OLD+XR1+H*XR1D);
    XR2=0.5*(XR2OLD+XR2+H*XR2D);
    S=S+H;
    if(S>=(TS-.00001))
        S=0;
        R1=sqrt((XR1-X)^2+(YR1-Y)^2);
        R2=sqrt((XR2-X)^2+(YR2-Y)^2);
        A1=(YR1-YR2)/(XR2-XR1);
        B1=(R1^2-R2^2-XR1^2-YR1^2+XR2^2+YR2^2)/(2*(XR2-XR1));
        A=1+A1^2;
        B=2*A1*B1-2*A1*XR1-2*YR1;
        C=XR1^2-2*XR1*B1+YR1^2-R1^2;
        YH=(-B-sqrt(B^2-4*A*C))/(2*A);
        XH=A1*YH+B1;
        THET=acos(((XR1-X)*(XR2-X)+(YR1-Y)*(YR2-Y))/(R1*R2));
        count=count+1;
        ArrayT(count)=T;
        ArrayX(count)=X;
        ArrayXH(count)=XH;
        ArrayY(count)=Y;
        ArrayYH(count)=YH;
    end
end
plot(ArrayT,ArrayX,'--')
hold on;
plot(ArrayT,ArrayXH)
hold off;
grid on;
xlabel('Time (Sec)');
ylabel('Downrange Receiver Location (Ft)');
axis([0 100 -150000 150000]);
legend('Actual','Estimate');