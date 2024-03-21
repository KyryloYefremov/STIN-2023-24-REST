from dataclasses import dataclass


@dataclass
class Payment:
    """
    Dataclass that represents a payment
    """
    amount: float
    currency: str
    payment_type: str
    date: str
    item_list: list[str]
