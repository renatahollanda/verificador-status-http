@echo off
:: Script de configuração para Windows

:: Verifica se o ambiente virtual existe
if not exist "venv\" (
    python -m venv venv
    echo Ambiente virtual criado.
    call venv\Scripts\activate.bat
    pip install requests
    echo Dependencias instaladas.
) else (
    echo Ambiente virtual ja existe.
    call venv\Scripts\activate.bat
    pip install --upgrade requests
    echo Dependencias verificadas/atualizadas.
)


echo.
echo Ambiente configurado com sucesso!
echo Para ativar manualmente: call venv\Scripts\activate.bat
echo Para desativar: deactivate
echo.
pause