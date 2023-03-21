from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.orden import Orden
from flask_app.models.usuario import Usuario


@app.route('/orden')
def orden():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": session['user_id']
    }
    return render_template('ordenes.html', usuario=Usuario.traer_id(data), orden1=Orden.traer_todo())
    #return render_template('agregar.html', usuarios=usuario.Usuario.traer_todo())


@app.route('/orden/agregar', methods=['POST'])
def crear_orden():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Orden.validar_orden(request.form):
        return redirect('/orden')
    data = {
        "fecha_time": request.form["fecha_time"],
        "total": request.form["total"],
        "usuario_id": request.form["usuario_id"],
        "cliente_id": request.form["cliente_id"],
        "servicio_id": request.form["servicio_id"],
        "estado_id": request.form["estado_id"]
    }
    Orden.save(data)
    return redirect('/orden')


@app.route('/orden/hacer/<int:id>')
def hacer_orden(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("orden1.html", orden=Orden.trae_uno(data), user=Usuario.traer_id(user_data))


@app.route('/orden/modificar/<int:id>')
def modificar_orden(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("modificar_orden.html", modificar_orden=Orden.trae_uno(data), user=Usuario.traer_id(user_data))


@app.route('/actualizar/orden', methods=['POST'])
def actualizar_orden():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Orden.validar_orden(request.form):
        return redirect('/orden')
    data = {
        "fecha_time": request.form["fecha_time"],
        "total": request.form["total"],
        "usuario_id": request.form["usuario_id"],
        "cliente_id": request.form["cliente_id"],
        "servicio_id": request.form["servicio_id"],
        "estado_id": request.form["estado_id"],
        "id": request.form['id']
    }
    Orden.actualizar(data)
    return redirect('/orden')


@app.route('/orden/eliminar/<int:id>')
def eliminar_orden(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    Orden.eliminar(data)
    return redirect('/orden')




@app.route('/orden/mostrar/<int:id>')
def mostrar_orden(id):
            if 'user_id' not in session:
                return redirect('/inisesion')
            data = {
                "id": id
            }
            user_data = {
                "id": session['user_id']
            }
            return render_template("mostrar_ordenes.html", orden_reg=Orden.traer_todo_ordenes(data), user=Usuario.traer_id(user_data))
