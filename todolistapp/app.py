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
        task = {'rowid':row[0],'description':row[1], 'reminder':row[2]}
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
        curs.execute("INSERT INTO tasks (description, reminder) VALUES((?),(?))", (task_name, reminder))
        conn.commit()   
        conn.close()      
    return redirect(url_for('index'))

@app.route('/edit/<btn>', methods=['GET','POST'])
def edit(btn):
    conn = sqlite3.connect("./static/data/tasks.db")
    curs = conn.cursor()
    if (request.method=='GET'):
        rows = curs.execute("SELECT * FROM tasks WHERE rowid="+str(btn))
        for row in rows:
            task = {'rowid':row[0],'description':row[1], 'reminder':row[2]}
        return render_template("edit.html", task=task) 
    elif (request.method=='POST'):
        task_name = request.form.get("edit-description")
        reminder = request.form.get("edit-date")
        curs.execute("UPDATE tasks SET description=(?),reminder=(?) WHERE rowid=(?)",(task_name, reminder, btn))
        conn.commit()
    conn.close() 
    return redirect(url_for('index'))  
   

@app.route('/complete/<btn>')
def complete(btn):
    conn = sqlite3.connect("./static/data/tasks.db")
    curs = conn.cursor()
    curs.execute("DELETE FROM tasks WHERE rowid=(?)", (btn,))
    conn.commit()     
    return redirect(url_for('index'))  

@app.route('/delete/<btn>')
def delete(btn):
    conn = sqlite3.connect("./static/data/tasks.db")
    curs = conn.cursor()
    curs.execute("DELETE FROM tasks WHERE rowid=(?)", (btn,))
    conn.commit()     
    return redirect(url_for('index'))  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    