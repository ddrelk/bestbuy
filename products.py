class Product:

    def __init__(self, name, price, quantity):
        try:
            if not name:
                raise ValueError("Name cannot be empty.")
            if price < 0:
                raise ValueError("Price cannot be negative.")
            if quantity <= 0:
                raise ValueError("Quantity must be a positive number.")
            self.name = str(name)
            self.price = int(price)
            self.quantity = float(quantity)
            self.active = True
        except ValueError as err:
            print("Error creating product:", str(err))

    def get_quantity(self):
        return float(self.quantity)

    def set_quantity(self, quantity):
        if quantity <= 0:
            self.active = False
        self.quantity += quantity

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def is_active(self):
        if self.quantity > 0:
            return True
        else:
            return False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        try:
            if quantity > self.quantity:
                raise ValueError("Insufficient quantity available for purchase.")
            self.quantity = self.quantity - float(quantity)
            total_price = self.price * quantity
            return total_price
        except ValueError as err:
            print("Error during purchase:", str(err))
