def SelectOrder(orders,orders_type):
    "Возращает список операций"
    return []

def mask_Account(acc):
    return '** XXXX'


def mask_cart(cart):
    return 'XXXX XX** **** XXXX'

def printTopOrder(order_count=5):
    "Выводит заданое количество последних операций по указаному типу"
    print(f"hi{order_count}")
    return order_count

printTopOrder(8)