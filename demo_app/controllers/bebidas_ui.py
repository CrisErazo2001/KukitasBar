from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.bebida import bebida
from flask_bcrypt import Bcrypt
import datetime
import requests
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
        return redirect('/bebida')

@app.route('/bebida')
def addbebidas():
    
        return render_template("disposicion_botellas.html")

@app.route('/bebida/get')
def getbebidas():
    
        return render_template("bebida_get.html")

@app.route('/bebida/delete')
def deletebebidas():
    
        return render_template("bebida_delete.html")

@app.route('/bebida/modify/<id>/<name>')
def updatebebidas(id, name):
        id = int(id)
        print(id)
        print(name)
        dataId = {
                'id_bebidas': id
        }
        dataName = {
                'nombre': name
        }
        url1 = 'http://127.0.0.1:5000/bebida/get/id'
        url2 = 'http://127.0.0.1:5000/bebida/get/name'
        r1 = requests.get(url1, params= dataId)
        r2 = requests.get(url2, params= dataName)
        result1 = r1.json()
        result2 = r2.json()
        print(result1)
        print(result2)
        return render_template("bebida_modify.html", id = id, name = name
                              ,id_bebidas=result1['id_bebidas'],nombre = result1['nombre'] , Pos_1 = result1['Pos_1'] ,Pos_2 =   result1['Pos_2'] ,Pos_3 = result1['Pos_3'] ,Pos_4 = result1['Pos_4'] ,Pos_5 = result1['Pos_5'] ,Pos_6 = result1['Pos_6'] ,Pos_7 = result1['Pos_7'] ,Pos_8 = result1['Pos_8'] ,Pos_9 = result1['Pos_9'] ,Pos_10 = result1['Pos_10'] ,Pos_11 = result1['Pos_11'] ,Pos_12 = result1['Pos_12'] ,Pos_13 = result1['Pos_13'] ,Pos_14 = result1['Pos_14'] ,Pos_15 = result1['Pos_15'] ,Pos_16 = result1['Pos_16'] ,Pos_17 = result1['Pos_17'] ,Pos_18 = result1['Pos_18'] ,Pos_19 = result1['Pos_19'] ,Pos_20 = result1['Pos_20'] ,Pos_21 = result1['Pos_21'] ,Pos_22 = result1['Pos_22'] ,Pos_23 = result1['Pos_23'] ,Pos_24 = result1['Pos_24'] ,Pos_25 = result1['Pos_25'] ,Pos_26 = result1['Pos_26'] ,Pos_27 = result1['Pos_27'], 
                               nombre_n = result1['nombre'] , Pos_1_n = result2['Pos_1'] ,Pos_2_n =   result2['Pos_2'] ,Pos_3_n = result2['Pos_3'] ,Pos_4_n = result2['Pos_4'] ,Pos_5_n = result2['Pos_5'] ,Pos_6_n = result2['Pos_6'] ,Pos_7_n = result2['Pos_7'] ,Pos_8_n = result2['Pos_8'] ,Pos_9_n = result2['Pos_9'] ,Pos_10_n = result2['Pos_10'] ,Pos_11_n = result2['Pos_11'] ,Pos_12_n = result2['Pos_12'] ,Pos_13_n = result2['Pos_13'] ,Pos_14_n = result2['Pos_14'] ,Pos_15_n = result2['Pos_15'] ,Pos_16_n = result2['Pos_16'] ,Pos_17_n = result2['Pos_17'] ,Pos_18_n = result2['Pos_18'] ,Pos_19_n = result2['Pos_19'] ,Pos_20_n = result2['Pos_20'] ,Pos_21_n = result2['Pos_21'] ,Pos_22_n = result2['Pos_22'] ,Pos_23_n = result2['Pos_23'] ,Pos_24_n = result2['Pos_24'] ,Pos_25_n = result2['Pos_25'] ,Pos_26_n = result2['Pos_26'] ,Pos_27_n = result2['Pos_27'])