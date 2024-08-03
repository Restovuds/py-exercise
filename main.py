class Goods:
    """
    Class implements methods and data about some goods
    """
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.photo = None
        self.dimensions = {
            "height": dimensions[0],
            "width": dimensions[1],
            "length": dimensions[2]
        }

    def __str__(self):
        res = f'Name: {self.name}\n'
        res += f'Price: {self.price}\n'
        res += f'Description: {self.description}\n'
        res += f'Photo: {self.photo}\n'
        res += f'Dimensions: {self.dimensions}\n'
        res += f'Volume: {self._get_volume()}'
        return res

    def _get_volume(self):
        return self.dimensions["length"] * self.dimensions["width"] * self.dimensions["height"]


goods1 = Goods('Mouse', 1300, "Bloody gaming max 10k sensor", [10, 15, 7.5])
goods2 = Goods('Keyboard', 2500, "Hator rockfall evo TCL", [5, 15, 30])

print(goods1)
print(goods2)
