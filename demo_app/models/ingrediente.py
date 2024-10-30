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


table_name = 'ingrediente'

class ingrediente:
    
    db_name = 'greepo'
    
    def __init__( self , data ):
        self.id_ingrediente  =  data['id_ingrediente']
        self.nombre  =  data['nombre']
        self.descripcion  =  data['descripcion']
        self.precio_unitario  =  data['precio_unitario']
        self.cantidad_unitaria  =  data['cantidad_unitaria']
        self.categoria  =  data['categoria']
        self.proveedor  =  data['proveedor']
        
        

        
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
        query = "INSERT INTO "+ table_name +" ( id_ingrediente,nombre,descripcion,precio_unitario,cantidad_unitaria,categoria,proveedor) VALUES ( %(id_ingrediente)s,%(nombre)s, %(descripcion)s, %(precio_unitario)s,%(cantidad_unitaria)s,%(categoria)s,%(proveedor)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_ingrediente = %(id_ingrediente)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result) == 0:
            result = []
        else:
            result = cls(result[0])
        return result

    
    def get_by_name(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE nombre = %(nombre)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        pedidos = []
        for ped in result:
            pedidos.append( cls(ped) )
        return pedidos
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_ingrediente = %(id_ingrediente)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
       
    @classmethod
    def delete_all(cls, data):
        query  = "DELETE FROM "+ table_name + ";"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result


    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET nombre = %(nombre)s, descripcion = %(descripcion)s, precio_unitario = %(precio_unitario)s, cantidad_unitaria = %(cantidad_unitaria)s, categoria = %(categoria)s, proveedor = %(proveedor)s"+" WHERE id_ingrediente = %(id_ingrediente)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
        
    
    def asdict(self):

        dict = {
            'id_ingrediente': self.id_ingrediente,
            'nombre': self.nombre,
            'descripcion': self.descripcion  ,
            'precio_unitario': self.precio_unitario ,
            'cantidad_unitaria': self.cantidad_unitaria ,
            'categoria': self.categoria,
            'proveedor': self.proveedor
        }
        
        return dict
    
    def asdict_front(self):

        dict = {
            'stockNumber': self.id_ingrediente,
            'nombre': self.nombre,
            'descripcion': self.descripcion  ,
            'costo': self.precio_unitario ,
            'cantidad': self.cantidad_unitaria ,
            'tipo': self.categoria,
            'proveedor': self.proveedor
        }
        
        return dict
    