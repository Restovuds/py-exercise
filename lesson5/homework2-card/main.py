from cart import Cart
from product import Product
from customer import Customer


if __name__ == '__main__':
    try:
        product_1 = Product('Banana', 57.80)
        product_2 = Product('Strawberry', 259)
        product_3 = Product('Milk', 36)

        customer_1 = Customer('Oleh', 'Radchenko', "348973459708")
        customer_2 = Customer('Dmitri', 'Rayko', "239082394803")

        card_1 = Cart(customer_1)
        card_2 = Cart(customer_2)

        card_1.add_product(product_1, 2)
        card_1.add_product(product_2, 0.3)

        card_2.add_product(product_1, 0.65)
        card_2.add_product(product_2, 3)
        card_2.add_product(product_3, 2)

        print(card_1)
        print(card_2)
    except (TypeError, ValueError) as err:
        print(err)





