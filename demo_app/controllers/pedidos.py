


from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.cantidad import cantidad
from demo_app.models.posicion import posicion_bebidas
from demo_app.models.ingrediente import ingrediente
from demo_app.models.pedido import pedido
from demo_app.models.receta import receta
from demo_app.models.historico_pedido import historico_pedido
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
from collections import Counter
import requests
import asyncio
from websockets.sync.client import connect

def webSocket_connection_2():
    with connect("ws://192.168.0.241:1880/ws/status-lista-pedidas") as websocket2:

        websocket2.send('1')

def verificar_cantidades_suficientes(receta_id):
    recetaSelected = receta.get_by_id({'id_receta': receta_id})
    keys, values = get_ing(recetaSelected.asdict())
    keys = keys[:-1]
    values = values[:-1]
    cantUsed = [x * 30 for x in values]  # Cantidad necesaria para cada ingrediente
    f = open('posicion.txt', 'r')
    id_aux = int(f.read())
    f.close()
    
    pos = posicion_bebidas.get_by_id({'id_posicion': id_aux})
    pos_list = pos.aslist()
    cant = cantidad.get_by_id({'id_cantidad': id_aux})
    cant_list = cant.asdict()
    
    for i, ingred in enumerate(keys):
        ing_aux = ingrediente.get_by_name({'nombre': ingred})
        cantidad_requerida = cantUsed[i]
        
        # Buscar en `pos_list` si existe suficiente cantidad para el ingrediente
        encontrado = False
        for j in range(len(pos_list)):
            if pos_list[j] == ing_aux.id_ingrediente:
                aux = 'cant' + str(j + 1)
                if cant_list[aux] >= cantidad_requerida:
                    encontrado = True
                    break
                
        
        if not encontrado:
            return False  # Si no hay suficiente de algún ingrediente, retorna False
    
    return True  # Si todos los ingredientes tienen suficiente cantidad, retorna True


def get_ing(receta):
    ingredientes = []
    for i in range(10):
        aux = 'ing'+str(i+1)
        ingredientes.append(receta[aux])
    conteo = Counter(ingredientes)
    conteo_dict = dict(conteo)
    clave = list(conteo_dict.keys())
    valor = list(conteo_dict.values())
    return clave,valor

@app.route('/')
def home():
    recetas = []    
    aux_data = receta.get_all()
    print(aux_data)
    
    for rec in aux_data:
        aux = rec.asdict_front()
        ingredientes = '' 
        for ing in aux['ingredientes']:
            ingredientes = ingredientes + ' ' + ing['nombre']
        aux['ingredientes'] = ingredientes
        recetas.append(aux)

      
    
    return render_template('restaurant.html', recetas = recetas)

@app.route('/pedido/nuevo', methods=['POST'])
def crear_pedido():
    is_valid = True
    categoria = "crear recetas"
    mensaje = "Receta Creada con éxito"
    status = 'ok'
    code = 200
    data = request.form
    searchReceta = {'nombre': data['nombre_bebida']}
    recetaSelected = receta.get_by_name(searchReceta)
    pedidos = pedido.get_all()
    

    # Validar si se pidió la bebida con hielo
    hielo = 1 if 'hielo' in data and data['hielo'] == 'on' else 0

    # Verificar si hay cantidades suficientes
    if not verificar_cantidades_suficientes(recetaSelected.id_receta):
        is_valid = False
        mensaje = "No hay suficientes cantidades de ingredientes para crear el pedido."
        status = 'error'
        code = 400
    else:
        # Calcular el tiempo estimado basado en la cola de pedidos
        pedidos = pedido.get_all()
        tiempo = recetaSelected.tiempo_prep
        
        for ped in pedidos:
            auxReceta = receta.get_by_id({'id_receta': ped.id_receta})
            tiempo += auxReceta.tiempo_prep

        dict_pedido = {
            'nombre_cliente': data['nombre_cliente'],  
            'id_receta': recetaSelected.id_receta, 
            'ready_at': datetime.now() + timedelta(minutes=tiempo),
            'status': 0,
            'hielo': hielo
        }

        # Guardar el pedido si hay cantidades suficientes
   
        pedido.save(dict_pedido)
        if pedidos == []:
            webSocket_connection_2()

    response = {
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code
    }
    if is_valid:

        return redirect('/')
    else:
        flash(mensaje,'error')
        return redirect('/')


@app.route('/pedido/send', methods=['GET'])
def send():
    is_valid = True
    is_valid_pos = True
    is_valid_cant = True
    firstTime = False
    ing = receta.get_all()
    f = open('posicion.txt', 'r')
    id_aux = int(f.read())
    f.close()
    pedidos = pedido.get_all()
    
    if not pedidos:
        is_valid = False
    elif pedidos[0].status == 0:
        ped = pedidos[0]
        ped.change_status()
        firstTime = True
    elif pedidos[0].status == 1:
        ped = pedidos[0]

    if is_valid:
        rec_aux = ped.id_receta
        rec = receta.get_by_id({'id_receta': rec_aux})
        hielo = ped.hielo
        keys, values = get_ing(rec.asdict())
        keys = keys[:-1]
        print(keys)
        values = values[:-1]
        cantUsed = [x * 30 for x in values]
        pos = posicion_bebidas.get_by_id({'id_posicion': id_aux})
        pos_list = pos.aslist()
        posiciones = []
        ingredientes = []
        for x in keys:
            try:
                ing_aux = ingrediente.get_by_name({'nombre': x})
                ingredientes.append(ing_aux.id_ingrediente)
                indice = pos_list.index(ing_aux.id_ingrediente)

                posiciones.append(indice + 1)
            except ValueError:
                is_valid_pos = False
                break

    if is_valid and is_valid_pos:
        pedido.update_by_id(ped.asdict())
        cant = cantidad.get_by_id({'id_cantidad': id_aux})
        cant_list = cant.asdict()
        z = 0
        counter = 0
        for p in posiciones:
            aux = 'cant' + str(p)
            while cant_list[aux] < cantUsed[z]:  # Sigue buscando si la cantidad no es suficiente
                try:
                    counter += 1
                    print('cant_list[aux]: ',cant_list[aux])
                    print('z: ',z)
                    # Busca el siguiente índice con el mismo ingrediente
                    print('ingredientes[z]: ',ingredientes[z])
                    indice = pos_list.index(ingredientes[z], pos_list.index(ingredientes[z]) + 1)
                    p = indice + 1  
                    print('indice: ',indice)
                    print('posiciones[z]: ',posiciones[z])
                    posiciones[z] = indice
                    aux = 'cant' + str(p)
                    if counter > len(pos_list):
                        is_valid_cant = False
                        break
                except ValueError:
                    is_valid_cant = False
                    break

            if is_valid_cant and cant_list[aux] >= cantUsed[z]:  # Verifica si es suficiente ahora
                cant_list[aux] -= cantUsed[z]
            else:
                is_valid_cant = False
                break

            z += 1

        if firstTime and is_valid_cant:
            cantidad.update_by_id(cant_list)

        for i in range(10 - len(keys)):
            posiciones.append(0)
            values.append(0)

    if not is_valid or not is_valid_pos or not is_valid_cant:
        posiciones = [0] * 10
        values = [0] * 10
        hielo = 0   

    print('is_valid: ', is_valid)
    print('is_valid_pos: ', is_valid_pos)
    return jsonify({'posiciones': posiciones, 'cantidades': values, 'hielo': hielo})



@app.route('/pedido/end',methods=['GET'])
def end():
    is_valid = True
    pedidos = pedido.get_all()
    
    if pedidos == []:
        is_valid = False
    elif pedidos[0].status == 0:
        is_valid = False

    if is_valid:
        ped = pedidos[0]
        rec_aux = ped.id_receta
        rec = receta.get_by_id({'id_receta':rec_aux})
        hielo = ped.hielo
        nombre_receta = rec.nombre
        created_at = ped.create_at
        keys,values = get_ing(rec.asdict())
        cantUsed = [x * 30 for x in values]
        ingredientes = ''
        cost = []
        cantXu = []
        for i in keys:
            ingredientes = ingredientes + '-' + i
            
            ing = ingrediente.get_by_name({'nombre': i})
            if ing != False:
                # print('nombre ', ing.precio_unitario)
                cost.append(ing.precio_unitario)
                cantXu.append(ing.cantidad_unitaria)
        costo_bebida = 0.0
        
        for c in range(len(keys)-1):
            # print('cL ',c)
            costo_bebida = costo_bebida + (float(cost[c])/int(cantXu[c]))*cantUsed[c]



        dict = {
            'costoBebida': costo_bebida, 
            'hielo': hielo,  
            'create_at': created_at,
            'ingredientes': ingredientes, 
            'nombre_receta': nombre_receta

        }

        historico_pedido.save(dict)
        pedido.delete_by_id({'id_pedido': ped.id_pedido})


    return jsonify({'status_end': is_valid})