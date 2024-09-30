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
    historial = historico_pedido.get_all()
    data = []
    for historico in historial:
        aux = historico.asdict()

        search_bebida = {
            'id_receta': aux['id_receta']
        }
        bebida = receta.get_by_id(search_bebida)
        if bebida == []:
            aux['id_receta'] = 'No existe en base de datos'
        else:
            aux['id_receta'] = bebida.nombre

        data.append(aux)

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
            bebida = receta.get_by_id(search_bebida)
            if bebida == []:
                aux1['id_receta'] = 'No existe en base de datos'
            else:
                aux1['id_receta'] = bebida.nombre
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
