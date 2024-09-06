from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.cantidad_bebidas import cantidad
from demo_app.models.bebida import bebida
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/cantidad/create',methods=['POST'])
def create_cantidad():
    print("creando una lista de cantidades")
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
        'cant_25': request.form['cant_25'],
        'cant_26': request.form['cant_26'],
        'cant_27': request.form['cant_27'],
        'id_bebidas': request.form['id_bebidas']

    }
    sv_data = cantidad.get_all()
    for can in sv_data:
        if can.id_bebidas == data['id_bebida']:

            return jsonify(error=400, text='Estas repitiendo id de lista de bebidas'), 400
        

    print("Data: ", data)  
    id = cantidad.save(data)
    
    return redirect('/cantidad')

@app.route('/cantidad/get-all')
def get_all_cantidades():
       
    data = cantidad.get_all()
    bebidas = []
    for beb in data:
        bebidas.append(beb.asdict())
    print(bebidas)
    
    return jsonify(bebidas)

@app.route('/cantidad/get/id')
def get_cantidad_by_id():
    
    print(request.args)
    data = {
        'id_cantidad': request.args["id_cantidad"]
    }
    result = cantidad.get_by_id(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/cantidad/get/id_bebidas')
def get_cantidad_by_id_bebidas():
       
    data = {
        'id_bebidas': request.args["id_bebidas"]
    }
    result = cantidad.get_by_id_bebidas(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/cantidad/delete/id',methods=['POST'])
def delete_cantidad_by_id():
       
    data = {
        'id_cantidad': request.form["id_cantidad"]
    }
    result = cantidad.delete_by_id(data)
    print(result)
    return redirect('/cantidad/delete')

@app.route('/cantidad/delete/id_bebidas',methods=['POST'])
def delete_cantidad_by_id_bebidas():
       
    data = {
        'id_bebidas': request.form["id_bebidas"]
    }
    result = cantidad.delete_by_id_bebidas(data)
    print(result)
    return redirect('/cantidad/delete')

@app.route('/cantidad/modify/id',methods=['POST'])
def update_cantidad_by_id():
       
    data = {
        'id_cantidad': request.form['id_cantidad'],
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
        'cant_25': request.form['cant_25'],
        'cant_26': request.form['cant_26'],
        'cant_27': request.form['cant_27'],
        'id_bebidas': request.form['id_bebidas']
    }
    result = cantidad.update_by_id(data)
    print(result)
    return redirect('/cantidad')

@app.route('/cantidad/modify/id_bebidas',methods=['cantT'])
def update_cantidad_by_id_bebidas():
       
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
        'cant_25': request.form['cant_25'],
        'cant_26': request.form['cant_26'],
        'cant_27': request.form['cant_27'],
        'id_bebidas': request.form['id_bebidas']
    }
    result = cantidad.update_by_id_bebidas(data)
    print(result)
    return redirect('/cantidad')