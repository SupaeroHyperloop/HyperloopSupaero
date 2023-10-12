#ifndef __MW_INTERNAL_SLDV_PS_ANALYSIS__
#ifdef __cplusplus
extern "C"
#else
extern
#endif
unsigned int* __mw_instrum_xRnwliZcfd3zpJl8CsgBaG_cclib_phits;

#ifdef __cplusplus
extern "C"
#else
extern
#endif
unsigned int __mw_instrum_xRnwliZcfd3zpJl8CsgBaG_cclib_enabled;

#define __MW_INSTRUM_RECORD_HIT_NO_TEST(id) ((void)((++__mw_instrum_xRnwliZcfd3zpJl8CsgBaG_cclib_phits[id - 1u]) || ((__mw_instrum_xRnwliZcfd3zpJl8CsgBaG_cclib_phits[id - 1u] = (~0u))!=0)))
#define __MW_INSTRUM_RECORD_HIT(id) ((__mw_instrum_xRnwliZcfd3zpJl8CsgBaG_cclib_enabled && __mw_instrum_xRnwliZcfd3zpJl8CsgBaG_cclib_phits) ? __MW_INSTRUM_RECORD_HIT_NO_TEST(id) : (void) 0)


#define __MW_INSTRUM_FCN_ENTER_1() 
#define __MW_INSTRUM_FCN_ENTER_2() 

#define __MW_INSTRUM_NODE_1() (__MW_INSTRUM_RECORD_HIT(1U))
#define __MW_INSTRUM_NODE_2() (__MW_INSTRUM_RECORD_HIT(2U))
#define __MW_INSTRUM_NODE_3() (__MW_INSTRUM_RECORD_HIT(3U))
#define __MW_INSTRUM_NODE_4() (__MW_INSTRUM_RECORD_HIT(4U))
#else /* __MW_INTERNAL_SLDV_PS_ANALYSIS__ */

#define __MW_INSTRUM_FCN_ENTER_1() 

#define __MW_INSTRUM_FCN_ENTER_2() 

#ifdef __cplusplus
extern "C"
#else
extern
#endif
void __MW_INSTRUM_RECORD_HIT_1EZ_xRnwliZcfd3zpJl8CsgBaG(void) { }
#define __MW_INSTRUM_NODE_1() __MW_INSTRUM_RECORD_HIT_1EZ_xRnwliZcfd3zpJl8CsgBaG()

#ifdef __cplusplus
extern "C"
#else
extern
#endif
void __MW_INSTRUM_RECORD_HIT_2XZ_xRnwliZcfd3zpJl8CsgBaG(void) { }
#define __MW_INSTRUM_NODE_2() __MW_INSTRUM_RECORD_HIT_2XZ_xRnwliZcfd3zpJl8CsgBaG()

#ifdef __cplusplus
extern "C"
#else
extern
#endif
void __MW_INSTRUM_RECORD_HIT_3EZ_xRnwliZcfd3zpJl8CsgBaG(void) { }
#define __MW_INSTRUM_NODE_3() __MW_INSTRUM_RECORD_HIT_3EZ_xRnwliZcfd3zpJl8CsgBaG()

#ifdef __cplusplus
extern "C"
#else
extern
#endif
void __MW_INSTRUM_RECORD_HIT_4XZ_xRnwliZcfd3zpJl8CsgBaG(void) { }
#define __MW_INSTRUM_NODE_4() __MW_INSTRUM_RECORD_HIT_4XZ_xRnwliZcfd3zpJl8CsgBaG()


#endif /* __MW_INTERNAL_SLDV_PS_ANALYSIS__ */

#line 1 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_HIL\\C code\\PI.c"
#line 1 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_HIL\\C code\\PI.h"
void model_initialize(void); 
double PI_controller(double error); 
#line 3 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_HIL\\C code\\PI.c"
double error_anterior = (0), accion_anterior = (0); 
const double P = (0.3); 
const double I = (5); 
const double periodo = (0.0002); 

void model_initialize(void) 
{ __MW_INSTRUM_FCN_ENTER_1(); __MW_INSTRUM_NODE_1(); 
error_anterior = (0); 
accion_anterior = (0); __MW_INSTRUM_NODE_2(); 
} 


double PI_controller(double error) 
{ __MW_INSTRUM_FCN_ENTER_2(); __MW_INSTRUM_NODE_3(); { 

double accion = (accion_anterior + error * P) + error_anterior * (I * periodo - P); 
error_anterior = error; 
accion_anterior = accion; 
{ double __mw_tmp_for_return = accion; __MW_INSTRUM_NODE_4(); return __mw_tmp_for_return; } } 

} 
