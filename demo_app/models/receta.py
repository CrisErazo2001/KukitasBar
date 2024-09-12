from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'recetas'

class receta:
    
    db_name = 'kukasbar'
    
    def __init__( self , data ):
        self.id_receta  =  data['id_receta']
        self.nombre = data['nombre']
        self.bebida_1  =  data['bebida_1']
        self.bebida_2  =  data['bebida_2']
        self.bebida_3  =  data['bebida_3']
        self.bebida_4  =  data['bebida_4']
        self.bebida_5  =  data['bebida_5']
        self.bebida_6  =  data['bebida_6']
        self.bebida_7  =  data['bebida_7']
        self.bebida_8  =  data['bebida_8']
        self.bebida_9  =  data['bebida_9']
        self.bebida_10  =  data['bebida_10']
        self.cant_1  =  data['cant_1']
        self.cant_2  =  data['cant_2']
        self.cant_3  =  data['cant_3']
        self.cant_4  =  data['cant_4']
        self.cant_5  =  data['cant_5']
        self.cant_6  =  data['cant_6']
        self.cant_7  =  data['cant_7']
        self.cant_8  =  data['cant_8']
        self.cant_9  =  data['cant_9']
        self.cant_10  =  data['cant_10']
        self.tiempo_prep  =  data['tiempo_prep']
        self.id_lista_bebidas = data['id_lista_bebidas']
        

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM "+ table_name +";"
        results = connectToMySQL(cls.db_name).query_db(query)
        recetas = []
        
        for rec in results:
            recetas.append( cls(rec) )
        return recetas
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO "+ table_name +" ( id_lista_bebidas,nombre,bebida_1,bebida_2,bebida_3,bebida_4,bebida_5,bebida_6,bebida_7,bebida_8,bebida_9,bebida_10,cant_1,cant_2,cant_3,cant_4,cant_5,cant_6,cant_7,cant_8,cant_9,cant_10,tiempo_prep ) VALUES (  %(id_lista_bebidas)s, %(nombre)s, %(bebida_1)s, %(bebida_2)s, %(bebida_3)s, %(bebida_4)s, %(bebida_5)s, %(bebida_6)s, %(bebida_7)s, %(bebida_8)s, %(bebida_9)s, %(bebida_10)s,%(cant_1)s, %(cant_2)s, %(cant_3)s, %(cant_4)s, %(cant_5)s, %(cant_6)s, %(cant_7)s, %(cant_8)s, %(cant_9)s, %(cant_10)s, %(tiempo_prep)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_receta = %(id_receta)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    @classmethod
    def get_by_id_lista_bebidas(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_lista_bebidas = %(id_lista_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        recetas = []
        
        for rec in result:
            recetas.append( cls(rec) )
        return recetas
    
    @classmethod
    def get_by_name(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE nombre = %(nombre)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        recetas = []
        
        for rec in result:
            recetas.append( cls(rec) )
        return recetas
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_receta = %(id_receta)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
      
    @classmethod
    def delete_by_id_lista_bebidas(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_lista_bebidas = %(id_lista_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    @classmethod
    


    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET id_lista_bebidas = %(id_lista_bebidas)s, nombre = %(nombre)s, bebida_1 = %(bebida_1)s, bebida_2 = %(bebida_2)s, bebida_3 = %(bebida_3)s, bebida_4 = %(bebida_4)s, bebida_5 = %(bebida_5)s, bebida_6 = %(bebida_6)s, bebida_7 = %(bebida_7)s, bebida_8 = %(bebida_8)s, bebida_9 = %(bebida_9)s, bebida_10 = %(bebida_10)s, cant_1 = %(cant_1)s,cant_2 = %(cant_2)s,cant_3 = %(cant_3)s,cant_4 = %(cant_4)s,cant_5 = %(cant_5)s,cant_6 = %(cant_6)s,cant_7 = %(cant_7)s,cant_8 = %(cant_8)s,cant_9 = %(cant_9)s,cant_10 = %(cant_10)s,tiempo_prep = %(tiempo_prep)s"+" WHERE id_receta = %(id_receta)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
        
    
    def asdict(self):

        dict = {
            'id_receta': self.id_receta, 
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
            'tiempo_prep': self.tiempo_prep,
            'id_lista_bebidas': self.id_lista_bebidas
            

        }
        
        return dict
    
