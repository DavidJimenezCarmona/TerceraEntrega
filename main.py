#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
app = Flask(__name__)
GoogleMaps(app)

from funciones import *
import json

def menu():
	print "Selecciona una opción"
	print "\t1 - Actualizar lista de tweets"
	print "\t2 - Mostrar mapa"
	print "\t9 - salir"

seguir = True

while seguir==True:
    menu()
    opcionMenu = raw_input("Por favor, elige una opción >> ")

    if opcionMenu=="1":
        tema = raw_input("Por favor, introduzca el tema que quiere rastrear en Twitter >> ")
        twitter_api = oauth_login()
        search_results = twitter_api.search.tweets(q=tema, geocode='40.4173175,-3.702233699999965,700km', result_type="recent")
        save_json("trends",search_results)

    elif opcionMenu=="2":
        seguir = False
        with open('trends.json') as data_file:
            data = json.load(data_file)

        lista = []
        for estado in data["statuses"]:
            if estado["coordinates"]!= None:
                coordenada = estado["coordinates"]
                lista.append([coordenada.values()[1][1] , coordenada.values()[1][0]])

        @app.route("/")
        def mapview():
            mymap = Map(
                identifier="view-side",
                lat=40.3450396,
                lng=-3.6517684,
                markers=lista,
                style="height:800px;width:800px;margin:0;"
            )

            return render_template('template2.html', mymap=mymap)

        if __name__ == "__main__":
            app.run(debug=False)

    elif opcionMenu=="9":
        print "Gracias por usar este script"
        seguir = False


