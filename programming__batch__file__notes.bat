@ECHO OFF
EXIT




REM	command reference A-Z: https://technet.microsoft.com/en-us/library/bb490890.aspx
rem get help on a command: ex. command /?


rem general syntax ---------------------------
rem print statement
ECHO.	print blank line
ECHO	print


rem commenting
rem comment


rem escape characters
%%
^

rem ignoring whitespace
rem use quotes around entire command,
"C:\Program Files (x86)\WinRar\Rar.exe"
rem  or quotes around areas with whitespace
C:\"Program Files (x86)"\WinRar\Rar.exe
rem alternatively, use command:
dir /X ~1 c:\
rem to print a list of alternative dir names.  eg:
DEFAUL~1.XML Default Desktop Policy.xml
PROGRA~1     Program Files 
PROGRA~2     Program Files (x86)



GOTO	rem go to :exit (spaces allowed but not other separators (semicolons,equal signs). Uses only the first eight characters)

:exit
CLS	#clears the screen

BREAK=ON	rem stop if the user presses < Ctrl >-< Break >
BREAK=OFF	rem continue until done


rem time -------------------------------------

PAUSE				rem stop execution of the batch file until someone presses a key, then continue.

SLEEP				rem ex. SLEEP 10 (In seconds)

TIMEOUT			rem ex. TIMEOUT 10 or TIMEOUT /t 10 (in seconds). If the user does press a key at any point, execution will resume immediately.




rem operands ---------------------------------

*multiply		rem ex. set /a sum1="num1 * num2"





rem strings ----------------------------------

rem concatenate:
set combinedString= str1 str2 str3




rem strip chars (in this case '!')
set string=%string:!=%

rem strip multiple chars (from 1.2.3.4 to 1,2,3,4) 
setlocal 
set string=1.2.3.4 
set string=%string:.=,%





rem variables --------------------------------

rem **the space before and after = is interpreted as part of the value.
rem variable=value   not varible = value unless a whitespace before the value is intended

rem assign variable:
set "variable=.proj"

rem assign empty variable:
set variable=

rem prompt user assigned
set /p variable= Printed text prompt string

rem expression result as variable
set /a variable=expression 

rem call variable:
%variable%



rem Windows environment variables:

%userprofile%	=C:\Users\<username>
%systemroot%	=C:WINDOWS
%temp% or %tmp%	=%USERPROFILE%\AppData\Local\Temp
%username%	=<username>
%homedrive%	=C:
%homepath%	=\Users\<username>
%systemdrive%	=C:
%public%	=C:Users\Public
%appdata%	=C:Users\<username>\AppData\Roaming
%localappdata%	=C:Users\<username>\AppData\Local
%programdata%	=C:ProgramData
%programfiles%	=C:Program Files
%programfiles(x86)%
%computername%




rem conditionals -----------------------------

rem if statement:
if %choice%==[%1]==[] goto start
if /i %choice%==one goto one
if /i %choice%==two goto two
if /i %choice%==end goto end





rem external files ---------------------------

rem check if file exists
if exist file.txt


rem create and write single line to file:
echo import maya.standalone > file.txt


rem write multiple lines to a file:
set "tmp=file.txt"

(
echo import maya.standalone
echo.
echo maya.standalone.initialize(name='python'^)
echo.
echo import %module%
echo maya.standalone.uninitialize(^)
)> %tmp%



rem rename a file



rem zip a file
compact /c /s:C:\Templates

rem using java:
rem c = Creates a new archive file.
rem M = Specifies that a manifest file should not be added to the archive.
rem f = Indicates target file name.
jar -cMf targetArchive.zip sourceDirectory

rem using powershell:
rem compress
Compress-Archive -Path C:\Test -DestinationPath C:\result
rem expand
Expand-Archive -Path result.zip -DestinationPath C:\Test
rem from batch file
powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::ExtractToDirectory('foo.zip', 'bar'); }"

rem convert to cab:
makecab <source> <dest>.cab
rem to decompress
expand <source>.cab <dest>
rem example: Create a self extracting archive containing movie.mov:
C:\> makecab movie.mov "temp.cab"
C:\> copy /b "%windir%\system32\extrac32.exe"+"temp.cab" "movie.exe"
C:\> del /q /f "temp.cab"

rem using 7zip:
"C:\Program Files\7-Zip\7z.exe" a  -r myzip.zip -w foo -mem=AES256
rem unzip to current directory ./
"C:\Program Files\7-Zip\7z.exe" x  myzip.zip  -o./ -y -r

rem using WinRar:
rem 'a' command. Adds to the archive
rem '-r'  switch. recursively archive/compress all files and subdirectories
rem '-ep' switch. Adds files to the archive without including the path information. Multiple can exist in the archive with the same name.
rem '-u' switch. Equivalent to the “u” command when combined with the “a” command. Adds new files and updates older versions of the files already in the archive'
rem '-df' switch. Deletes files after they are moved to the archive
rem '-x' switch. Excludes the specified files from the operation
rem '-idq' enable quiet mode to display only error messages
rem '-ep1' exclude base directory from specified file/folder names
rem '-y' assume Yes on all queries
"%ProgramFiles%\WinRAR\Rar.exe" a -r -y -df "%dir%\%file%.rar" "%dir%\%file%"
rem extract to current dir
rem 'x' command. Extracts with full paths
rem 'e' command. Extracts and ignores paths
if exist "%dir%\%file%.rar" "%ProgramFiles%\WinRAR\Rar.exe" x -y "%dir%\%file%.rar"
rem or to perform an operation on only certain files: 
rem extracts *.gif files from yourfile.rar to c:\extractfolder\ -trailing backslash required:
"%ProgramFiles%\WinRAR\Rar.exe" x c:\yourfile.rar *.gif c:\extractfolder\





rem reg keys ---------------------------------

rem delete key
reg delete "HKCU\Some\Registry\Path" /f
rem alt:
[-HKEY_LOCAL_MACHINE\SOFTWARE\YourSoft\MyKey]
rem to remove an entry, place a minus "-" after the = char
[HKEY_LOCAL_MACHINE\SOFTWARE\YourSoft\MyKey]
"MyEntry"=-




EXIT