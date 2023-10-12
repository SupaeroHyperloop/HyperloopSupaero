/*
 * Code generation for system model 'PI_control'
 * For more details, see corresponding source file PI_control.c
 *
 */

#ifndef RTW_HEADER_PI_control_h_
#define RTW_HEADER_PI_control_h_
#ifndef PI_control_COMMON_INCLUDES_
#define PI_control_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "rtw_continuous.h"
#include "rtw_solver.h"
#endif                                 /* PI_control_COMMON_INCLUDES_ */

#include "PI_control_types.h"
#include "interfaceHeader.h"

/* Real-time Model Data Structure */
struct tag_RTM_PI_control_T {
  const char_T **errorStatus;
};

typedef struct {
  RT_MODEL_PI_control_T rtm;
} MdlrefDW_PI_control_T;

/* Model reference registration function */
extern void PI_control_initialize(const char_T **rt_errorStatus,
  RT_MODEL_PI_control_T *const PI_control_M);
extern void PI_control(const real_T *rtu_Inport, real_T *rty_Outport);

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'PI_control'
 */
#endif                                 /* RTW_HEADER_PI_control_h_ */
