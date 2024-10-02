'''

Este script contiente la ruta /bebida/posicion/create que crea tanto las posicion de las bebidas en el soporte y la cantidad en onzas
de cada botella. Tambien permite la modificacion de cada uno. Cuenta con las validaciones repectivas para no ingresar letras donde van
numeros, ingresar la cantidad de botellas minimas y no poder ingresar 0 en cantidades.

'''


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.cantidad_bebidas import cantidad
from demo_app.models.lista_bebidas import lista_bebidas
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

bebidas_id = 0

@app.route('/bebida/posicion/create',methods=['POST'])
def create_bebida_pos_cant():
    print("creando una lista de bebidas")
    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    print(bebidas_id)
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
            if not aux_list_cant.isnumeric():
                print('----------------------Una cantidad no es un numero------------------------------')
                flash('Una cantidad no es un numero', 'error')
                return redirect('/bebida#tab2')
            elif aux_list_cant == '0':
                print('----------------------La cantidad no puede ser 0------------------------------')
                flash('La cantidad no puede ser 0', 'error')
                return redirect('/bebida#tab2')
            else:
                posiciones.append(aux_list_pos) 
                cantidades.append(aux_list_cant)
        elif aux_list_pos == '' and aux_list_cant == '':
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
            posiciones.index(i)
        except ValueError:
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


