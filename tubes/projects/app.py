from flask import Flask, render_template, request, redirect, url_for
from db import conn
from db import mysql
import json, os

conn = mysql.connect()

app = Flask(__name__)

@app.route('/')
def index():
    query = "select * from users"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    # return render_template('/auth/index.html', data=result)
    return render_template('index.html', data=result)

@app.route('/add')
def add():
    return "OK"

@app.route('/store', methods=['POST'])
def store():
    msg = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        level    = request.form['level']
        query = "insert into users(username, password, level) values('"+ username +"', '"+ password +"', '"+ level +"')"
        cursor = conn.cursor()
        cursor.execute(query)
        # if cursor.execute(query):
        #     msg = "Insert berhasil"
        # else:
        #     msg = "Insert gagal"
    conn.commit()

    return redirect(url_for('index'))

@app.route('/show/<uid>')
def show(uid):
    query = "select * from users where uid='"+ uid +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return render_template('edit.html', data=result)

@app.route('/update/<uid>', methods=['POST'])
def update(uid):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        level    = request.form['level']
        query = "update users set username='"+ username +"', password='"+ password +"', level='"+ level +"' where uid='"+ uid +"'"
        cursor = conn.cursor()
        cursor.execute(query)
        # if cursor.execute(query):
        #     msg = "Insert berhasil"
        # else:
        #     msg = "Insert gagal"
    conn.commit()

    return redirect(url_for('index'))

@app.route('/delete/<uid>')
def delete(uid):
    query = "delete from users where uid='"+ uid +"'"
    cursor = conn.cursor()
    
    msg = ""
    if cursor.execute(query):
        msg = redirect(url_for('index'))
    else:
        msg = "Delete gagal"
    conn.commit()
    return msg

if __name__ == "__main__":
    app.run(debug=True)