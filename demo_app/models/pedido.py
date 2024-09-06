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
        self.id_bebidas = data['id_bebidas']
        self.id_recetas  =  data['id_recetas']
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
        query = "INSERT INTO "+ table_name +" ( nombre_cliente,id_bebidas,id_recetas,create_at,ready_at) VALUES ( %(nombre_cliente)s, %(id_bebidas)s, %(id_recetas)s, %(create_at)s, %(ready_at)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_pedidos = %(id_pedidos)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    @classmethod
    def get_by_id_recetas(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_recetas = %(id_recetas)s;"
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
    def delete_by_id_bebidas(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_recetas = %(id_recetas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    @classmethod
    def delete_by_name(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE nombre_cliente = %(nombre_cliente)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    @classmethod
    def delete_all(cls, data):
        query  = "DELETE FROM "+ table_name + ";"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result


    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET id_bebidas = %(id_bebidas)s, nombre = %(nombre)s, bebida_1 = %(bebida_1)s, bebida_2 = %(bebida_2)s, bebida_3 = %(bebida_3)s, bebida_4 = %(bebida_4)s, bebida_5 = %(bebida_5)s, bebida_6 = %(bebida_6)s, bebida_7 = %(bebida_7)s, bebida_8 = %(bebida_8)s, bebida_9 = %(bebida_9)s, bebida_10 = %(bebida_10)s, cant_1 = %(cant_1)s,cant_2 = %(cant_2)s,cant_3 = %(cant_3)s,cant_4 = %(cant_4)s,cant_5 = %(cant_5)s,cant_6 = %(cant_6)s,cant_7 = %(cant_7)s,cant_8 = %(cant_8)s,cant_9 = %(cant_9)s,cant_10 = %(cant_10)s,tiempo_prep = %(tiempo_prep)s"+" WHERE id_receta = %(id_receta)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
        
    
    def asdict(self):

        dict = {
            'id_receta': self.id_receta, 
            'id_bebidas': self.id_bebidas,  
            'nombre': self.nombre, 
            'bebida_1': self.bebida_1, 
            'bebida_2': self.bebida_2 , 
            'bebida_3': self.bebida_3, 
            'bebida_4':  self.bebida_4 , 
            'bebida_5':  self.bebida_5 , 
            'bebida_6': self.bebida_6  ,
            'bebida_7': self.bebida_7  ,
            'bebida_8': self.bebida_8  ,
            'bebida_9': self.bebida_9  ,
            'bebida_10': self.bebida_10 ,
            'cant_1': self.cant_1, 
            'cant_2': self.cant_2 , 
            'cant_3': self.cant_3, 
            'cant_4':  self.cant_4 , 
            'cant_5':  self.cant_5 , 
            'cant_6': self.cant_6  ,
            'cant_7': self.cant_7  ,
            'cant_8': self.cant_8  ,
            'cant_9': self.cant_9  ,
            'cant_10': self.cant_10 ,
            'tiempo_prep': self.tiempo_prep
            

        }
        
        return dict