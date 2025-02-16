import csv
import time
import requests
import os
from send_sandeco import SendSandeco

# URL do arquivo Markdown
# url = "https://raw.githubusercontent.com/ecodelearn/canais-sandeco/refs/heads/main/regras-reduzidas.md" # regras-reduzidas.md
# url = "https://raw.githubusercontent.com/ecodelearn/canais-sandeco/refs/heads/main/livros-reduzido-api.md" # livros-reduzido-api.md
url = "https://raw.githubusercontent.com/ecodelearn/canais-sandeco/refs/heads/main/lembrete-grupo-livros.md" # lembrete-grupo-livros.md

response = requests.get(url)
msg = response.text

# Caminho do arquivo CSV
csv_file_path = '/home/ecode/trabalho/estudos/sandecoCrewAI/grupos_todos.csv'

# Função para enviar mensagem usando SendSandeco
def send_message(celular, msg):
    sender = SendSandeco()  # Corrigir a definição do objeto 'sender'
    sender.textMessage(celular, msg)  # Usar o método correto 'textMessage'

# Ler o arquivo CSV e enviar mensagens
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        celular = row['numero']
        send_message(celular, msg)
        time.sleep(5)  # Espera de 2 segundos entre os envios
