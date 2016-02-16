
REM download python27
REM powershell Invoke-WebRequest https://www.python.org/ftp/python/2.7.11/python-2.7.11.amd64.msi -OutFile %TEMP%\python-2.7.11.amd64.msi
powershell -nop -c "iex(New-Object Net.WebClient).DownloadString('https://www.python.org/ftp/python/2.7.11/python-2.7.11.amd64.msi')"

REM install python27
REM /a for admininistrative install
msiexec /a /i python-2.7.11.amd64.msi TARGETDIR=%TEMP%\python27\ /quiet

REM remove install file
setx path "%path%;%TEMP%\python27\

REM add to path

 






