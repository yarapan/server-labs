from Display import Display


class Author(Display):
    def __init__(self, id_author, first_name, last_name, birth_date, death_date=None, bio=None):
        self._id_author = id_author
        self._first_name = first_name
        self._last_name = last_name
        self._books = []
        self._birth_date = birth_date
        self._death_date = death_date
        self._bio = bio

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def add_book(self, book):
        self._books.append(book)
        book.author = self

    def display_info(self):
        return f"Автор: {self._first_name} {self._last_name}, Кількість книг: {len(self._books)}"
