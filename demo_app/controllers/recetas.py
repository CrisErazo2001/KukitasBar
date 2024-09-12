from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.receta import receta
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.cantidad_bebidas import cantidad
from flask_bcrypt import Bcrypt
from datetime import datetime
import requests
import asyncio
from websockets.sync.client import connect

def webSocket_connection():
    with connect("ws://192.168.0.241:1880/ws/receta") as websocket:
        
        websocket.send('1')
        

receta_envio={}

@app.route('/receta/create',methods=['POST'])
def create_receta():
    print("creando una receta")
    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    print(bebidas_id)
    if bebidas_id == '' or bebidas_id == '0':
        bebidas_id = 0
    else:
        bebidas_id = int(bebidas_id)
    cantidades = []
    for i in range(10):
        y = 'cant_'+str(i+1)
        x = request.form[y]
        if x =='':
            cantidades.append(0)
        else:
            cantidades.append(x)

    data = {
            
            'id_lista_bebidas': bebidas_id, 
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
            'cant_1': cantidades[0], 
            'cant_2': cantidades[1], 
            'cant_3': cantidades[2],
            'cant_4':  cantidades[3], 
            'cant_5':  cantidades[4], 
            'cant_6': cantidades[5],
            'cant_7': cantidades[6],
            'cant_8': cantidades[7],
            'cant_9': cantidades[8],
            'cant_10': cantidades[9],
            'tiempo_prep': request.form["tiempo_prep"]
            
        }

    data2 = {
        'nombre': data['nombre']
    }
    search = receta.get_by_name(data2)
    for rec in search:
        if rec.id_lista_bebidas == bebidas_id:
            return jsonify(error=400, text='Estas repitiendo nombre para esta lista de bebidas'), 400
        else:
            continue

    print("Data: ", data)  

    receta.save(data)
    
    return redirect('/bebida#tab3')

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

@app.route('/receta/get/id_lista_bebidas')
def get_receta_by_id_lista_bebidas():
       
    data = {
        'id_lista_bebidas': request.args["id_lista_bebidas"]
    }
    result = receta.get_by_id_lista_bebidas(data)
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

@app.route('/receta/delete/id_lista_bebidas',methods=['POST'])
def delete_receta_by_id_lista_bebidas():
       
    data = {
        'id_lista_bebidas': request.form["id_lista_bebidas"]
    }
    result = receta.delete_by_id_lista_bebidas(data)
    print(result)
    return redirect('/receta/delete')

@app.route('/receta/modify/id',methods=['POST'])
def update_receta_by_id():

    date_str = request.form["tiempo_prep"]
    date_format = '%M:%S'

    date_obj = datetime.strptime(date_str, date_format)
       
    data = {
            
            'id_lista_bebidas': request.form['id_lista_bebidas'], 
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


@app.route('/receta/send')
def send_receta():
    global receta_envio

    return jsonify(receta_envio)

@app.route('/receta/generar-posiciones',methods=['POST'])
def generar_posicion_receta():
    global receta_envio
    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    if bebidas_id == '' or bebidas_id == '0':
            bebidas_id = 0
    else:
        bebidas_id = int(bebidas_id)
    
    data = {
        'nombre': request.form['nombre']
    }
    print(data)
    data2 = {
        'id_lista_bebidas': bebidas_id
    }
    search = receta.get_by_name(data)
    
    for rec in search:
        if rec.id_lista_bebidas == bebidas_id:
            result = rec.asdict()
        else:
            continue

    search2 = posicion_bebidas.get_by_id_lista_bebidas(data2)
    data3 = {
        'id_posicion_bebidas': search2.id_posicion_bebidas
    }
    # search3 = cantidad.get_by_id_posicion_bebidas(data3)
    search2 = search2.aslist()
    # search3 = search3.aslist()
    posiciones = []
    cantidades = []
    for i in range(10):
        x = 'bebida_'+str(i+1)
        y = 'cant_'+str(i+1)
        if result[x] == '':
            posiciones.append(0)
            cantidades.append(0)
            continue
        posiciones.append(search2.index(result[x]))
        cantidades.append(result[y])
    f.close()
    print('posiciones: ', posiciones)
    print('cantidades ', cantidades)

    receta_envio = {
        'posiciones': posiciones,
        'cantidades': cantidades
    }

    webSocket_connection()



    return redirect('/bebida#tab3')



