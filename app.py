from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)
#app.config['SERVER_NAME'] = 'localhost:5000'


#@app.route('/sms', methods=['POST'], host='tonyboni.com:5000')
@app.route('/sms', methods=['POST'])
def sms():
    print(request.form)
    number = request.form['From']
    message_body = request.form['Body']
    #message_body = "test"

    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    
    return str(resp)

@app.route("/voice", methods=['POST'])
def voice():
    # Start our TwiML response
    resp = VoiceResponse()
    

    # Read a message aloud to the caller
    resp.say("hello Gabrielle!  Let's  play a game... I'm thinking of a letter between teeee, and, veeeee.  What is it?! Say it now.", voice='male')
    resp.record()

    resp.hangup()

    return str(resp)


@app.route('/')
def index():
    return 'Web App with Python Flask!'


if __name__ == '__main__':
    #app.run()
    app.run(host='tonyboni.com', port=5000)
#app.run(host='tonyboni.com', port=5000)

