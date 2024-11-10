'''

Este script cuenta con todas las rutas para crear y modificar las recetas de bebidas. Incluye todas las validaciones:
No poder ingresar letras donde van cantidades, no poder ingresar 0 como cantidad, solo poder utilizar un maximo de 10 onzas en
total de cantidades, no poder repetir nombres por lista de bebidas disponibles e ingresar un tiempo de preparacion apropiado.

'''


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.receta import receta
from demo_app.models.pedido import pedido
from flask_bcrypt import Bcrypt
from datetime import datetime
import requests
import math


@app.route('/recetas', methods=['GET'])
def get_list_recetas():
    is_valid = True
    categoria = "recetas"
    mensaje = "Exitoso"
    status = 'success'
    code = 200
    data = [] 
    aux_data = receta.get_all()
    print(aux_data)
    for rec in aux_data:
        data.append(rec.asdict_front())
    
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    return jsonify(value) 

@app.route('/receta/nuevo', methods=['POST'])
def crear_recetas():
    is_valid = True
    categoria = "crear recetas"
    mensaje = "Receta Creada con exito"
    status = 'success'
    code = 200
    data = request.json
    recetas = receta.get_all()
    print('data: ',data)
    if data['nombre'] == '':
        is_valid = False
        categoria = "crear recetas"
        mensaje = "Por favor, ingrese un nombre"
        status = 'error'
        code = 400
    elif len(data['nombre']) > 45:
        is_valid = False
        categoria = "crear recetas"
        mensaje = "El nombre de la receta es muy largo"
        status = 'error'
        code = 400
    elif data['ingredientes'] == []:
        is_valid = False
        categoria = "crear recetas"
        mensaje = "Por favor, ingrese ingredientes"
        status = 'error'
        code = 400
    else:
        for rec in recetas:
            if rec.nombre == data['nombre']:
                is_valid = False
                categoria = "crear recetas"
                mensaje = "No puede crear recetas con el mismo nombre"
                status = 'error'
                code = 400


    if is_valid:
        cant = len(data['ingredientes'])
        ingredientes = []
        for i in data['ingredientes']:
            ingredientes.append(i['nombre'])
        
        for x in range(10-cant):
            ingredientes.append('')
    
        tiempo_prep = 1 + (cant * 10 * 1/60) # tiene que estar en minutos, entonces: cantidad de bebida x segundos por paso x 1/60 
        tiempo_prep = int(math.ceil(tiempo_prep))

        dict = {
        
            'nombre': data['nombre'], 
            'ing1': ingredientes[0], 
            'ing2': ingredientes[1], 
            'ing3': ingredientes[2], 
            'ing4': ingredientes[3],
            'ing5': ingredientes[4],
            'ing6': ingredientes[5],
            'ing7': ingredientes[6],
            'ing8': ingredientes[7],
            'ing9': ingredientes[8],
            'ing10': ingredientes[9],
            'tiempo_prep': tiempo_prep
            
        }
        receta.save(dict)
    


    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code

    }
    return jsonify(value)


@app.route('/receta/modificar', methods=['POST'])
def modificar_recetas():
    is_valid = True
    categoria = "modificar recetas"
    mensaje = "Receta editada correctamente"
    status = 'success'
    code = 200
    data = request.json

    print('data: ', data)
    recetas = receta.get_all()
    aux_receta = {
        'id_receta': data['id_receta']
    }
    modReceta = receta.get_by_id(aux_receta)
    
    if data['nombre'] == '':
        is_valid = False
        categoria = "crear recetas"
        mensaje = "Por favor, ingrese un nombre"
        status = 'error'
        code = 400
    elif len(data['nombre']) > 45:
        is_valid = False
        categoria = "crear recetas"
        mensaje = "El nombre de la receta es muy largo"
        status = 'error'
        code = 400
    elif data['ingredientes'] == []:
        is_valid = False
        categoria = "crear recetas"
        mensaje = "Por favor, ingrese ingredientes"
        status = 'error'
        code = 400
    else:
        for rec in recetas:
            if rec.nombre == data['nombre'] and modReceta.nombre != data['nombre']:
                is_valid = False
                categoria = "crear recetas"
                mensaje = "No puede crear recetas con el mismo nombre"
                status = 'error'
                code = 400


    if is_valid:
        cant = len(data['ingredientes'])
        ingredientes = []
        for i in data['ingredientes']:
            ingredientes.append(i['nombre'])
        
        for x in range(10-cant):
            ingredientes.append('')
    
        tiempo_prep = 1 + (cant * 10 * 1/60) # tiene que estar en minutos, entonces: cantidad de bebida x segundos por paso x 1/60 
        tiempo_prep = int(math.ceil(tiempo_prep))

        dict = {
            'id_receta': modReceta.id_receta,
            'nombre': data['nombre'], 
            'ing1': ingredientes[0], 
            'ing2': ingredientes[1], 
            'ing3': ingredientes[2], 
            'ing4': ingredientes[3],
            'ing5': ingredientes[4],
            'ing6': ingredientes[5],
            'ing7': ingredientes[6],
            'ing8': ingredientes[7],
            'ing9': ingredientes[8],
            'ing10': ingredientes[9],
            'tiempo_prep': tiempo_prep
            
        }
        receta.update_by_id(dict)
        
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        'data': data 

    }
    return jsonify(value)  

@app.route('/receta/eliminar', methods=['POST'])
def eliminar_recetas():
    is_valid = True
    categoria = "eliminar recetas"
    mensaje = "Receta eliminada"
    status = 'success'
    code = 200
    data = request.json
    aux_receta = {
        'nombre': data['nombre']
        
    }
    recetaSelected = receta.get_by_name(aux_receta)
    pedidos = pedido.get_all()
    #validar si no hay un pedido en cola con esta receta
    for ped in pedidos:
        if ped.id_receta == recetaSelected.id_receta:
            is_valid = False
            categoria = "eliminar recetas"
            mensaje = "No puede eliminar una bebida que se encuentre en cola de pedidos"
            status = 'error'
            code = 400
    if is_valid:
        eliminarReceta = receta.delete_by_name(aux_receta)
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code

    }
    return jsonify(value)

@app.route('/receta/toggleStatus', methods=['POST'])
def toggleStatus_recetas():
    is_valid = True
    categoria = "eliminar recetas"
    mensaje = "Receta eliminada"
    status = 'success'
    code = 200
    data = request.json

    aux_receta = {
        'id_receta': data['id_receta']
        
    }
    recetaSelected = receta.get_by_id(aux_receta)
    recetaSelected.change_status()
    aux = recetaSelected.asdict()
    receta.update_status(aux)
    
    
    print('data toggle status: ',recetaSelected.asdict())
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code

    }
    return jsonify(value)