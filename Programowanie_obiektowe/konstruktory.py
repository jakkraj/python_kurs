# Zad 1
import random


# Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order, Apple i Potato:

# Product: nazwa, nazwa kategorii, cena jednostkowa
# Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta), łączna cena (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
# Apple: nazwa gatunku, rozmiar, cena za kg
# Potato: nazwa gatunku, rozmiar, cena za kg

# Utwórz kilka obiektów każdej klasy.


# Zad 2
# Napisz funkcję wypisującą produkt i zamówienie. Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.


# Zad 3
# Napisz funkcję generującą zamówienie z losową listą produktów na przykład: Produkt-1, Produkt-2 itd.


# Zad 4
# Podziel projekt - utwórz nowy pakiet shop i przenieś do osobnych modułów (plików) w pakiecie store:
#
# Klasę Apple
# Klasę Potato
# Klasę Product oraz funkcje generujące i wypisujące produkt
# Klasę Order oraz funkcje generujące i wypisujące zamówienie
# Utwórz skrypt uruchomieniowy main, który importuje i wykorzystuje powyższe klasy i funkcje




class Product:
    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price

class Order:
    def __init__(self, first_name, last_name, list_of_products = None):
        if list_of_products is None:
            list_of_products = []
        self.list_of_products = list_of_products
        self.first_name = first_name
        self.last_name = last_name

        total_price = 0
        for product in list_of_products:
            total_price += product.unit_price
        self.total_price = total_price

class Apple:
    def __init__(self, spacies, size, unit_price):
        self.spacies = spacies
        self.size = size
        self.unit_price = unit_price

class Potato:
    def __init__(self, spacies, size, unit_price):
        self.spacies = spacies
        self.size = size
        self.unit_price = unit_price



# def run():
#     green_apple = Apple(spacies='Green', size='M', unit_price=1.5)
#     red_apple = Apple(spacies='Red', size='S', unit_price=1.8)
#     #print(green_apple.apple_spacies, green_apple)
#     #print(red_apple.apple_spacies, red_apple)
#
#     young_potato = Potato(spacies='Young', size='S', unit_price=1.2)
#     #print(young_potato.potato_spacies, young_potato)
#
#     cookies = Product(name='Cookies', category='Food', unit_price=5.5)
#     empty_order = Order(first_name='Jakub', last_name='Krajewski')
#     order = Order(first_name='Jakub', last_name='Krajewski', list_of_products=[cookies, cookies])
#     print_order(empty_order)
#     print_order(order)
#     # print(cookies)
#     # print(empty_order)
#     # print(order)


def print_product(product):
    print(f'Nazwa: {product.name}, kategoria: {product.category}, cena: {product.unit_price}')

def print_order(order):
    print('=' * 20)
    print(f'Imię: {order.first_name}, Nazwisko: {order.last_name}')
    print(f'Produkty: ')
    for product in order.list_of_products:
        print_product(product)
    print(f'Łączna wartość zamówienia: {order.total_price}')


def generate_order():
    number_of_product = random.randint(1, 10)
    products = []
    for product_number in range(number_of_product):
        product_name = f'Produkt-{product_number}'
        category_name = 'Inne'
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        products.append(product)

    order = Order(first_name='Jakub', last_name='Krajewski', list_of_products=products)
    return order

def run():
    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)

if __name__ == '__main__':
    run()
#     print('=========================')
#     print_product()

