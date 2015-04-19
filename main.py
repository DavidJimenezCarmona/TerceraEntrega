#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
app = Flask(__name__)
GoogleMaps(app)

from funciones import *
import json


def cargarMapa(origen):
    lista = []
    for estado in origen["statuses"]:
        if estado["coordinates"]!= None:
            coordenada = estado["coordinates"]
            lista.append([coordenada.values()[1][1] , coordenada.values()[1][0]])
    mymap = Map(
                identifier="view-side",
                lat=40.3450396,
                lng=-3.6517684,
                zoom=5,
                markers=lista,
                style="height:800px;width:800px;margin:0;"
            )
    return mymap

@app.route("/buscar", methods=['POST'])
def buscar():
    twitter_api = oauth_login()
    search_results = twitter_api.search.tweets(q=request.form['busqueda'] , geocode='40.4173175,-3.702233699999965,700km', result_type="recent")
    save_json("trends",search_results)
    return render_template('template.html', mymap=cargarMapa(search_results))

@app.route("/anterior", methods=['POST'])
def anterior():
    with open('trends.json') as data_file:
        data = json.load(data_file)
    return render_template('template.html', mymap=cargarMapa(data))


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


