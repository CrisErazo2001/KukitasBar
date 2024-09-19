from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.cantidad_bebidas import cantidad
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

bebidas_id = 0

@app.route('/bebida/posicion/create',methods=['POST'])
def create_bebida_pos():
    print("creando una lista de bebidas")
    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    print(bebidas_id)
    if bebidas_id == '' or bebidas_id == '0':
        bebidas_id = 0
    else:
        bebidas_id = int(bebidas_id)
    
    posiciones = []
    cantidades = []
    for i in range(24):
        aux_pos = 'Pos_'+str(i+1)
        aux_cant = 'cant_'+str(i+1)
        aux_list_pos = request.form[aux_pos]
        aux_list_cant = request.form[aux_cant]
        if aux_list_pos != '' and aux_list_cant != '':
            if not aux_list_cant.isnumeric():
                return jsonify(error=400, text='Tu cantidad no es un numero'), 400
            elif aux_list_cant == '0':
                return jsonify(error=400, text='Tu cantidad no puede ser 0'), 400
            else:
                posiciones.append(aux_list_pos) 
                cantidades.append(aux_list_cant)
        elif aux_list_pos == '' and aux_list_cant == '':
            posiciones.append('') 
            cantidades.append(0)
        elif aux_list_pos != '' and aux_list_cant == '':
            return jsonify(error=400, text='Tienes una bebida sin cantidad'), 400
        elif aux_list_pos == '' and aux_list_cant != '':
            return jsonify(error=400, text='Tienes una cantidad sin bebida'), 400
        
    data1 = {
        'Pos_1': posiciones[0],
        'Pos_2': posiciones[1],
        'Pos_3': posiciones[2],
        'Pos_4': posiciones[3],
        'Pos_5': posiciones[4],
        'Pos_6': posiciones[5],
        'Pos_7': posiciones[6],
        'Pos_8': posiciones[7],
        'Pos_9': posiciones[8],
        'Pos_10': posiciones[9],
        'Pos_11': posiciones[10],
        'Pos_12': posiciones[11],
        'Pos_13': posiciones[12],
        'Pos_14': posiciones[13],
        'Pos_15': posiciones[14],
        'Pos_16': posiciones[15],
        'Pos_17': posiciones[16],
        'Pos_18': posiciones[17],
        'Pos_19': posiciones[18],
        'Pos_20': posiciones[19],
        'Pos_21': posiciones[20],
        'Pos_22': posiciones[21],
        'Pos_23': posiciones[22],
        'Pos_24': posiciones[23],
        'Pos_25': '',
        'Pos_26': '',
        'Pos_27': '',
        'nombre': '',
        'id_lista_bebidas': bebidas_id

    }
    
    sv_data = posicion_bebidas.get_all()
    for beb in sv_data:
        if beb.id_lista_bebidas == data1['id_lista_bebidas']:
            return jsonify(error=400, text='Estas repitiendo id_lista_bebidas'), 400
        else: 
            continue
    
    posicion_bebidas.save(data1)

    id = posicion_bebidas.get_all()
    id = id[len(id)-1]


    data2 = {
        'cant_1': cantidades[0],
        'cant_2': cantidades[1],
        'cant_3': cantidades[2],
        'cant_4': cantidades[3],
        'cant_5': cantidades[4],
        'cant_6': cantidades[5],
        'cant_7': cantidades[6],
        'cant_8': cantidades[7],
        'cant_9': cantidades[8],
        'cant_10': cantidades[9],
        'cant_11': cantidades[10],
        'cant_12': cantidades[11],
        'cant_13': cantidades[12],
        'cant_14': cantidades[13],
        'cant_15': cantidades[14],
        'cant_16': cantidades[15],
        'cant_17': cantidades[16],
        'cant_18': cantidades[17],
        'cant_19': cantidades[18],
        'cant_20': cantidades[19],
        'cant_21': cantidades[20],
        'cant_22': cantidades[21],
        'cant_23': cantidades[22],
        'cant_24': cantidades[23],
        'cant_25': 0,
        'cant_26': 0,
        'cant_27': 0,
        'id_posicion_bebidas' : id.id_posicion_bebidas
        
    }
    
    sv_data2 = cantidad.get_all()
    for cant in sv_data2:
        if cant.id_posicion_bebidas == data2['id_posicion_bebidas']:
            return jsonify(error=400, text='Estas repitiendo id_posicion_bebidas'), 400
        else: 
            continue
    cantidad.save(data2)
    f.close()
    return redirect('/bebida')

@app.route('/bebida/posicion/get-all')
def get_all_bebidas_pos():
       
    data = posicion_bebidas.get_all()
    bebidas = []
    for beb in data:
        bebidas.append(beb.asdict())
    print(bebidas)
    
    return jsonify(bebidas)

@app.route('/bebida/posicion/get/id')
def get_bebida_by_id_pos():
    
    print(request.args)
    data = {
        'id_posicion_bebidas': request.args["id_posicion_bebidas"]
    }
    result = posicion_bebidas.get_by_id(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/bebida/posicion/get/name')
def get_bebida_by_name_pos():
       
    data = {
        'nombre': request.args["nombre"]
    }
    result = posicion_bebidas.get_by_name(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/bebida/posicion/delete/id',methods=['POST'])
def delete_bebida_by_id_pos():
       
    data = {
        'id_posicion_bebidas': request.form["id_posicion_bebidas"]
    }
    result = posicion_bebidas.delete_by_id(data)
    print(result)
    return redirect('/bebida/posicion/delete')

@app.route('/bebida/posicion/delete/name',methods=['POST'])
def delete_bebida_by_name_pos():
       
    data = {
        'nombre': request.form["nombre"]
    }
    result = posicion_bebidas.delete_by_name(data)
    print(result)
    return redirect('/bebida/posicion/delete')

@app.route('/bebida/posicion/modify/id',methods=['POST'])
def update_bebida_by_id_pos():
       
    data = {
        'id_posicion_bebidas': request.form['id_posicion_bebidas'],
        'id_lista_bebidas': request.form['id_lista_bebidas'],
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
    result = posicion_bebidas.update_by_id(data)
    print(result)
    return redirect('/bebida')

@app.route('/bebida/posicion/modify/name',methods=['POST'])
def update_bebida_by_name_pos():
       
    data = {
        'id_lista_bebidas': request.form['id_lista_bebidas'],
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
    result = posicion_bebidas.update_by_name(data)
    print(result)
    return redirect('/bebida')

