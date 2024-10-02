'''
Este es el script donde se crea la clase User para poder crear, modificar y eliminar filas en la tabla de 
la base de datos en MySql llamada 'usuarios'

'''


from demo_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
from flask import flash
import json

class User:
    
    db_name = 'kukasbar'
    
    def __init__( self , data ):
        self.id_usuario = data['id_usuario']
        self.user = data['user']
        self.password = data['password']
        self.created_at = data['created_at']
        self.tipo = data['tipo']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.db_name).query_db(query)
        usuarios = []
        
        for user in results:
            usuarios.append( cls(user) )
        return usuarios
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios ( user, password, tipo ) VALUES ( %(user)s, %(password)s , %(tipo)s );"
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_by_id(cls, data):
        query  = "SELECT * FROM usuarios WHERE id_usuario = %(id_usuario)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def change_password(cls, data):
        query  = "UPDATE usuarios SET password = %(password)s WHERE id_usuario = %(id_usuario)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    
    @classmethod
    def user_by_nombre(cls, data):
        query  = "SELECT * FROM usuarios WHERE user = %(user)s";
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def delete_by_id(cls, data):
        query  = "DELETE FROM usuarios WHERE id_usuario = %(id_usuario)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    @staticmethod
    def validate_register(user):
        
        is_valid = True
        categoria = "register"
        mensaje = "Exitoso"
        status = 'ok'
        code = 200
        
        query = "SELECT * FROM usuarios WHERE nombre_usuario = %(nombre_usuario)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)
        
        if len(results) >= 1:
            mensaje = "Ya existe este nombre_usuario."
            is_valid=False
            status = 'error'
            code = 400

        if len(user['nombre']) < 3:
            mensaje = "Nombre debe tener por lo menos 3 caracteres"
            is_valid= False
            status = 'error'
            code = 400

        if not re.search(PASSWORD_REGEX, user['password']):
            mensaje = "Contraseña debe tener números, letras mayúsculas y minúculas, caracteres especiales"
            is_valid=False
            status = 'error'
            code = 400

        if len(user['password']) < 8:
            mensaje = "Contraseña debe tener por lo menos 8 caracteres"
            is_valid= False
            status = 'error'
            code = 400

        if user['password'] != user['confirm']:
            mensaje = "Contraseñas no coinciden"
            is_valid= False
            status = 'error'
            code = 400
            
        value = {
            "valid": is_valid,
            "message": mensaje,
            "category": categoria,
            "status": status,
            "code": code
        }
        
        return json.dumps(value)