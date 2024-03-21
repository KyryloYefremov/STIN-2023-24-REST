from flask import Flask, request
from datetime import datetime

from src.controllers.payment_controller import PaymentController

app = Flask(__name__)
payment_controller = PaymentController()


@app.route("/")
def home():
    return "<h1> Hello Flask </h1>"


@app.route("/time")
def get_time():
    return str(datetime.now()) + "\n"


@app.route("/pay", methods=['POST'])
def pay():
    payload = request.json
    try:
        payment_controller.proceed_payment(payload)
    except ValueError as e:
        response = {
            'status': '400',
            'message': str(e)
        }
    else:
        response = {
            'status': '200',
            'message': 'Payment Successful'
        }

    return response


if __name__ == '__main__':
    app.run(port=8080)
