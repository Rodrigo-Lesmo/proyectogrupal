from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.orden import Orden
from flask_app.models.usuario import Usuario
from flask_app.models.servicio_select import Orden_ser
from flask_app.models.servicio_select import Orden_clien




@app.route('/orden')
def orden():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": session['user_id']
    }
    return render_template('ordenes.html', usuario=Usuario.traer_id(data), orden1=Orden.traer_todo(), servicio=Orden_ser.traer_servicios(), cliente=Orden_clien.traer_clientes())


@app.route('/orden_ope')
def orden_ope():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": session['user_id']
    }
    return render_template('ordenes_ope.html', usuario=Usuario.traer_id(data), orden1=Orden.traer_todo(), servicio=Orden_ser.traer_servicios(), cliente=Orden_clien.traer_clientes())


@app.route('/orden/agregar', methods=['POST'])
def crear_orden():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Orden.validar_orden(request.form):
        return redirect('/orden')
    data = {
        "fecha_time": request.form["fecha_time"],
        "total": request.form["total"],
        "cant": request.form["cant"],
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
    return render_template("modificar_ordenes.html", modificar_orden=Orden.trae_uno(data), user=Usuario.traer_id(user_data), cliente=Orden_clien.traer_clientes(), servicio=Orden_ser.traer_servicios())


@app.route('/orden/modificar_ope/<int:id>')
def modificar_orden_ope(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("modificar_ordenes_ope.html", modificar_orden=Orden.trae_uno(data), user=Usuario.traer_id(user_data), cliente=Orden_clien.traer_clientes(), servicio=Orden_ser.traer_servicios())

@app.route('/actualizar/orden', methods=['POST'])
def actualizar_orden():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Orden.validar_orden(request.form):
        return redirect('/orden')
    data = {
        "total": request.form["total"],
        "usuario_id": request.form["usuario_id"],
        "cliente_id": request.form["cliente_id"],
        "servicio_id": request.form["servicio_id"],
        "estado_id": request.form["estado_id"],
        "updated_up": request.form["updated_up"],
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
            return render_template("mostrar_ordenes.html", orden_mostrar=Orden.traer_todo_ordenes(data), user=Usuario.traer_id(user_data))
