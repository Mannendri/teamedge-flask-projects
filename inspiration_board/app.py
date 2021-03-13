from flask import Flask, request, render_template, current_app as app
from sense_hat import SenseHat  
from time import sleep

app = Flask(__name__)
sense = SenseHat()
messages = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        messages.append(message)
        sense.show_message(message)
    return render_template('index.html')

@app.route('/all_messages')
def all_messages():
    for message in messages:
        sense.show_message(message)
    return render_template('all_messages.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
