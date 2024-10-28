'''
Este es el script donde se crea la clase receta para poder crear, modificar y eliminar filas en la tabla de 
la base de datos en MySql llamada 'recetas'

'''


from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'receta'

class receta:
    
    db_name = 'greepo'
    
    def __init__( self , data ):
        self.id_receta  =  data['id_receta']
        self.nombre = data['nombre']
        self.ing1  =  data['ing1']
        self.ing2  =  data['ing2']
        self.ing3  =  data['ing3']
        self.ing4  =  data['ing4']
        self.ing5  =  data['ing5']
        self.ing6  =  data['ing6']
        self.ing7  =  data['ing7']
        self.ing8  =  data['ing8']
        self.ing9  =  data['ing9']
        self.ing10  =  data['ing10']
        self.tiempo_prep  =  data['tiempo_prep']
        
        

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM "+ table_name +";"
        results = connectToMySQL(cls.db_name).query_db(query)
        recetas = []
        if len(results) == 0:
            recetas = []
        else:
            for rec in results:
                recetas.append(cls(rec))

        return recetas
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO "+ table_name +" ( nombre,ing1,ing2,ing3,ing4,ing5,ing6,ing7,ing8,ing9,ing10,tiempo_prep ) VALUES ( %(nombre)s, %(ing1)s, %(ing2)s, %(ing3)s, %(ing4)s, %(ing5)s, %(ing6)s, %(ing7)s, %(ing8)s, %(ing9)s, %(ing10)s,%(cant_1)s, %(cant_2)s, %(cant_3)s, %(cant_4)s, %(cant_5)s, %(cant_6)s, %(cant_7)s, %(cant_8)s, %(cant_9)s, %(cant_10)s, %(tiempo_prep)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_receta = %(id_receta)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result) == 0:
            result = []
        else:
            result = cls(result[0])
        return result
    
    
    @classmethod
    def get_by_name(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE nombre = %(nombre)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        recetas = []
        if len(result) == 0:
            recetas = []
        else:
            for rec in result:
                recetas.append( cls(rec) )
        return recetas
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_receta = %(id_receta)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    


    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET nombre = %(nombre)s, ing1 = %(ing1)s, ing2 = %(ing2)s, ing3 = %(ing3)s, ing4 = %(ing4)s, ing5 = %(ing5)s, ing6 = %(ing6)s, ing7 = %(ing7)s, ing8 = %(ing8)s, ing9 = %(ing9)s, ing10 = %(ing10)s,tiempo_prep = %(tiempo_prep)s"+" WHERE id_receta = %(id_receta)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
        
    
    def asdict(self):

        dict = {
            'id_receta': self.id_receta, 
            'nombre': self.nombre, 
            'ing1': self.ing1, 
            'ing2': self.ing2 , 
            'ing3': self.ing3, 
            'ing4':  self.ing4 , 
            'ing5':  self.ing5 , 
            'ing6': self.ing6  ,
            'ing7': self.ing7  ,
            'ing8': self.ing8  ,
            'ing9': self.ing9  ,
            'ing10': self.ing10 ,
            'tiempo_prep': self.tiempo_prep
            
        }
        
        return dict
    
