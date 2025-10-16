from Display import Display


class Payment(Display):
    def __init__(self, id_payment, method_payment):
        self._id_payment = id_payment
        self._method_payment = method_payment

    @property
    def id_payment(self):
        return self._id_payment

    @property
    def method_payment(self):
        return self._method_payment

    def display_info(self):
        return f"Оплата\nid: {self._id_payment}, Спосіб: {self._method_payment}"
