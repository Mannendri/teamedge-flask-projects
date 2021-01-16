from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/mannendri')
def mannendri():
	return render_template('mannendri.html')

@app.route('/tianna')
def tianna():
	return render_template('tianna.html')

@app.route('/cooper')
def cooper():
	return render_template('cooper.html')

@app.route('/catherine')
def catherine():
	return render_template('catherine.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')