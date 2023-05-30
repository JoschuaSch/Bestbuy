class Product:
    """Class that represents a product in the store."""

    def __init__(self, name, price, quantity):
        """Initializes an instance of the Product class."""
        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid values.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Returns the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the quantity of the product."""
        if quantity < 0:
            raise Exception("Quantity can`t be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Reduces the quantity of the product and returns the total price."""
        if quantity > self.quantity:
            raise Exception("The quantity is not available.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return self.price * quantity




