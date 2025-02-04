import os
import streamlit as st
from send_sandeco import SendSandeco  # Certifique-se de que a classe Send está importada corretamente

# Inicializar a classe Send
mensageiro = SendSandeco()

# Criar a pasta 'temp' para salvar arquivos
if not os.path.exists('temp'):
    os.makedirs('temp')

# Configuração do Streamlit
st.title("Envio de Mensagens - EvolutionAPI")
st.sidebar.header("Selecione o tipo de mensagem")

# Escolher o tipo de mensagem
tipo = st.sidebar.selectbox("Tipo de mensagem", ["Texto", "Imagem", "Vídeo", "Áudio", "PDF", "Documento"])

# Campo para o número de telefone
numero = st.text_input("Número do destinatário (formato internacional)", placeholder="+559999999999")

if tipo == "Texto":
    # Mensagem de texto
    mensagem = st.text_area("Mensagem de texto", placeholder="Digite sua mensagem aqui...")
    mentions = st.text_input("Mencionar números (separados por vírgula)", placeholder="559888888888,559877777777").split(',')

    if st.button("Enviar Mensagem de Texto"):
        if numero and mensagem:
            resposta = mensageiro.textMessage(numero, mensagem, mentions if mentions != [''] else [])
            st.success(f"Mensagem enviada: {resposta}")
        else:
            st.error("Por favor, insira o número e a mensagem.")

elif tipo == "Imagem":
    # Envio de imagem
    imagem = st.file_uploader("Selecione uma imagem", type=["jpg", "jpeg", "png"])
    legenda = st.text_input("Legenda da imagem")

    if st.button("Enviar Imagem"):
        if numero and imagem:
            caminho_imagem = f"temp/{imagem.name}"
            with open(caminho_imagem, "wb") as f:
                f.write(imagem.read())

            resposta = mensageiro.image(numero, caminho_imagem, legenda)
            st.success(f"Imagem enviada: {resposta}")
        else:
            st.error("Por favor, insira o número e selecione uma imagem.")

elif tipo == "Vídeo":
    # Envio de vídeo
    video = st.file_uploader("Selecione um vídeo", type=["mp4", "avi", "mov"])
    legenda = st.text_input("Legenda do vídeo")

    if st.button("Enviar Vídeo"):
        if numero and video:
            caminho_video = f"temp/{video.name}"
            with open(caminho_video, "wb") as f:
                f.write(video.read())

            resposta = mensageiro.video(numero, caminho_video, legenda)
            st.success(f"Vídeo enviado: {resposta}")
        else:
            st.error("Por favor, insira o número e selecione um vídeo.")

elif tipo == "Áudio":
    # Envio de áudio
    audio = st.file_uploader("Selecione um arquivo de áudio", type=["mp3", "wav", "ogg"])

    if st.button("Enviar Áudio"):
        if numero and audio:
            caminho_audio = f"temp/{audio.name}"
            with open(caminho_audio, "wb") as f:
                f.write(audio.read())

            resposta = mensageiro.audio(numero, caminho_audio)
            st.success(f"Áudio enviado: {resposta}")
        else:
            st.error("Por favor, insira o número e selecione um áudio.")

elif tipo == "PDF":
    # Envio de PDF
    pdf = st.file_uploader("Selecione um arquivo PDF", type=["pdf"])
    legenda = st.text_input("Legenda do PDF")

    if st.button("Enviar PDF"):
        if numero and pdf:
            caminho_pdf = f"temp/{pdf.name}"
            with open(caminho_pdf, "wb") as f:
                f.write(pdf.read())

            resposta = mensageiro.PDF(numero, caminho_pdf, legenda)
            st.success(f"PDF enviado: {resposta}")
        else:
            st.error("Por favor, insira o número e selecione um PDF.")

elif tipo == "Documento":
    # Envio de documento
    documento = st.file_uploader("Selecione um documento (Word, etc.)", type=["doc", "docx", "txt"])
    legenda = st.text_input("Legenda do documento")

    if st.button("Enviar Documento"):
        if numero and documento:
            caminho_documento = f"temp/{documento.name}"
            with open(caminho_documento, "wb") as f:
                f.write(documento.read())

            resposta = mensageiro.document(numero, caminho_documento, legenda)
            st.success(f"Documento enviado: {resposta}")
        else:
            st.error("Por favor, insira o número e selecione um documento.")

# Limpeza da pasta 'temp' após envio
if st.button("Limpar arquivos temporários"):
    for arquivo in os.listdir('temp'):
        os.remove(os.path.join('temp', arquivo))
    st.success("Arquivos temporários limpos.")
