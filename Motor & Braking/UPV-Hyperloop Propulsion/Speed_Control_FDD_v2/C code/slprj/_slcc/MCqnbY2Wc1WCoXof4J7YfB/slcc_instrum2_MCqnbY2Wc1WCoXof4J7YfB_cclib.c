#ifndef __MW_INTERNAL_SLDV_PS_ANALYSIS__
#ifdef __cplusplus
extern "C"
#else
extern
#endif
unsigned int* __mw_instrum_MCqnbY2Wc1WCoXof4J7YfB_cclib_phits;

#ifdef __cplusplus
extern "C"
#else
extern
#endif
unsigned int __mw_instrum_MCqnbY2Wc1WCoXof4J7YfB_cclib_enabled;

#define __MW_INSTRUM_RECORD_HIT_NO_TEST(id) ((void)((++__mw_instrum_MCqnbY2Wc1WCoXof4J7YfB_cclib_phits[id - 1u]) || ((__mw_instrum_MCqnbY2Wc1WCoXof4J7YfB_cclib_phits[id - 1u] = (~0u))!=0)))
#define __MW_INSTRUM_RECORD_HIT(id) ((__mw_instrum_MCqnbY2Wc1WCoXof4J7YfB_cclib_enabled && __mw_instrum_MCqnbY2Wc1WCoXof4J7YfB_cclib_phits) ? __MW_INSTRUM_RECORD_HIT_NO_TEST(id) : (void) 0)

#else /* __MW_INTERNAL_SLDV_PS_ANALYSIS__ */


#endif /* __MW_INTERNAL_SLDV_PS_ANALYSIS__ */

#line 1 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_FDD_v2\\C code\\pi_con_C_sandbox\\manualstub\\man_stub.c"
#line 7 "C:\\Users\\mique\\iCloudDrive\\Hyperloop Upv\\Speed_Control_FDD_v2\\C code\\pi_con_C_sandbox\\manualstub\\man_stub.h"
#ifndef _MANUAL_STUB_HEADER_
#define _MANUAL_STUB_HEADER_
#line 17
#endif /* _MANUAL_STUB_HEADER_ */
int __dummy_to_avoid_empty_file;
