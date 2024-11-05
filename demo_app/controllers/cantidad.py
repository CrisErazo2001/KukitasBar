'''

'''


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from flask_bcrypt import Bcrypt
from demo_app.models.cantidad import cantidad
from demo_app.models.posicion import posicion_bebidas
from demo_app.models.ingrediente import ingrediente
import datetime
import math


@app.route('/cantidades',methods=['GET'])
def get_cantidades():

    is_valid = True
    categoria = "cantidades"
    mensaje = "Cantidades seleccionadas con exito"
    status = 'success'
    code = 200
    data = []
    f = open('posicion.txt','r')
    id_aux = int(f.read())
    f.close()
    if id_aux != 0 :
        pos = posicion_bebidas.get_by_id({'id_posicion': id_aux})
        pos_list = pos.aslist()
        cant = cantidad.get_by_id({'id_cantidad': id_aux})
        cant_aux = cant.aslist()
        cantXu = []
        for i in range(len(pos_list)):
            ing = []
            if pos_list[i] != 0:
                ing = ingrediente.get_by_id({'id_ingrediente': pos_list[i]})
            
            if ing == []:
                cantXu.append(0)
            else:
                cantXu.append(int(ing.cantidad_unitaria))

        for i in range(28):
            datosIniciales = { 'cantidadActual': cant_aux[i], 'cantidadUsada': cantXu[i]-cant_aux[i]}
            # print(datosIniciales)
            data.append(datosIniciales)
    else:
        for i in range(28):
            data.append({ 'cantidadActual': 0, 'cantidadUsada': 0})
      
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    return jsonify(value)

@app.route('/cantidad/rellenar',methods=['POST'])
def set_cantidades():

    is_valid = True
    categoria = "cantidades"
    mensaje = "Exitoso rellenar "
    status = 'success'
    code = 200
    data = request.json
    
    # print(data)
    f = open('posicion.txt','r')
    id_aux = int(f.read())
    f.close()
    pos = posicion_bebidas.get_by_id({'id_posicion': id_aux})
    pos_list = pos.aslist()
    cant = cantidad.get_by_id({'id_cantidad': id_aux})
    cant_aux = cant.asdict()
    pos_aux = int(data['pos'])

    id_aux = pos_list[pos_aux]
    ing = ingrediente.get_by_id({'id_ingrediente':id_aux})
    canXu = 0
    if ing != []:
        mensaje=mensaje+"ingrediente numero "+str(pos_aux)
        canXu = ing.cantidad_unitaria
    else:
        mensaje = "No esta rellenando ningun ingrediente"
        status = 'warning'
        code = 300
    cant_aux['cant'+str(pos_aux+1)]=canXu
    cantidad.update_by_id(cant_aux)
    
    
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    return jsonify(value)

@app.route('/cantidad/rellenar-todo',methods=['POST'])
def set_all_cantidades():

    is_valid = True
    categoria = "cantidades"
    mensaje = "Exitoso rellenar todo"
    status = 'success'
    code = 200
    data = request.json
    
    f = open('posicion.txt','r')
    id_aux = int(f.read())
    f.close()
    pos = posicion_bebidas.get_by_id({'id_posicion': id_aux})
    pos_list = pos.aslist()
    cant = cantidad.get_by_id({'id_cantidad': id_aux})
    cant_aux = cant.aslist()
    cantXu = []
    for i in range(len(pos_list)):
        ing = []
        if pos_list[i] != 0:
            ing = ingrediente.get_by_id({'id_ingrediente': pos_list[i]})
        
        if ing == []:
            cantXu.append(0)
        else:
            cantXu.append(int(ing.cantidad_unitaria))

    dict2 = {
        'id_cantidad':id_aux, 
        'cant1': cantXu[0], 
        'cant2': cantXu[1] , 
        'cant3': cantXu[2], 
        'cant4':  cantXu[3] , 
        'cant5':  cantXu[4], 
        'cant6': cantXu[5],
        'cant7': cantXu[6],
        'cant8': cantXu[7],
        'cant9': cantXu[8],
        'cant10': cantXu[9],
        'cant11': cantXu[10],
        'cant12': cantXu[11],
        'cant13': cantXu[12],
        'cant14': cantXu[13],
        'cant15': cantXu[14],
        'cant16': cantXu[15],
        'cant17': cantXu[16],
        'cant18': cantXu[17],
        'cant19': cantXu[18],
        'cant20': cantXu[19],
        'cant21': cantXu[20],
        'cant22': cantXu[21],
        'cant23': cantXu[22],
        'cant24': cantXu[23],
        'cant25': cantXu[24],
        'cant26': cantXu[25],
        'cant27': cantXu[26],
        'cant28': cantXu[27]

    }
    cantidad.update_by_id(dict2)

    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    return jsonify(value)