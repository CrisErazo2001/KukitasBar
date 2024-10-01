from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'historial'

class historico_pedido:
    
    db_name = 'kukasbar'
    
    def __init__( self , data ):
        self.id_historial  =  data['id_historial']
        self.nombre_cliente  =  data['nombre_cliente']
        self.lista = data['lista']
        self.receta  =  data['receta']
        self.create_at  =  data['create_at']
        self.ready_at  =  data['ready_at']
        
        
        

        
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
        query = "INSERT INTO "+ table_name +" ( nombre_cliente,receta,create_at,lista) VALUES ( %(nombre_cliente)s, %(receta)s, %(create_at)s,%(lista)s);"
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
    def get_by_receta(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE receta = %(receta)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        pedidos = []
        for ped in result:
            pedidos.append( cls(ped) )
        return pedidos
    
    def get_by_name(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE nombre_cliente = %(nombre_cliente)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        pedidos = []
        for ped in result:
            pedidos.append( cls(ped) )
        return pedidos
    
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


    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET lista = %(lista)s, nombre_cliente = %(nombre_cliente)s, receta = %(receta)s, ready_at = %(ready_at)s"+" WHERE id_historial = %(id_historial)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
        
    
    def asdict(self):

        dict = {
            'id_historial': self.id_historial, 
            'nombre_cliente': self.nombre_cliente,  
            'receta': self.receta, 
            'lista': self.lista,
            'create_at': self.create_at , 
            'ready_at': self.ready_at,
            

        }
        
        return dict
    
        