'''

Este script contiene la ruta principal de la pagina web que nos dirige al menu de login y la ruta de la pagina principal
la cual nos dirige al menu restaurante donde podemos realizar los pedidos de las bebidas

'''


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.lista_bebidas import lista_bebidas
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.user import User
from demo_app.models.receta import receta
from flask_bcrypt import Bcrypt
import datetime
import requests
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    
     return render_template('login.html')

@app.route('/home')
def home():
        
    

    f = open("bebida_id.txt", "r+")
    bebidas_id = f.read()
    
    if bebidas_id == '' or bebidas_id == '0':
        bebidas_id = 0
    else:
        bebidas_id = int(bebidas_id)
    sv_data = lista_bebidas.get_all()
    listas = []
    for lista in sv_data:
        nombre = lista.asdict()
        listas.append(nombre['nombre'])

    data = {
    
        'id_lista_bebidas': bebidas_id
    }
    
    if bebidas_id != 0:
        if lista_bebidas.get_by_id(data) != []:
            sv_data2 = lista_bebidas.get_by_id(data)
            bebidas = [sv_data2.bebida_1,sv_data2.bebida_2,sv_data2.bebida_3,sv_data2.bebida_4,sv_data2.bebida_5,sv_data2.bebida_6,sv_data2.bebida_7,sv_data2.bebida_8,sv_data2.bebida_9,sv_data2.bebida_10,sv_data2.bebida_11,sv_data2.bebida_12]
        else:
            
            bebidas = []
    else:
            bebidas = []
    bebidas_total = ['']
    for x in bebidas:
        if x != '':
            bebidas_total.append(x)
        else:
            continue

    recetas = receta.get_by_id_lista_bebidas(data)
    recetas_total = []
    for rec in recetas:
        r = rec.asdict()
        ingredientes = ''
        for i in range(10):
            aux_1 = 'bebida_'+str(i+1)
            if r[aux_1] != '':
                ingredientes=ingredientes + r[aux_1] + ', '
            else:
                continue
        ingredientes = ingredientes[:-2]
        aux = {
                'nombre':r['nombre'],
                'ingredientes': ingredientes
        }
        recetas_total.append(aux)
    
    
    
    f.close()
    
    return render_template('restaurant.html',lista_bebidas = listas,bebidas = bebidas_total, recetas = recetas_total)


