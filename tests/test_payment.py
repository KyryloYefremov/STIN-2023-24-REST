import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.controllers.payment_controller import PaymentController
from src.app import app


def test_proceed_payment_valid_card():
    """
    Test the proceed_payment method with valid card payment
    """
    payload = {
        "amount": 100,
        "currency": "USD",
        "payment_type": "card",
        "date": "01.01.2021",
        "item_list": ["item1", "item2"]
    }
    payment_controller = PaymentController()
    assert payment_controller.proceed_payment(payload) is None


def test_proceed_payment_empty_payment_type():
    """
    Test the proceed_payment method with non-valid payment (no type specified)
    """
    payload = {
        "amount": 100,
        "currency": "USD",
        "payment_type": "",
        "date": "01.01.2021",
        "item_list": ["item1", "item2"]
    }
    payment_controller = PaymentController()
    with pytest.raises(ValueError):
        payment_controller.proceed_payment(payload)


def test_proceed_payment_valid_cash():
    """
    Test the proceed_payment method with valid cash payment
    """
    payload = {
        "amount": 100,
        "currency": "USD",
        "payment_type": "cash",
        "date": "01.01.2021",
        "item_list": ["item1", "item2"]
    }
    payment_controller = PaymentController()
    assert payment_controller.proceed_payment(payload) is None


def test_proceed_payment_invalid_payment_type():
    """
    Test the proceed_payment method with invalid payment type
    """
    payload = {
        "amount": 100,
        "currency": "USD",
        "payment_type": "asqcsaw",
        "date": "01.01.2021",
        "item_list": ["item1", "item2"]
    }
    payment_controller = PaymentController()
    with pytest.raises(ValueError):
        payment_controller.proceed_payment(payload)


def test_create_payment_valid():
    """
    Test the create_payment method with valid payload
    """
    payload = {
        "amount": 100,
        "currency": "USD",
        "payment_type": "card",
        "date": "01.01.2021",
        "item_list": ["item1", "item2"]
    }
    payment_controller = PaymentController()
    assert payment_controller._create_payment(payload) is not None


def test_create_payment_invalid_amount():
    """
    Test the create_payment method with invalid amount
    """
    payload = {
        "amount": -100,
        "currency": "USD",
        "payment_type": "card",
        "date": "01.01.2021",
        "item_list": ["item1", "item2"]
    }
    payment_controller = PaymentController()
    with pytest.raises(ValueError):
        payment_controller._create_payment(payload)


def test_create_payment_empty_currency():
    """
    Test the create_payment method with empty currency
    """
    payload = {
        "amount": 100,
        "currency": "",
        "payment_type": "card",
        "date": "01.01.2021",
        "item_list": ["item1", "item2"]
    }
    payment_controller = PaymentController()
    with pytest.raises(ValueError):
        payment_controller._create_payment(payload)


def test_create_payment_empty_date():
    """
    Test the create_payment method with empty date
    """
    payload = {
        "amount": 100,
        "currency": "USD",
        "payment_type": "card",
        "date": "",
        "item_list": ["item1", "item2"]
    }
    payment_controller = PaymentController()
    assert payment_controller._create_payment(payload) is not None
    assert payment_controller._create_payment(payload).date is not None
    assert payment_controller._create_payment(payload).date != ""


def test_app_get_time():
    """
    Test the get_time method from the app
    """
    with app.test_client() as c:
        response = c.get('/time')
        assert response.status_code == 200
        assert response.data is not None


