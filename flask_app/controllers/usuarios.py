from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.usuario import Usuario

from flask_bcrypt import Bcrypt



bcrypt = Bcrypt(app)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registro', methods=['POST'])
def registro():
    if not Usuario.validar_registro(request.form):
        return redirect('/registrar')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "level": request.form['level'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = Usuario.save(data)
    session['user_id'] = id

    return redirect('/pagina1')


@app.route('/registrar')
def registrar():
    return render_template("registros.html")

@app.route('/ingreso', methods=['POST'])
def ingreso():
    user = Usuario.traer_email(request.form)

    if not user:
        flash("El correo no es valido, verifique!", "ingreso")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("La contraseña no corresponde", "ingreso")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/pagina1')

@app.route('/pagina1')
def pagina1():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        'id': session['user_id']
    }
    return render_template("pagina1.html", user=Usuario.traer_id(data))


@app.route('/inisesion')
def inisesion():
    session.clear()
    return redirect('/')
