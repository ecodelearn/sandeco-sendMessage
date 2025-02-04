from flask import Flask, request
from message_sandeco import MessageSandeco
from send_sandeco import SendSandeco

app = Flask(__name__)

@app.route("/messages-upsert", methods=['POST'])
def webhook():

    try:
        data = request.get_json()        
        msg = MessageSandeco(data)         
                            

        send = SendSandeco()
        send.textMessage(number=msg.phone,
                         msg=msg.text_message)

    except:
        print("Erro")
    
        
    return ""
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



