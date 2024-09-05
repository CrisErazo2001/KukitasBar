from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.bebida import bebida
from flask_bcrypt import Bcrypt
import datetime
bcrypt = Bcrypt(app)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/bebida')
def addbebidas():
    
        return render_template("bebida.html")

@app.route('/bebida/get')
def getbebidas():
    
        return render_template("bebida_get.html")

@app.route('/bebida/delete')
def deletebebidas():
    
        return render_template("bebida_delete.html")