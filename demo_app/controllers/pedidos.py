from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.pedido import pedido
from demo_app.models.posicion_bebidas import posicion_bebidas
from flask_bcrypt import Bcrypt
from datetime import datetime
import requests
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/pedido/create',methods=['POST'])
def create_pedido():
    print("creando una receta")
    url1 = 'http://127.0.0.1:5000/bebida/get/id'
    r1 = requests.get(url1)
    result1 = r1.json()
    
    date_str = request.form["ready_at"]
    date_format = '%H:%M:%S'

    date_obj = datetime.strptime(date_str, date_format)

    data = {
            
            'id_bebidas': result1['bebida_list_id'], 
            'nombre_cliente':request.form["nombre_cliente"], 
            'id_receta': request.form["id_receta"],
            'ready_at': request.form["ready_at"]
        }
          

    print("Data: ", data)  
    id = pedido.save(data)
    
    return redirect('/pedido')

@app.route('/pedido/get-all')
def get_all_pedido():
       
    data = pedido.get_all()
    pedidos = []
    for ped in data:
        pedidos.append(ped.asdict())
    print(pedidos)
    
    return jsonify(pedidos)



@app.route('/pedido/get/id')
def get_pedido_by_id():
    
    print(request.args)
    data = {
        'id_receta': request.args["id_receta"]
    }
    result = pedido.get_by_id(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/pedido/get/id_receta')
def get_pedido_by_id_receta():
       
    data = {
        'id_receta': request.args["id_receta"]
    }
    result = pedido.get_by_id_receta(data)
    pedidos = []
    for ped in result:
        pedidos.append(ped.asdict())
    print(pedidos)
    
    return jsonify(pedidos)

@app.route('/pedido/get/name')
def get_pedido_by_name():
       
    data = {
        'nombre_cliente': request.args["nombre_cliente"]
    }
    result = pedido.get_by_name(data)
    pedidos = []
    for ped in result:
        pedidos.append(ped.asdict())
    print(pedidos)
    
    return jsonify(pedidos)

@app.route('/pedido/delete/id',methods=['POST'])
def delete_pedido_by_id():
       
    data = {
        'id_pedidos': request.form["id_pedidos"]
    }
    result = pedido.delete_by_id(data)
    print(result)
    return redirect('/pedido/delete')

@app.route('/pedido/delete/all')
def delete_pedido_all():
     
    result = pedido.delete_all()
    print(result)
    return redirect('/pedido/delete')

@app.route('/pedido/modify/id',methods=['POST'])
def update_pedido_by_id():

    date_str = request.form["ready_at"]
    date_format = '%H:%M:%S'

    date_obj = datetime.strptime(date_str, date_format)
       
    data = {
            
            'id_pedidos': request.form['id_pedidos'], 
            'nombre_cliente': request.form['nombre_cliente'],  
            'id_bebidas': request.form['id_bebidas'], 
            'id_receta': request.form['id_receta'],  
            'ready_at': date_obj
            
        }
    result = pedido.update_by_id(data)
    print(result)
    return redirect('/pedido')



@app.route('/pedidos',methods=['GET'])
def pedidos():

    data = [
        {"nombre": "Juan", "tiempo": 30},
        {"nombre": "Ana", "tiempo": 25},
        {"nombre": "Luis", "tiempo": 28},
    ]
    return render_template('pantalla_espera.html',data = data,nombre_cliente_actual='mateo',nombre_bebida='nombre',lista_ingredientes='ingredientes')

