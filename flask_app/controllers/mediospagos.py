from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.crearpago import Crearpago
from flask_app.models.mediopago import Mediopago
from flask_app.models.usuario import Usuario


@app.route('/medio-pago')
def mediospagos():
    if 'user_id' not in session:
        return redirect('/inisesion')
    return render_template('medios-pagos.html', medios=Mediopago.get_all())

@app.route('/medio/agregar', methods=['POST'])
def crearmedio():
    data = {
        "medio": request.form["medio"]
    }
    Mediopago.save(data)
    return redirect('/medio-pago')

@app.route('/medio/eliminar/<int:id>')
def eliminar_medio(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    Mediopago.eliminar(data)
    return redirect('/medio-pago')

@app.route('/pago/modificar/<int:id>')
def modificar_medio(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    
    return render_template("modificar-medio.html", modificar_medio=Mediopago.get_by_id(data))


@app.route('/actualizar/medio', methods=['POST'])
def actualizar_medio():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "medio": request.form["medio"],
        "id" : request.form["id"]
    }
    Mediopago.actualizar(data)
    return redirect('/medio-pago')