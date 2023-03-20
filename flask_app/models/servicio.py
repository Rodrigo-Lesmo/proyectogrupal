from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Servicio:
    def __init__(self, data):
        self.id = data['id']
        self.service_name = data['service_name']
        self.description = data['description']
        self.precio = data['precio']
        self.created_up = data['created_up']
        self.updated_up = data['updated_up']
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO servicios (service_name, description, precio, created_up, updated_up) VALUES (%(service_name)s, %(description)s,  %(precio)s, now(),now());"
        return connectToMySQL('bdgrupal').query_db(query,data)
   
    @classmethod
    def traer_todo(cls):
        query = "SELECT id, service_name, description, precio, created_up, updated_up FROM servicios;"
        toda_servicio= []
        results = connectToMySQL('bdgrupal').query_db(query)
        for row in results:
            toda_servicio.append(cls(row))
            print(row)
        return toda_servicio
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM servicios;"
        results = connectToMySQL('bdgrupal').query_db(query)
        all_servicios= []
        for row in results:
            all_servicios.append( cls(row) )
        return all_servicios
    

    @classmethod
    def trae_uno(cls, data):
        query = "SELECT r.id, r.service_name,r.description, r.precio, r.created_up, r.updated_up FROM servicios r WHERE r.id = %(id)s;"
        results = connectToMySQL('bdgrupal').query_db(query, data)
        return cls(results[0])

    @classmethod
    def actualizar(cls,data):
        query = "UPDATE servicios SET service_name=%(service_name)s,description=%(description)s,precio=%(precio)s,updated_up=NOW() WHERE id = %(id)s;"
        return connectToMySQL('bdgrupal').query_db(query, data)
    @classmethod
    def eliminar(cls,data):
        query = "DELETE FROM servicios WHERE id = %(id)s;"
        return connectToMySQL('bdgrupal').query_db(query, data)

    @staticmethod
    def validar_servicio(servicio):
        is_valid = True
        if len(servicio['service_name']) < 2:
            flash("El nombre del servicio debe tener por lo menos 2 caracteres", "servicio")
            is_valid = False
        if len(servicio['description']) < 5:
            flash("La descrición debe tener por lo menos 5 caracteres", "servicio")
            is_valid = False
        if len(servicio['precio']) < 1:
            is_valid = False
            flash("Asigne un precio","servicio")

        return is_valid
