from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    print(request.form)
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    
    return str(resp)


@app.route("/voice", methods=['POST'])
def voice():
    resp = VoiceResponse()
    
    audio = "Hello from Tony Teaches Tech. Subscribe then leave me a message."
    resp.say(audio, voice='male')
    resp.record()
    resp.hangup()

    return str(resp)


@app.route('/')
def index():
    return "Subscribe to Tony Teaches Tech!"


if __name__ == '__main__':
    app.run(host='tonyboni.com', port=5000)

