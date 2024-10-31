'''
Este es el script donde se crea la clase cantidad para poder crear, modificar y eliminar filas en la tabla de 
la base de datos en MySql llamada 'cantidad_bebidas'

'''

from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json
import math



table_name = 'cantidad_bebidas'

class cantidad:
    
    db_name = 'kukasbar'
    
    def __init__( self , data ):
        self.id_cantidad  =  data['id_cantidad']
        self.cant1  =  data['cant1']
        self.cant2  =  data['cant2']
        self.cant3  =  data['cant3']
        self.cant4  =  data['cant4']
        self.cant5  =  data['cant5']
        self.cant6  =  data['cant6']
        self.cant7  =  data['cant7']
        self.cant8  =  data['cant8']
        self.cant9  =  data['cant9']
        self.cant10  =  data['cant10']
        self.cant11  =  data['cant11']
        self.cant12  =  data['cant12']
        self.cant13  =  data['cant13']
        self.cant14  =  data['cant14']
        self.cant15  =  data['cant15']
        self.cant16  =  data['cant16']
        self.cant17  =  data['cant17']
        self.cant18  =  data['cant18']
        self.cant19  =  data['cant19']
        self.cant20  =  data['cant20']
        self.cant21  =  data['cant21']
        self.cant22  =  data['cant22']
        self.cant23  =  data['cant23']
        self.cant24  =  data['cant24']
        self.cant25  =  data['cant25']
        self.cant26  =  data['cant26']
        self.cant27  =  data['cant27']
        self.cant28  =  data['cant28']

        

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM "+ table_name +";"
        results = connectToMySQL(cls.db_name).query_db(query)
        cant = []
        
        for can in results:
            cant.append( cls(can) )
        return cant
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO "+ table_name +" ( cant1,cant2,cant3,cant4,cant5,cant6,cant7,cant8,cant9,cant10,cant11,cant12,cant13,cant14,cant15,cant16,cant17,cant18,cant19,cant20,cant21,cant22,cant23,cant24,cant25,cant26,cant27,cant28 ) VALUES ( %(cant1)s, %(cant2)s, %(cant3)s, %(cant4)s, %(cant5)s, %(cant6)s, %(cant7)s, %(cant8)s, %(cant9)s, %(cant10)s, %(cant11)s, %(cant12)s, %(cant13)s, %(cant14)s, %(cant15)s, %(cant16)s, %(cant17)s, %(cant18)s, %(cant19)s, %(cant20)s, %(cant21)s, %(cant22)s, %(cant23)s, %(cant24)s, %(cant25)s, %(cant26)s, %(cant27)s, %(cant28)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_cantidad = %(id_cantidad)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result) == 0:
            result = []
        else:
            result = cls(result[0])
        return result
    
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_cantidad = %(id_cantidad)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
  
    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" cant1 = %(cant1)s,cant2 = %(cant2)s,cant3 = %(cant3)s,cant4 = %(cant4)s,cant5 = %(cant5)s,cant6 = %(cant6)s,cant7 = %(cant7)s,cant8 = %(cant8)s,cant9 = %(cant9)s,cant10 = %(cant10)s,cant11 = %(cant11)s,cant12 = %(cant12)s,cant13 = %(cant13)s,cant14 = %(cant14)s,cant15 = %(cant15)s,cant16 = %(cant16)s,cant17 = %(cant17)s,cant18 = %(cant18)s,cant19 = %(cant19)s,cant20 = %(cant20)s,cant21 = %(cant21)s,cant22 = %(cant22)s,cant23 = %(cant23)s,cant24 = %(cant24)s,cant25 = %(cant25)s,cant26 = %(cant26)s,cant27 = %(cant27)s,cant28 = %(cant28)s"+" WHERE id_cantidad = %(id_cantidad)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    
    
    def asdict(self):

        dict = {
            'id_cantidad': self.id_cantidad, 
            'id_posicion_bebidas': self.id_posicion_bebidas,  
            'cant1': self.cant1, 
            'cant2': self.cant2, 
            'cant3': self.cant3,
            'cant4':  self.cant4,
            'cant5':  self.cant5,
            'cant6': self.cant6,
            'cant7': self.cant7,
            'cant8': self.cant8,
            'cant9': self.cant9,
            'cant10': self.cant10,
            'cant11': self.cant11,
            'cant12': self.cant12,
            'cant13': self.cant13,
            'cant14': self.cant14,
            'cant15': self.cant15,
            'cant16': self.cant16,
            'cant17': self.cant17,
            'cant18': self.cant18,
            'cant19': self.cant19,
            'cant20': self.cant20,
            'cant21': self.cant21,
            'cant22': self.cant22,
            'cant23': self.cant23,
            'cant24': self.cant24,
            'cant25': self.cant25,
            'cant26': self.cant26,
            'cant27': self.cant27,
            'cant28': self.cant28

        }
        
        return dict
    
    def aslist(self):

        lista = [
            self.cant1, 
            self.cant2 , 
            self.cant3, 
            self.cant4 , 
            self.cant5 , 
            self.cant6  ,
            self.cant7  ,
            self.cant8  ,
            self.cant9  ,
            self.cant10 ,
            self.cant11  ,
            self.cant12  ,
            self.cant13  ,
            self.cant14 ,
            self.cant15 ,
            self.cant16  ,
            self.cant17  ,
            self.cant18  ,
            self.cant19  ,
            self.cant20 ,
            self.cant21  ,
            self.cant22  ,
            self.cant23 ,
            self.cant24 ,
            self.cant25  ,
            self.cant26  ,
            self.cant27 ,
            self.cant28

        ]
        
        return lista
    
    
    