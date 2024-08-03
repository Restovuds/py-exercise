class Order:
    def __init__(self, order_no, buyer_no):
        self.order_no = order_no
        self.buyer_no = buyer_no
        self.goods_list = []

    def __str__(self):
        res = f'order No: {self.order_no}'
        res += f'\nBuyer No: {self.buyer_no}\n'
        res += '\n'.join(map(str, self.goods_list))
        return res


order1 = Order(order_no=534872346, buyer_no=6236)
order1.goods_list = [[1, "Keyboard"], [2, "Mouse"], [3, "Microphone"]]

print(order1)
