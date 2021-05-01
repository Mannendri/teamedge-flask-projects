from flask import Flask, render_template, request, redirect, url_for
from flask_apscheduler import APScheduler
import sqlite3

app = Flask (__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/')
def index():
    conn = sqlite3.connect("./static/data/tasks.db")
    curs = conn.cursor()
    tasks = []
    rows = curs.execute("SELECT * FROM tasks")
    for row in rows:
        task = {'description':row[0], 'reminder':row[1]}
        tasks.append(task)
    conn.close() 
    return render_template('index.html', tasks=tasks)

@app.route('/todo', methods=['POST'])
def todo():
    if request.method == 'POST':
        conn = sqlite3.connect("./static/data/tasks.db")
        curs = conn.cursor()
        task_name = request.form.get("description")
        reminder = request.form.get("date")    
        #connect to database and insert task
        curs.execute("INSERT INTO tasks VALUES((?),(?))", (task_name, reminder))
        conn.commit()        
   
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    