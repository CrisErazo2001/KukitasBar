'''

Este script contiene las rutas de las paginas de la seccion de administracion. 

La ruta /admin contiene la pagina donde se muestran las tablas del historico y tambien se ve la lista de pedidos 
en cola y permite eliminar pedidos

La ruta /admin/user-modify te dirige a la pagina de administracion de usuarios donde se permite cambiar la contraseña de usuarios
y eliminar usuarios

La ruta /admin/history-delete es la funcion que permite eliminar el historial de pedidos

'''

from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.lista_bebidas import lista_bebidas
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.receta import receta
from demo_app.models.pedido import pedido
from flask_bcrypt import Bcrypt
from demo_app.models.user import User
from demo_app.models.historico_pedido import historico_pedido
import datetime
import requests
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/admin')
def dashboard():

    if 'user_id' not in session:
        flash('Ingresa con una cuenta','error')
        return redirect('/')
    id_usuario ={
        'id_usuario': session['user_id']
    }
    user = User.get_by_id(id_usuario)
    if user.tipo != 'admin':
        session.clear()
        flash('No tienes acceso a esta funcion','error')
        return redirect('/')
#historial de bebidas
    historial = historico_pedido.get_all()

    data = []
    for historico in historial:
        aux = historico.asdict()

        aux['receta'] = aux['receta'] + ' - ' + aux['lista']

        data.append(aux)
#lista de bebidas pendientes
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

    return render_template('dashboard.html', data=data, lista_pedidos=lista_pedidos)


@app.route('/admin/user-modify')
def user_modify():
    users_aux = User.get_all()
    users = []
    for user in users_aux:
        aux = user.user
        users.append(aux)

    return render_template('user_modify.html', users=users)


@app.route('/admin/history-delete')
def history_delete():
    historico_pedido.delete_all()

    return redirect('/admin')
