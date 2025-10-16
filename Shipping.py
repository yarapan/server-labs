from Display import Display


class Shipping(Display):
    def __init__(self, id_shipping, method_shipping, cost):
        self._id_shipping = id_shipping
        self._method_shipping = method_shipping
        self._cost = cost

    @property
    def id_shipping(self):
        return self._id_shipping

    @property
    def method_shipping(self):
        return self._method_shipping

    @property
    def cost(self):
        return self._cost

    def display_info(self):
        return f"Доставка\nid: {self._id_shipping}, Спосіб: {self._method_shipping}"
