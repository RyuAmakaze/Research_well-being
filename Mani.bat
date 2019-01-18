rem for openSMILE

cd C:\Program Files\opensmile-2.3.0\bin\Win32
set i=1
:loop

rem class label 0 means the user is puzzled, 1 means normal condition.
SMILExtract_Release -C config/IS10_paraling.conf -I input_%i%.wav -O output_IS10.arff -instname input_%i% -class 0

rem ↓↓IS09 config file ver 
:SMILExtract_Release -C config/IS09_emotion.conf -I input_%i%.wav -O output_IS10.arff -instname input_%i% -class 0

set /a i+=1
if %i% leq 100 goto loop
