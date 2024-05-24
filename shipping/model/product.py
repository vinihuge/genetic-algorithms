

class Product:

    def __init__(self, name: str, space: float, value: float):
        self.name = name
        self.space = space
        self.value = value

    def __repr__(self):
        return self.name + " - " + str(self.space) + " - " + str(self.value)

    def __str__(self):
        return self.name + " - " + str(self.space) + " - " + str(self.value)


PRODUCTS = [
    Product("Geladeira Dako", 0.751, 999.90),
    Product("Iphone 6", 0.0000899, 2911.12),
    Product("Iphone X", 0.0000899, 3911.12),
    Product("TV 55' ", 0.400, 4346.99),
    Product("TV 50' ", 0.290, 3999.90),
    Product("TV 42' ", 0.200, 2999.00),
    Product("TV 32' ", 0.180, 2499.00),
    Product("Notebook Dell", 0.00350, 2499.90),
    Product("Ventilador Panasonic", 0.496, 199.90),
    Product("Microondas Electrolux", 0.0424, 308.66),
    Product("Microondas LG", 0.0544, 429.90),
    Product("Microondas Panasonic", 0.0319, 299.29),
    Product("Geladeira Brastemp", 0.635, 849.00),
    Product("Geladeira Consul", 0.870, 1199.89),
    Product("Notebook Lenovo", 0.498, 1999.90),
    Product("Notebook Asus", 0.527, 3999.00),
]

    