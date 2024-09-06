from demo_app import app
#from flask_cors import CORS
import requests

from demo_app.controllers import bebidas, bebidas_ui,recetas




APP = app
#CORS(APP)


if __name__=="__main__":
    APP.run(debug=True)
    #APP.run(debug=True,host='192.17.10.3', port=65100)
    # APP.run(debug=True)