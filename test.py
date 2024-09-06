from demo_app.models.bebida import bebida
from demo_app.models.receta import receta
import requests




url3 = 'http://192.168.68.128:5000/receta/send/1'
response = requests.get(url3)
response= response.json()
print(response)
print(response['cantidades'])
print(response['posiciones'])