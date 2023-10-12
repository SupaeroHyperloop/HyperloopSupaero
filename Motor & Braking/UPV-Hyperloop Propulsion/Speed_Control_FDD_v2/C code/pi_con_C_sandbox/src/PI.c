#include "PI.h"

double error_anterior=0, accion_anterior=0;
const double P=0.3;
const double I=5;
const double periodo=0.0002;


double PI_controller (double error)
{

    double accion=accion_anterior+error*P+error_anterior*(I*periodo-P);
    error_anterior=error;
    accion_anterior=accion;
    return accion;

}