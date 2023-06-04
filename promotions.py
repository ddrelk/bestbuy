from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        normal_price = product.price * quantity
        discounted_price = (self.percent * normal_price) / 100
        total_price = normal_price - discounted_price
        return total_price


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = quantity - quantity // 2
        half_price_items = quantity // 2
        total_price = (full_price_items * product.price) + (half_price_items * product.price / 2)
        return total_price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        total_price = (quantity - free_items) * product.price
        return total_price
