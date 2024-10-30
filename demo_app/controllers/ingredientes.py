'''

Este script contiene la ruta principal de la pagina web que nos dirige al menu de login y la ruta de la pagina principal
la cual nos dirige al menu restaurante donde podemos realizar los pedidos de las bebidas

'''


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.ingrediente import ingrediente
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
    data = []

    aux_data = ingrediente.get_all()
    for ing in aux_data:
        data.append(ing.asdict_front())
    
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

    #obtener todos los ingredientes existentes
    ingredientes = ingrediente.get_all()


    is_valid = True
    categoria = "crear ingredientes"
    mensaje = "Ingrediente Creado"
    status = 'ok'
    code = 200


    data = request.json
    ingredienteNuevo = {
        'id_ingrediente': int(data['stockNumber']),
        'nombre': data['nombre'],
        'descripcion': data['descripcion'],
        'precio_unitario': float(data['costo']),
        'cantidad_unitaria': int(data['cantidad']),
        'categoria': data['tipo'],
        'proveedor': data['proveedor']
    }
    #validaciones para ingresar nuevo ingrediente
    
    if ingredienteNuevo['id_ingrediente'] <= 0:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "El id no puede ser 0 o menor a 0"
        status = 'error'
        code = 400
    elif ingredienteNuevo['nombre'] == '':
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "Por favor, ingrese un nombre"
        status = 'error'
        code = 400
    elif len(ingredienteNuevo['nombre']) > 45:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "El nombre no puede superar los 45 caracteres"
        status = 'error'
        code = 400
    elif len(ingredienteNuevo['descripcion']) >= 250:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "La descripcion no puede ser mayor a 250 caracteres"
        status = 'error'
        code = 400
    elif ingredienteNuevo['categoria'] == '':
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "Por favor, ingrese una categoria"
        status = 'error'
        code = 400
    elif ingredienteNuevo['proveedor'] == '':
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "Por favor, ingrese un proveedor"
        status = 'error'
        code = 400
    elif len(ingredienteNuevo['proveedor']) > 45:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "El proveedor no puede superar los 45 caracteres"
        status = 'error'
        code = 400
    elif ingredienteNuevo['precio_unitario'] <= 0:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "El costo no puede ser 0 o menor a 0"
        status = 'error'
        code = 400
    elif ingredienteNuevo['cantidad_unitaria'] <= 0:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "La cantidad unitaria no puede ser 0 o menor a 0"
        status = 'error'
        code = 400
    else:
        for x in ingredientes:
            if ingredienteNuevo['id_ingrediente'] == x.id_ingrediente:
                is_valid = False
                categoria = "crear ingredientes"
                mensaje = "No pueden existir ingredientes con el mismo ID"
                status = 'error'
                code = 400
                break
            elif ingredienteNuevo['nombre'] == x.nombre:
                is_valid = False
                categoria = "crear ingredientes"
                mensaje = "No pueden existir ingredientes con el mismo nombre"
                status = 'error'
                code = 400
            break
    
    if is_valid:
        ingrediente.save(ingredienteNuevo)
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code 
    }
    return jsonify(value)


@app.route('/ingrediente/modificar', methods=['POST'])
def modificar_ingredientes():

    #obtener todos los ingredientes existentes
    ingredientes = ingrediente.get_all()

    is_valid = True
    categoria = "modificar ingredientes"
    mensaje = "Modificacion Exitosa"
    status = 'ok'
    code = 200
    data = request.json
    aux_ingrediente = {
        'id_ingrediente': int(data['stockNumber']),
        'nombre': data['nombre'],
        'descripcion': data['descripcion'],
        'precio_unitario': float(data['costo']),
        'cantidad_unitaria': int(data['cantidad']),
        'categoria': data['tipo'],
        'proveedor': data['proveedor']
    }
    modIngrediente = ingrediente.get_by_id(aux_ingrediente)
    #validaciones para ingresar nuevo ingrediente
    for x in ingredientes:
        if aux_ingrediente['nombre'] == x.nombre and aux_ingrediente['nombre'] != modIngrediente.nombre:
            is_valid = False
            categoria = "crear ingredientes"
            mensaje = "No pueden existir ingredientes con el mismo nombre"
            status = 'error'
            code = 400
            break
    if aux_ingrediente['id_ingrediente'] <= 0:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "El id no puede ser 0 o menor a 0"
        status = 'error'
        code = 400
    elif aux_ingrediente['nombre'] == '':
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "Por favor, ingrese un nombre"
        status = 'error'
        code = 400
    elif len(aux_ingrediente['descripcion']) >= 250:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "La descripcion no puede ser mayor a 250 caracteres"
        status = 'error'
        code = 400
    elif aux_ingrediente['categoria'] == '':
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "Por favor, ingrese una categoria"
        status = 'error'
        code = 400
    elif aux_ingrediente['proveedor'] == '':
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "Por favor, ingrese un proveedor"
        status = 'error'
        code = 400
    elif aux_ingrediente['precio_unitario'] <= 0:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "El costo no puede ser 0 o menor a 0"
        status = 'error'
        code = 400
    elif aux_ingrediente['cantidad_unitaria'] <= 0:
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "La cantidad unitaria no puede ser 0 o menor a 0"
        status = 'error'
        code = 400

    if is_valid:
        ingrediente.update_by_id(aux_ingrediente)

    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code 

    }
    return jsonify(value)


@app.route('/ingrediente/eliminar', methods=['POST'])
def eliminar_ingredientes():
    is_valid = True
    categoria = "eliminar ingredientes"
    mensaje = "Ingrediente eliminado"
    status = 'ok'
    code = 200
    data = request.json
    aux_ingrediente = {
        'id_ingrediente': int(data['stockNumber'])
        
    }
    deleteIngrediente = ingrediente.delete_by_id(aux_ingrediente)
    # if deleteIngrediente == None:
    #     is_valid = True
    #     categoria = "eliminar ingredientes"
    #     mensaje = "Error al eliminar ingrediente"
    #     status = 'error'
    #     code = 400

    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code 
    }
    return jsonify(value)