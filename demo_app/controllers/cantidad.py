'''

'''


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from flask_bcrypt import Bcrypt
import datetime
import math


@app.route('/cantidades',methods=['GET'])
def get_cantidades():

    is_valid = True
    categoria = "ingredientes"
    mensaje = "Exitoso"
    status = 'ok'
    code = 200
    data = []
    for i in range(28):
        datosIniciales = { 'cantidadActual': 750, 'cantidadUsada': 0}
        data.append(datosIniciales)
      
    data[15] = { 'cantidadActual': 25, 'cantidadUsada': 0}
    data[25] = { 'cantidadActual': 35, 'cantidadUsada': 0}
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    return jsonify(value)