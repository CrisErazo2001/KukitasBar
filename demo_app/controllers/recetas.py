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
    
    if bebidas_id == 0: 
        flash('Primero debe seleccionar una lista de bebidas', 'error')
        return redirect('/bebida#tab1')
    
    nombre_bebida = request.form["nombre"]
    if nombre_bebida == '':
        flash('No ha ingresado un nombre', 'error')
        return redirect('/bebida#tab3')
    if(nombre_bebida.find(" ")!=-1):
        flash('El nombre no puede contener espacios', 'error')
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
            rec = rec.asdict()
            rec['id_lista_bebidas'] = data['id_lista_bebidas']
            rec['nombre'] = data['nombre']
            rec['bebida_1'] = data['bebida_1']
            rec['bebida_2'] = data['bebida_2']
            rec['bebida_3'] = data['bebida_3']
            rec['bebida_4'] = data['bebida_4']
            rec['bebida_5'] = data['bebida_5']
            rec['bebida_6'] = data['bebida_6']
            rec['bebida_7'] = data['bebida_7']
            rec['bebida_8'] = data['bebida_8']
            rec['bebida_9'] = data['bebida_9']
            rec['bebida_10'] = data['bebida_10']
            rec['cant_1'] = data['cant_1']
            rec['cant_2'] = data['cant_2']
            rec['cant_3'] = data['cant_3']
            rec['cant_4'] = data['cant_4']
            rec['cant_5'] = data['cant_5']
            rec['cant_6'] = data['cant_6']
            rec['cant_7'] = data['cant_7']
            rec['cant_8'] = data['cant_8']
            rec['cant_9'] = data['cant_9']
            rec['cant_10'] = data['cant_10']
            rec['tiempo_prep'] = data['tiempo_prep']
            print('---------------------Actualizar receta---------------')
            receta.update_by_id(rec)
            
            return redirect('/bebida#tab3')
        else:
            continue

    print("Data: ", data)  

    receta.save(data)
    
    return redirect('/bebida#tab3')


@app.route('/receta/seleccionar',methods=['POST'])
def select_receta():

    f = open("bebida_id.txt", "r")
    bebidas_id = f.read()
    print(bebidas_id)
    if bebidas_id == '' or bebidas_id == '0':
        bebidas_id = 0
    else:
        bebidas_id = int(bebidas_id)
    f.close()

    nombre = request.form['nombre']
    if nombre == '':
        f = open("receta_id.txt", "w")
        f.write('0')
        f.close()
    else:

        list_recetas = receta.get_all()
        if list_recetas != []:
            for rec in list_recetas:
                if rec.id_lista_bebidas == bebidas_id and nombre == rec.nombre:
                    result = rec.id_receta
                    break
                else: 
                    continue
            f = open("receta_id.txt", "w")
            if result > 0:
                f.write(str(result))
            else:
                f.write('0')
                flash('No se encontro la bebida','error')
                return redirect('/bebida#tab3')
            f.close()
        else:
            flash('No se encontraron bebidas','error')
            return redirect('/bebida#tab3')
    
    return redirect('/bebida#tab3')

            
@app.route('/receta/delete')
def delete_receta():
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
    if receta_id > 0:
        result_receta = receta.get_by_id(data_receta)
        if result_receta != []:
            search_pedidos = pedido.get_all()
            if search_pedidos != []:
                for ped in search_pedidos:
                    if ped.id_receta == receta_id:
                        flash('No puede eliminar una bebida que se encuentra en lista de pedids','error')
                        return redirect('/bebida#tab3')
            else:
                receta.delete_by_id(data_receta)
                return redirect('/bebida#tab3')
        else:
            flash('No se encontro la receta','error')
            return redirect('/bebida#tab3')
    else:
        flash('No se encontro la receta','error')
        return redirect('/bebida#tab3')
    
    