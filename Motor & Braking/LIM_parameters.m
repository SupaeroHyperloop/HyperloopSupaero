clear all
%s subscript means stator / primary
%r subscript means rotor / secondary / linor
%Parameters from MPC paper referred as number 11
Rs = 1.298 ; %Primary resistance
Rr = 0.976 ; %Secondary resistance
R_s=Rs ;
R_R=Rr ;
Ls=0.0684 ; %Primary inductance
Lr=0.0416 ; %Secondary inudctance
Lm =0.0416 ; %magnetization inductance ; %magnetization inductance
L_M=Lm;
L_ls = Ls -Lm; %s t a t o r / primary leakage inductance
L_lr = Lr -Lm; %rotor / secondary leakage inductance
Ll=L_ls+L_lr ;
L_alpha=(Ls+Lm)*(Lr+Lm) -Lm^2;
%pole pitch in meters %w=pi / tau ∗v or w=pi /(2∗ tau )∗ v
p = 4 ; %pole p a i r s
%D = 0 . 1 ; %Viscous damping
m = 10; %Mass of motor
L=1; %length of LIM
L_sigma=L_ls+L_lr ; %Sum of leakage inudctance
R_R_hat=Rr ;
tau=L/p; %obtained from paper


%all the hat terms are estimated value , currently taken as actual value
R_hat=Rs+Rr ;
L_M_hat=Lm; %Magnetizing inductance
L_sigma_hat=L_sigma ;
psi_ref =1*250/(100*pi ) ; %steady state value
%psi_ref =1∗450∗ sqr t (2/3)/100/ pi ;
id_ref=psi_ref /L_M_hat; %id controls the flux
iq_ref=0.5 ;

%Only when we do not use speed controller and iq control the torque
m_hat=m;

%Current c o n t r o l l e r
tr=1e-3 ;
alpha_c=(log(9)/tr) ;
Ra= alpha_c*L_sigma_hat - R_hat ; %active resistance used for minimising steady state error
kp_c=alpha_c*L_sigma_hat ; %chapter 4
ki_c=alpha_c*(R_hat+Ra ) ;
%ki_c=alpha_c ∗R_hat;
%V_sat=415*sqrt(2/3);
V_sat = 1000;

%Speed C o n t r o l l e r
alpha_s=1/120*alpha_c ;
K=2/3;
%ba=(alpha_s*J_hat - b_hat)/psi_ref;
kp_s=alpha_s*m_hat/ psi_ref ;
ki_s=alpha_s^2*m_hat/ psi_ref ;
iq_max=sqrt(100^2 - id_ref ^2); %This value has to be f i g u r e d out according to motor curren%Field weakening chapter 9
I_nom=psi_ref/L_M_hat;
I_min=0.1*I_nom ;
Vbase=250;
zeta=(L_sigma_hat+L_M_hat)/L_sigma_hat ;
iq_ref_nom=1;
I_max=3*I_nom ; %Value of I_max
wbase_fw=50*2*pi ;

