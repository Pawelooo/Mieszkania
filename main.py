import os
from flask import Flask, render_template, url_for, json, app

app = Flask(__name__)


@app.route('/')
def showjson():
    return render_template('base.html')


@app.route('/olx')
def show_offers_olx():
    with open('lista_mieszkan.json', 'r') as file:
        data = json.load(file)
    return render_template('olx.html', data=data)


@app.route('/oto_dom')
def show_offers_oto_dom():
    with open('lista_mieszkan_oto.json', 'r') as file:
        data = json.load(file)
    return render_template('oto_dom.html', data=data)


app.run(debug=True)
