#------------------------ Tool Specifications & Options ----------------------

COMPILER  =  lcc

CC        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcc64.exe"
LD        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclnk64.exe"
LIBCMD    =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclib64.exe"
CFLAGS    =  -dll -noregistrylookup  -c -Zp8 -DLCC_WIN64 -DMATLAB_MEX_FILE -nodeclspec
LDFLAGS   =  -s -dll -entry LibMain sKf0DvY611GjE8GRWA58UG_cclib.def -L"C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\lib64"

OBJECTS = \
	   PI.obj \
	   man_stub.obj \
	   slcc_interface_sKf0DvY611GjE8GRWA58UG.obj \
	   customcode_sKf0DvY611GjE8GRWA58UG.obj \
	   lccstub.obj \

STATICLIBS = \

#------------------------------ Include/Lib Path ------------------------------

INCLUDE_PATH = \
     -I"c:\program files\matlab\r2022b\extern\include" \
     -I"c:\program files\matlab\r2022b\simulink\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\slprj\_slcc\skf0dvy611gje8grwa58ug" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\c code\prueba_sandbox\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\c code" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\c code\prueba_sandbox\src" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_fdd_v2\c code\prueba_sandbox\manualstub" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\include64" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\mex" \

#--------------------------------- Rules --------------------------------------

sKf0DvY611GjE8GRWA58UG_cclib.dll : $(MAKEFILE) $(OBJECTS)
	$(LD) $(LDFLAGS) /OUT:sKf0DvY611GjE8GRWA58UG_cclib.dll $(OBJECTS)  $(STATICLIBS) "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmex.lib" "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmx.lib"
PI.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~3\CCODE~1\PRUEBA~2\src\PI.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_FDD_v2\C code\Prueba_sandbox\src\PI.c"
man_stub.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~3\CCODE~1\PRUEBA~2\MANUAL~1\man_stub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_FDD_v2\C code\Prueba_sandbox\manualstub\man_stub.c"
slcc_interface_sKf0DvY611GjE8GRWA58UG.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~3\slprj\_slcc\SKF0DV~1\SLCC_I~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_FDD_v2\slprj\_slcc\sKf0DvY611GjE8GRWA58UG\slcc_interface_sKf0DvY611GjE8GRWA58UG.c"
customcode_sKf0DvY611GjE8GRWA58UG.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~3\slprj\_slcc\SKF0DV~1\CUSTOM~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_FDD_v2\slprj\_slcc\sKf0DvY611GjE8GRWA58UG\customcode_sKf0DvY611GjE8GRWA58UG.c"
lccstub.obj :	C:\PROGRA~1\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c"
