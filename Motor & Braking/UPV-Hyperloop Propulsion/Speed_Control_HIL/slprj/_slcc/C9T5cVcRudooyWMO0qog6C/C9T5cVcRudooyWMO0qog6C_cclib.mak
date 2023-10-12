#------------------------ Tool Specifications & Options ----------------------

COMPILER  =  lcc

CC        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcc64.exe"
LD        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclnk64.exe"
LIBCMD    =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclib64.exe"
CFLAGS    =  -dll -noregistrylookup  -c -Zp8 -DLCC_WIN64 -DMATLAB_MEX_FILE -nodeclspec
LDFLAGS   =  -s -dll -entry LibMain C9T5cVcRudooyWMO0qog6C_cclib.def -L"C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\lib64"

OBJECTS = \
	   PI.obj \
	   man_stub.obj \
	   slcc_interface_C9T5cVcRudooyWMO0qog6C.obj \
	   customcode_C9T5cVcRudooyWMO0qog6C.obj \
	   lccstub.obj \

STATICLIBS = \

#------------------------------ Include/Lib Path ------------------------------

INCLUDE_PATH = \
     -I"c:\program files\matlab\r2022b\extern\include" \
     -I"c:\program files\matlab\r2022b\simulink\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\slprj\_slcc\c9t5cvcrudooywmo0qog6c" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\c code\prueba_controlador_sandbox\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\c code" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\c code\prueba_controlador_sandbox\src" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\c code\prueba_controlador_sandbox\manualstub" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\include64" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\mex" \

#--------------------------------- Rules --------------------------------------

C9T5cVcRudooyWMO0qog6C_cclib.dll : $(MAKEFILE) $(OBJECTS)
	$(LD) $(LDFLAGS) /OUT:C9T5cVcRudooyWMO0qog6C_cclib.dll $(OBJECTS)  $(STATICLIBS) "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmex.lib" "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmx.lib"
PI.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\CCODE~1\PRUEBA~1\src\PI.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\C code\Prueba_controlador_sandbox\src\PI.c"
man_stub.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\CCODE~1\PRUEBA~1\MANUAL~1\man_stub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\C code\Prueba_controlador_sandbox\manualstub\man_stub.c"
slcc_interface_C9T5cVcRudooyWMO0qog6C.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\C9T5CV~1\SLCC_I~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\C9T5cVcRudooyWMO0qog6C\slcc_interface_C9T5cVcRudooyWMO0qog6C.c"
customcode_C9T5cVcRudooyWMO0qog6C.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\C9T5CV~1\CUSTOM~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\C9T5cVcRudooyWMO0qog6C\customcode_C9T5cVcRudooyWMO0qog6C.c"
lccstub.obj :	C:\PROGRA~1\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c"
