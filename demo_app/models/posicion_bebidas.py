from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'posicion_bebidas'

class posicion_bebidas:
    
    db_name = 'kukasbar'
    
    def __init__( self , data ):
        self.id_posicion_bebidas  =  data['id_posicion_bebidas']
        self.Pos_1  =  data['Pos_1']
        self.Pos_2  =  data['Pos_2']
        self.Pos_3  =  data['Pos_3']
        self.Pos_4  =  data['Pos_4']
        self.Pos_5  =  data['Pos_5']
        self.Pos_6  =  data['Pos_6']
        self.Pos_7  =  data['Pos_7']
        self.Pos_8  =  data['Pos_8']
        self.Pos_9  =  data['Pos_9']
        self.Pos_10  =  data['Pos_10']
        self.Pos_11  =  data['Pos_11']
        self.Pos_12  =  data['Pos_12']
        self.Pos_13  =  data['Pos_13']
        self.Pos_14  =  data['Pos_14']
        self.Pos_15  =  data['Pos_15']
        self.Pos_16  =  data['Pos_16']
        self.Pos_17  =  data['Pos_17']
        self.Pos_18  =  data['Pos_18']
        self.Pos_19  =  data['Pos_19']
        self.Pos_20  =  data['Pos_20']
        self.Pos_21  =  data['Pos_21']
        self.Pos_22  =  data['Pos_22']
        self.Pos_23  =  data['Pos_23']
        self.Pos_24  =  data['Pos_24']
        self.Pos_25  =  data['Pos_25']
        self.Pos_26  =  data['Pos_26']
        self.Pos_27  =  data['Pos_27']
        self.nombre  =  data['nombre']
        self.id_lista_bebidas = data['id_lista_bebidas']

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM "+ table_name +";"
        results = connectToMySQL(cls.db_name).query_db(query)
        bebidas = []
        
        for bebida in results:
            bebidas.append( cls(bebida) )
        return bebidas
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO "+ table_name +" ( Pos_1,Pos_2,Pos_3,Pos_4,Pos_5,Pos_6,Pos_7,Pos_8,Pos_9,Pos_10,Pos_11,Pos_12,Pos_13,Pos_14,Pos_15,Pos_16,Pos_17,Pos_18,Pos_19,Pos_20,Pos_21,Pos_22,Pos_23,Pos_24,Pos_25,Pos_26,Pos_27,nombre,id_lista_bebidas ) VALUES ( %(Pos_1)s, %(Pos_2)s, %(Pos_3)s, %(Pos_4)s, %(Pos_5)s, %(Pos_6)s, %(Pos_7)s, %(Pos_8)s, %(Pos_9)s, %(Pos_10)s, %(Pos_11)s, %(Pos_12)s, %(Pos_13)s, %(Pos_14)s, %(Pos_15)s, %(Pos_16)s, %(Pos_17)s, %(Pos_18)s, %(Pos_19)s, %(Pos_20)s, %(Pos_21)s, %(Pos_22)s, %(Pos_23)s, %(Pos_24)s, %(Pos_25)s, %(Pos_26)s, %(Pos_27)s, %(nombre)s, %(id_lista_bebidas)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_posicion_bebidas = %(id_posicion_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_by_id_lista_bebidas(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_lista_bebidas = %(id_lista_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_by_name(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE nombre = %(nombre)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_posicion_bebidas = %(id_posicion_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    @classmethod
    def delete_by_name(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE nombre = %(nombre)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET nombre = %(nombre)s, Pos_1 = %(Pos_1)s,Pos_2 = %(Pos_2)s,Pos_3 = %(Pos_3)s,Pos_4 = %(Pos_4)s,Pos_5 = %(Pos_5)s,Pos_6 = %(Pos_6)s,Pos_7 = %(Pos_7)s,Pos_8 = %(Pos_8)s,Pos_9 = %(Pos_9)s,Pos_10 = %(Pos_10)s,Pos_11 = %(Pos_11)s,Pos_12 = %(Pos_12)s,Pos_13 = %(Pos_13)s,Pos_14 = %(Pos_14)s,Pos_15 = %(Pos_15)s,Pos_16 = %(Pos_16)s,Pos_17 = %(Pos_17)s,Pos_18 = %(Pos_18)s,Pos_19 = %(Pos_19)s,Pos_20 = %(Pos_20)s,Pos_21 = %(Pos_21)s,Pos_22 = %(Pos_22)s,Pos_23 = %(Pos_23)s,Pos_24 = %(Pos_24)s,Pos_25 = %(Pos_25)s,Pos_26 = %(Pos_26)s,Pos_27 = %(Pos_27)s,id_lista_bebidas = %(id_lista_bebidas)s"+" WHERE id_posicion_bebidas = %(id_posicion_bebidas)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    @classmethod
    def update_by_name(cls, data):
        query  = "UPDATE "+ table_name +" SET nombre = %(nombre)s, Pos_1 = %(Pos_1)s,Pos_2 = %(Pos_2)s,Pos_3 = %(Pos_3)s,Pos_4 = %(Pos_4)s,Pos_5 = %(Pos_5)s,Pos_6 = %(Pos_6)s,Pos_7 = %(Pos_7)s,Pos_8 = %(Pos_8)s,Pos_9 = %(Pos_9)s,Pos_10 = %(Pos_10)s,Pos_11 = %(Pos_11)s,Pos_12 = %(Pos_12)s,Pos_13 = %(Pos_13)s,Pos_14 = %(Pos_14)s,Pos_15 = %(Pos_15)s,Pos_16 = %(Pos_16)s,Pos_17 = %(Pos_17)s,Pos_18 = %(Pos_18)s,Pos_19 = %(Pos_19)s,Pos_20 = %(Pos_20)s,Pos_21 = %(Pos_21)s,Pos_22 = %(Pos_22)s,Pos_23 = %(Pos_23)s,Pos_24 = %(Pos_24)s,Pos_25 = %(Pos_25)s,Pos_26 = %(Pos_26)s,Pos_27 = %(Pos_27)s,id_lista_bebidas = %(id_lista_bebidas)s"+" WHERE nombre = %(nombre)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    
    def asdict(self):

        dict = {
            'id_posicion_bebidas': self.id_posicion_bebidas,  
            'Pos_1': self.Pos_1, 
            'Pos_2': self.Pos_2 , 
            'Pos_3': self.Pos_3, 
            'Pos_4':  self.Pos_4 , 
            'Pos_5':  self.Pos_5 , 
            'Pos_6': self.Pos_6  ,
            'Pos_7': self.Pos_7  ,
            'Pos_8': self.Pos_8  ,
            'Pos_9': self.Pos_9  ,
            'Pos_10': self.Pos_10 ,
            'Pos_11': self.Pos_11  ,
            'Pos_12': self.Pos_12  ,
            'Pos_13': self.Pos_13  ,
            'Pos_14': self.Pos_14 ,
            'Pos_15': self.Pos_15 ,
            'Pos_16': self.Pos_16  ,
            'Pos_17': self.Pos_17  ,
            'Pos_18': self.Pos_18  ,
            'Pos_19': self.Pos_19  ,
            'Pos_20': self.Pos_20 ,
            'Pos_21': self.Pos_21  ,
            'Pos_22': self.Pos_22  ,
            'Pos_23': self.Pos_23  ,
            'Pos_24': self.Pos_24  ,
            'Pos_25': self.Pos_25  ,
            'Pos_26': self.Pos_26  ,
            'Pos_27': self.Pos_27  ,
            'nombre': self.nombre ,
            'id_lista_bebidas': self.id_lista_bebidas   

        }
        
        return dict
    
    def aslist(self):

        lista = [
            self.id_posicion_bebidas,  
            self.Pos_1, 
            self.Pos_2 , 
            self.Pos_3, 
            self.Pos_4 , 
            self.Pos_5 , 
            self.Pos_6  ,
            self.Pos_7  ,
            self.Pos_8  ,
            self.Pos_9  ,
            self.Pos_10 ,
            self.Pos_11  ,
            self.Pos_12  ,
            self.Pos_13  ,
            self.Pos_14 ,
            self.Pos_15 ,
            self.Pos_16  ,
            self.Pos_17  ,
            self.Pos_18  ,
            self.Pos_19  ,
            self.Pos_20 ,
            self.Pos_21  ,
            self.Pos_22  ,
            self.Pos_23  ,
            self.Pos_24  ,
            self.Pos_25  ,
            self.Pos_26  ,
            self.Pos_27  
        ]
        
        return lista