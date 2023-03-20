from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Orden:
    def __init__(self, data):
        self.id = data['id']
        self.fecha_time = data['fecha_time']
        self.total = data['total']
        self.cant = data['cant']
        self.usuario_id = data['usuario_id']
        self.cliente_id = data['cliente_id']
        self.estado_id = data['estado_id']
        self.servicio_id = data['servicio_id']
        self.Nombre_Apellido_Clie = data['Nombre_Apellido_Clie']
        self.Nombre_Apellido_Usu = data['Nombre_Apellido_Usu']
        self.service_name = data['service_name']
        self.descripcion = data['descripcion']
        self.created_up = data['created_up']
        self.updated_up = data['updated_up']
     


        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ordenes(fecha_time, total, created_up, updated_up, usuario_id, cliente_id, servicio_id, estado_id) VALUES(now(), %(total)s*%(cant)s, now(), now(), %(id)s, %(cliente_id)s, %(servicio_id)s, 1); "
        return connectToMySQL('bdgrupal').query_db(query,data)
   
    @classmethod
    def traer_todo(cls):
        query = "SELECT ordenes.id, ordenes.fecha_time, ordenes.cant, ordenes.total, concat(clientes.first_name, ' ', clientes.last_name) as Nombre_Apellido_Clie, clientes.address,  clientes.location, clientes.phone, clientes.email, estados.descripcion, servicios.description, servicios.service_name, servicios.precio,concat(usuarios.first_name, ' ', usuarios.last_name) as Nombre_Apellido_Usu , ordenes.usuario_id, ordenes.cliente_id, ordenes.servicio_id, ordenes.estado_id, ordenes.created_up, ordenes.updated_up FROM ordenes JOIN clientes ON clientes.id = ordenes.cliente_id join estados on estados.id = ordenes.estado_id JOIN usuarios ON usuarios.id = ordenes.usuario_id join servicios on servicios.id = ordenes.servicio_id;"
        toda_orden= []
        results = connectToMySQL('bdgrupal').query_db(query)
        for row in results:
            toda_orden.append(cls(row))
            print(row)
        return toda_orden
    @classmethod
    def traer_todo_ordenes(cls):
        query = "SELECT ordenes.id, ordenes.fecha_time, ordenes.total, concat(clientes.first_name, ' ', clientes.last_name) as Nombre_Apellido_Clie, clientes.address,  clientes.location, clientes.phone, clientes.email, estados.descripcion, servicios.description, servicios.service_name, servicios.precio,concat(usuarios.first_name, ' ', usuarios.last_name) as Nombre_Apellido_Usu, ordenes.cant, , ordenes.usuario_id, ordenes.cliente_id, ordenes.servicio_id, ordenes.estado_id, ordenes.created_up, ordenes.updated_up FROM ordenes JOIN clientes ON clientes.id = ordenes.cliente_id join estados on estados.id = ordenes.estado_id JOIN usuarios ON usuarios.id = ordenes.usuario_id join servicios on servicios.id = ordenes.servicio_id where ordenes.id=%(id)s ;"
        toda_ordenes = []
        results = connectToMySQL('bdgrupal').query_db(query)
        for row in results:
            toda_ordenes.append(cls(row))
            print(row)
        return toda_ordenes
    @classmethod
    def traer_servicios(cls):
        query = "SELECT id, service_name FROM servicios;"
        results = connectToMySQL('bdgrupal').query_db(query)
        all_servicios = []
        for row in results:
               all_servicios.append(cls(row))
        return all_servicios

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ordenes;"
        results = connectToMySQL('bdgrupal').query_db(query)
        all_ordenes= []
        for row in results:
            all_ordenes.append( cls(row) )
        return all_ordenes
    

    
    @classmethod
    def trae_uno(cls, data):
        query = "SELECT ordenes.id, ordenes.usuario_id, ordenes.cliente_id,ordenes.cant, ordenes.estado_id, ordenes.servicio_id, ordenes.created_up, ordenes.updated_up, ordenes.fecha_time, ordenes.total, concat(clientes.first_name, ' ', clientes.last_name) as Nombre_Apellido_Clie,  clientes.address,  clientes.location, clientes.phone, clientes.email, estados.descripcion, servicios.description, servicios.service_name, servicios.precio,concat(usuarios.first_name, ' ', usuarios.last_name) as Nombre_Apellido_Usu FROM ordenes JOIN clientes ON clientes.id = ordenes.cliente_id join estados on estados.id = ordenes.estado_id JOIN usuarios ON usuarios.id = ordenes.usuario_id join servicios on servicios.id = ordenes.servicio_id where ordenes.id= %(id)s"
        results = connectToMySQL('bdgrupal').query_db(query, data)
        return cls(results[0])
    @classmethod
    def actualizar(cls,data):
        query = "UPDATE ordenes SET total=%(total)s, usuario_id=%(usuario_id)s, cliente_id=%(cliente_id)s, servicio_id=%(servicio_id)s, estado_id=%(estado_id)s,updated_up=NOW() WHERE id = %(id)s;"
        return connectToMySQL('bdgrupal').query_db(query, data)

    @classmethod
    def actualizar_ope(cls, data):
        query = "UPDATE ordenes SET usuario_id=%(usuario_id)s, estado_id=%(estado_id)s,updated_up=NOW() WHERE id = %(id)s;"
        return connectToMySQL('bdgrupal').query_db(query, data)
    @classmethod
    def eliminar(cls,data):
        query = "DELETE FROM ordenes WHERE id = %(id)s;"
        return connectToMySQL('bdgrupal').query_db(query, data)

    @staticmethod
    def validar_orden(orden):
        is_valid = True
        if len(orden['cant']) < 1:
            flash("La cantidad debe  cargarse", "orden")
            is_valid = False
        return is_valid
