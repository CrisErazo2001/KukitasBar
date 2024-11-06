


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from flask_bcrypt import Bcrypt
from demo_app.models.cantidad import cantidad
from demo_app.models.posicion import posicion_bebidas
from demo_app.models.ingrediente import ingrediente
from demo_app.models.pedido import pedido
from demo_app.models.receta import receta
import datetime
import math




@app.route('/posiciones',methods=['GET'])
def get_posiciones():

    is_valid = True
    categoria = "posiciones"
    mensaje = "Exitoso"
    status = 'success'
    code = 200
    data = []

    f = open('posicion.txt','r')

    posSelected = int(f.read())

    if posSelected == 0:
        numero = ''
        data = [numero for _ in range(28)]
        nombre = ''
    else:
        pos = posicion_bebidas.get_by_id({'id_posicion': posSelected})
        nombre = pos.nombre
        aux_data = pos.aslist()
        for p in aux_data:
            if p == 0:
                data.append('')
            else:
                aux_ing = ingrediente.get_by_id({'id_ingrediente': p})
                data.append(aux_ing.nombre)
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        'data': data,
        'nombre': nombre
    }
    return jsonify(value)


@app.route('/posiciones/nombres',methods=['GET'])
def get_name_posiciones():

    is_valid = True
    categoria = "posiciones"
    mensaje = "Exitoso"
    status = 'success'
    code = 200
    data = [{'value':0 ,'label': 'Ninguno'}]
    
    distribuciones = posicion_bebidas.get_all()
    for p in distribuciones:
        data.append({'value': p.id_posicion, 'label': p.nombre})
   
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    return jsonify(value)
    

@app.route('/posicion/set',methods=['POST'])
def set_distribucion():

    is_valid = True
    categoria = "posiciones"
    mensaje = "Exitoso set distribucion"
    status = 'success'
    code = 200
    data = request.json
    
    print('data: ',data)

    f = open('posicion.txt','r')
    id_aux = f.read()
    if id_aux == '':
        id_aux = 0
    else:
        id_aux = int(id_aux)
    f.close()

    #abrir o crear un archivo de txt
    f = open('posicion.txt','w')
    if data['nombre'] == '':
        is_valid = True
        categoria = "posiciones"
        mensaje = "Para cambiar de distribucion, escoja uno nuevo en el selector o cree uno nuevo"
        status = 'info'
        code = 200

        f.write(str(id_aux))

    elif data['nombre']['value'] == 0 :
        is_valid = True
        categoria = "posiciones"
        mensaje = "No se ha seleccionado ninguna ditribucion"
        status = 'warning'
        code = 300

        f.write(str(0))
    else:
        pos = posicion_bebidas.get_by_id({'id_posicion': data['nombre']['value']})
        mensaje = "Se ha seleccionado la distribucion " + pos.nombre
        f.write(str(pos.id_posicion))


    f.close()

    
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code
    }
    return jsonify(value)

@app.route('/posicion/save-distribucion',methods=['POST'])
def save_distribucion():

    is_valid = True
    categoria = "posiciones"
    mensaje = "Exitoso guardar distribucion"
    status = 'success'
    code = 200
    data = request.json
    nombre = False
    if data['nombreSeleccionado'] == '' or data['nombreSeleccionado']['value'] == 0:
        nombre = True
    
    # print(data)
    # if nombre and data['nuevoNombre'] == '':
    #     is_valid = False
    #     categoria = "posiciones"
    #     mensaje = "Seleccione un set de distribucion o ingrese un nombre a la nueva distribucion"
    #     status = 'error'
    #     code = 400
    # el
    if data['nuevoNombre'] != '':
        posiciones = []
        cantidades = []
        distribuciones = posicion_bebidas.get_all()
        for dis in distribuciones:
            if dis.nombre == data['nuevoNombre']:
                is_valid = False
                categoria = "posiciones"
                mensaje = "No pueden existir sets de distribucion con el mismo nombre"
                status = 'error'
                code = 400
        if is_valid:
            for pos in data['posiciones']: 
                
                if pos == '':
                    posiciones.append(0)
                    cantidades.append(0)
                else:
                    aux = ingrediente.get_by_name({'nombre': pos})
                    posiciones.append(aux.id_ingrediente)
                    cantidades.append(int(aux.cantidad_unitaria))
            dict = {
                'nombre': data['nuevoNombre'], 
                'pos1': posiciones[0], 
                'pos2': posiciones[1] , 
                'pos3': posiciones[2], 
                'pos4':  posiciones[3] , 
                'pos5':  posiciones[4], 
                'pos6': posiciones[5],
                'pos7': posiciones[6],
                'pos8': posiciones[7],
                'pos9': posiciones[8],
                'pos10': posiciones[9],
                'pos11': posiciones[10],
                'pos12': posiciones[11],
                'pos13': posiciones[12],
                'pos14': posiciones[13],
                'pos15': posiciones[14],
                'pos16': posiciones[15],
                'pos17': posiciones[16],
                'pos18': posiciones[17],
                'pos19': posiciones[18],
                'pos20': posiciones[19],
                'pos21': posiciones[20],
                'pos22': posiciones[21],
                'pos23': posiciones[22],
                'pos24': posiciones[23],
                'pos25': posiciones[24],
                'pos26': posiciones[25],
                'pos27': posiciones[26],
                'pos28': posiciones[27]

            }
            
            posicion_bebidas.save(dict)
            
            distribuciones = posicion_bebidas.get_all()
            id_dist = distribuciones[len(distribuciones)-1].id_posicion
            f = open("posicion.txt",'w')
            f.write(str(id_dist))
            f.close()
            dict2 = {
                'id_cantidad':id_dist, 
                'cant1': cantidades[0], 
                'cant2': cantidades[1] , 
                'cant3': cantidades[2], 
                'cant4':  cantidades[3] , 
                'cant5':  cantidades[4], 
                'cant6': cantidades[5],
                'cant7': cantidades[6],
                'cant8': cantidades[7],
                'cant9': cantidades[8],
                'cant10': cantidades[9],
                'cant11': cantidades[10],
                'cant12': cantidades[11],
                'cant13': cantidades[12],
                'cant14': cantidades[13],
                'cant15': cantidades[14],
                'cant16': cantidades[15],
                'cant17': cantidades[16],
                'cant18': cantidades[17],
                'cant19': cantidades[18],
                'cant20': cantidades[19],
                'cant21': cantidades[20],
                'cant22': cantidades[21],
                'cant23': cantidades[22],
                'cant24': cantidades[23],
                'cant25': cantidades[24],
                'cant26': cantidades[25],
                'cant27': cantidades[26],
                'cant28': cantidades[27]

            }
            cantidad.save(dict2)

    else:
        f = open('posicion.txt','r')
        posicionActualizar = int(f.read())
        pos_aux = posicion_bebidas.get_by_id({'id_posicion':posicionActualizar})

        posiciones = []
        cantidades = []
        for pos in data['posiciones']:
                        
            if pos == '':
                posiciones.append(0)
                cantidades.append(0)
            else:
                aux = ingrediente.get_by_name({'nombre': pos})
                posiciones.append(aux.id_ingrediente)
                cantidades.append(int(aux.cantidad_unitaria))
        print('cant 28: ',cantidades[27])
        dict = {
            'id_posicion': posicionActualizar,
            'pos1': posiciones[0], 
            'pos2': posiciones[1] , 
            'pos3': posiciones[2], 
            'pos4':  posiciones[3] , 
            'pos5':  posiciones[4], 
            'pos6': posiciones[5],
            'pos7': posiciones[6],
            'pos8': posiciones[7],
            'pos9': posiciones[8],
            'pos10': posiciones[9],
            'pos11': posiciones[10],
            'pos12': posiciones[11],
            'pos13': posiciones[12],
            'pos14': posiciones[13],
            'pos15': posiciones[14],
            'pos16': posiciones[15],
            'pos17': posiciones[16],
            'pos18': posiciones[17],
            'pos19': posiciones[18],
            'pos20': posiciones[19],
            'pos21': posiciones[20],
            'pos22': posiciones[21],
            'pos23': posiciones[22],
            'pos24': posiciones[23],
            'pos25': posiciones[24],
            'pos26': posiciones[25],
            'pos27': posiciones[26],
            'pos28': posiciones[27]

        }
        
        posicion_bebidas.update_by_id(dict)
        
        
        f = open("posicion.txt",'w')
        f.write(str(posicionActualizar))
        f.close()
        dict2 = {
            'id_cantidad':posicionActualizar, 
            'cant1': cantidades[0], 
            'cant2': cantidades[1] , 
            'cant3': cantidades[2], 
            'cant4':  cantidades[3] , 
            'cant5':  cantidades[4], 
            'cant6': cantidades[5],
            'cant7': cantidades[6],
            'cant8': cantidades[7],
            'cant9': cantidades[8],
            'cant10': cantidades[9],
            'cant11': cantidades[10],
            'cant12': cantidades[11],
            'cant13': cantidades[12],
            'cant14': cantidades[13],
            'cant15': cantidades[14],
            'cant16': cantidades[15],
            'cant17': cantidades[16],
            'cant18': cantidades[17],
            'cant19': cantidades[18],
            'cant20': cantidades[19],
            'cant21': cantidades[20],
            'cant22': cantidades[21],
            'cant23': cantidades[22],
            'cant24': cantidades[23],
            'cant25': cantidades[24],
            'cant26': cantidades[25],
            'cant27': cantidades[26],
            'cant28': cantidades[27]

        }
        cantidad.update_by_id(dict2)
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code
    }
    return jsonify(value)

@app.route('/posicion/borrar',methods=['POST'])
def delete_distribucion():

    is_valid = True
    categoria = "posiciones"
    mensaje = "Exitoso borrar todo"
    status = 'success'
    code = 200
    data = request.json
    
    f = open('posicion.txt','r')
    id_aux = int(f.read())
    f.close()
    posicion_bebidas.delete_by_id({'id_posicion': id_aux})

    cantidad.delete_by_id({'id_cantidad': id_aux})
    f = open('posicion.txt','w')
    f.write(str(0))
    f.close()
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    return jsonify(value)


