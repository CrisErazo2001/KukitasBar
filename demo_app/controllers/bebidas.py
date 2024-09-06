from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.bebida import bebida
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/bebida/create',methods=['POST'])
def create_bebida():
    print("creando una lista de bebidas")
    data = {
        'Pos_1': request.form["Pos_1"],
        'Pos_2': request.form["Pos_2"],
        'Pos_3': request.form['Pos_3'],
        'Pos_4': request.form['Pos_4'],
        'Pos_5': request.form['Pos_5'],
        'Pos_6': request.form['Pos_6'],
        'Pos_7': request.form['Pos_7'],
        'Pos_8': request.form['Pos_8'],
        'Pos_9': request.form['Pos_9'],
        'Pos_10': request.form['Pos_10'],
        'Pos_11': request.form['Pos_11'],
        'Pos_12': request.form['Pos_12'],
        'Pos_13': request.form['Pos_13'],
        'Pos_14': request.form['Pos_14'],
        'Pos_15': request.form['Pos_15'],
        'Pos_16': request.form['Pos_16'],
        'Pos_17': request.form['Pos_17'],
        'Pos_18': request.form['Pos_18'],
        'Pos_19': request.form['Pos_19'],
        'Pos_20': request.form['Pos_20'],
        'Pos_21': request.form['Pos_21'],
        'Pos_22': request.form['Pos_22'],
        'Pos_23': request.form['Pos_23'],
        'Pos_24': request.form['Pos_24'],
        'Pos_25': request.form['Pos_25'],
        'Pos_26': request.form['Pos_26'],
        'Pos_27': request.form['Pos_27'],
        'nombre': request.form['nombre']

    }
    print("Data: ", data)  
    id = bebida.save(data)
    
    return redirect('/bebida')

@app.route('/bebida/get-all')
def get_all_bebidas():
       
    data = bebida.get_all()
    bebidas = []
    for beb in data:
        bebidas.append(beb.asdict())
    print(bebidas)
    
    return jsonify(bebidas)

@app.route('/bebida/get/id')
def get_bebida_by_id():
    
    print(request.args)
    data = {
        'id_bebidas': request.args["id_bebidas"]
    }
    result = bebida.get_by_id(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/bebida/get/name')
def get_bebida_by_name():
       
    data = {
        'nombre': request.args["nombre"]
    }
    result = bebida.get_by_name(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/bebida/delete/id',methods=['POST'])
def delete_bebida_by_id():
       
    data = {
        'id_bebidas': request.form["id_bebidas"]
    }
    result = bebida.delete_by_id(data)
    print(result)
    return redirect('/bebida/delete')

@app.route('/bebida/delete/name',methods=['POST'])
def delete_bebida_by_name():
       
    data = {
        'nombre': request.form["nombre"]
    }
    result = bebida.delete_by_name(data)
    print(result)
    return redirect('/bebida/delete')

@app.route('/bebida/modify/id',methods=['POST'])
def update_bebida_by_id():
       
    data = {
        'id_bebidas': request.form['id_bebidas'],
        'Pos_1': request.form["Pos_1"],
        'Pos_2': request.form["Pos_2"],
        'Pos_3': request.form['Pos_3'],
        'Pos_4': request.form['Pos_4'],
        'Pos_5': request.form['Pos_5'],
        'Pos_6': request.form['Pos_6'],
        'Pos_7': request.form['Pos_7'],
        'Pos_8': request.form['Pos_8'],
        'Pos_9': request.form['Pos_9'],
        'Pos_10': request.form['Pos_10'],
        'Pos_11': request.form['Pos_11'],
        'Pos_12': request.form['Pos_12'],
        'Pos_13': request.form['Pos_13'],
        'Pos_14': request.form['Pos_14'],
        'Pos_15': request.form['Pos_15'],
        'Pos_16': request.form['Pos_16'],
        'Pos_17': request.form['Pos_17'],
        'Pos_18': request.form['Pos_18'],
        'Pos_19': request.form['Pos_19'],
        'Pos_20': request.form['Pos_20'],
        'Pos_21': request.form['Pos_21'],
        'Pos_22': request.form['Pos_22'],
        'Pos_23': request.form['Pos_23'],
        'Pos_24': request.form['Pos_24'],
        'Pos_25': request.form['Pos_25'],
        'Pos_26': request.form['Pos_26'],
        'Pos_27': request.form['Pos_27'],
        'nombre': request.form['nombre']
    }
    result = bebida.update_by_id(data)
    print(result)
    return redirect('/bebida')

@app.route('/bebida/modify/name',methods=['POST'])
def update_bebida_by_name():
       
    data = {
        
        'Pos_1': request.form["Pos_1"],
        'Pos_2': request.form["Pos_2"],
        'Pos_3': request.form['Pos_3'],
        'Pos_4': request.form['Pos_4'],
        'Pos_5': request.form['Pos_5'],
        'Pos_6': request.form['Pos_6'],
        'Pos_7': request.form['Pos_7'],
        'Pos_8': request.form['Pos_8'],
        'Pos_9': request.form['Pos_9'],
        'Pos_10': request.form['Pos_10'],
        'Pos_11': request.form['Pos_11'],
        'Pos_12': request.form['Pos_12'],
        'Pos_13': request.form['Pos_13'],
        'Pos_14': request.form['Pos_14'],
        'Pos_15': request.form['Pos_15'],
        'Pos_16': request.form['Pos_16'],
        'Pos_17': request.form['Pos_17'],
        'Pos_18': request.form['Pos_18'],
        'Pos_19': request.form['Pos_19'],
        'Pos_20': request.form['Pos_20'],
        'Pos_21': request.form['Pos_21'],
        'Pos_22': request.form['Pos_22'],
        'Pos_23': request.form['Pos_23'],
        'Pos_24': request.form['Pos_24'],
        'Pos_25': request.form['Pos_25'],
        'Pos_26': request.form['Pos_26'],
        'Pos_27': request.form['Pos_27'],
        'nombre': request.form['nombre']
    }
    result = bebida.update_by_name(data)
    print(result)
    return redirect('/bebida')