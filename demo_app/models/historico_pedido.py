'''
Este es el script donde se crea la clase historico_pedido para poder crear, modificar y eliminar filas en la tabla de 
la base de datos en MySql llamada 'historial'

'''

from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'historial'

class historico_pedido:
    
    db_name = 'greepo'
    
    def __init__( self , data ):
        self.id_historial  =  data['id_historial']
        self.nombre_receta  =  data['nombre_receta']
        self.ingredientes = data['ingredientes']
        self.create_at  =  data['create_at']
        self.ready_at  =  data['ready_at']
        self.hielo  =  data['hielo']
        self.costoBebida = data['costoBebida']
        
        

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM "+ table_name +";"
        results = connectToMySQL(cls.db_name).query_db(query)
        pedidos = []
        
        for ped in results:
            pedidos.append( cls(ped) )
        return pedidos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO "+ table_name +" ( nombre_receta,ingredientes,create_at,hielo,costoBebida) VALUES ( %(nombre_receta)s, %(ingredientes)s, %(create_at)s,%(hielo)s,%(costoBebida)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_historial = %(id_historial)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result) == 0:
            result = []
        else:
            result = cls(result[0])
        return result
    
    
 
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_historial = %(id_historial)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
       
    @classmethod
    def delete_all(cls):
        query  = "DELETE FROM "+ table_name + ";"
        result = connectToMySQL(cls.db_name).query_db(query)
        return result

    
        
    
    def asdict(self):

        dict = {
            'costoBebida': self.costoBebida, 
            'hielo': self.hielo,  
            'ready_at': self.ready_at, 
            'create_at': self.create_at,
            'ingredientes': self.ingredientes , 
            'nombre_receta': self.nombre_receta,
            'id_historial':self.id_historial
            

        }
        
        return dict
    
        