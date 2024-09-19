from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.receta import receta
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.cantidad_bebidas import cantidad
from demo_app.models.pedido import pedido
from flask_bcrypt import Bcrypt
from datetime import datetime
import requests
import asyncio
from websockets.sync.client import connect

receta_envio={}
aux_id_cantidades = 0

def reducir_cantidades(dic,id_cantidad):
    solicitud = {
        'id_cantidad': id_cantidad
    }
    search = cantidad.get_by_id(solicitud)
    cantidaddes_lista = [search.cant_1,search.cant_2,search.cant_3,search.cant_4,search.cant_5,search.cant_6,search.cant_7,search.cant_8,search.cant_9,search.cant_10,search.cant_11,search.cant_12,search.cant_13,search.cant_14,search.cant_15,search.cant_16,search.cant_17,search.cant_18,search.cant_19,search.cant_20,search.cant_21,search.cant_22,search.cant_23,search.cant_24,search.cant_25,search.cant_26,search.cant_27,search.id_posicion_bebidas]
    for i in range(10):
        cantidades = dic['cantidades']
        posiciones = dic['posiciones']
        if cantidades[i] > 0:
            aux = posiciones[i]
            cantidaddes_lista[aux-1] = cantidaddes_lista[aux-1]-cantidades[i]

    data = {
        'id_cantidad': id_cantidad,
        'cant_1': cantidaddes_lista[0],
        'cant_2': cantidaddes_lista[1],
        'cant_3': cantidaddes_lista[2],
        'cant_4': cantidaddes_lista[3],
        'cant_5': cantidaddes_lista[4],
        'cant_6': cantidaddes_lista[5],
        'cant_7': cantidaddes_lista[6],
        'cant_8': cantidaddes_lista[7],
        'cant_9': cantidaddes_lista[8],
        'cant_10': cantidaddes_lista[9],
        'cant_11': cantidaddes_lista[10],
        'cant_12': cantidaddes_lista[11],
        'cant_13': cantidaddes_lista[12],
        'cant_14': cantidaddes_lista[13],
        'cant_15': cantidaddes_lista[14],
        'cant_16': cantidaddes_lista[15],
        'cant_17': cantidaddes_lista[16],
        'cant_18': cantidaddes_lista[17],
        'cant_19': cantidaddes_lista[18],
        'cant_20': cantidaddes_lista[19],
        'cant_21': cantidaddes_lista[20],
        'cant_22': cantidaddes_lista[21],
        'cant_23': cantidaddes_lista[22],
        'cant_24': cantidaddes_lista[23],
        'cant_25': cantidaddes_lista[24],
        'cant_26': cantidaddes_lista[25],
        'cant_27': cantidaddes_lista[26],
        'id_posicion_bebidas': cantidaddes_lista[27]
    }
    cantidad.update_by_id(data)


def generar_posicion_receta(id_receta):
    
    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    if bebidas_id == '' or bebidas_id == '0':
            bebidas_id = 0
    else:
        bebidas_id = int(bebidas_id)
    
    data_pbeb = {
        'id_lista_bebidas': bebidas_id
    }

    pedidos = pedido.get_all()

    data_bebida = {
        'id_receta' : pedidos[0].id_receta
    }

    bebida = receta.get_by_id(data_bebida)

    pbeb = posicion_bebidas.get_by_id_lista_bebidas(data_pbeb)

    data_cant = {
        'id_posicion_bebidas': pbeb.id_posicion_bebidas
    }

    cant = cantidad.get_by_id_posicion_bebidas(data_cant)
    id_cantidades = cant.id_cantidad
    bebida = bebida.asdict()
    pbeb = pbeb.aslist()
    cant = cant.asdict()
    
    posiciones = []
    cantidades = []
    aux = pbeb
    for i in range(10):
        x = 'bebida_'+str(i+1)
        y = 'cant_'+str(i+1)
        
        
        pos = aux.index(bebida[x])
        c = bebida[y]
        z = 'cant_'+str(pos)
        

        while c > cant[z]:
            print('c: ',c)
            print('cant[z]: ',cant[z])
            aux[pos] = 'Siguiente'
            pos = aux.index(bebida[x])
            z = 'cant_'+str(pos)
        print('aux: ',aux)

        if bebida[x] == '':
            posiciones.append(0)
            cantidades.append(0)
        else:
            posiciones.append(pos)
            cantidades.append(c)


    receta_envio = {
        'posiciones': posiciones,
        'cantidades': cantidades
    }

    



    return receta_envio,id_cantidades


def webSocket_connection():
    with connect("ws://192.168.0.241:1880/ws/receta") as websocket:
        
        websocket.send('1')
        



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

@app.route('/receta/terminada')
def fin_receta():
    global receta_envio
    global aux_id_cantidades
    result = pedido.get_all()
    if result == []:
        return jsonify('No hay pedidos en lista')
    # result = result[::-1]
    print(result[0].id_pedidos)
    data = {
        'id_pedidos': result[0].id_pedidos
    }
    pedido.delete_by_id(data)
    reducir_cantidades(receta_envio,aux_id_cantidades)
    return redirect('/receta/send')
    # webSocket_connection()
    # return 200


@app.route('/receta/send')
def send_receta():
    global receta_envio
    global aux_id_cantidades
    pedidos = pedido.get_all()
    if pedidos == []:
        return jsonify('No hay pedidos en lista')
    receta_envio, aux_id_cantidades = generar_posicion_receta(pedidos[0].id_pedidos)

    return jsonify(receta_envio)





