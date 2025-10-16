from Display import Display


class Book(Display):
    def __init__(self, id_book, title, isbn, price, author):
        self._id_book = id_book
        self._title = title
        self._isbn = isbn
        self.price = price
        self._author = author
        self._genres = []

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Ціна повинна бути більша за 0")
        self._price = value

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    def add_genre(self, genre):
        self._genres.append(genre)

    def display_info(self):
        author_name = f"{self._author.first_name} {self._author.last_name}"
        return f"Книга: «{self._title}» (Автор: {author_name}) (Ціна: {self._price} грн)"
