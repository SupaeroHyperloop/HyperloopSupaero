function [Du] = FDM(u,x)
% Computes the discrete derivative of the function u with respect to x
% ═════════════════════════════════════════════════════════════════════════
% Created by:       Ferran de andres (01.2022)
% Last updated by:  Ferran de Andres (01.2022)
% ═════════════════════════════════════════════════════════════════════════
% Versions:        1.0:Function implementation fpr first derivative. 
%                  1.1: -
% ═════════════════════════════════════════════════════════════════════════
% INPUT:
% u:        Vector. Function to be derivated. 
% x:        Vector. Grid points.
% ═════════════════════════════════════════════════════════════════════════
% OUTPUT
% Du:       Vector. Discrete derivative of u w.r.t x
% ═════════════════════════════════════════════════════════════════════════

%%% Input checks
narginchk(2,2);

if (~all(size(u) == size(x)))&&(~all(flip(size(u)) == size(x)))
    error('The size of u and x must be equal')
end

if size(u,1) == 1
    u = u.';
end
if size(x,1) == 1
    x = x.';
end

if size(u,2) ~= 1
    error('The dimensions of the function u are incorrect. It should be a column-wise (or row-wise) defined vector');
elseif size(x,2) ~=1
    error('The dimensions of the function x are incorrect. It should be a column-wise (or row-wise) defined vector');
end

%%% Algorithm initialization
h_i = (x(2:end) - x(1:(end-1)));

h_i_p = h_i(2:end);
h_i_m = h_i(1:(end-1));
H_i   = h_i_p + h_i_m;

u_0 = u(1);
u_N = u(end);

u   = u(2:(end-1));

%%% FDM operator 
alpha_i = - (h_i_p).* (H_i.*h_i_m).^(-1);
beta_i  = (h_i_p.^2 - h_i_m.^2).*(h_i_m.*h_i_p.*H_i).^-1;
gamma_i = (h_i_m).*(H_i.*h_i_p).^(-1);

n = length(u);

D = spdiags([alpha_i beta_i gamma_i],-1:1,n,n);

%%% BC
i = [1, length(u)];
j = [1, 1];
v = [u_0 * alpha_i(1), u_N * gamma_i(end)];

BC = sparse(i,j,v);

%%% Derivative computation 
Du = D*u + BC;
