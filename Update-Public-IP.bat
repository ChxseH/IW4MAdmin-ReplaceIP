:: Make this file a task schedule for 1 am or something.

@echo off
:: Grab my Public IP. Throw it in Documents\IP.txt.
C:\curl-7.69.1-win64-mingw\bin\curl.exe https://ip.chasehall.net/pub.php > %USERPROFILE%\Documents\IP.txt

:: Kill IW4MAdmin
taskkill /F /FI "WindowTitle eq IW4MAdmin" /T

:: Replace IW4MAdminSettings.json with our new IP.
python Update-Public-IP.py

:: Start IW4MAdmin Again
cd IW4MAdmin
set DOTNET_CLI_TELEMETRY_OPTOUT=1 
echo y | dotnet Lib\IW4MAdmin.dll