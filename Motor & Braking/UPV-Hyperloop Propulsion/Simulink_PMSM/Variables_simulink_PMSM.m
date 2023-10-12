Ts = 1e-6;       %Frecuencia del solver
Tspeed = 2e-4;   %Frecuecia PI velocidad
Tcurr = 1e-4;    %Frecuencia PI corriente


Vbat = 48;       %Tension de baterias

fsw = 1e3;      %Frecuencia de conmutacion de PWM
Tsw = 5e-7;      %Muestreo PWM

Kpvel = 6;      %Proporcional PI velocidad
Kivel = 3;      %Integral PI velocidad

Kpid = 1;        %Proporcional PI id
Kiid = 2;       %Integral PI id

Kpiq = Kpid;     %Proporcional PI id
Kiiq = Kpiq;     %Integral PI id

Refvel = 300;    %Referencia de velocidad    