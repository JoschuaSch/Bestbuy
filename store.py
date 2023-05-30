class Store:
    """Store class which represents a store with a list of products."""

    def __init__(self, product_list):
        """Initializes an instance of the Store class."""
        self.product_list = product_list

    def add_product(self, product):
        """Adds a new product to the store."""
        self.product_list.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.product_list.remove(product)

    def get_total_quantity(self):
        """Returns the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self):
        """Returns all active products in the store."""
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list):
        """Places an order for a list of products and returns the total price."""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price