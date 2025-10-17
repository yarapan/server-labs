from Display import Display


class Client(Display):
    def __init__(self, id_client, first_name, last_name, phone, email, address):
        self._id_client = id_client
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._email = email
        self._address = address

    @property
    def id_client(self):
        return self._id_client

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone(self):
        return self._phone

    @property
    def email(self):
        return self._email

    @property
    def address(self):
        return self._address

    def display_info(self):
        return (f"Клієнт №{self._id_client} | {self._first_name} {self._last_name}\n|"
                f"Телефон: {self._phone}| Пошта: {self._email}|Адреса: {self._address}")
