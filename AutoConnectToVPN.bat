@echo off
REM set VPN_NAME="<Enter VPN Name>"

REM rasdial %VPN_NAME%

REM if %errorlevel% neq 0 (
    REM echo Failed to connect to %VPN_NAME%
REM ) else (
    REM echo Successfully connected to %VPN_NAME%
REM )
REM pause >nul

REM @echo off
set VPN_NAME="MSFT-AzVPN-Manual"

REM Check if the VPN is connected
rasdial | findstr /C:"%VPN_NAME%" >nul
echo Prad's script is checking if VPN is still connected. If not, then his script will attempt to connect... [thank Prad later]
if %errorlevel% neq 0 (
    echo Prad says: VPN is disconnected. Attempting to reconnect...
    rasdial %VPN_NAME%
    if %errorlevel% neq 0 (
        echo Prad says: Failed to reconnect to %VPN_NAME%.
    ) else (
        echo Prad says: Successfully reconnected to %VPN_NAME%.
    )
) else (
    echo Prad says: VPN is still connected.
)

@REM Prad's VPN Monitor
@REM Prad's script will check if VPN is still connected. If not, then his script will attempt to connect... [thank Prad later]
