# AgenteS

Este projeto consiste em um conjunto de scripts e aplicações para enviar e receber mensagens via WhatsApp utilizando a API Evolution.

## Componentes

*   `agente.py`: Script para enviar mensagens a partir de uma lista de números de telefone em um arquivo CSV, utilizando um template Markdown hospedado em um URL.
*   `app.py`: Aplicação Streamlit para enviar mensagens de texto, imagem, vídeo, áudio, PDF e documento.
*   `enviar_whatsapp.py`: Aplicação Streamlit simplificada para enviar mensagens de texto.
*   `evo_receber.py`: Servidor Flask para receber mensagens via webhook e responder automaticamente.
*   `hello.py`: Script simples que imprime "Hello from sandecocrewai!".
*   `message_sandeco.py`: Define a classe `MessageSandeco` para processar dados de mensagens recebidas.
*   `receber_whatsapp.py`: Servidor Flask similar ao `evo_receber.py` para receber e responder mensagens.
*   `regras.py`: Script idêntico ao `agente.py`.
*   `send_sandeco.py`: Define a classe `SendSandeco` para enviar mensagens de texto e mídia utilizando a API Evolution.
*   `teste_envio.py`: Script para testar o envio de mensagens utilizando a classe `SendSandeco`.

## Variáveis de Ambiente

Os seguintes variáveis de ambiente são necessárias para o funcionamento do projeto:

*   `EVO_API_TOKEN`: Token da API Evolution.
*   `EVO_INSTANCE_NAME`: Nome da instância Evolution.
*   `EVO_INSTANCE_TOKEN`: Token da instância Evolution.
*   `EVO_BASE_URL`: URL base da API Evolution.

## Dependências

*   `evolutionapi>=0.0.9`
*   `flask>=3.1.0`
*   `python-dotenv>=1.0.1`
*   `streamlit>=1.41.1`

## Instalação

1.  Clone o repositório.
2.  Crie um ambiente virtual: `python -m venv .venv`
3.  Ative o ambiente virtual: `source .venv/bin/activate`
4.  Instale as dependências usando `uv`: `uv pip install -r requirements.txt` ou `uv pip install .`
5.  Configure as variáveis de ambiente.
6.  Execute os scripts e aplicações.
