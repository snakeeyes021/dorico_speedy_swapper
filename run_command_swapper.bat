@echo off
setlocal enabledelayedexpansion

REM Get the directory of the batch file
set "batch_dir=%~dp0"

REM Read configuration
for /F "tokens=1,2 delims==" %%a in (%batch_dir%config.txt) do (
    set %%a=%%b
)

REM Run Python script with the correct paths
python "%batch_dir%command_swapper.py"

endlocal
