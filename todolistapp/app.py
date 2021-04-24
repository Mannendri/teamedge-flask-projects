from flask import Flask, render_template
from flask_apscheduler import APScheduler

app = Flask (__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    