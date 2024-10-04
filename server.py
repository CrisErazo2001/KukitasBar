'''
Este script contiene la aplicacion Flask. Para arrancar el aplicativo utilizar la instruccion 'python server.py' pero tomar encuenta
que es necesario arrancar el entorno virtual para tener acceso a todas las librerias necesarias.

Para entrar al entorno virtual ingresar con el comando 
{venv}/Scripts/activate.bat desde el cmd 
o
{venv}/Scripts/Activate.ps1 desde PowerShell

donde {venv} es el nombre de su entorno virtual
'''


from demo_app import app
# from flask_cors import CORS
import requests

from demo_app.controllers import bebidas_ui, dashboard, posicion_bebidas, lista_bebidas, recetas, pedidos, users


APP = app
# CORS(APP)


if __name__ == "__main__":
    APP.run(debug=True)
    # APP.run(debug=True,host='000.000.000.000') descomentar esta linea para arrancar el sistema desde la red y no solo en local asi se puede acceder desde cualquier punto de la red, cambiar host con la ip del servidor
