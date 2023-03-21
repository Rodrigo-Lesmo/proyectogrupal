from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.estado import Estado
from flask_app.models.usuario import Usuario


@app.route('/estado')
def estado():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": session['user_id']
    }
    return render_template('estados.html', usuario=Usuario.traer_id(data), estado1=Estado.traer_todo())
    #return render_template('agregar.html', usuarios=usuario.Usuario.traer_todo())

@app.route('/estado/agregar', methods=['POST'])
def crear_estado():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Estado.validar_estado(request.form):
        return redirect('/estado')
    data = {
        "descripcion": request.form["descripcion"]
    }
    Estado.save(data)
    return redirect('/estado')


@app.route('/estado/hacer/<int:id>')
def hacer_estado(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("estado.html", estado=Estado.trae_uno(data), user=Usuario.traer_id(user_data))


@app.route('/estado/modificar/<int:id>')
def modificar_estado(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("modificar_estado.html", modificar_estado=Estado.trae_uno(data), user=Usuario.traer_id(user_data))


@app.route('/actualizar/estado', methods=['POST'])
def actualizar_estado():
    if 'user_id' not in session:
        return redirect('/inisesion')
    if not Estado.validar_estado(request.form):
        return redirect('/estado')
    data = {
        "descripcion": request.form["descripcion"],
        "id": request.form['id']
    }
    Estado.actualizar(data)
    return redirect('/estado')


@app.route('/estado/eliminar/<int:id>')
def eliminar_estado(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    Estado.eliminar(data)
    return redirect('/estado')




@app.route('/estado/mostrar/<int:id>')
def mostrar_estado(id):
            if 'user_id' not in session:
                return redirect('/inisesion')
            data = {
                "id": id
            }
            user_data = {
                "id": session['user_id']
            }
            return render_template("mostrar_resultados.html", estado_reg=Estado.traer_todo_estados(data), user=Usuario.traer_id(user_data))
