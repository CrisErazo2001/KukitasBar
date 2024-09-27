from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.lista_bebidas import lista_bebidas
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.receta import receta
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
          data.append(aux)
     return render_template('dashboard.html',data=data)

@app.route('/admin/user-modify')
def user_modify():
    users_aux = User.get_all()
    users = []
    for user in users_aux:
         aux = user.user
         users.append(aux)
         
    return render_template('user_modify.html',users = users)