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
from demo_app.models.pedido import pedido
from demo_app.models.user import User
from demo_app.models.receta import receta
from flask_bcrypt import Bcrypt
import datetime
from random import randint
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'




@app.route('/pedidos',methods=['GET'])
def get_lista_pedidos():

    is_valid = True
    categoria = "lista de pedidos"
    mensaje = "Exitoso"
    status = 'success'
    code = 200
    pedidos = pedido.get_all()
    if pedidos == []:
        is_valid = True
        categoria = "lista de pedidos"
        mensaje = "No hay pedidos en cola"
        status = 'warning'
        code = 300
    data = []
    for ped in pedidos:
        data.append(ped.asdict_front())
        
    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        "data": data
    }
    
    return jsonify(value)


@app.route('/pedido/eliminar', methods=['POST'])
def eliminar_pedidos():
    is_valid = True
    categoria = "eliminar pedido"
    mensaje = "Pedido Eliminado Correctamente"
    status = 'success'
    code = 200
    data = request.json
    print(data)
    pedidoSelected = pedido.get_by_id({'id_pedido': data['id_pedido']})
    if pedidoSelected.status == 1:
        is_valid = False
        categoria = "eliminar pedido"
        mensaje = "No se puede eliminar un pedido en produccion"
        status = 'error'
        code = 400
    if is_valid:
        pedido.delete_by_id({'id_pedido': data['id_pedido']})

    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code

    }
    return jsonify(value)
    
@app.route('/lista-pedidos', methods=['GET'])
def show_pedidos():
    nombre_cliente_actual = ''
    nombre_bebida = ''
    lista_ingredientes = ''
    data = []
    pedidos = pedido.get_all()
    if pedidos != []:
        if pedidos[0].status == 1:
            nombre_cliente_actual = pedidos[0].nombre_cliente
            rec = receta.get_by_id({'id_receta':pedidos[0].id_receta})
            lista = rec.ingredientes()
            for i in lista:
                if i == '':
                    break
                lista_ingredientes = lista_ingredientes + ' - ' + i

            nombre_bebida = rec.nombre
    
    for p in pedidos:
        if p.status == 1:
            continue
        aux = p.asdict()
        aux_receta = receta.get_by_id(aux)
        
        aux['id_receta'] = aux_receta.nombre
       
        data.append(aux)
    
    return render_template('pantalla_espera.html', data=data, nombre_cliente_actual=nombre_cliente_actual, nombre_bebida=nombre_bebida, lista_ingredientes=lista_ingredientes)
