from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.cantidad_bebidas import cantidad
from demo_app.models.posicion_bebidas import posicion_bebidas
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/cantidad/create',methods=['POST'])
def create_cantidad():
    print("creando una lista de cantidades")
    data = {
        'nombre': request.form["nombre"]
    }
    beb = posicion_bebidas.get_by_name(data)

    data = {
        'cant_1': request.form["cant_1"],
        'cant_2': request.form["cant_2"],
        'cant_3': request.form['cant_3'],
        'cant_4': request.form['cant_4'],
        'cant_5': request.form['cant_5'],
        'cant_6': request.form['cant_6'],
        'cant_7': request.form['cant_7'],
        'cant_8': request.form['cant_8'],
        'cant_9': request.form['cant_9'],
        'cant_10': request.form['cant_10'],
        'cant_11': request.form['cant_11'],
        'cant_12': request.form['cant_12'],
        'cant_13': request.form['cant_13'],
        'cant_14': request.form['cant_14'],
        'cant_15': request.form['cant_15'],
        'cant_16': request.form['cant_16'],
        'cant_17': request.form['cant_17'],
        'cant_18': request.form['cant_18'],
        'cant_19': request.form['cant_19'],
        'cant_20': request.form['cant_20'],
        'cant_21': request.form['cant_21'],
        'cant_22': request.form['cant_22'],
        'cant_23': request.form['cant_23'],
        'cant_24': request.form['cant_24'],
        'cant_25': 0,
        'cant_26': 0,
        'cant_27': 0,
        'id_bebidas' : beb.id_posicion_bebidas
        

    }
    sv_data = cantidad.get_all()
    for can in sv_data:
        if can.id_bebidas == data['id_bebidas']:
            return jsonify(error=400, text='Estas repitiendo id de lista de bebidas'), 400
        

    print("Data: ", data)  
    id = cantidad.save(data)
    
    return redirect('/bebida#tab3')

