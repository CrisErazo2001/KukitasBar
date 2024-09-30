from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.user import User
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/login',methods=['POST'])
def login():
    user = User.user_by_nombre(request.form)
    
    if not user:
        flash('Usuario Incorrecto o no existe','error')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
    #if not user.password == request.form['password']:
        flash('Contraseña incorrecta','error')
        return redirect('/')
    session['user_id'] = user.id_usuario
    print("tengo usuario? ",user)
    if user.tipo == "admin":
        return redirect('/admin')
    if user.tipo == "operator":
        return redirect('/bebida')

    return redirect('/')

# @app.route("/admin")
# def admin():
#     return render_template("admin.html")


@app.route('/register')
def register():
    if 'user_id' not in session:
        flash('Ingresa con una cuenta','error')
        return redirect('/logout')
    id_usuario ={
        'id_usuario': session['user_id']
    }
    user = User.get_by_id(id_usuario)
    if user.tipo != 'admin':
        flash('No tienes acceso a esta funcion','error')
        return redirect('/logout')


    print("cambiando de html a registro")
    return render_template("register.html")


@app.route('/user/create',methods=['POST'])
def create_user():
    
    user_class = ''
    aux_request = ''
    try:
        aux_request = request.form["admin"]
    except:
        user_class = 'operator'
    if aux_request == 'on':
        user_class = 'admin'
    data = {
        "user": request.form["user"],
        "password": bcrypt.generate_password_hash(request.form['password']),
        'tipo': user_class
        #"password": request.form['password']
    }
    print("Data: ", data)  
    usuarios = User.get_all()
    for user in usuarios:
        if user.user == data['user']:
            flash('ya existe un usuario con este nombre','error')
            return redirect('/register')
    User.save(data)
    

    return redirect('/admin')

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



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')