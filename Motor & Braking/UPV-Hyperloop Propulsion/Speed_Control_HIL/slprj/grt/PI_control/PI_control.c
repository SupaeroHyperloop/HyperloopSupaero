/*
 * Code generation for system model 'PI_control'
 *
 * Model                      : PI_control
 * Model version              : 1.1
 * Simulink Coder version : 9.8 (R2022b) 13-May-2022
 * C source code generated on : Wed Mar  8 20:26:02 2023
 *
 * Note that the functions contained in this file are part of a Simulink
 * model, and are not self-contained algorithms.
 */

#include "PI_control.h"
#include "rtwtypes.h"
#include "PI_control_private.h"

/* Output and update for referenced model: 'PI_control' */
void PI_control(const real_T *rtu_Inport, real_T *rty_Outport)
{
  /* CCaller: '<Root>/PI_controller' */
  *rty_Outport = PI_controller(*rtu_Inport);
}

/* Model initialize function */
void PI_control_initialize(const char_T **rt_errorStatus, RT_MODEL_PI_control_T *
  const PI_control_M)
{
  /* Registration code */

  /* initialize error status */
  rtmSetErrorStatusPointer(PI_control_M, rt_errorStatus);
}
