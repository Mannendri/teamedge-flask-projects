from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Mannendri\'s Rainbow Project"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

