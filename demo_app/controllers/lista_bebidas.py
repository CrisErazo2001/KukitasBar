'''

Este script incluye las rutas necesarias para crear y eliminar las listas de bebidas. 

La ruta /bebidas/create crea la lista de bebidas

La ruta /bebida/define-lista-global selecciona una lista de bebidas para poder crear la distribucion de botellas y cantidades ademas
de acceder a las recetas relacionadas con la lista de bebidas.

La ruta /bebida/define-lista-global/get entrega el nombre de la lista de bebidas seleccionada en formato json

La ruta /lista/delete elimina una lista de bebidas siembre y cuando no existan pedidos en lista de espera

'''


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.lista_bebidas import lista_bebidas
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.cantidad_bebidas import cantidad
from demo_app.models.pedido import pedido
from demo_app.models.user import User
from demo_app.models.receta import receta
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

bebidas_id = 0

@app.route('/bebidas/create',methods=['POST'])
def create_bebida():
    nombre = request.form["nombre"]
    bebidas = []

    if nombre == '':
        flash('No ingresaste un nombre', 'error')
        return redirect('/bebida')
    if(nombre.find(" ")!=-1):
        flash('El nombre no puede contener espacios', 'error')
        return redirect('/bebida')
    lleno = False
    for i in range(12):
        aux = 'bebida_'+str(i+1)
        if request.form[aux] != '':
            lleno = True
            break
        else:
            continue
    if not lleno:
        flash('No has ingresado ninguna bebida', 'error')
        return redirect('/bebida')
    
    data = {
        'nombre':nombre, 
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
        'bebida_11': request.form["bebida_11"],
        'bebida_12': request.form["bebida_12"]
        # 'id_lista_bebidas': request.form['id_lista_bebidas']

    }
    sv_data = lista_bebidas.get_all()
    for beb in sv_data:
        if beb.nombre == data['nombre']:
            flash('Hay otra lista con el mismo nombre', 'error')
            return redirect('/bebida')
        else: 
            continue
    print("Data: ", data)  
    id = lista_bebidas.save(data)
    
    return redirect('/bebida')

@app.route('/bebida/define-lista-global',methods=['POST'])
def define_bebida_list():
    f = open("bebida_id.txt", "w")
    global bebidas_id 
    
    data = {
      
        'nombre': request.form['nombre']
    }
    if data['nombre'] != '':
        lista = lista_bebidas.get_by_name(data)
        bebidas_id = lista.id_lista_bebidas
        print('Bebidas ID: ', bebidas_id)
        
        f.write(str(bebidas_id))
        f.close()
        return redirect('/bebida#tab2')
    else:
        f.write(str(0))
        f.close()
        return redirect('/bebida')

@app.route('/bebida/define-lista-global/get')
def get_bebida_list():
    global bebidas_id 
    data = {
      
        'bebida_list_id': bebidas_id
    }
    
    return jsonify(data)

@app.route('/bebida')
def addbebidas():
        
    if 'user_id' not in session:
        
        flash('Ingresa con una cuenta','error')
        return redirect('/')
    
    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    
    if bebidas_id == '' or bebidas_id == '0':
        bebidas_id = 0
    else:
        bebidas_id = int(bebidas_id)

    f2 = open('receta_id.txt','r')
    receta_id = f2.read()
    if receta_id == '' or receta_id == '0':
        receta_id = 0
    else:
        receta_id = int(receta_id)
    f2.close()
    data_receta = {
        'id_receta': receta_id
    }
    if receta_id > 0 and bebidas_id > 0:
        result_receta = receta.get_by_id(data_receta)
        if result_receta != []:
            result_receta = result_receta.asdict()
        else:
            result_receta = {
                'nombre': '', 
                'bebida_1':'', 
                'bebida_2': '', 
                'bebida_3':'', 
                'bebida_4': '', 
                'bebida_5': '', 
                'bebida_6': '',
                'bebida_7': '',
                'bebida_8': '' ,
                'bebida_9': '',
                'bebida_10': '',
                'cant_1': 0, 
                'cant_2': 0, 
                'cant_3': 0, 
                'cant_4': 0, 
                'cant_5': 0, 
                'cant_6': 0,
                'cant_7': 0,
                'cant_8': 0,
                'cant_9': 0,
                'cant_10': 0 ,
                'tiempo_prep': 0
                
            }
    else:
        result_receta = {
            'nombre': '', 
            'bebida_1':'', 
            'bebida_2': '', 
            'bebida_3':'', 
            'bebida_4': '', 
            'bebida_5': '', 
            'bebida_6': '',
            'bebida_7': '',
            'bebida_8': '' ,
            'bebida_9': '',
            'bebida_10': '',
            'cant_1': 0, 
            'cant_2': 0, 
            'cant_3': 0, 
            'cant_4': 0, 
            'cant_5': 0, 
            'cant_6': 0,
            'cant_7': 0,
            'cant_8': 0,
            'cant_9': 0,
            'cant_10': 0 ,
            'tiempo_prep': 0
            
        }

    
    
    sv_data = lista_bebidas.get_all()
    
    listas = []
    lista_bebidas_nombre = ''
    for lista in sv_data:
        nombre = lista.asdict()
        listas.append(nombre['nombre'])

    data = {
    
        'id_lista_bebidas': bebidas_id
    }
    
    
    if bebidas_id == 0:
        bebidas = []
        lista_bebidas_nombre = ''
        bebidas_total = []
        recetas_total = []
        posiciones_bebidas = {
            'id_posicion_bebidas': 0,  
            'Pos_1': '', 
            'Pos_2': '', 
            'Pos_3': '',  
            'Pos_4':  '',  
            'Pos_5':  '',  
            'Pos_6': '', 
            'Pos_7': '', 
            'Pos_8': '', 
            'Pos_9': '', 
            'Pos_10': '', 
            'Pos_11': '', 
            'Pos_12': '', 
            'Pos_13': '', 
            'Pos_14': '', 
            'Pos_15': '', 
            'Pos_16': '', 
            'Pos_17': '', 
            'Pos_18': '', 
            'Pos_19': '', 
            'Pos_20': '', 
            'Pos_21': '', 
            'Pos_22': '', 
            'Pos_23': '', 
            'Pos_24': '', 
            'Pos_25': '', 
            'Pos_26': '', 
            'Pos_27': '', 
            'id_lista_bebidas': 0   

        }
        cantidades_bebidas = {
            'id_cantidad': 0, 
            'id_posicion_bebidas': 0,  
            'cant_1': 0,
            'cant_2': 0,
            'cant_3': 0, 
            'cant_4':  0, 
            'cant_5':  0,
            'cant_6': 0,
            'cant_7': 0,
            'cant_8': 0,
            'cant_9': 0,
            'cant_10': 0,
            'cant_11': 0,
            'cant_12': 0,
            'cant_13': 0,
            'cant_14': 0,
            'cant_15': 0,
            'cant_16': 0,
            'cant_17': 0,
            'cant_18': 0,
            'cant_19': 0,
            'cant_20': 0,
            'cant_21': 0,
            'cant_22': 0,
            'cant_23': 0,
            'cant_24': 0,
            'cant_25': 0,
            'cant_26': 0,
            'cant_27': 0, 

        }
    
    
        
    else:
        
        if lista_bebidas.get_by_id(data) != []:
            sv_data2 = lista_bebidas.get_by_id(data)
            lista_bebidas_nombre = sv_data2.nombre
            bebidas = [sv_data2.bebida_1,sv_data2.bebida_2,sv_data2.bebida_3,sv_data2.bebida_4,sv_data2.bebida_5,sv_data2.bebida_6,sv_data2.bebida_7,sv_data2.bebida_8,sv_data2.bebida_9,sv_data2.bebida_10,sv_data2.bebida_11,sv_data2.bebida_12]
        else:
            
            bebidas = []
        bebidas_total = []
        for x in bebidas:
            if x != '':
                bebidas_total.append(x)
            else:
                continue

        recetas = receta.get_by_id_lista_bebidas(data)
        recetas_total = []
        for rec in recetas:
            recetas_total.append(rec.asdict()['nombre'])
        
        
        posiciones_bebidas = posicion_bebidas.get_by_id_lista_bebidas(data)
        
        if posiciones_bebidas == []:
            posiciones_bebidas = {
                'id_posicion_bebidas': 0,  
                'Pos_1': '', 
                'Pos_2': '', 
                'Pos_3': '',  
                'Pos_4':  '',  
                'Pos_5':  '',  
                'Pos_6': '', 
                'Pos_7': '', 
                'Pos_8': '', 
                'Pos_9': '', 
                'Pos_10': '', 
                'Pos_11': '', 
                'Pos_12': '', 
                'Pos_13': '', 
                'Pos_14': '', 
                'Pos_15': '', 
                'Pos_16': '', 
                'Pos_17': '', 
                'Pos_18': '', 
                'Pos_19': '', 
                'Pos_20': '', 
                'Pos_21': '', 
                'Pos_22': '', 
                'Pos_23': '', 
                'Pos_24': '', 
                'Pos_25': '', 
                'Pos_26': '', 
                'Pos_27': '', 
                'id_lista_bebidas': 0   

            }
            cantidades_bebidas = {
                'id_cantidad': 0, 
                'id_posicion_bebidas': 0,  
                'cant_1': 0,
                'cant_2': 0,
                'cant_3': 0, 
                'cant_4':  0, 
                'cant_5':  0,
                'cant_6': 0,
                'cant_7': 0,
                'cant_8': 0,
                'cant_9': 0,
                'cant_10': 0,
                'cant_11': 0,
                'cant_12': 0,
                'cant_13': 0,
                'cant_14': 0,
                'cant_15': 0,
                'cant_16': 0,
                'cant_17': 0,
                'cant_18': 0,
                'cant_19': 0,
                'cant_20': 0,
                'cant_21': 0,
                'cant_22': 0,
                'cant_23': 0,
                'cant_24': 0,
                'cant_25': 0,
                'cant_26': 0,
                'cant_27': 0, 

            }
        else:
            solicitud = {
                'id_posicion_bebidas':posiciones_bebidas.id_posicion_bebidas
            }
            cantidades_bebidas = cantidad.get_by_id_posicion_bebidas(solicitud)
            cantidades_bebidas = cantidades_bebidas.asdict()
            posiciones_bebidas = posiciones_bebidas.asdict()
        
        
    f.close()

    lista_pedidos = []
    pedidos = pedido.get_all()
    if pedidos != []:
        for ped in pedidos:
            if ped.status == 1:
                continue
            aux1 = ped.asdict()
            search_bebida = {
                'id_receta': aux1['id_receta']
            }
            search_lista = {
                'id_lista_bebidas': aux1['id_lista_bebidas']
            }
            bebida = receta.get_by_id(search_bebida)
            lista = lista_bebidas.get_by_id(search_lista)
            if bebida == [] or lista == []:
                aux1['id_receta'] = 'No existe en base de datos'
            else:
                aux1['id_receta'] = f'{bebida.nombre} - {lista.nombre} '

            lista_pedidos.append(aux1)
    
    
    return render_template("disposicion_botellas_2.html",lista_bebidas = listas,bebidas = bebidas_total, recetas = recetas_total, posicion_bebidas = posiciones_bebidas,cantidades_bebidas = cantidades_bebidas,lista_bebidas_nombre = lista_bebidas_nombre, receta = result_receta, lista_pedidos = lista_pedidos)

@app.route('/lista/delete',methods=['POST'])
def delete_lista():
    pedidos = pedido.get_all()
    if pedidos != []:
        flash('No puede eliminar una lista con pedidos en la lista de espea', 'error')
        return redirect('/bebida')
    lista_bebidas_nombre = request.form['lista_bebidas_nombre']
    search_lista = {
        'nombre': lista_bebidas_nombre
    }
    lista = lista_bebidas.get_by_name(search_lista)
    id_lista = lista.id_lista_bebidas
    search_pos = {
        'id_lista_bebidas': id_lista
    }
    pos = posicion_bebidas.get_by_id_lista_bebidas(search_pos)
    search_cant = {
        'id_posicion_bebidas': pos.id_posicion_bebidas
    }
    cant = cantidad.get_by_id_posicion_bebidas(search_cant)
    recetas = receta.get_by_id_lista_bebidas(search_pos)
    for rec in recetas:
        id = {
            'id_receta': rec.id_receta
        }
        receta.delete_by_id(id)

    id_cant = {
        'id_cantidad':cant.id_cantidad
    }
    cantidad.delete_by_id(id_cant)
    id_pos = {
        'id_posicion_bebidas': pos.id_posicion_bebidas
    }
    posicion_bebidas.delete_by_id(id_pos)
    id_lista = {
        'id_lista_bebidas': id_lista
    }
    lista_bebidas.delete_by_id(id_lista)

    return redirect('/bebida')