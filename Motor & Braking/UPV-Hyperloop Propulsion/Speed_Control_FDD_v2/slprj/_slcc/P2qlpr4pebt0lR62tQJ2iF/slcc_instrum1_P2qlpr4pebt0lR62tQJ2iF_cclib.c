#ifndef __MW_INTERNAL_SLDV_PS_ANALYSIS__
#ifdef __cplusplus
extern "C"
#else
extern
#endif
unsigned int* __mw_instrum_P2qlpr4pebt0lR62tQJ2iF_cclib_phits;

#ifdef __cplusplus
extern "C"
#else
extern
#endif
unsigned int __mw_instrum_P2qlpr4pebt0lR62tQJ2iF_cclib_enabled;

#define __MW_INSTRUM_RECORD_HIT_NO_TEST(id) ((void)((++__mw_instrum_P2qlpr4pebt0lR62tQJ2iF_cclib_phits[id - 1u]) || ((__mw_instrum_P2qlpr4pebt0lR62tQJ2iF_cclib_phits[id - 1u] = (~0u))!=0)))
#define __MW_INSTRUM_RECORD_HIT(id) ((__mw_instrum_P2qlpr4pebt0lR62tQJ2iF_cclib_enabled && __mw_instrum_P2qlpr4pebt0lR62tQJ2iF_cclib_phits) ? __MW_INSTRUM_RECORD_HIT_NO_TEST(id) : (void) 0)


#define __MW_INSTRUM_FCN_ENTER_1() 

#define __MW_INSTRUM_NODE_1() (__MW_INSTRUM_RECORD_HIT(1U))
#define __MW_INSTRUM_NODE_2() (__MW_INSTRUM_RECORD_HIT(2U))
#else /* __MW_INTERNAL_SLDV_PS_ANALYSIS__ */

#define __MW_INSTRUM_FCN_ENTER_1() 

#ifdef __cplusplus
extern "C"
#else
extern
#endif
void __MW_INSTRUM_RECORD_HIT_1EZ_P2qlpr4pebt0lR62tQJ2iF(void) { }
#define __MW_INSTRUM_NODE_1() __MW_INSTRUM_RECORD_HIT_1EZ_P2qlpr4pebt0lR62tQJ2iF()

#ifdef __cplusplus
extern "C"
#else
extern
#endif
void __MW_INSTRUM_RECORD_HIT_2XZ_P2qlpr4pebt0lR62tQJ2iF(void) { }
#define __MW_INSTRUM_NODE_2() __MW_INSTRUM_RECORD_HIT_2XZ_P2qlpr4pebt0lR62tQJ2iF()


#endif /* __MW_INTERNAL_SLDV_PS_ANALYSIS__ */

#line 1 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_FDD_v2\\C code\\pruebas_c_sandbox\\src\\PI.c"
#line 1 "c:\\users\\mique\\iclouddrive\\hyperloop upv\\speed_control_fdd_v2\\c code\\pruebas_c_sandbox\\include\\PI.h"
#ifndef PI_H_
#define PI_H_
#line 5 "c:\\users\\mique\\iclouddrive\\hyperloop upv\\speed_control_fdd_v2\\c code\\pruebas_c_sandbox\\include\\aggregatedHeader.h"
#ifndef AGGREGATEDHEADER_H_
#define AGGREGATEDHEADER_H_

double PI_controller(double error); 

#endif /* AGGREGATEDHEADER_H_ */
#line 4 "c:\\users\\mique\\iclouddrive\\hyperloop upv\\speed_control_fdd_v2\\c code\\pruebas_c_sandbox\\include\\PI.h"
#endif /* PI_H_ */
#line 3 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_FDD_v2\\C code\\pruebas_c_sandbox\\src\\PI.c"
double error_anterior = (0), accion_anterior = (0); 
const double P = (0.3); 
const double I = (5); 
const double periodo = (0.0002); 


double PI_controller(double error) 
{ __MW_INSTRUM_FCN_ENTER_1(); __MW_INSTRUM_NODE_1(); { 

double accion = (accion_anterior + error * P) + error_anterior * (I * periodo - P); 
error_anterior = error; 
accion_anterior = accion; 
{ double __mw_tmp_for_return = accion; __MW_INSTRUM_NODE_2(); return __mw_tmp_for_return; } } 

} 
