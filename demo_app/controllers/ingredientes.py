'''

Este script contiene la ruta principal de la pagina web que nos dirige al menu de login y la ruta de la pagina principal
la cual nos dirige al menu restaurante donde podemos realizar los pedidos de las bebidas

'''


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.user import User
from demo_app.models.receta import receta
from flask_bcrypt import Bcrypt
import datetime
import requests
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

'''
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
'''

@app.route('/ingredientes', methods=['GET'])
def get_list_ingredientes():
    is_valid = True
    categoria = "ingredientes"
    mensaje = "Exitoso"
    status = 'ok'
    code = 200
    data = [
    { 'nombre': 'Ron', 'tipo': 'Alcohol', 'costo': '1.20', 'cantidad': '750', 'stockNumber': 123, 'descripcion': 'Aged Rum', 'proveedor': 'ABC Suppliers' },
    { 'nombre': 'Vodka', 'tipo': 'Alcohol', 'costo': '1.20', 'cantidad': '750', 'stockNumber': 124, 'descripcion': 'Premium Vodka', 'proveedor': 'XYZ Distributors' }
    ]
    
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    return jsonify(value)

@app.route('/ingrediente/nuevo', methods=['POST'])
def crear_ingredientes():
    is_valid = True
    categoria = "crear ingredientes"
    mensaje = "Exitoso"
    status = 'ok'
    code = 200
    data = request.json
    print(data)
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        'data': data 

    }
    return jsonify(value)


@app.route('/ingrediente/modificar', methods=['POST'])
def modificar_ingredientes():
    is_valid = True
    categoria = "modificar ingredientes"
    mensaje = "La cagaste"
    status = 'ok'
    code = 400
    data = request.json
    print(data)
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        'data': data 

    }
    return jsonify(value)


@app.route('/ingrediente/eliminar', methods=['POST'])
def eliminar_ingredientes():
    is_valid = True
    categoria = "eliminar ingredientes"
    mensaje = "No deboraste"
    status = 'ok'
    code = 400
    data = request.json
    print(data)
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        'data': data 

    }
    return jsonify(value)