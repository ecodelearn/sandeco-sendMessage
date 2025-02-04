
from flask import Flask, request
from message_sandeco import MessageSandeco
from send_sandeco import SendSandeco

app = Flask(__name__)

@app.route("/messages-upsert", methods=['POST'])
def funcao():
    
    data = request.get_json()     

    msg = MessageSandeco(data)
        
    sender = SendSandeco()
    
    sender.textMessage(number=msg.phone, msg=msg.text_message)
    
    return ""


if __name__ == "__main__":
    app.run(host="https://webhook.brjhow.com.br/webhook/92eae098-cd35-4602-8c13-d2f95bb9822c", port="443", debug=True)

    # https://webhook.site/