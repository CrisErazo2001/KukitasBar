from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'cantidad_bebidas'

class cantidad:
    
    db_name = 'kukasbar'
    
    def __init__( self , data ):
        self.id_cantidad  =  data['id_cantidad']
        self.id_posicion_bebidas  =  data['id_posicion_bebidas']
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
        self.cant_11  =  data['cant_11']
        self.cant_12  =  data['cant_12']
        self.cant_13  =  data['cant_13']
        self.cant_14  =  data['cant_14']
        self.cant_15  =  data['cant_15']
        self.cant_16  =  data['cant_16']
        self.cant_17  =  data['cant_17']
        self.cant_18  =  data['cant_18']
        self.cant_19  =  data['cant_19']
        self.cant_20  =  data['cant_20']
        self.cant_21  =  data['cant_21']
        self.cant_22  =  data['cant_22']
        self.cant_23  =  data['cant_23']
        self.cant_24  =  data['cant_24']
        self.cant_25  =  data['cant_25']
        self.cant_26  =  data['cant_26']
        self.cant_27  =  data['cant_27']
        

        
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
        query = "INSERT INTO "+ table_name +" ( cant_1,cant_2,cant_3,cant_4,cant_5,cant_6,cant_7,cant_8,cant_9,cant_10,cant_11,cant_12,cant_13,cant_14,cant_15,cant_16,cant_17,cant_18,cant_19,cant_20,cant_21,cant_22,cant_23,cant_24,cant_25,cant_26,cant_27,id_posicion_bebidas ) VALUES ( %(cant_1)s, %(cant_2)s, %(cant_3)s, %(cant_4)s, %(cant_5)s, %(cant_6)s, %(cant_7)s, %(cant_8)s, %(cant_9)s, %(cant_10)s, %(cant_11)s, %(cant_12)s, %(cant_13)s, %(cant_14)s, %(cant_15)s, %(cant_16)s, %(cant_17)s, %(cant_18)s, %(cant_19)s, %(cant_20)s, %(cant_21)s, %(cant_22)s, %(cant_23)s, %(cant_24)s, %(cant_25)s, %(cant_26)s, %(cant_27)s, %(id_posicion_bebidas)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_cantidad = %(id_cantidad)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    @classmethod
    def get_by_id_posicion_bebidas(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_posicion_bebidas = %(id_posicion_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_cantidad = %(id_cantidad)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    @classmethod
    def delete_by_id_posicion_bebidas(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_posicion_bebidas = %(id_posicion_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET id_posicion_bebidas = %(id_posicion_bebidas)s, cant_1 = %(cant_1)s,cant_2 = %(cant_2)s,cant_3 = %(cant_3)s,cant_4 = %(cant_4)s,cant_5 = %(cant_5)s,cant_6 = %(cant_6)s,cant_7 = %(cant_7)s,cant_8 = %(cant_8)s,cant_9 = %(cant_9)s,cant_10 = %(cant_10)s,cant_11 = %(cant_11)s,cant_12 = %(cant_12)s,cant_13 = %(cant_13)s,cant_14 = %(cant_14)s,cant_15 = %(cant_15)s,cant_16 = %(cant_16)s,cant_17 = %(cant_17)s,cant_18 = %(cant_18)s,cant_19 = %(cant_19)s,cant_20 = %(cant_20)s,cant_21 = %(cant_21)s,cant_22 = %(cant_22)s,cant_23 = %(cant_23)s,cant_24 = %(cant_24)s,cant_25 = %(cant_25)s,cant_26 = %(cant_26)s,cant_27 = %(cant_27)s"+" WHERE id_cantidad = %(id_cantidad)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    @classmethod
    def update_by_id_posicion_bebidas(cls, data):
        query  = "UPDATE "+ table_name +" SET id_posicion_bebidas = %(id_posicion_bebidas)s, cant_1 = %(cant_1)s,cant_2 = %(cant_2)s,cant_3 = %(cant_3)s,cant_4 = %(cant_4)s,cant_5 = %(cant_5)s,cant_6 = %(cant_6)s,cant_7 = %(cant_7)s,cant_8 = %(cant_8)s,cant_9 = %(cant_9)s,cant_10 = %(cant_10)s,cant_11 = %(cant_11)s,cant_12 = %(cant_12)s,cant_13 = %(cant_13)s,cant_14 = %(cant_14)s,cant_15 = %(cant_15)s,cant_16 = %(cant_16)s,cant_17 = %(cant_17)s,cant_18 = %(cant_18)s,cant_19 = %(cant_19)s,cant_20 = %(cant_20)s,cant_21 = %(cant_21)s,cant_22 = %(cant_22)s,cant_23 = %(cant_23)s,cant_24 = %(cant_24)s,cant_25 = %(cant_25)s,cant_26 = %(cant_26)s,cant_27 = %(cant_27)s"+" WHERE id_posicion_bebidas = %(id_posicion_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    
    def asdict(self):

        dict = {
            'id_cantidad': self.id_cantidad, 
            'id_posicion_bebidas': self.id_posicion_bebidas,  
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
            'cant_11': self.cant_11  ,
            'cant_12': self.cant_12  ,
            'cant_13': self.cant_13  ,
            'cant_14': self.cant_14 ,
            'cant_15': self.cant_15 ,
            'cant_16': self.cant_16  ,
            'cant_17': self.cant_17  ,
            'cant_18': self.cant_18  ,
            'cant_19': self.cant_19  ,
            'cant_20': self.cant_20 ,
            'cant_21': self.cant_21  ,
            'cant_22': self.cant_22  ,
            'cant_23': self.cant_23  ,
            'cant_24': self.cant_24  ,
            'cant_25': self.cant_25  ,
            'cant_26': self.cant_26  ,
            'cant_27': self.cant_27  

        }
        
        return dict
    
    def aslist(self):

        lista = [
            self.cant_1, 
            self.cant_2 , 
            self.cant_3, 
            self.cant_4 , 
            self.cant_5 , 
            self.cant_6  ,
            self.cant_7  ,
            self.cant_8  ,
            self.cant_9  ,
            self.cant_10 ,
            self.cant_11  ,
            self.cant_12  ,
            self.cant_13  ,
            self.cant_14 ,
            self.cant_15 ,
            self.cant_16  ,
            self.cant_17  ,
            self.cant_18  ,
            self.cant_19  ,
            self.cant_20 ,
            self.cant_21  ,
            self.cant_22  ,
            self.cant_23  ,
            self.cant_24  ,
            self.cant_25  ,
            self.cant_26  ,
            self.cant_27  

        ]
        
        return lista
    
    
    