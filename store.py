class Store:
    def __init__(self, product):
        self.product = list(product)

    def add_product(self, product):
        self.product.append(product)

    def remove_product(self, product):
        self.product.remove(product)

    def get_total_quantity(self):
        total_quantity = sum(product.get_quantity() for product in self.product if product.is_active())
        return int(total_quantity)

    def get_all_products(self):
        try:
            result = [product for product in self.product if product.is_active()]
            return result

        except AttributeError:
            pass

    def order(self, shopping_list):
        try:
            total_price = 0.0
            for product, quantity in shopping_list:
                if product in self.product:
                    total_price += product.buy(quantity)
            return total_price
        except TypeError:
            pass

    def list_product(self):
        result = [product.show() for product in self.product if product.is_active()]
        count = 1
        for i in result:
            print(f"{count}. {i}")
            count += 1
