from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Crearpago:
    def __init__(self, data):
        self.id = data['id']
        self.nro_factura = data['nro_factura']
        self.fecha_hora = data['fecha_hora']
        self.transaccion = data['transaccion']
        self.timbrado = data['timbrado']
        self.medio_pago_id = data['medio_pago_id']
        self.ordenes_id = data['ordenes_id']
        self.total = data['total']
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO pagos (nro_factura, fecha_hora, transaccion, timbrado, medio_pago_id, ordenes_id, total) VALUES (%(nro_factura)s, now(),%(transaccion)s,%(timbrado)s,%(medio_pago_id)s,%(ordenes_id)s,%(total)s);"
        return connectToMySQL('proyectogrupal').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pagos;"
        results = connectToMySQL('proyectogrupal').query_db(query)
        all_pagos= []
        for row in results:
            all_pagos.append( cls(row) )
            print(all_pagos)
        return all_pagos
    
    @classmethod
    def eliminar(cls,data):
        query = "DELETE FROM pagos WHERE id = %(id)s;"
        return connectToMySQL('proyectogrupal').query_db(query, data)
    
    @classmethod
    def actualizar(cls,data):
        query = "UPDATE pagos SET nro_factura=%(nro_factura)s, transaccion=%(transaccion)s,timbrado=%(timbrado)s,medio_pago_id=%(medio_pago_id)s,ordenes_id=%(ordenes_id)s,total=%(total)s WHERE id = %(id)s;"
        print (query)
        return connectToMySQL('proyectogrupal').query_db(query, data)