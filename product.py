import Pyro5.api


@Pyro5.api.expose
class Product:
    def __init__(self, name, description, price):
        self._name = name
        self._description = description
        self._price = price

    def get_name(self):            # Java: String getName()
        return self._name

    def get_description(self):     # Java: String getDescription()
        return self._description

    def get_price(self):           # Java: double getPrice()
        return self._price
