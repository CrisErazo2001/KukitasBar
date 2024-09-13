from flask import Flask, render_template, request
from demo_app import app

@app.route('/test', methods=['GET', 'POST'])
def index_2():
    # Lista de botones
    buttons = ["Inicio", "Servicios", "Contacto", "Acerca de"]
    data = [
        {"nombre": "Juan", "edad": 30, "ciudad": "Quito"},
        {"nombre": "Ana", "edad": 25, "ciudad": "Guayaquil"},
        {"nombre": "Luis", "edad": 28, "ciudad": "Cuenca"},
    ]

    if request.method == 'POST':
        # Recibimos el valor del botón presionado
        clicked_button = request.form.get('button_value')
        return f"Has presionado el botón: {clicked_button}"

    return render_template('index.html', buttons=buttons, data = data)
