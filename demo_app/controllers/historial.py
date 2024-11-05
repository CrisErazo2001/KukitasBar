
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



@app.route('/historial', methods=['GET'])
def get_historial():
    is_valid = True
    categoria = "historial"
    mensaje = "Historial recuperado con exito"
    status = 'success'
    code = 200
    data = []
    
    historial = historico_pedido.get_all()

    for i in historial:
        data.append(i.asdict())


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


@app.route('/historial/eliminar', methods=['GET'])
def delete_historial():
    is_valid = True
    categoria = "historial"
    mensaje = "Historial eliminado con exito"
    status = 'success'
    code = 200
    
    historial = historico_pedido.delete_all()

 
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code

    }
    return jsonify(value)