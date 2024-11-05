'''

Este script contiente la ruta /bebida/posicion/create que crea tanto las posicion de las bebidas en el soporte y la cantidad en onzas
de cada botella. Tambien permite la modificacion de cada uno. Cuenta con las validaciones repectivas para no ingresar letras donde van
numeros, ingresar la cantidad de botellas minimas y no poder ingresar 0 en cantidades.

'''


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

'''
def litros_a_onzas(litros):
    onzas_por_litro = 33.814
    onzas = int(litros) * onzas_por_litro
    return math.floor(onzas)



bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

bebidas_id = 0

@app.route('/bebida/posicion/create',methods=['POST'])
def create_bebida_pos_cant():
    
        
    print("creando una lista de bebidas")
    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    
    if bebidas_id == '' or bebidas_id == '0':
        bebidas_id = 0
    else:
        bebidas_id = int(bebidas_id)
    if bebidas_id == 0:
        flash('Primero debe seleccionar una lista de bebidas', 'error')
        return redirect('/bebida#tab1')
    id_lista_bebidas = {
        'id_lista_bebidas': bebidas_id
    }
    print('----------------------Validando errores------------------------------')
    lleno = False
    for i in range(24):
        aux = 'Pos_'+str(i+1)
        if request.form[aux] != '':
            lleno = True
            break
        else:
            continue
    if not lleno:
        print('----------------------No se han ingresado bebidas------------------------------')
        flash('No has ingresado ninguna bebida', 'error')
        return redirect('/bebida#tab2')
    
    posiciones = []
    cantidades = []
    bebidas = []

    if bebidas_id != 0:
        if lista_bebidas.get_by_id(id_lista_bebidas) != []:
            sv_data2 = lista_bebidas.get_by_id(id_lista_bebidas)
            
            bebidas = [sv_data2.bebida_1,sv_data2.bebida_2,sv_data2.bebida_3,sv_data2.bebida_4,sv_data2.bebida_5,sv_data2.bebida_6,sv_data2.bebida_7,sv_data2.bebida_8,sv_data2.bebida_9,sv_data2.bebida_10,sv_data2.bebida_11,sv_data2.bebida_12]
        else:
            
            bebidas = []
    else:
            bebidas = []
    bebidas_total = []
    for x in bebidas:
        if x != '':
            bebidas_total.append(x)
        else:
            continue
    
    for i in range(24):
        aux_pos = 'Pos_'+str(i+1)
        aux_cant = 'cant_'+str(i+1)
        aux_list_pos = request.form[aux_pos]
        
        aux_list_cant = request.form[aux_cant]
        
        if aux_list_pos != '' and aux_list_cant != '':
            print('aux_list_pos: ', aux_list_pos)
            print('aux_list_cant: ', aux_list_cant) 
            if not aux_list_cant.isnumeric():
                print('----------------------Una cantidad no es un numero------------------------------')
                flash('Una cantidad no es un numero', 'error')
                return redirect('/bebida#tab2')
            elif aux_list_cant == '0.0' or aux_list_cant == '0':
                print('----------------------La cantidad no puede ser 0------------------------------')
                flash('La cantidad no puede ser 0', 'error')
                return redirect('/bebida#tab2')
            else:
                print('............................................ guardando')
                posiciones.append(aux_list_pos) 
                cantidades.append(aux_list_cant)
        elif aux_list_pos == '' and aux_list_cant == '':
            print('entre a vacio............................................')
            posiciones.append('') 
            cantidades.append(0)
        elif aux_list_pos != '' and aux_list_cant == '':
            print('----------------------Existe una bebida sin cantidad------------------------------')
            flash('Existe una bebida sin cantidad', 'error')
            return redirect('/bebida#tab2')
        elif aux_list_pos == '' and aux_list_cant != '':
            print('----------------------Existe una cantidad sin bebida------------------------------')
            flash('Existe una cantidad sin bebida', 'error')
            return redirect('/bebida#tab2')
        
    
    for i in bebidas_total:
        try:
            
            print(i)
            posiciones.index(i)
        except ValueError:
            print('bebida de la lista: ', i)
            print('----------------------Debe utilizar al menos una vez todas las bebidas------------------------------')
            flash('Debe utilizar al menos una vez todas las bebidas', 'error')
            return redirect('/bebida#tab2')

    print('----------------------No hubieron errores------------------------------')

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
        'id_lista_bebidas': bebidas_id

    }
    
    sv_data = posicion_bebidas.get_all()
    existe = False
    for beb in sv_data:
        if beb.id_lista_bebidas == data1['id_lista_bebidas']:
            print('----------------------Actualizando posicion------------------------------')
            posicion_bebidas.update_by_id_lista_bebidas(data1)
            id = beb
            existe = True
            break
        else: 
            continue
    if not existe:
        posicion_bebidas.save(data1)
        id = posicion_bebidas.get_all()
        id = id[len(id)-1]

    print('...............cantidad:', type(cantidades[0]))
    data2 = {
        'cant_1': (cantidades[0]),
        'cant_2': (cantidades[1]),
        'cant_3': (cantidades[2]),
        'cant_4': (cantidades[3]),
        'cant_5': (cantidades[4]),
        'cant_6': (cantidades[5]),
        'cant_7': (cantidades[6]),
        'cant_8': (cantidades[7]),
        'cant_9': (cantidades[8]),
        'cant_10': (cantidades[9]),
        'cant_11': (cantidades[10]),
        'cant_12': (cantidades[11]),
        'cant_13': (cantidades[12]),
        'cant_14': (cantidades[13]),
        'cant_15': (cantidades[14]),
        'cant_16': (cantidades[15]),
        'cant_17': (cantidades[16]),
        'cant_18': (cantidades[17]),
        'cant_19': (cantidades[18]),
        'cant_20': (cantidades[19]),
        'cant_21': (cantidades[20]),
        'cant_22': (cantidades[21]),
        'cant_23': (cantidades[22]),
        'cant_24': (cantidades[23]),
        'cant_25': 0,
        'cant_26': 0,
        'cant_27': 0,
        'id_posicion_bebidas' : id.id_posicion_bebidas
        
    }
    
    sv_data2 = cantidad.get_all()
    existe = False
    for cant in sv_data2:
        if cant.id_posicion_bebidas == data2['id_posicion_bebidas']:
            print('----------------------Actualizando cantidad------------------------------')
            cantidad.update_by_id_posicion_bebidas(data2)
            existe = True
            break
        else: 
            continue

    if not existe:
        cantidad.save(data2)
    f.close()
    return redirect('/bebida#tab2')

'''





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


