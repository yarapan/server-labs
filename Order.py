from Client import Client
from Payment import Payment
from Shipping import Shipping
from Display import Display
from datetime import date


class Order(Client, Shipping, Payment, Display):
    def __init__(self, id_order, client: Client, payment: Payment, shipping: Shipping, order_date=None):
        self._id_order = id_order
        self.order_date = order_date if order_date else date.today()
        self._items = []
        self._total_pay = 0.0

        Client.__init__(self, client.id_client, client.first_name, client.last_name,
                        client.phone, client.email, client.address)
        Payment.__init__(self, payment.id_payment, payment.method_payment)
        Shipping.__init__(self, shipping.id_shipping,
                          shipping.method_shipping, shipping.cost)

    def _calculate_cost(self):
        return sum(book.price * quantity for book, quantity in self._items) + self.cost

    def add_book(self, book, quantity):
        self._items.append((book, quantity))
        self._total_pay = self._calculate_cost()

    @property
    def total_pay(self):
        return self._total_pay

    @property
    def items(self):
        return self._items

    def display_info(self):
        return (f"Замовлення №{self._id_order}: {self.first_name} {self.last_name} | "
                f"Сума (з доставкою): {self.total_pay} грн | "
                f"Доставка: {self.method_shipping} ({self.cost} грн) | Оплата: {self.method_payment}")
