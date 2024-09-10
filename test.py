from demo_app.models.posicion_bebidas import bebida
from demo_app.models.receta import receta
import requests



url1 = 'http://127.0.0.1:5000/bebida/define/3'
url2 = 'http://127.0.0.1:5000/bebida/define/get'
r1 = requests.get(url1)
r2 = requests.get(url2)
result1 = r1.json()
result2 = r2.json()

print(result1)
print(result2)

data = {
    
    'id_bebidas': result1['bebida_list_id'], 
    'nombre':1, 
    'bebida_1': 1,
    'bebida_2': 1,
    'bebida_3': 1,
    'bebida_4': 1,
    'bebida_5':  1,
    'bebida_6':1,
    'bebida_7': 1,
    'bebida_8': 1,
    'bebida_9': 1,
    'bebida_10': 1,
    'cant_1': 12,
    'cant_2': 12, 
    'cant_3': 21,
    'cant_4': 12, 
    'cant_5': 12, 
    'cant_6': 12,
    'cant_7': 12,
    'cant_8': 12,
    'cant_9': 12,
    'cant_10': 12,
    'tiempo_prep': 7,
    
}

url3 = 'http://127.0.0.1:5000/receta/send/1'
response = requests.get(url3)
response= response.json()
print(response)