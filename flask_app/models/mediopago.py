from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Mediopago:
    def __init__(self, data):
        self.id = data['id']
        self.medio = data['medio']
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO medio_pago (medio) VALUES (%(medio)s);"
        return connectToMySQL('proyectogrupal').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM medio_pago;"
        results = connectToMySQL('proyectogrupal').query_db(query)
        all_medios= []
        for row in results:
            all_medios.append( cls(row) )
            print(all_medios)
        return all_medios
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM medio_pago WHERE id = %(id)s;"
        results = connectToMySQL('proyectogrupal').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def eliminar(cls,data):
        query = "DELETE FROM medio_pago WHERE id = %(id)s;"
        return connectToMySQL('proyectogrupal').query_db(query, data)
    
    @classmethod
    def actualizar(cls,data):
        query = "UPDATE medio_pago SET medio=%(medio)s WHERE id = %(id)s;"
        print (query)
        return connectToMySQL('proyectogrupal').query_db(query, data)