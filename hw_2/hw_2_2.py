import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json', 'a') as f:
        json.dump(order, f, indent=4)


write_order_to_json('item_1', 1, 100, 'user_1', '01.01.2021')
