
vel=0.1;
V=[];
f=[];
while(vel<13.9)

    [V_aux,f_aux]=v_f(vel);
    V=[V V_aux];
    f=[f f_aux];
    vel=vel+0.1;
end

plot(f,V)
grid
yaxis(-5,240)