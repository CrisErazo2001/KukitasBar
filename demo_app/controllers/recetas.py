from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.receta import receta
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.cantidad_bebidas import cantidad
from demo_app.models.pedido import pedido
from flask_bcrypt import Bcrypt
from datetime import datetime
import requests




@app.route('/receta/create',methods=['POST'])
def create_receta():
    
    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    print(bebidas_id)
    if bebidas_id == '' or bebidas_id == '0':
        bebidas_id = 0
    else:
        bebidas_id = int(bebidas_id)

    nombre_bebida = request.form["nombre"]
    if nombre_bebida == '':
        flash('No ha ingresado un nombre', 'error')
        return redirect('/bebida#tab3')
    
    lleno = False
    for i in range(10):
        aux = 'bebida_'+str(i+1)
        if request.form[aux] != '':
            lleno = True
            break
        else:
            continue
    if not lleno:
        flash('No has ingresado ninguna bebida', 'error')
        return redirect('/bebida#tab3')
    
    bebidas = []
    cantidades = []
    for i in range(10):
        aux_bebida = 'bebida_'+str(i+1)
        aux_cant = 'cant_'+str(i+1)
        aux_list_bebida = request.form[aux_bebida]
        aux_list_cant = request.form[aux_cant]
        if aux_list_bebida != '' and aux_list_cant != '':
            if not aux_list_cant.isnumeric():
                flash('La cantidad no es un numero', 'error')
                return redirect('/bebida#tab3')
            elif aux_list_cant == 0:
                flash('La cantidad no puede ser 0', 'error')
                return redirect('/bebida#tab3')
            else:
                bebidas.append(aux_list_bebida) 
                cantidades.append(aux_list_cant)
        elif aux_list_bebida == '' and aux_list_cant == '':
            bebidas.append('') 
            cantidades.append(0)
        elif aux_list_bebida != '' and aux_list_cant == '':
            flash('Existe una bebida sin cantidad', 'error')
            return redirect('/bebida#tab3')
        elif aux_list_bebida == '' and aux_list_cant != '':
            flash('Existe una cantidad sin bebida', 'error')
            return redirect('/bebida#tab3')
    
    
    
    tiempo_prep = request.form["tiempo_prep"]
    if not tiempo_prep.isnumeric():
        flash('No ha ingresado un tiempo de preparacion o no es un numero', 'error')
        return redirect('/bebida#tab3')
    elif tiempo_prep == '0':
        flash('El tiempo de preparacion ingresado no puede ser 0', 'error')
        return redirect('/bebida#tab3')
    
    total_cantidad = 0    
    for i in cantidades:
        total_cantidad = total_cantidad + int(i)

    if total_cantidad > 10:
        flash('La suma total de las cantidades no puede ser superior a 10', 'error')
        return redirect('/bebida#tab3')

    data = {
            
            'id_lista_bebidas': bebidas_id, 
            'nombre': nombre_bebida, 
            'bebida_1': bebidas[0],
            'bebida_2': bebidas[1],
            'bebida_3': bebidas[2],
            'bebida_4': bebidas[3], 
            'bebida_5': bebidas[4],
            'bebida_6': bebidas[5],
            'bebida_7': bebidas[6],
            'bebida_8': bebidas[7],
            'bebida_9': bebidas[8],
            'bebida_10': bebidas[9],
            'cant_1': cantidades[0], 
            'cant_2': cantidades[1], 
            'cant_3': cantidades[2],
            'cant_4':  cantidades[3], 
            'cant_5':  cantidades[4], 
            'cant_6': cantidades[5],
            'cant_7': cantidades[6],
            'cant_8': cantidades[7],
            'cant_9': cantidades[8],
            'cant_10': cantidades[9],
            'tiempo_prep': tiempo_prep
            
        }

    data2 = {
        'nombre': data['nombre']
    }
    search = receta.get_by_name(data2)
    for rec in search:
        if rec.id_lista_bebidas == bebidas_id:
            flash('Se esta repitiendo nombre para esta lista de bebidas', 'error')
            return redirect('/bebida#tab3')
        else:
            continue

    print("Data: ", data)  

    receta.save(data)
    
    return redirect('/bebida#tab3')

@app.route('/receta/get-all')
def get_all_recetas():
       
    data = receta.get_all()
    recetas = []
    for rec in data:
        recetas.append(rec.asdict())
    print(recetas)
    
    return jsonify(recetas)



@app.route('/receta/get/id')
def get_receta_by_id():
    
    print(request.args)
    data = {
        'id_receta': request.args["id_receta"]
    }
    result = receta.get_by_id(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/receta/get/id_lista_bebidas')
def get_receta_by_id_lista_bebidas():
       
    data = {
        'id_lista_bebidas': request.args["id_lista_bebidas"]
    }
    result = receta.get_by_id_lista_bebidas(data)
    recetas = []
    for rec in result:
        recetas.append(rec.asdict())
    print(recetas)
    
    return jsonify(recetas)

@app.route('/receta/delete/id',methods=['POST'])
def delete_receta_by_id():
       
    data = {
        'id_receta': request.form["id_receta"]
    }
    result = receta.delete_by_id(data)
    print(result)
    return redirect('/receta/delete')

@app.route('/receta/delete/id_lista_bebidas',methods=['POST'])
def delete_receta_by_id_lista_bebidas():
       
    data = {
        'id_lista_bebidas': request.form["id_lista_bebidas"]
    }
    result = receta.delete_by_id_lista_bebidas(data)
    print(result)
    return redirect('/receta/delete')

@app.route('/receta/modify/id',methods=['POST'])
def update_receta_by_id():

    date_str = request.form["tiempo_prep"]
    date_format = '%M:%S'

    date_obj = datetime.strptime(date_str, date_format)
       
    data = {
            
            'id_lista_bebidas': request.form['id_lista_bebidas'], 
            'nombre':request.form["nombre"], 
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
            'cant_1': request.form["cant_1"], 
            'cant_2': request.form["cant_2"], 
            'cant_3': request.form["cant_3"],
            'cant_4':  request.form["cant_4"], 
            'cant_5':  request.form["cant_5"], 
            'cant_6': request.form["cant_6"],
            'cant_7': request.form["cant_7"],
            'cant_8': request.form["cant_8"],
            'cant_9': request.form["cant_9"],
            'cant_10': request.form["cant_10"],
            'tiempo_prep': date_obj
            
        }
    result = receta.update_by_id(data)
    print(result)
    return redirect('/receta')






