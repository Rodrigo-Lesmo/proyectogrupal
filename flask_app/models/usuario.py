from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re  # the regex module
# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Usuario:
    db = "proyectogrupal"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.level = data['level']
        self.created_up = data['created_up']
        self.updated_up = data['updated_up']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (first_name,last_name,email,password,level) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,3)"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def traer_todo(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def traer_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(query)

        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def traer_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    @staticmethod
    def validar_registro(usuario):
        is_valid = True
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(Usuario.db).query_db(query, usuario)
        if len(results) >= 1:
            flash("El correo ya existe!!!", "registro")
            is_valid = False
        if not EMAIL_REGEX.match(usuario['email']):
            flash("El email no es valido!!!", "registro")
            is_valid = False
        if len(usuario['first_name']) < 2:
            flash("Su nombre debe tener por lo menos 3 caracteres", "registro")
            is_valid = False
        if len(usuario['last_name']) < 2:
            flash("Su apellido debe tener por lo menos 3 caracteres", "registro")
            is_valid = False
        if len(usuario['password']) < 8:
            flash("La contraseña debe tenr por lo menos 8 caracteres", "registro")
            is_valid = False
        if usuario['password'] != usuario['confirm']:
            flash("Las contraseñas no coinciden", "registro")
    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM actividades LEFT JOIN usuarios  on usuarios.id = actividades.usuario_id;"
        user1 = []
        results = connectToMySQL('bdproyecto').query_db(query,data)
        for row in results:
            user1.append(cls(row))
        return user1
