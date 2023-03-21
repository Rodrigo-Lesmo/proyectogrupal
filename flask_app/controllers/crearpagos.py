from flask import render_template, redirect, request, session, flash, jsonify
from flask_app import app
from flask_app.models.crearpago import Crearpago
from flask_app.models.usuario import Usuario
from flask_app.models.orden import Orden
from flask_app.models.mediopago import Mediopago
import requests
from requests.auth import HTTPBasicAuth
import os

PAYPAL_API_URL = f"https://api-m.sandbox.paypal.com"



# PAYPAL payment price
IB_TAX_APP_PRICE = float(20.00)
IB_TAX_APP_PRICE_CURRENCY = "USD"


@app.route('/crear-pago')
def crearpago():
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": session['user_id']
    }
    return render_template('crear-pago.html', paypal_business_client_id= os.environ.get("PAYPAL_BUSINESS_CLIENT_ID"),
                           price=IB_TAX_APP_PRICE, currency=IB_TAX_APP_PRICE_CURRENCY, ordenes=Orden.get_all(), medio=Mediopago.get_all(),
                           pagos=Crearpago.get_all(),usuario=Usuario.traer_id(data))

@app.route('/pago/agregar', methods=['POST'])
def crear_pago():
    data = {
        "nro_factura" : request.form['nro_factura'],
        "transaccion" : request.form['transaccion'],
        "timbrado" : request.form['timbrado'],
        "medio_pago_id" : request.form['medio_pago_id'],
        "ordenes_id" : request.form['ordenes_id'],
        "total" : request.form['total']
    }
    Crearpago.save(data)
    return redirect('/crear-pago')

@app.route('/pago/eliminar/<int:id>')
def eliminar_pago(id):
    if 'user_id' not in session:
        return redirect('/inisesion')
    data = {
        "id": id
    }
    Crearpago.eliminar(data)
    return redirect('/crear-pago')



@app.route("/payment/<order_id>/capture", methods=["POST"])
def capture_payment(order_id):  # Checks and confirms payment
    captured_payment = paypal_capture_function(order_id)
    if is_approved_payment(captured_payment):
        # Do something (for example Update user field)
        return jsonify(captured_payment)
    


def paypal_capture_function(order_id):
    post_route = f"/v2/checkout/orders/{order_id}/capture"
    paypal_capture_url = PAYPAL_API_URL + post_route
    basic_auth = HTTPBasicAuth(
        os.environ.get("PAYPAL_BUSINESS_CLIENT_ID"), os.environ.get("PAYPAL_BUSINESS_SECRET"))
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url=paypal_capture_url,
                             headers=headers, auth=basic_auth)
    response.raise_for_status()
    json_data = response.json()
    return json_data


def is_approved_payment(captured_payment):
    status = captured_payment.get("status")
    amount = captured_payment.get("purchase_units")[0].get(
        "payments").get("captures")[0].get("amount").get("value")
    currency_code = captured_payment.get("purchase_units")[0].get("payments").get("captures")[0].get("amount").get(
        "currency_code")
    transaction_id = captured_payment.get("purchase_units")[0].get(
        "payments").get("captures")[0].get("id")
    session['transaccion'] = transaction_id
    print(f"Payment happened. Details: {status}, {amount}, {currency_code}, {transaction_id}")
    return redirect('/crear-pago')


    
