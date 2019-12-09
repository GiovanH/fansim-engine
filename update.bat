@echo off

echo Checking for updates...
"C:\Program Files\Git\mingw64\bin\git.exe" fetch origin master
"C:\Program Files\Git\mingw64\bin\git.exe" pull origin master

pause
