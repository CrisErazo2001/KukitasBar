
from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.pedido import pedido
from demo_app.models.receta import receta
from demo_app.models.historico_pedido import historico_pedido
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta

import requests
import asyncio
from websockets.sync.client import connect



@app.route('/')
def home():
    recetas = []    
    aux_data = receta.get_all()
    print(aux_data)
    
    for rec in aux_data:
        aux = rec.asdict_front()
        ingredientes = '' 
        for ing in aux['ingredientes']:
            ingredientes = ingredientes + ' ' + ing['nombre']
        aux['ingredientes'] = ingredientes
        recetas.append(aux)

      
    
    return render_template('restaurant.html', recetas = recetas)

@app.route('/pedido/nuevo', methods=['POST'])
def crear_pedido():
    is_valid = True
    categoria = "crear recetas"
    mensaje = "Receta Creada con exito"
    status = 'ok'
    code = 200
    data = request.form
    searchReceta = {
        'nombre': data['nombre_bebida']
    }
    recetaSelected = receta.get_by_name(searchReceta)


    #validar si se pidio la bebida con hielo
    try:
        if data['hielo'] == 'on':
            hielo = 1  
    except :
        hielo = 0 
    
    #ver cuantos pedidos estan en cola para hacer calculo del tiempo
    pedidos = pedido.get_all()
    tiempo = recetaSelected.tiempo_prep
    
    for ped in pedidos:
        auxReceta = receta.get_by_id({'id_receta': ped.id_receta})
        tiempo = tiempo + auxReceta.tiempo_prep

    print()
    
    dict = {
     
        'nombre_cliente': data['nombre_cliente'],  
        'id_receta': recetaSelected.id_receta, 
        'ready_at': datetime.now() + timedelta(minutes=tiempo),
        'status': 0,
        'hielo': hielo

    }

    pedido.save(dict)

    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code

    }
    return redirect('/')