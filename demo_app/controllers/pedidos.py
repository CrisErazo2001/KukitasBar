from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.pedido import pedido
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.receta import receta
from demo_app.models.cantidad_bebidas import cantidad
from demo_app.models.historico_pedido import historico_pedido
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta

import requests
import asyncio
from websockets.sync.client import connect

receta_envio = {}
aux_id_cantidades = 0
pedido_actual = pedido


def reducir_cantidades(dic, id_cantidad):
    solicitud = {
        'id_cantidad': id_cantidad
    }
    search = cantidad.get_by_id(solicitud)
    cantidaddes_lista = [search.cant_1, search.cant_2, search.cant_3, search.cant_4, search.cant_5, search.cant_6, search.cant_7, search.cant_8, search.cant_9, search.cant_10, search.cant_11, search.cant_12, search.cant_13, search.cant_14,
                         search.cant_15, search.cant_16, search.cant_17, search.cant_18, search.cant_19, search.cant_20, search.cant_21, search.cant_22, search.cant_23, search.cant_24, search.cant_25, search.cant_26, search.cant_27, search.id_posicion_bebidas]
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


def generar_posicion_receta(id_receta, id_lista_bebidas):

    data_pbeb = {
        'id_lista_bebidas': id_lista_bebidas
    }

    data_bebida = {
        'id_receta': id_receta
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

        try:
            pos = aux.index(bebida[x])
        except ValueError as ve:
            return {}, 0

        c = bebida[y]
        z = 'cant_'+str(pos)

        while c > cant[z]:
            aux[pos] = 'Siguiente'
            try:
                pos = aux.index(bebida[x])
            except ValueError as ve:
                return {}, 0

            z = 'cant_'+str(pos)

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

    return receta_envio, id_cantidades




def webSocket_connection_2():
    with connect("ws://192.168.0.241:1880/ws/status-lista-pedidas") as websocket2:

        websocket2.send('1')





@app.route('/pedido/create', methods=['POST'])
def create_pedido():

    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    solicitud = {
        'id_lista_bebidas': bebidas_id
    }

    nombre_bebida = request.form['nombre_bebida']
    search_bebida = receta.get_by_id_lista_bebidas(solicitud)
    for x in search_bebida:
        if nombre_bebida == x.nombre:
            result = x
            break
        else:
            continue

    search_pedidos = pedido.get_all()
    tiempo = result.tiempo_prep
    for y in search_pedidos:
        sol = {
            'id_receta': y.id_receta
        }
        aux_beb = receta.get_by_id(sol)
        tiempo = tiempo + aux_beb.tiempo_prep
    data = {

        'nombre_cliente': request.form["nombre_cliente"],
        'id_receta': result.id_receta,
        'id_lista_bebidas': bebidas_id,
        'ready_at': datetime.now() + timedelta(minutes=tiempo),
        'status': '0'
    }

    pos, id_cant = generar_posicion_receta(result.id_receta, bebidas_id)
    print('pos: ', pos)
    if pos == {}:
        flash('No tienes la bebida suficiente', 'error')
        return redirect('/home')
    print('------------------------------Verificar lista pedidos-----------------------------------------')
    result = pedido.get_all()
    lista_vacia = False
    if result == []:
        lista_vacia = True

    pedido.save(data)

    
    if lista_vacia:
        webSocket_connection_2()

    f.close()
    return redirect('/home')


@app.route('/pedido', methods=['GET'])
def pedidos():
    global pedido_actual

    result = pedido.get_all()
    data = []
    if result == []:
        data = [{
            'nombre': '',
            'bebida': '',
            'tiempo': '',
            'ingredientes': ''
        }]
        pedido_aux = {
            'nombre': '',
            'bebida': '',
            'tiempo': '',
            'ingredientes': ''
        }

    else:
        cont = 0
        for ped in result:
            if ped.status == 1:
                solicitud = {
                    'id_receta': ped.id_receta
                }
                rec = receta.get_by_id(solicitud)
                rec_aux = rec.asdict()
                ingredientes = ''
                for i in range(10):
                    aux_bebida = 'bebida_'+str(i+1)
                    if rec_aux[aux_bebida] != '':
                        ingredientes = ingredientes + \
                            rec_aux[aux_bebida] + ', '
                    else:
                        continue
                ingredientes = ingredientes[:-2]
                pedido_aux = {
                    'nombre': ped.nombre_cliente,
                    'bebida': rec.nombre,
                    'tiempo': ped.ready_at,
                    'ingredientes': ingredientes
                }

                continue
            else:
                cont = cont + 1
                solicitud = {
                    'id_receta': ped.id_receta
                }
                rec = receta.get_by_id(solicitud)
                rec_aux = rec.asdict()
                ingredientes = ''
                for i in range(10):
                    aux_bebida = 'bebida_'+str(i+1)
                    if rec_aux[aux_bebida] != '':
                        ingredientes = ingredientes + \
                            rec_aux[aux_bebida] + ', '
                    else:
                        continue
                ingredientes = ingredientes[:-2]
                x = {
                    'nombre': ped.nombre_cliente,
                    'bebida': rec.nombre,
                    'tiempo': ped.ready_at,
                    'ingredientes': ingredientes
                }
                data.append(x)
        if cont == len(result):
            pedido_aux = {
                'nombre': '',
                'bebida': '',
                'tiempo': '',
                'ingredientes': ''
            }

    return render_template('pantalla_espera.html', data=data, nombre_cliente_actual=pedido_aux['nombre'], nombre_bebida=pedido_aux['bebida'], lista_ingredientes=pedido_aux['ingredientes'])


@app.route('/pedido/end')
def fin_receta():
    global receta_envio
    id_cantidades = 0

    result = pedido.get_all()
    if result == []:
        return redirect('/pedido/status')
    if result[0].status == 1:
        sol = {
            'id_lista_bebidas': result[0].id_lista_bebidas
        }
        aux_pos = posicion_bebidas.get_by_id_lista_bebidas(sol)
        sol = {
            'id_posicion_bebidas': aux_pos.id_posicion_bebidas
        }
        aux_cant = cantidad.get_by_id_posicion_bebidas(sol)
        id_cantidades = aux_cant.id_cantidad
        print(result[0].id_pedidos)
        data = {
            'id_pedidos': result[0].id_pedidos
        }
        data2 = {
            'nombre_cliente': result[0].nombre_cliente,
            'id_receta': result[0].id_receta,
            'id_lista_bebidas': result[0].id_lista_bebidas,
            'create_at': result[0].create_at,

        }

        pedido.delete_by_id(data)
        historico_pedido.save(data2)
        reducir_cantidades(receta_envio, id_cantidades)
        return jsonify({'status_end': True})
    # webSocket_connection()
    # return 200
    else:
        return jsonify({'status_end': False})


@app.route('/pedido/send')
def send_receta():
    global receta_envio
    global aux_id_cantidades
    global pedido_actual

    pedidos = pedido.get_all()
    if pedidos == []:
        return jsonify({
            'posiciones': [0,0,0,0,0,0,0,0,0,0],
            'cantidades': [0,0,0,0,0,0,0,0,0,0]
        })
    else:
        pedido_actual = pedidos[0]
        if pedido_actual.status == 1:
            receta_envio, aux_id_cantidades = generar_posicion_receta(
                pedido_actual.id_receta, pedido_actual.id_lista_bebidas)
        else:
            pedido_actual.change_status()
            aux_pedido = pedido_actual.asdict()
            pedido.update_by_id(aux_pedido)
            receta_envio, aux_id_cantidades = generar_posicion_receta(
                pedido_actual.id_receta, pedido_actual.id_lista_bebidas)
        if receta_envio == {}:
            return jsonify(error=101, text='No dispones de la bebida suficiente'), 101
    return jsonify(receta_envio)


@app.route('/pedido/status')
def send_status_pedidos():

    pedidos = pedido.get_all()
    if pedidos == []:
        result = {
            'status': False
        }
    elif len(pedidos)==1:
        if pedidos[0].status == 0:
            result = {
                'status': True
            }
        else:
            result = {
                'status': False
            }
    else:
        result = {
            'status': True
        }

    return jsonify(result)


@app.route('/pedido/historial/delete-all')
def delete_all_historial():
    historico_pedido.delete_all()
    return redirect('/statics')


@app.route('/pedido/eliminar-by-id', methods=['POST'])
def pedido_delete():
    pedido.delete_by_id(request.form)
         
    return redirect('/admin')