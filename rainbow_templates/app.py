from flask import Flask, render_template, current_app as app

app = Flask(__name__)
colors = ['red','orange','yellow','green','blue','indigo','violet']

@app.route('/')
def index():
    return 'Welcome to Mannendri\'s Rainbow Project'

@app.route('/rainbow')
def rainbow():
    return render_template('rainbow.html', colors = colors)
@app.route('/red')
def red():
    return render_template('index.html', color="Red")
    
@app.route('/orange')
def orange():
    return render_template('index.html', color="Orange")

@app.route('/yellow')
def yellow():
    return render_template('index.html', color="Yellow")

@app.route('/green')
def green():
    return render_template('index.html', color="Green")

@app.route('/blue')
def blue():
    return render_template('index.html', color="Blue")

@app.route('/indigo')
def indigo():
    return render_template('index.html', color="Indigo")

@app.route('/violet')
def violet():
    return render_template('index.html', color="Violet")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

