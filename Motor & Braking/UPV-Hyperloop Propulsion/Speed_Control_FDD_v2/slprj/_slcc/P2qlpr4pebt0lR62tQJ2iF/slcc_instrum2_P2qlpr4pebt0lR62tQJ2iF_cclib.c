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

#else /* __MW_INTERNAL_SLDV_PS_ANALYSIS__ */


#endif /* __MW_INTERNAL_SLDV_PS_ANALYSIS__ */

#line 1 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_FDD_v2\\C code\\pruebas_c_sandbox\\manualstub\\man_stub.c"
#line 7 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_FDD_v2\\C code\\pruebas_c_sandbox\\manualstub\\man_stub.h"
#ifndef _MANUAL_STUB_HEADER_
#define _MANUAL_STUB_HEADER_
#line 5 "c:\\users\\mique\\iclouddrive\\hyperloop upv\\speed_control_fdd_v2\\c code\\pruebas_c_sandbox\\include\\aggregatedHeader.h"
#ifndef AGGREGATEDHEADER_H_
#define AGGREGATEDHEADER_H_

double PI_controller(double error); 

#endif /* AGGREGATEDHEADER_H_ */
#line 21 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_FDD_v2\\C code\\pruebas_c_sandbox\\manualstub\\man_stub.h"
#endif /* _MANUAL_STUB_HEADER_ */
