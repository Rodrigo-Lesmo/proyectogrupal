from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.cliente import Cliente
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt
import re



bcrypt = Bcrypt(app)

@app.route('/cliente')
def cliente():
    return render_template('clientes.html')
data={}
@app.route('/cliente/save',methods=['POST'])
def save_cliente():
    print("MIRAR: ")
    print(request.form)
    id = str(Cliente.save(request.form))
    return redirect('/cliente/'+id)

@app.route('/cliente/<int:id>')
def cliente_view(id):
    data ={"id":id}
    txt="https://www.google.com/maps?q=-25.5350484,-54.6279505&z=17&hl=es"
    y=re.findall("(\-(\d+(?:[\.\,]\d{7})?))|((\d+(?:[\.\,]\d{7})?))",txt)
    cliente = Cliente.traer_por_id(data)
    
    cliente['lat'] = y[0][0]
    cliente['long'] = y[1][0]
    return render_template("cliente-VIEW.html",cliente=cliente)

@app.route('/map')
def mapa():
   
    #txt = "https://www.google.com/maps?q=-25.4038088,-54.6216586&z=17&hl=es"
    txt="https://www.google.com/maps?q=-25.5350484,-54.6279505&z=17&hl=es"
    y=re.findall("(\-(\d+(?:[\.\,]\d{7})?))|((\d+(?:[\.\,]\d{7})?))",txt)
    print(y[0][0])
    print(y[1][0])
    
    return render_template('mapa.html')

@app.route('/registros', methods=['POST'])
def registros():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "address": request.form['address'],
        "location": request.form['location'],
        "phone": request.form['phone'],
    }
    return redirect('/cliente')
