@echo off

rem Hack, in case you installed git but the path is incorrect
set PATH=%PATH%;C:\Program Files\Git\mingw64\bin\

echo Checking for updates...
git fetch origin master
git pull origin master

pause
