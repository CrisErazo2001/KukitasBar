from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'pedidos'

class pedido:
    
    db_name = 'kukasbar'
    
    def __init__( self , data ):
        self.id_pedidos  =  data['id_pedidos']
        self.nombre_cliente  =  data['nombre_cliente']
        self.id_lista_bebidas = data['id_lista_bebidas']
        self.id_receta  =  data['id_receta']
        self.create_at  =  data['create_at']
        self.ready_at  =  data['ready_at']
        self.status  =  data['status']
        
        

        
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
        query = "INSERT INTO "+ table_name +" ( nombre_cliente,id_receta,ready_at,id_lista_bebidas,status) VALUES ( %(nombre_cliente)s, %(id_receta)s, %(ready_at)s,%(id_lista_bebidas)s,%(status)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_pedidos = %(id_pedidos)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    @classmethod
    def get_by_id_receta(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_receta = %(id_receta)s;"
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
        query  = "DELETE FROM "+ table_name +" WHERE id_pedidos = %(id_pedidos)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
       
    @classmethod
    def delete_all(cls, data):
        query  = "DELETE FROM "+ table_name + ";"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result


    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET id_lista_bebidas = %(id_lista_bebidas)s, nombre_cliente = %(nombre_cliente)s, id_receta = %(id_receta)s, ready_at = %(ready_at)s, status = %(status)s"+" WHERE id_pedidos = %(id_pedidos)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
        
    
    def asdict(self):

        dict = {
            'id_pedidos': self.id_pedidos, 
            'nombre_cliente': self.nombre_cliente,  
            'id_receta': self.id_receta, 
            'id_lista_bebidas': self.id_lista_bebidas,
            'create_at': self.create_at , 
            'ready_at': self.ready_at,
            'status': self.status

        }
        
        return dict
    
    def change_status(self):
        self.status = 1
        