#------------------------ Tool Specifications & Options ----------------------

COMPILER  =  lcc

CC        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcc64.exe"
LD        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclnk64.exe"
LIBCMD    =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclib64.exe"
CFLAGS    =  -dll -noregistrylookup  -c -Zp8 -DLCC_WIN64 -DMATLAB_MEX_FILE -nodeclspec
LDFLAGS   =  -s -dll -entry LibMain rrqZW4cM9gSckZtd089LjF_cclib.def -L"C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\lib64"

OBJECTS = \
	   PI.obj \
	   man_stub.obj \
	   slcc_interface_rrqZW4cM9gSckZtd089LjF.obj \
	   customcode_rrqZW4cM9gSckZtd089LjF.obj \
	   lccstub.obj \

STATICLIBS = \

#------------------------------ Include/Lib Path ------------------------------

INCLUDE_PATH = \
     -I"c:\program files\matlab\r2022b\extern\include" \
     -I"c:\program files\matlab\r2022b\simulink\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\slprj\_slcc\rrqzw4cm9gsckztd089ljf" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\controladorcorriente_sandbox\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\controladorcorriente_sandbox\src" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\controladorcorriente_sandbox\manualstub" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\include64" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\mex" \

#--------------------------------- Rules --------------------------------------

rrqZW4cM9gSckZtd089LjF_cclib.dll : $(MAKEFILE) $(OBJECTS)
	$(LD) $(LDFLAGS) /OUT:rrqZW4cM9gSckZtd089LjF_cclib.dll $(OBJECTS)  $(STATICLIBS) "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmex.lib" "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmx.lib"
PI.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\CONTRO~1\src\PI.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\ControladorCorriente_sandbox\src\PI.c"
man_stub.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\CONTRO~1\MANUAL~1\man_stub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\ControladorCorriente_sandbox\manualstub\man_stub.c"
slcc_interface_rrqZW4cM9gSckZtd089LjF.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\RRQZW4~1\SLCC_I~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\rrqZW4cM9gSckZtd089LjF\slcc_interface_rrqZW4cM9gSckZtd089LjF.c"
customcode_rrqZW4cM9gSckZtd089LjF.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\RRQZW4~1\CUSTOM~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\rrqZW4cM9gSckZtd089LjF\customcode_rrqZW4cM9gSckZtd089LjF.c"
lccstub.obj :	C:\PROGRA~1\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c"
