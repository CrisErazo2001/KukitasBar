from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.receta import receta
from demo_app.models.posicion_bebidas import bebida
from flask_bcrypt import Bcrypt
from datetime import datetime
import requests
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/receta/create',methods=['POST'])
def create_receta():
    print("creando una receta")
    # url1 = 'http://127.0.0.1:5000/bebida/define/get'
    # r1 = requests.get(url1)
    # result1 = r1.json()
    
    # result = bebida.get_by_id(result1['bebida_list_id'])
    # dict = result.asdict()
    # pos = list(dict.keys())
    # values = list(dict.values())
    if request.form["bebida_1"] != '':
        bebida_1=request.form["bebida_1"]
    else:
        bebida_1=0

    if request.form["bebida_2"] != '':
        bebida_2=request.form["bebida_2"]
    else:
        bebida_2=0
    if request.form["bebida_3"] != '':
        bebida_3=request.form["bebida_3"]
    else:
        bebida_3=0
    if request.form["bebida_4"] != '':
        bebida_4=request.form["bebida_4"]
    else:
        bebida_4=0
    if request.form["bebida_5"] != '':
        bebida_5=request.form["bebida_5"]
    else:
        bebida_5=0
    if request.form["bebida_6"] != '':
        bebida_6=request.form["bebida_6"]
    else:
        bebida_6=0
    if request.form["bebida_7"] != '':
        bebida_7=request.form["bebida_7"]
    else:
        bebida_7=0
    if request.form["bebida_8"] != '':
        bebida_8=request.form["bebida_8"]
    else:
        bebida_8=0
    if request.form["bebida_9"] != '':
        bebida_9=request.form["bebida_9"]
    else:
        bebida_9=0
    if request.form["bebida_10"] != '':
        bebida_10=request.form["bebida_10"]
    else:
        bebida_10=0
    if request.form["cant_1"] != '':
        cant_1=request.form["cant_1"]
    else:
        cant_1=0

    if request.form["cant_2"] != '':
        cant_2=request.form["cant_2"]
    else:
        cant_2=0
    if request.form["cant_3"] != '':
        cant_3=request.form["cant_3"]
    else:
        cant_3=0
    if request.form["cant_4"] != '':
        cant_4=request.form["cant_4"]
    else:
        cant_4=0
    if request.form["cant_5"] != '':
        cant_5=request.form["cant_5"]
    else:
        cant_5=0
    if request.form["cant_6"] != '':
        cant_6=request.form["cant_6"]
    else:
        cant_6=0
    if request.form["cant_7"] != '':
        cant_7=request.form["cant_7"]
    else:
        cant_7=0
    if request.form["cant_8"] != '':
        cant_8=request.form["cant_8"]
    else:
        cant_8=0
    if request.form["cant_9"] != '':
        cant_9=request.form["cant_9"]
    else:
        cant_9=0
    if request.form["cant_10"] != '':
        cant_10=request.form["cant_10"]
    else:
        cant_10=0

    data = {
            
            'id_bebidas': request.form['id_bebidas'], 
            'nombre':request.form["nombre"], 
            'bebida_1': bebida_1,
            'bebida_2': bebida_2, 
            'bebida_3': bebida_3,
            'bebida_4': bebida_4, 
            'bebida_5':  bebida_5, 
            'bebida_6': bebida_6,
            'bebida_7': bebida_7,
            'bebida_8': bebida_8,
            'bebida_9': bebida_9,
            'bebida_10': bebida_10,
            'cant_1': cant_1, 
            'cant_2': cant_2, 
            'cant_3': cant_3,
            'cant_4':  cant_4, 
            'cant_5':  cant_5, 
            'cant_6': cant_6,
            'cant_7': cant_7,
            'cant_8': cant_8,
            'cant_9': cant_9,
            'cant_10': cant_10,
            'tiempo_prep': request.form["tiempo_prep"]
            
        }
          

    print("Data: ", data)  
    id = receta.save(data)
    
    return redirect('/bebida#tab2')

@app.route('/receta/get-all')
def get_all_recetas():
       
    data = receta.get_all()
    recetas = []
    for rec in data:
        recetas.append(rec.asdict())
    print(recetas)
    
    return jsonify(recetas)



@app.route('/receta/get/id')
def get_receta_by_id():
    
    print(request.args)
    data = {
        'id_receta': request.args["id_receta"]
    }
    result = receta.get_by_id(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/receta/get/id_bebidas')
def get_receta_by_id_bebidas():
       
    data = {
        'id_bebidas': request.args["id_bebidas"]
    }
    result = receta.get_by_id_bebidas(data)
    recetas = []
    for rec in result:
        recetas.append(rec.asdict())
    print(recetas)
    
    return jsonify(recetas)

@app.route('/receta/delete/id',methods=['POST'])
def delete_receta_by_id():
       
    data = {
        'id_receta': request.form["id_receta"]
    }
    result = receta.delete_by_id(data)
    print(result)
    return redirect('/receta/delete')

@app.route('/receta/delete/id_bebidas',methods=['POST'])
def delete_receta_by_id_bebidas():
       
    data = {
        'id_bebidas': request.form["id_bebidas"]
    }
    result = receta.delete_by_id_bebidas(data)
    print(result)
    return redirect('/receta/delete')

@app.route('/receta/modify/id',methods=['POST'])
def update_receta_by_id():

    date_str = request.form["tiempo_prep"]
    date_format = '%M:%S'

    date_obj = datetime.strptime(date_str, date_format)
       
    data = {
            
            'id_bebidas': request.form['bebida_list_id'], 
            'nombre':request.form["nombre"], 
            'bebida_1': request.form["bebida_1"],
            'bebida_2': request.form["bebida_2"], 
            'bebida_3': request.form["bebida_3"],
            'bebida_4': request.form["bebida_4"], 
            'bebida_5':  request.form["bebida_5"], 
            'bebida_6': request.form["bebida_6"],
            'bebida_7': request.form["bebida_7"],
            'bebida_8': request.form["bebida_8"],
            'bebida_9': request.form["bebida_9"],
            'bebida_10': request.form["bebida_10"],
            'cant_1': request.form["cant_1"], 
            'cant_2': request.form["cant_2"], 
            'cant_3': request.form["cant_3"],
            'cant_4':  request.form["cant_4"], 
            'cant_5':  request.form["cant_5"], 
            'cant_6': request.form["cant_6"],
            'cant_7': request.form["cant_7"],
            'cant_8': request.form["cant_8"],
            'cant_9': request.form["cant_9"],
            'cant_10': request.form["cant_10"],
            'tiempo_prep': date_obj
            
        }
    result = receta.update_by_id(data)
    print(result)
    return redirect('/receta')


@app.route('/receta/send/<id>')
def send_receta(id):
    data = {'id_receta': int(id)}
    response = receta.get_by_id(data)
    response = response.pasos_receta()

    return jsonify(response)


