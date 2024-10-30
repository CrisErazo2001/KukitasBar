'''

Este script contiene las rutas de las paginas de la seccion de login y para administrar usuarios. 

La ruta /login valida el usuario y contraseña ingresado y te redirige a la pagina correspondiente y asigna la sension al id de usuario

La ruta /register muestra la pagina de registro de usuario

La ruta /user/create crea un nuevo usuario 

La ruta /user/modify modifica la contraseña de un usuario ya reado

La ruta /user/delete elimina un usuario

La ruta /logout elimina la id del usuario de la sesion y te redirige a la pagina de login

'''



from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.user import User
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'



'''
@app.route('/user/modify',methods=['POST'])
def modify_user():
    print("modificando usuarios espero lol")
    data = {
        "user": request.form["user"],
    }
    print("Data: ", data)  
    if data['user'] != '':
        user_aux = User.user_by_nombre(data)
        data = {
            "id_usuario": user_aux.id_usuario,
            "password": bcrypt.generate_password_hash(request.form['password'])
            #"password": request.form['password']
        }
        user_aux.change_password(data)
    else: 
        return redirect('/admin/user-modify')

    return redirect('/admin/user-modify')

@app.route('/user/delete',methods=['POST'])
def delete_user():
    print("modificando usuarios espero lol")
    data = {
        "user": request.form["user"],
    }
    
    if data['user'] != '':
        user_aux = User.user_by_nombre(data)
        data = {
            "id_usuario": user_aux.id_usuario,
            
        }
        user_aux.delete_by_id(data)
    else: 
        return redirect('/admin/user-modify')

    return redirect('/admin/user-modify')
'''

@app.route('/login',methods=['POST'])
def login():
    is_valid = True
    categoria = "login"
    mensaje = "Exitoso"
    status = 'success'
    code = 200
    redirect = ''

    user = User.user_by_nombre(request.form)
    
    if not user: #valida si existe el usuario
        is_valid = False
        mensaje = "Usuario incorrecto o no existente"
        status = 'error'
        code = 400
    elif not bcrypt.check_password_hash(user.password, request.form['password']): #valida si la contrasena es corecta
        is_valid = False
        mensaje = "Contraseña incorrecta"
        status = 'error'
        code = 400
    else:
        session['user_id'] = user.id_usuario #crea una sesion de usuario para ingresar solo a las paginas correspondientes
        
        if user.tipo == "admin":
            redirect = 'admin'
        if user.tipo == "operator":
            redirect = 'operator'

    
    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code,
        'redirect': redirect
    }
    return jsonify(value)


@app.route('/register', methods=['POST'])
def create_user():

    is_valid = True
    categoria = "register"
    mensaje = "Usuario creado con exito"
    status = 'success'
    code = 200
    
    data = request.json  # Obtener datos en formato JSON
    if data['admin']:
        user_class = 'admin'
    else:
        user_class = 'operator'
    
    user = {
        'user': data['username'],
        'password': bcrypt.generate_password_hash(data['password']),
        'tipo': user_class
    }

    User.save(user)
    

    

    value = {   #valor de salida de la api
        "valid": is_valid,
        "message": mensaje,
        "category": categoria,
        "status": status,
        "code": code
    }
    return jsonify(value)

@app.route('/user',methods=['GET'])
def get_user():

    is_valid = True
    categoria = "User"
    user = "Dorean"
    status = 'success'
    code = 200
    

    value = {   #valor de salida de la api
        "valid": is_valid,
        "user": user,
        "category": categoria,
        "status": status,
        "code": code
    }
    return jsonify(value)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')