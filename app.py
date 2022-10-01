from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse, Say

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
    response = VoiceResponse()
    say = Say('Hi', voice='Polly.Emma')
    say.break_(strength='x-weak', time='100ms')
    say.p('Welcome to the Tony Teaches Tech voice mail box.')
    say.p('Please subscribe, then leave me a message.')
    say.break_(strength='x-weak', time='50ms')
    say.p('Goodbye!')

    response.append(say)
    response.record()
    response.hangup()

    return str(response)


@app.route('/')
def index():
    return """<p>Subscribe to
    <a href='https://youtube.com/tonyteachestech/'>
        Tony Teaches Tech</a>!</p>
    """


if __name__ == '__main__':
    app.run(host='phone.tonyteaches.tech', port=5000)

