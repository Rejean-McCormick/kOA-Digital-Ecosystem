@echo off
setlocal
cd /d "%~dp0"
python "%~dp0tools\koa_tandem_vps\installer.py" rollback
set "RC=%ERRORLEVEL%"
if not "%RC%"=="0" echo [BLOQUE] Voir l erreur ci-dessus. Aucune action distante lancee.
echo.
pause
exit /b %RC%
