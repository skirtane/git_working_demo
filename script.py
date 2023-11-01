from flask import *

app = Flask(__name__)

@app.route('/home/<name>')
def hello(name):
	return "Hello " +name 

@app.route('/home/<int:age>')
def printAge(age):
    return "Age =%d\n"%age

@app.route('/home/admin')
def admin():
    return "Its admin"

@app.route('/home/student')
def student():
    return "Its student"

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    #passwd = request.form['passwd']
    return "Welcome %s"%uname
app.run(debug=True)