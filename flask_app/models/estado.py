from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Estado:
    def __init__(self, data):
        self.id = data['id']
        self.descripcion = data['descripcion']
        self.created_up = data['created_up']
        self.updated_up = data['updated_up']
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO estados (descripcion, created_up, updated_up) VALUES (%(descripcion)s, now(),now());"
        return connectToMySQL('bdgrupal').query_db(query,data)
   
    @classmethod
    def traer_todo(cls):
        query = "SELECT id, descripcion, created_up, updated_up FROM estados;"
        toda_estado= []
        results = connectToMySQL('bdgrupal').query_db(query)
        for row in results:
            toda_estado.append(cls(row))
            print(row)
        return toda_estado
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM estados;"
        results = connectToMySQL('bdgrupal').query_db(query)
        all_estados= []
        for row in results:
            all_estados.append( cls(row) )
        return all_estados
    

    @classmethod
    def trae_uno(cls, data):
        query = "SELECT r.id, r.descripcion, r.created_up, r.updated_up FROM estados r WHERE r.id = %(id)s;"
        results = connectToMySQL('bdgrupal').query_db(query, data)
        return cls(results[0])

    @classmethod
    def actualizar(cls,data):
        query = "UPDATE estados SET descripcion=%(descripcion)s,updated_up=NOW() WHERE id = %(id)s;"
        return connectToMySQL('bdgrupal').query_db(query, data)
    @classmethod
    def eliminar(cls,data):
        query = "DELETE FROM estados WHERE id = %(id)s;"
        return connectToMySQL('bdgrupal').query_db(query, data)

    @staticmethod
    def validar_estado(estado):
        is_valid = True
        if len(estado['descripcion']) < 5:
            flash("La descripción debe tener por lo menos 5 caracteres", "estado")
            is_valid = False
   
        return is_valid
