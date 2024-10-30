'''
Este es el script donde se crea la clase pedido para poder crear, modificar y eliminar filas en la tabla de 
la base de datos en MySql llamada 'pedidos'

'''


from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'pedidos'

class pedido:
    
    db_name = 'greepo'
    
    def __init__( self , data ):
        self.id_pedido  =  data['id_pedido']
        self.nombre_cliente  =  data['nombre_cliente']
        self.id_receta  =  data['id_receta']
        self.create_at  =  data['create_at']
        self.ready_at  =  data['ready_at']
        self.status  =  data['status']
        self.hielo  =  data['hielo']
        
        

        
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
        query = "INSERT INTO "+ table_name +" ( nombre_cliente,id_receta,ready_at,status,hielo) VALUES ( %(nombre_cliente)s, %(id_receta)s, %(ready_at)s,%(status)s,%(hielo)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_pedido = %(id_pedido)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result) == 0:
            result = []
        else:
            result = cls(result[0])
        return result
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
        query  = "DELETE FROM "+ table_name +" WHERE id_pedido = %(id_pedido)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
       
    @classmethod
    def delete_all(cls, data):
        query  = "DELETE FROM "+ table_name + ";"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result


    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET nombre_cliente = %(nombre_cliente)s, id_receta = %(id_receta)s, ready_at = %(ready_at)s, status = %(status)s, hielo = %(hielo)s"+" WHERE id_pedido = %(id_pedido)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
        
    
    def asdict(self):

        dict = {
            'id_pedido': self.id_pedido, 
            'nombre_cliente': self.nombre_cliente,  
            'id_receta': self.id_receta, 
            'create_at': self.create_at , 
            'ready_at': self.ready_at,
            'status': self.status,
            'hielo': self.hielo

        }
        
        return dict
    
    def asdict_front(self):

        dict = {
            'id_pedido': self.id_pedido, 
            'nombre_cliente': self.nombre_cliente,  
            'id_bebida': self.id_receta, 
            'create_at': self.create_at , 
            'deliver_at': self.ready_at
        }
        
        return dict
    
    def change_status(self):
        self.status = 1
        