'''
Este es el script donde se crea la clase posicion_bebidas para poder crear, modificar y eliminar filas en la tabla de 
la base de datos en MySql llamada 'posicion_bebidas'

'''


from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json


table_name = 'posicion'

class posicion_bebidas:
    
    db_name = 'greepo'
    
    def __init__( self , data ):
        self.id_posicion  =  data['id_posicion']
        self.nombre = data['nombre']
        self.pos1  =  data['pos1']
        self.pos2  =  data['pos2']
        self.pos3  =  data['pos3']
        self.pos4  =  data['pos4']
        self.pos5  =  data['pos5']
        self.pos6  =  data['pos6']
        self.pos7  =  data['pos7']
        self.pos8  =  data['pos8']
        self.pos9  =  data['pos9']
        self.pos10  =  data['pos10']
        self.pos11  =  data['pos11']
        self.pos12  =  data['pos12']
        self.pos13  =  data['pos13']
        self.pos14  =  data['pos14']
        self.pos15  =  data['pos15']
        self.pos16  =  data['pos16']
        self.pos17  =  data['pos17']
        self.pos18  =  data['pos18']
        self.pos19  =  data['pos19']
        self.pos20  =  data['pos20']
        self.pos21  =  data['pos21']
        self.pos22  =  data['pos22']
        self.pos23  =  data['pos23']
        self.pos24  =  data['pos24']
        self.pos25  =  data['pos25']
        self.pos26  =  data['pos26']
        self.pos27  =  data['pos27']
        self.pos28  =  data['pos28']

        
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
        query = "INSERT INTO "+ table_name +" ( nombre,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11,pos12,pos13,pos14,pos15,pos16,pos17,pos18,pos19,pos20,pos21,pos22,pos23,pos24,pos25,pos26,pos27,pos28) VALUES ( %(nombre)s,%(pos1)s, %(pos2)s, %(pos3)s, %(pos4)s, %(pos5)s, %(pos6)s, %(pos7)s, %(pos8)s, %(pos9)s, %(pos10)s, %(pos11)s, %(pos12)s, %(pos13)s, %(pos14)s, %(pos15)s, %(pos16)s, %(pos17)s, %(pos18)s, %(pos19)s, %(pos20)s, %(pos21)s, %(pos22)s, %(pos23)s, %(pos24)s, %(pos25)s, %(pos26)s, %(pos27)s, %(pos28)s);"
        return connectToMySQL(cls.db_name).query_db( query, data )

    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM "+ table_name +" WHERE id_posicion = %(id_posicion)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        if len(result) == 0:
            result = []
        else:
            result = cls(result[0])
        return result
    
    
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM "+ table_name +" WHERE id_posicion = %(id_posicion)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    
    @classmethod
    def update_by_id(cls, data):
        query  = "UPDATE "+ table_name +" SET pos1 = %(pos1)s,pos2 = %(pos2)s,pos3 = %(pos3)s,pos4 = %(pos4)s,pos5 = %(pos5)s,pos6 = %(pos6)s,pos7 = %(pos7)s,pos8 = %(pos8)s,pos9 = %(pos9)s,pos10 = %(pos10)s,pos11 = %(pos11)s,pos12 = %(pos12)s,pos13 = %(pos13)s,pos14 = %(pos14)s,pos15 = %(pos15)s,pos16 = %(pos16)s,pos17 = %(pos17)s,pos18 = %(pos18)s,pos19 = %(pos19)s,pos20 = %(pos20)s,pos21 = %(pos21)s,pos22 = %(pos22)s,pos23 = %(pos23)s,pos24 = %(pos24)s,pos25 = %(pos25)s,pos26 = %(pos26)s,pos27 = %(pos27)s,pos28 = %(pos28)s WHERE id_posicion = %(id_posicion)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
  
    
    def asdict(self):

        dict = {
            'id_posicion': self.id_posicion, 
            'nombre': self.nombre, 
            'pos1': self.pos1, 
            'pos2': self.pos2 , 
            'pos3': self.pos3, 
            'pos4':  self.pos4 , 
            'pos5':  self.pos5 , 
            'pos6': self.pos6  ,
            'pos7': self.pos7  ,
            'pos8': self.pos8  ,
            'pos9': self.pos9  ,
            'pos10': self.pos10 ,
            'pos11': self.pos11  ,
            'pos12': self.pos12  ,
            'pos13': self.pos13  ,
            'pos14': self.pos14 ,
            'pos15': self.pos15 ,
            'pos16': self.pos16  ,
            'pos17': self.pos17  ,
            'pos18': self.pos18  ,
            'pos19': self.pos19  ,
            'pos20': self.pos20 ,
            'pos21': self.pos21  ,
            'pos22': self.pos22  ,
            'pos23': self.pos23  ,
            'pos24': self.pos24  ,
            'pos21': self.pos25  ,
            'pos22': self.pos26  ,
            'pos23': self.pos27  ,
            'pos24': self.pos28

        }
        
        return dict
    
    def aslist(self):

        lista = [
            
            self.pos1, 
            self.pos2 , 
            self.pos3, 
            self.pos4 , 
            self.pos5 , 
            self.pos6  ,
            self.pos7  ,
            self.pos8  ,
            self.pos9  ,
            self.pos10 ,
            self.pos11  ,
            self.pos12  ,
            self.pos13  ,
            self.pos14 ,
            self.pos15 ,
            self.pos16  ,
            self.pos17  ,
            self.pos18  ,
            self.pos19  ,
            self.pos20 ,
            self.pos21  ,
            self.pos22  ,
            self.pos23  ,
            self.pos24  ,
            self.pos25  ,
            self.pos26  ,
            self.pos27  ,
            self.pos28 
        ]
        
        return lista