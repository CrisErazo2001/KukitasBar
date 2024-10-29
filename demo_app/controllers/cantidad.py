'''

Este script contiente la ruta /bebida/posicion/create que crea tanto las posicion de las bebidas en el soporte y la cantidad en onzas
de cada botella. Tambien permite la modificacion de cada uno. Cuenta con las validaciones repectivas para no ingresar letras donde van
numeros, ingresar la cantidad de botellas minimas y no poder ingresar 0 en cantidades.

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
    for i in range(24):
        datosIniciales = { 'cantidadActual': 750, 'cantidadUsada': 0}
        data.append(datosIniciales)
      
        
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    return jsonify(value)