from sqlite3 import connect
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    connection = connect('lists.db')
    cursor = connection.cursor()

    rows = cursor.execute('SELECT * FROM lists').fetchall()

    connection.close()

    return render_template('index.html', rows=rows)


@app.route('/insert', methods=['POST'])
def insert():
    name = request.form.get('name')

    connection = connect('lists.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO lists (name) VALUES (?)', (name,))

    connection.commit()
    connection.close()

    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    return redirect('/')
