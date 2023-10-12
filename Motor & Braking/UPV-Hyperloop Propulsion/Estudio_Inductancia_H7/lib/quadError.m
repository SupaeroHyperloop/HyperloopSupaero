function [err] = quadError(u_h, u)
% Computes the quadratic error 
% ═════════════════════════════════════════════════════════════════════════
% Created by:       Ferran de andres (01.2022)
% Last updated by:  Ferran de Andres (01.2022)
% ═════════════════════════════════════════════════════════════════════════
% Versions:        1.0:Function implementation for quadratic error. 
%                  1.1: -
% ═════════════════════════════════════════════════════════════════════════
% INPUT:
% u_h:      Array. Test function.
% u:        Array. Reference.
% ═════════════════════════════════════════════════════════════════════════
% OUTPUT
% err:       Scalar. Quadratic error
% ═════════════════════════════════════════════════════════════════════════

%%% Input checks
narginchk(2,2);

%%% Quadratic error computation

Z_h     = sum(sum(abs(u)));           % Normalization factor 

err_mat = (((u_h - u).^2).^0.5)/Z_h;
err     = sum(sum(err_mat));
