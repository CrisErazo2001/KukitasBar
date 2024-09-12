from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'bebidas'

class lista_bebidas:
    
    db_name = 'kukasbar'
    
    def __init__( self , data ):
        self.id_lista_bebidas  =  data['id_lista_bebidas']
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
        self.bebida_11  =  data['bebida_11']
        self.bebida_12  =  data['bebida_12']
            

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM "+ table_name +";"
        results = connectToMySQL(cls.db_name).query_db(query)
        recetas = []
        print(results)
        for rec in results:
            recetas.append( cls(rec) )
        return recetas
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO "+ table_name +" ( nombre,bebida_1,bebida_2,bebida_3,bebida_4,bebida_5,bebida_6,bebida_7,bebida_8,bebida_9,bebida_10,bebida_11,bebida_12) VALUES (  %(nombre)s, %(bebida_1)s, %(bebida_2)s, %(bebida_3)s, %(bebida_4)s, %(bebida_5)s, %(bebida_6)s, %(bebida_7)s, %(bebida_8)s, %(bebida_9)s, %(bebida_10)s, %(bebida_11)s, %(bebida_12)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_lista_bebidas = %(id_lista_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        print('Result: ',result)
        if result == False:
            return []
        else: 
            return cls(result[0])
    @classmethod
    
    def get_by_name(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE nombre = %(nombre)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_receta = %(id_receta)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
      
    @classmethod
    def delete_by_id_bebidas(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_lista_bebidas = %(id_lista_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    @classmethod
    def delete_by_name(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE nombre = %(nombre)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result


    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET nombre = %(nombre)s, bebida_1 = %(bebida_1)s, bebida_2 = %(bebida_2)s, bebida_3 = %(bebida_3)s, bebida_4 = %(bebida_4)s, bebida_5 = %(bebida_5)s, bebida_6 = %(bebida_6)s, bebida_7 = %(bebida_7)s, bebida_8 = %(bebida_8)s, bebida_9 = %(bebida_9)s, bebida_10 = %(bebida_10)s, bebida_11 = %(bebida_11)s, bebida_12 = %(bebida_12)s"+" WHERE id_lista_bebidas = %(id_lista_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
        
    
    def asdict(self):

        dict = {
            'id_receta': self.id_lista_bebidas,   
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
            'bebida_10': self.bebida_10 

        }
        
        return dict
    
    