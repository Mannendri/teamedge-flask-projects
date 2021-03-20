from flask import Flask, request, render_template, current_app as app
from sense_emu import SenseHat  
from time import sleep

app = Flask(__name__)
sense = SenseHat()
messages = {}
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == "POST":
        message = request.form.get("message")
        author = request.form.get("author")
        messages[author] = message
        sense.show_message(message)
    return render_template('success.html', message = message, author = author)

@app.route('/all_messages')
def all_messages():
    return render_template('all_messages.html', messages = messages)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
