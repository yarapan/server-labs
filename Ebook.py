import Digital
import Book


class Ebook(Digital, Book):
    def __init__(self, id_book, title, isbn, price, author, file_format, file_size_mb):

        Book.__init__(self, id_book, title, isbn, price, author)
        Digital.__init__(self, file_format, file_size_mb)

    def display_info(self):
        book_info = Book.display_info(self)
        digital_info = Digital.display_info(self)
        return f"{book_info} | {digital_info}"
