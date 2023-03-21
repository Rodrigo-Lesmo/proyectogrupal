from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Orden:
    def __init__(self, data):
        self.id = data['id']
        self.fecha_time = data['fecha_time']
        self.total = data['total']
        self.usuario_id = data['usuario_id']
        self.cliente_id = data['cliente_id']
        self.estado_id = data['estado_id']
        self.servicio_id = data['servicio_id']
        self.created_up = data['created_up']
        self.updated_up = data['updated_up']
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ordenes(fecha_time, total, created_up, updated_up, usuario_id, cliente_id, servicio_id, estado_id) VALUES('2023-03-18 22:28:25', 200000, now(), now(), 12, 1, 1, 1); "
        return connectToMySQL('proyectogrupal').query_db(query,data)
   
    @classmethod
    def traer_todo(cls):
        query = "SELECT ordenes.fecha_time, ordenes.total, concat(clientes.first_name, ' ', clientes.last_name) as Nombre_Apellido_Clie,  clientes.address,  clientes.location, clientes.phone, clientes.email, estados.descripcion, servicios.description, servicios.service_name, servicios.precio,concat(usuarios.first_name, ' ', usuarios.last_name) as Nombre_Apellido_Usu FROM ordenes JOIN clientes ON clientes.id = ordenes.cliente_id join estados on estados.id = ordenes.estado_id JOIN usuarios ON usuarios.id = ordenes.usuario_id join servicios on servicios.id = ordenes.servicio_id"
        
        results = connectToMySQL('proyectogrupal').query_db(query)
        toda_orden= []
        for row in results:
            toda_orden.append(cls(row))
            print(row)
        return toda_orden
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ordenes;"
        results = connectToMySQL('proyectogrupal').query_db(query)
        all_ordenes= []
        for row in results:
            all_ordenes.append( cls(row) )
        return all_ordenes
    

    @classmethod
    def trae_uno(cls, data):
        query = "SELECT ordenes.fecha_time, ordenes.total, concat(clientes.first_name, ' ', clientes.last_name) as Nombre_Apellido_Clie,  clientes.address,  clientes.location, clientes.phone, clientes.email, estados.descripcion, servicios.description, servicios.service_name, servicios.precio,concat(usuarios.first_name, ' ', usuarios.last_name) as Nombre_Apellido_Usu FROM ordenes JOIN clientes ON clientes.id = ordenes.cliente_id join estados on estados.id = ordenes.estado_id JOIN usuarios ON usuarios.id = ordenes.usuario_id join servicios on servicios.id = ordenes.servicio_id where %(id)s"
        results = connectToMySQL('proyectogrupal').query_db(query, data)
        return cls(results[0])

    @classmethod
    def actualizar(cls,data):
        query = "UPDATE ordenes SET fecha_time=%(fecha_time)s, total=%(total)s, usuario_id=%(usuario_id)s, cliente_id=%(cliente_id)s, servicio_id=%(servicio_id)s, estado_id=%(estado_id)s,updated_up=NOW() WHERE id = %(id)s;"
        return connectToMySQL('proyectogrupal').query_db(query, data)
    @classmethod
    def eliminar(cls,data):
        query = "DELETE FROM estados WHERE id = %(id)s;"
        return connectToMySQL('proyectogrupal').query_db(query, data)

    @staticmethod
    def validar_estado(estado):
        is_valid = True
        if len(estado['descripcion']) < 5:
            flash("La descripción debe tener por lo menos 5 caracteres", "estado")
            is_valid = False
   
        return is_valid
