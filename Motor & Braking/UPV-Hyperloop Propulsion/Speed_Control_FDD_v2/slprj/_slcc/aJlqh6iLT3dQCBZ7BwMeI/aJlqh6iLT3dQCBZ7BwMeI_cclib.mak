#------------------------ Tool Specifications & Options ----------------------

COMPILER  =  lcc

CC        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcc64.exe"
LD        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclnk64.exe"
LIBCMD    =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclib64.exe"
CFLAGS    =  -dll -noregistrylookup  -c -Zp8 -DLCC_WIN64 -DMATLAB_MEX_FILE -nodeclspec
LDFLAGS   =  -s -dll -entry LibMain aJlqh6iLT3dQCBZ7BwMeI_cclib.def -L"C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\lib64"

OBJECTS = \
	   PI.obj \
	   man_stub.obj \
	   slcc_interface_aJlqh6iLT3dQCBZ7BwMeI.obj \
	   customcode_aJlqh6iLT3dQCBZ7BwMeI.obj \
	   lccstub.obj \

STATICLIBS = \

#------------------------------ Include/Lib Path ------------------------------

INCLUDE_PATH = \
     -I"c:\program files\matlab\r2022b\extern\include" \
     -I"c:\program files\matlab\r2022b\simulink\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\slprj\_slcc\ajlqh6ilt3dqcbz7bwmei" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\c code\pruebas_c_sandbox\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\c code" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\c code\pruebas_c_sandbox\src" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\c code\pruebas_c_sandbox\manualstub" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\include64" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\mex" \

#--------------------------------- Rules --------------------------------------

aJlqh6iLT3dQCBZ7BwMeI_cclib.dll : $(MAKEFILE) $(OBJECTS)
	$(LD) $(LDFLAGS) /OUT:aJlqh6iLT3dQCBZ7BwMeI_cclib.dll $(OBJECTS)  $(STATICLIBS) "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmex.lib" "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmx.lib"
PI.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~3\CCODE~1\PRUEBA~1\src\PI.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_FDD_v2\C code\pruebas_c_sandbox\src\PI.c"
man_stub.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~3\CCODE~1\PRUEBA~1\MANUAL~1\man_stub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_FDD_v2\C code\pruebas_c_sandbox\manualstub\man_stub.c"
slcc_interface_aJlqh6iLT3dQCBZ7BwMeI.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~3\slprj\_slcc\AJLQH6~1\SLCC_I~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_FDD_v2\slprj\_slcc\aJlqh6iLT3dQCBZ7BwMeI\slcc_interface_aJlqh6iLT3dQCBZ7BwMeI.c"
customcode_aJlqh6iLT3dQCBZ7BwMeI.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~3\slprj\_slcc\AJLQH6~1\CUSTOM~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_FDD_v2\slprj\_slcc\aJlqh6iLT3dQCBZ7BwMeI\customcode_aJlqh6iLT3dQCBZ7BwMeI.c"
lccstub.obj :	C:\PROGRA~1\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c"
