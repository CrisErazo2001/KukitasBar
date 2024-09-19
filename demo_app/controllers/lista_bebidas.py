from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.lista_bebidas import lista_bebidas
from demo_app.models.posicion_bebidas import posicion_bebidas
from demo_app.models.cantidad_bebidas import cantidad
from demo_app.models.receta import receta
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

bebidas_id = 0

@app.route('/bebidas/create',methods=['POST'])
def create_bebida():
    print("creando una lista de bebidas")
    data = {
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
        'bebida_11': request.form["bebida_11"],
        'bebida_12': request.form["bebida_12"]
        # 'id_lista_bebidas': request.form['id_lista_bebidas']

    }
    sv_data = lista_bebidas.get_all()
    for beb in sv_data:
        if beb.nombre == data['nombre']:
            return jsonify(error=400, text='Estas repitiendo nombre'), 400
        else: 
            continue
    print("Data: ", data)  
    id = lista_bebidas.save(data)
    
    return redirect('/bebida')

@app.route('/bebida/get-all')
def get_all_bebidas():
       
    data = lista_bebidas.get_all()
    bebidas = []
    for beb in data:
        bebidas.append(beb.asdict())
    print(bebidas)
    
    return jsonify(bebidas)

@app.route('/bebida/get/id')
def get_bebida_by_id():
    
    data = {
        'id_lista_bebidas': request.args["id_lista_bebidas"]
    }
    result = lista_bebidas.get_by_id(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/bebida/get/name')
def get_bebida_by_name():
       
    data = {
        'nombre': request.args["nombre"]
    }
    result = lista_bebidas.get_by_name(data)
    result = result.asdict()
    return jsonify(result)

@app.route('/bebida/delete/id',methods=['POST'])
def delete_bebida_by_id():
       
    data = {
        'id_lista_bebidas': request.form["id_lista_bebidas"]
    }
    result = lista_bebidas.delete_by_id(data)
    print(result)
    return redirect('/bebida/delete')

@app.route('/bebida/delete/name',methods=['POST'])
def delete_bebida_by_name():
       
    data = {
        'nombre': request.form["nombre"]
    }
    result = lista_bebidas.delete_by_name(data)
    print(result)
    return redirect('/bebida/delete')

@app.route('/bebida/modify/id',methods=['POST'])
def update_bebida_by_id():
       
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
        'bebida_11': request.form["bebida_11"],
        'bebida_12': request.form["bebida_12"]
    }
    result = lista_bebidas.update_by_id(data)
    print(result)
    return redirect('/bebida')



@app.route('/bebida/define-lista-global',methods=['POST'])
def define_bebida_list():
    f = open("bebida_id.txt", "w")
    global bebidas_id 
    
    data = {
      
        'nombre': request.form['nombre']
    }
    lista = lista_bebidas.get_by_name(data)
    bebidas_id = lista.id_lista_bebidas
    print('Bebidas ID: ', bebidas_id)
    f.write(str(bebidas_id))
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
         
        f = open("bebida_id.txt", "r")
        bebidas_id = f.read()
        
        if bebidas_id == '' or bebidas_id == '0':
            bebidas_id = 0
        else:
            bebidas_id = int(bebidas_id)
        
        sv_data = lista_bebidas.get_all()
        
        listas = []
        for lista in sv_data:
            nombre = lista.asdict()
            listas.append(nombre['nombre'])

        data = {
      
            'id_lista_bebidas': bebidas_id
        }
        
        
        if bebidas_id != 0:
            if lista_bebidas.get_by_id(data) != []:
                sv_data2 = lista_bebidas.get_by_id(data)
                lista_bebidas_nombre = sv_data2.nombre
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

        recetas = receta.get_by_id_lista_bebidas(data)
        recetas_total = []
        for rec in recetas:
            recetas_total.append(rec.asdict()['nombre'])
        
        
        posiciones_bebidas = posicion_bebidas.get_by_id_lista_bebidas(data)
         
        if posiciones_bebidas == []:
            posiciones_bebidas = {}
            cantidades_bebidas = {}
        else:
            solicitud = {
                'id_posicion_bebidas':posiciones_bebidas.id_posicion_bebidas
            }
            cantidades_bebidas = cantidad.get_by_id_posicion_bebidas(solicitud)
            cantidades_bebidas = cantidades_bebidas.asdict()
            posiciones_bebidas = posiciones_bebidas.asdict()
        
        
        f.close()
        
        
        return render_template("disposicion_botellas_2.html",lista_bebidas = listas,bebidas = bebidas_total, recetas = recetas_total, posicion_bebidas = posiciones_bebidas,cantidades_bebidas = cantidades_bebidas,lista_bebidas_nombre = lista_bebidas_nombre)
