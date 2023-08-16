from datetime import datetime
import MySQLdb.cursors
from flask import Flask, flash, redirect, render_template, request, session,url_for
from flask_mysqldb import MySQL
import mammoth
from io import BytesIO

#I have no idea what it does, but the app crashes without it :D 
UPLOAD_FOLDER = '/UoB/test'



app = Flask(__name__)
mysql = MySQL(app)

#Database Config
app.config['SECRET_KEY'] = "____"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = '____'
app.config['MYSQL_PASSWORD'] = '_____'
app.config['MYSQL_DB'] = 'CIS015-3'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#authentication route (Login)(default)
@app.route('/',methods=['GET','POST'])
def auth():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        cur.execute('SELECT username,password,role from users where username=%s and password = %s',(username,password))
        res = cur.fetchone()
        if res:
            session['loggedin'] = True
            session['id'] = username
            session['password'] = password
            session['role'] = res['role']
            return redirect(url_for('index'))
        else:
            flash('Wrong Username or Password')
            return render_template('login.html')
    return render_template('login.html')


#homepage route
@app.route('/home',methods=['GET','POST'])
def index():
    cur = mysql.connection.cursor()
    if request.method == 'GET':
        today = datetime.now()
        cur.execute("SELECT * FROM projects")
        projectDetails = cur.fetchall()
        cur.execute("SELECT * FROM tasks order by idTasks ASC ")
        tasksDetails = cur.fetchall()
        cur.execute("SELECT * FROM users")
        usersDetails = cur.fetchall()
        cur.execute("SELECT users.idUsers, users.username,users.lastname,\
        COUNT(CASE WHEN usertasks.status = 'STARTED' THEN 1 END) AS num_pending,\
        COUNT(CASE WHEN usertasks.status = 'WIP' THEN 1 END) AS num_in_progress,\
        COUNT(CASE WHEN usertasks.status = 'DONE' THEN 1 END) AS num_completed\
        FROM users\
        LEFT JOIN usertasks ON users.idUsers = usertasks.idusers\
        GROUP BY users.idUsers;")
        userTaskDetails = cur.fetchall()
        return render_template('homepage.html',projectDetails=projectDetails,today=today.date(),tasksDetails=tasksDetails,usersDetails=usersDetails,userTaskDetails=userTaskDetails)
    if request.method == 'POST':
        if 'file-startup' in request.files:
            file = request.files['file-startup']
            name = file.filename
            content = file.read()
            cur.execute("INSERT INTO testthisone (name,content,department) VALUES (%s,%s,'startup')",(name,content))
            cur.execute("UPDATE usertasks SET status = 'DONE' WHERE idusertasks = (SELECT idusers FROM users WHERE status != 'DONE' and idusers = 2 ORDER BY RAND() LIMIT 1);")
            mysql.connection.commit()
            return redirect(url_for('index'))
        if 'file-quality' in request.files:
            file = request.files['file-quality']
            name = file.filename
            content = file.read()
            cur.execute("insert into testthisone (name,content,department) VALUES (%s,%s,'quality')",(name,content))
            cur.execute("UPDATE usertasks SET status = 'DONE' WHERE idusers = 4")
            mysql.connection.commit()
            return redirect(url_for('index'))
        if 'file-risk' in request.files:
            file = request.files['file-risk']
            name = file.filename
            content = file.read()
            cur.execute('insert into testthisone (name,content,department) VALUES (%s,%s,"risk")',(name,content))
            cur.execute("UPDATE usertasks SET status = 'DONE' WHERE idusertasks = (SELECT idusers FROM users WHERE status != 'DONE' and idusers = 2 ORDER BY RAND() LIMIT 1);")
            mysql.connection.commit()
            return redirect(url_for('index'))
        if 'file-scheduling' in request.files:
            file = request.files['file-scheduling']
            name = file.filename
            content = file.read()
            cur.execute("insert into testthisone (name,content,department) VALUES (%s,%s,'scheduling')",(name,content))
            cur.execute("UPDATE usertasks SET status = 'DONE' WHERE idusertasks = (SELECT idusers FROM users WHERE status != 'DONE' and idusers = 3 ORDER BY RAND() LIMIT 1);")
            mysql.connection.commit()
            return redirect(url_for('index'))
    return redirect(url_for('index'))


#Results route (Dynamically generated for each task)
@app.route('/display', methods=['GET', 'POST'])
def display():
    cur = mysql.connection.cursor()
    description = request.args.get('page')
    category = request.args.get('catergory')
    if request.method == 'GET':
        cur.execute('SELECT * FROM testthisone WHERE department = %s', (description,))
        rows = cur.fetchall()
        data = []
        for row in rows:
            id, name, content, department = row
            contentO = BytesIO(content)
            html = mammoth.convert_to_html(contentO).value
            data.append({'id': id, 'name': name, 'html': html})
        return render_template('testfiles.html', data=data)

    


if "__main__" == __name__:
    Flask.run(app,debug=True)

