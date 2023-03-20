from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.servicio import Servicio
from flask_app.models.usuario import Usuario


@app.route('/servicio')
def servicio():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": session['user_id']
    }
    return render_template('servicios.html', usuario=Usuario.traer_id(data), servicio1=Servicio.traer_todo())
    #return render_template('agregar.html', usuarios=usuario.Usuario.traer_todo())

@app.route('/servicio/agregar', methods=['POST'])
def crear_servicio():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Servicio.validar_servicio(request.form):
        return redirect('/servicio')
    data = {
        "service_name": request.form["service_name"],
        "description": request.form["description"],
        "precio": request.form["precio"]
    }
    Servicio.save(data)
    return redirect('/servicio')


@app.route('/servicio/hacer/<int:id>')
def hacer_servicio(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("servicio1.html", servicio=Servicio.trae_uno(data), user=Usuario.traer_id(user_data))


@app.route('/servicio/modificar/<int:id>')
def modificar_servicio(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("modificar_servicio.html", modificar_servicio=Servicio.trae_uno(data), user=Usuario.traer_id(user_data))


@app.route('/actualizar/servicio', methods=['POST'])
def actualizar_servicio():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Servicio.validar_servicio(request.form):
        return redirect('/servicio')
    data = {
        "service_name": request.form["service_name"],
        "description": request.form["description"],
        "precio": (request.form["precio"]),
        "id": request.form['id']
    }
    Servicio.actualizar(data)
    return redirect('/servicio')


@app.route('/servicio/eliminar/<int:id>')
def eliminar_servicio(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    Servicio.eliminar(data)
    return redirect('/servicio')


@app.route('/registro/agregar', methods=['POST'])
def crear_registro():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Registro.validar_registro(request.form):
        return redirect('/servicio')
    data = {
        "service_name": request.form["service_name"],
        "description": request.form["description"],
        "precio": request.form["precio"],
        "user_id": session["user_id"]
    }
    Registro.save(data)
    return redirect('/servicio')

@app.route('/servicio/mostrar/<int:id>')
def mostrar_registro(id):
            if 'user_id' not in session:
                return redirect('/inisesion')
            data = {
                "id": id
            }
            user_data = {
                "id": session['user_id']
            }
            return render_template("mostrar_resultados.html", servicio_reg=Servicio.traer_todo_servicios(data), user=Usuario.traer_id(user_data))
