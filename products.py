from promotions import Promotion


class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise TypeError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")

        self.name = str(name)
        self.price = int(price)
        self.quantity = float(quantity)
        self.active = True
        self.promotion = None

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
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "Promotion: None"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, {promotion_info}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity available for purchase.")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity
        self.quantity = self.quantity - float(quantity)
        return total_price

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        if isinstance(promotion, Promotion) or promotion is None:
            self.promotion = promotion
        else:
            raise ValueError("Invalid promotion type. Must be an instance of Promotion or None.")


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=float('inf'))

    def show(self):
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "Promotion: None"
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, {promotion_info}"

    def get_quantity(self):
        return 0


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "Promotion: None"
        return f"{self.name}, Price: ${self.price}, Limited to 1 per order!, {promotion_info}"

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError("Error while making order! Only 1 is allowed from this product!")
        return self.price
