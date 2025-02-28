::version::gitleaks_8.24.0_windows_x64
@echo off
REM Run Gitleaks against the specified directory
tools\gitleaks_windows\gitleaks.exe detect -v --report-path gitleaks-report.json --source %1
