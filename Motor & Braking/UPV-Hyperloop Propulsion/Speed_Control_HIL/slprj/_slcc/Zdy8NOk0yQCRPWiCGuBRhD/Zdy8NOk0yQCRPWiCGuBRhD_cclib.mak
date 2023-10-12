#------------------------ Tool Specifications & Options ----------------------

COMPILER  =  lcc

CC        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcc64.exe"
LD        =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclnk64.exe"
LIBCMD    =  "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\bin\lcclib64.exe"
CFLAGS    =  -dll -noregistrylookup  -c -Zp8 -DLCC_WIN64 -DMATLAB_MEX_FILE -nodeclspec
LDFLAGS   =  -s -dll -entry LibMain Zdy8NOk0yQCRPWiCGuBRhD_cclib.def -L"C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\lib64"

OBJECTS = \
	   PI.obj \
	   slcc_interface_Zdy8NOk0yQCRPWiCGuBRhD.obj \
	   customcode_Zdy8NOk0yQCRPWiCGuBRhD.obj \
	   lccstub.obj \

STATICLIBS = \

#------------------------------ Include/Lib Path ------------------------------

INCLUDE_PATH = \
     -I"c:\program files\matlab\r2022b\extern\include" \
     -I"c:\program files\matlab\r2022b\simulink\include" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\slprj\_slcc\zdy8nok0yqcrpwicgubrhd" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil\c code" \
     -I"c:\users\mique\iclouddrive\hyperloop upv\speed_control_hil" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\include64" \
     -I"c:\program files\matlab\r2022b\sys\lcc64\lcc64\mex" \

#--------------------------------- Rules --------------------------------------

Zdy8NOk0yQCRPWiCGuBRhD_cclib.dll : $(MAKEFILE) $(OBJECTS)
	$(LD) $(LDFLAGS) /OUT:Zdy8NOk0yQCRPWiCGuBRhD_cclib.dll $(OBJECTS)  $(STATICLIBS) "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmex.lib" "C:\Program Files\MATLAB\R2022b\extern\lib\win64\microsoft\libmx.lib"
PI.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\CCODE~1\PI.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\C code\PI.c"
slcc_interface_Zdy8NOk0yQCRPWiCGuBRhD.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\ZDY8NO~1\SLCC_I~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\Zdy8NOk0yQCRPWiCGuBRhD\slcc_interface_Zdy8NOk0yQCRPWiCGuBRhD.c"
customcode_Zdy8NOk0yQCRPWiCGuBRhD.obj :	C:\Users\mique\ICLOUD~1\HYPERL~1\SPEED_~4\slprj\_slcc\ZDY8NO~1\CUSTOM~1.C
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Users\mique\iCloudDrive\Hyperloop Upv\Speed_Control_HIL\slprj\_slcc\Zdy8NOk0yQCRPWiCGuBRhD\customcode_Zdy8NOk0yQCRPWiCGuBRhD.c"
lccstub.obj :	C:\PROGRA~1\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "C:\Program Files\MATLAB\R2022b\sys\lcc64\lcc64\mex\lccstub.c"
