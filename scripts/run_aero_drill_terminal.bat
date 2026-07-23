@echo off
setlocal
call "%~dp0..\ros2_ws\install\setup.bat"
if errorlevel 1 exit /b %errorlevel%
set RMW_IMPLEMENTATION=rmw_fastrtps_cpp
ros2 run aerospace_olp_bringup aero_drill_terminal %*
exit /b %errorlevel%
