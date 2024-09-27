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
    print('-------------REQUEST FORM---------------')
    print(request.form)
    print('-------------USER---------------')
    print(user)
    if not user:
        flash('Usuario Incorrecto o no existe','error')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
    #if not user.password == request.form['password']:
        flash('Contraseña incorrecta','error')
        return redirect('/')
    session['user_id'] = user.id_usuario
    print("tengo usuario? ",user)
    if user.user == "admin":
        return redirect('/admin')
    if user.user == "operator":
        return redirect('/bebida')

    return redirect('/')

# @app.route("/admin")
# def admin():
#     return render_template("admin.html")


@app.route('/register')
def register():
    print("cambiando de html a registro")
    return render_template("register.html")


@app.route('/user/create',methods=['POST'])
def create_user():
    print("creando usuarios espero lol")
    data = {
        "user": request.form["user"],
        "password": bcrypt.generate_password_hash(request.form['password'])
        #"password": request.form['password']
    }
    print("Data: ", data)  
    usuarios = User.get_all()
    for user in usuarios:
        if user.user == data['user']:
            flash('ya existe un usuario con este nombre','error')
            return redirect('/register')
    id = User.save(data)
    session['user_id'] = id

    return redirect('/')

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