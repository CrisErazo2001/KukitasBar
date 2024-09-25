from demo_app import app
#from flask_cors import CORS
import requests

from demo_app.controllers import bebidas_ui, posicion_bebidas,lista_bebidas,recetas,pedidos




APP = app
#CORS(APP)


if __name__=="__main__":
    APP.run(debug=True)
    # APP.run(debug=True,host='192.168.0.250')
    # APP.run(debug=True)