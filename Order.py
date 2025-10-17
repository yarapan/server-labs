from datetime import date
from Display import Display


class Order(Display):
    def __init__(self, id_order, client, payment, shipping, order_date=None):
        self._id_order = id_order
        self._client = client
        self._payment = payment
        self._shipping = shipping
        self._order_date = order_date if order_date else date.today()
        self._items = []
        self._total_pay = 0.0

    def _calculate_cost(self):
        return sum(book.price * quantity for book, quantity in self._items) + self._shipping.cost

    def add_book(self, book, quantity):
        self._items.append((book, quantity))
        self._total_pay = self._calculate_cost()

    @property
    def total_pay(self):
        return self._total_pay

    @property
    def items(self):
        return self._items

    @property
    def client(self):
        return self._client

    @property
    def payment(self):
        return self._payment

    @property
    def shipping(self):
        return self._shipping

    def display_info(self):
        return (
            f"Замовлення №{self._id_order}: {self._client.first_name} {self._client.last_name} | "
            f"Сума (з доставкою): {self.total_pay} грн | "
            f"Доставка: {self._shipping.method_shipping} ({self._shipping.cost} грн) | "
            f"Оплата: {self._payment.method_payment}"
        )
