from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Orden_ser:
    def __init__(self, data):
       
        self.servicio_id = data['id']
        self.service_name = data['service_name']
        self.precio = data['precio']

  
    @classmethod
    def traer_servicios(cls):
           query = "SELECT id, service_name, precio FROM servicios;"
           results = connectToMySQL('bdgrupal').query_db(query)
           all_servicios= []
           for row in results:
               all_servicios.append( cls(row) )
           return all_servicios
    

class Orden_clien:
    def __init__(self, data):

        self.servicio_id = data['id']
        self.nombre_apellido = data['nombre_apellido']

    @classmethod
    def traer_clientes(cls):
        query = "SELECT id, concat(first_name, ' ',last_name) as nombre_apellido FROM clientes;"
        results = connectToMySQL('bdgrupal').query_db(query)
        all_clientes = []
        for row in results:
               all_clientes.append(cls(row))
        return all_clientes
