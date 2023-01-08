
from db import *
from datetime import *
import time
import sys
import mysql.connector
# First we set our credentials

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
app.debug = True
cnx = mysql.connector.connect(user='root', password='dacjd156n.',host='some-mysql')
cursor = cnx.cursor()
create_database(cnx,cursor)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Sub')
def sub_page():
    return 'Sub Page'

@app.route('/register', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']

        cnx = mysql.connector.connect(user='root', password='dacjd156n.',host='some-mysql')
        cursor = cnx.cursor()
        insert_user(cnx,cursor,username,password)

        return redirect(url_for('login'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="5000")
