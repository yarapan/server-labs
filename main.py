def main():
    from Author import Author
    from Book import Book
    from Client import Client
    from Payment import Payment
    from Shipping import Shipping
    from Order import Order
    from datetime import date

    nova_poshta = Shipping(
        id_shipping=1, method_shipping="Нова Пошта", cost=70.00)
    ukr_poshta = Shipping(
        id_shipping=2, method_shipping="УкрПошта", cost=45.00)

    card_online = Payment(
        id_payment=1, method_payment="Онлайн карткою (LiqPay)")
    cash_delivery = Payment(
        id_payment=2, method_payment="Готівкою (Післяплата)")

    author1 = Author(id_author=1, first_name="Сергій",
                     last_name="Жадан", birth_date=date(1974, 8, 23))
    author2 = Author(id_author=2, first_name="Оксана",
                     last_name="Забужко", birth_date=date(1960, 9, 19))
    author3 = Author(id_author=3, first_name="Юрій",
                     last_name="Андрухович", birth_date=date(1960, 3, 13))

    book1 = Book(id_book=1, title='Інтернат',
                 isbn='978-617-7691-03-7', price=199.50, author=author1)
    book2 = Book(id_book=102, title="Ворошиловград",
                 isbn="978-617-7561-12-8", price=250.00, author=author1)
    book3 = Book(id_book=103, title="Польові дослідження українського сексу",
                 isbn="978-966-508-251-8", price=235.00, author=author2)
    book4 = Book(id_book=104, title="Дванадцять обручів",
                 isbn="978-966-03-2410-5", price=290.00, author=author3)

    author1.add_book(book1)
    author1.add_book(book2)
    author2.add_book(book3)
    author3.add_book(book4)

    client1 = Client(id_client=10, first_name="Іван", last_name="Мельник", phone="+380951112233",
                     email="ivan.melnyk@gmail.com", address="м. Львів, вул. Городоцька, 50")
    client2 = Client(id_client=11, first_name="Олена", last_name="Ковальчук",
                     phone="+380674445566", email="o.kovalchuk@i.ua", address="м. Київ, просп. Перемоги, 10")

    order1 = Order(id_order=1, client=client1,
                   payment=card_online, shipping=nova_poshta)
    order1.add_book(book1, quantity=1)
    order1.add_book(book4, quantity=1)

    order2 = Order(id_order=2, client=client2,
                   payment=card_online, shipping=nova_poshta)
    order2.add_book(book4, quantity=2)
    order2.add_book(book1, quantity=1)

    print("Деталі замовлення:")
    print(order1.display_info())
    print(f"Книги в замовленні:")
    for book, quantity in order1.items:
        print(f"   - {book.title} x {quantity} = {book.price * quantity} грн")

    print("="*40)
    print(order2.display_info())
    print(f"Книги в замовленні:")
    for book, quantity in order2.items:
        print(f"   - {book.title} x {quantity} = {book.price * quantity} грн")
    print("="*40)

    print("Каталог книг:")
    print(book1.display_info())
    print(book2.display_info())
    print(book3.display_info())
    print(book4.display_info())
    print("="*40)

    print("Зареєстровані клієнти:")
    print(client1.display_info())
    print("-" * 40)
    print(client2.display_info())
    print("-" * 40)


if __name__ == "__main__":
    main()
