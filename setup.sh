#!/bin/bash

# Cria um ambiente virtual Python caso não exista ou atualiza as dependências se o ambiente virtual foi criado
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Ambiente virtual criado."
    source venv/bin/activate
    echo "Instalando dependências..."
    pip install requests
    echo "Dependências instaladas."
else 
    echo "Ambiente virtual já existe. Verificando dependências..."
    source venv/bin/activate
    pip install --upgrade requests  # Atualiza as dependências, se necessário
fi

echo "Ambiente configurado com sucesso!"
echo "Para ativar manualmente: source venv/bin/activate"
echo "Para desativar: deactivate"
