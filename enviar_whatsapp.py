import streamlit as st
from send_sandeco import Send

# Instancia a classe Send
sender = Send()

# Configuração da interface do Streamlit
st.title("Envio de Mensagens com EvolutionAPI")
st.subheader("Preencha os campos abaixo para enviar sua mensagem")

# Campos para entrada de dados
number = st.text_input("Número de telefone (com DDI e DDD, exemplo: 5562981...):")
message = st.text_area("Mensagem:")
send_button = st.button("Enviar Mensagem")

# Lógica de envio simplificada
if send_button:
    if number and message:
        try:
            # Chama o método textMessage da classe Send
            response = sender.textMessage(number, message)
            
            if 'id' in response['key']:
                st.success(f"Mensagem enviada com sucesso!")
            else:
                st.error(f"Ops! Alguma coisa aconteceu,\n não deu para enviar a mensagem")
            
        except Exception as e:
            st.error(f"Erro ao enviar mensagem: {e}")
    else:
        st.warning("Por favor, preencha todos os campos antes de enviar.")