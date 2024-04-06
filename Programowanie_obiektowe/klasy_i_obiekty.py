class Product:
    pass

class Order:
    pass

class Apple:
    pass

class Potato:
    pass


if __name__ == '__main__':

    champion = Apple()
    green_apple = Apple()

    potato = Potato()
    sweet_potato = Potato()


    # apple_list = [Apple, Apple, Apple]
    # potato_list = [Potato, Potato, Potato, Potato]

    print(type(champion))

    orders = [Order(), Order(), Order(), Order(), Order()]

    print(orders)


    products = {
        'champion': Product(),
        'green_apple': Product(),
        'potato': Product(),
        'sweet_potato': Product()
    }

    print(products)