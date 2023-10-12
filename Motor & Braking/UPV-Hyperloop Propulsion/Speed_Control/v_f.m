function [V,f]= v_f(vel)

pasoPolar=0.114;

f=vel/(2*pasoPolar);

%Calcular perfil de V
f_corte_inf=6;
V_min=92;

V_max=220;

f_corte_sup=f_corte_inf*V_max/V_min;

if(f<f_corte_inf)
    V=V_min;
elseif(f<f_corte_sup)
    V=V_min/f_corte_inf*f;
else
    V=V_max;
end







