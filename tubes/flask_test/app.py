from flask import Flask, render_template, url_for, request
import requests
from flaskext.mysql import MySQL
import json

app = Flask(__name__)
url = "https://api.djuang.id/api/"

@app.route('/')
def index():
    data = [
        ["G001", "Aman"],
        ["G002", "Aman2"],
        ["G003", "Aman3"],
    ]

    return render_template('index.html', value=data)

@app.route('/apis')
def apis():
    r = requests.get("https://api.djuang.id/api/vehiclebrands")
    jsonData = r.json()

    # print(r)
    return render_template('apis.html', data=jsonData)

@app.route('/openapis')
def openapis():
    jsonPenyakit = open('./data/penyakit.json')
    jsonGejala = open('./data/gejala.json')
    penyakit = json.load(jsonPenyakit)
    gejala = json.load(jsonGejala)
    
    return render_template('openapis.html', penyakit=penyakit, gejala=gejala)

@app.route('/diag')
def diag():
    jsonGejala = open('./data/gejala.json')
    gejala = json.load(jsonGejala)
    return render_template('diagnose.html', gejala=gejala)

@app.route('/check', methods=['POST'])
def check():
    data = []
    gejala = []
    if request.method == 'POST':
        # nama = request.form['nama']
        # umur = request.form['umur']
        gejala = request.form.getlist('gejala')
        print(gejala)
        return gejala[3]

@app.route('/users')
def users():
    r = requests.get("https://api.djuang.id/api/users")
    jsonData = r.json()

    # print(r)
    return render_template('user.html', data=jsonData)

@app.route('/badan')
def badan():
    return render_template('badan.html')

@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/add', methods=['POST'])
def add():
    r = requests.post("https://api.djuang.id/api/vehiclebrands")
    
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
