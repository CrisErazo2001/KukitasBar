

from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.ingrediente import ingrediente
from demo_app.models.pedido import pedido
from demo_app.models.receta import receta
from demo_app.models.cantidad import cantidad
from demo_app.models.posicion import posicion_bebidas
from demo_app.models.ingrediente import ingrediente
from flask_bcrypt import Bcrypt
import datetime
import requests
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/ingredientes', methods=['GET'])
def get_list_ingredientes():
    is_valid = True
    categoria = "ingredientes"
    mensaje = "Exitoso"
    status = 'success'
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

@app.route('/ingredientes/nombres', methods=['GET'])
def get_nombres_ingredientes():
    is_valid = True
    categoria = "ingredientes"
    mensaje = "Exitoso"
    status = 'success'
    code = 200
    data = [{'value': '','label':'Ninguna'}]

    aux_data = ingrediente.get_all()
    for ing in aux_data:
        data.append({'value': ing.nombre,'label':ing.nombre, 'cant': ing.cantidad_unitaria})
    
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
    status = 'success'
    code = 200


    data = request.json
    ingredienteNuevo = {
        # 'id_ingrediente': int(data['stockNumber']),
        'nombre': data['nombre'],
        'descripcion': data['descripcion'],
        'precio_unitario': float(data['costo']),
        'cantidad_unitaria': int(data['cantidad']),
        'categoria': data['tipo'],
        'proveedor': data['proveedor']
    }
    #validaciones para ingresar nuevo ingrediente
    
    # if ingredienteNuevo['id_ingrediente'] <= 0:
    #     is_valid = False
    #     categoria = "crear ingredientes"
    #     mensaje = "El id no puede ser 0 o menor a 0"
    #     status = 'error'
    #     code = 400
    # el
    if ingredienteNuevo['nombre'] == '':
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
            # if ingredienteNuevo['id_ingrediente'] == x.id_ingrediente:
            #     is_valid = False
            #     categoria = "crear ingredientes"
            #     mensaje = "No pueden existir ingredientes con el mismo ID"
            #     status = 'error'
            #     code = 400
            #     break
            # el
            if ingredienteNuevo['nombre'] == x.nombre:
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

    f = open('posicion.txt','r')
    id_aux = int(f.read())
    f.close()
    pos = posicion_bebidas.get_by_id({'id_posicion': id_aux})
    pos_list = pos.aslist()
    
    #obtener todos los ingredientes existentes
    ingredientes = ingrediente.get_all()

    is_valid = True
    categoria = "modificar ingredientes"
    mensaje = "Modificacion Exitosa"
    status = 'success'
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
    modIngrediente = ingrediente.get_by_name(aux_ingrediente)
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
    
    try:
        indice = pos_list.index(aux_ingrediente['id_ingrediente'])
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "No se puede editar el ingrediente si se encuentra seleccionado en el set de distribucion"
        status = 'error'
        code = 400
    except ValueError:
        print(f"El ingrediente {aux_ingrediente['id_ingrediente']} no está en la lista.")

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

    f = open('posicion.txt','r')
    id_aux = int(f.read())
    f.close()
    pos = posicion_bebidas.get_by_id({'id_posicion': id_aux})
    pos_list = pos.aslist()

    is_valid = True
    categoria = "eliminar ingredientes"
    mensaje = "Ingrediente eliminado"
    status = 'success'
    code = 200
    data = request.json
    aux_ingrediente = {
        'id_ingrediente': int(data['stockNumber'])
        
    }
    
    pedidos = pedido.get_all()
    
    if pedidos != []:
        is_valid = False
        categoria = "eliminar ingredientes"
        mensaje = "No se pueden eliminar ingredientes si hay pedidos en cola"
        status = 'error'
        code = 400
    try:
        indice = pos_list.index(aux_ingrediente['id_ingrediente'])
        is_valid = False
        categoria = "crear ingredientes"
        mensaje = "No se puede eliminar el ingrediente si se encuentra seleccionado en el set de distribucion"
        status = 'error'
        code = 400
    except ValueError:
        print(f"El ingrediente {aux_ingrediente['id_ingrediente']} no está en la lista.")

    if is_valid:
        deleteIngrediente = ingrediente.delete_by_id(aux_ingrediente)
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code 
    }
    return jsonify(value)