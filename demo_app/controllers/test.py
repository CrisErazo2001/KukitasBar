from flask import render_template, redirect, session, request, flash, jsonify, make_response
import json
from demo_app import app
from demo_app.models.receta import receta
from demo_app.models.pedido import pedido
from flask_bcrypt import Bcrypt
from datetime import datetime
import requests
import math


@app.route('/api',methods=['GET'])
def api_test():
    return jsonify(
        {
            'userid': 1,
            'title': 'Flask React app',
            'completed': False
        }
    )


@app.route('/api/post', methods=['POST'])
def handle_data():
    data = request.json  # Obtener datos en formato JSON
    # Procesar los datos como sea necesario
    
    return jsonify({"message": "Datos recibidos correctamente", "data": data})
