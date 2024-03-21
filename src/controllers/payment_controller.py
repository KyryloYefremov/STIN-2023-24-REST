import json
from datetime import datetime
from src.tools.converter import json_to_xml
from src.models.payment import Payment


class PaymentController:
    """
    Controller that handles the payment process
    """

    def proceed_payment(self, payload: json) -> None:
        """
        Gets the payload and proceeds the payment based on the payment type
        :param payload: json that contains the payment details
        (amount, currency, payment_type, date, item_list)
        """

        payment = self._create_payment(payload)

        if payment.payment_type == 'card':
            self._pay(payment.amount, payment.currency)
        elif payment.payment_type == 'cash':
            del payload['item_list']
            xml_data = json_to_xml({"root": payload})
            self._cash(xml_data)
        else:
            raise ValueError('Invalid payment type')

    @staticmethod
    def _create_payment(payload: json) -> Payment:
        """
        Validates the payload and creates a Payment object
        :param payload: json that contains the payment details
        :return: Payment object
        """

        if payload['amount'] <= 0:
            raise ValueError('Amount must be greater than 0')
        if not payload['currency']:
            raise ValueError('Currency must not be empty')
        if not payload['payment_type']:
            raise ValueError('Payment type must not be empty')
        if not payload['date']:
            payload['date'] = datetime.now().strftime("%d.%m.%Y")

        return Payment(**payload)

    @staticmethod
    def _pay(amount: float, currency: str) -> None:
        """
        Makes a card payment with the given amount and currency
        :param amount: payment value
        :param currency: payment currency
        """
        print(f"{amount} / {currency}")

    @staticmethod
    def _cash(xml_data):
        """
        Makes a cash payment with the given xml data
        :param xml_data: payment details in xml format
        """
        print(xml_data)
