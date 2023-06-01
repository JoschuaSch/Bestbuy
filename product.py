from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract base class representing a product."""

    def __init__(self, name, price, quantity, promotions=None):
        if promotions is None:
            promotions = []
        if not name:
            raise Exception("Product name can´t be empty!")
        if price < 0:
            raise Exception("Product price can´t be negative!!")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotions = promotions

    def set_promotions(self, promotions):
        """Sets the promotions for the product."""
        self.promotions = promotions

    @abstractmethod
    def buy(self, quantity):
        """Abstract method to buy a product."""
        pass

    @abstractmethod
    def is_active(self):
        """Abstract method to check if a product is active."""
        pass

    def show(self, index):
        """Shows the product information with index number."""
        quantity_str = 'Unlimited' if self.quantity is None or self.quantity == float('inf') else self.quantity
        promotion_names = ', '.join(promotion.name for promotion in self.promotions)
        if not promotion_names:
            promotion_names = "None"
        if self.name == "Shipping":
            quantity_info = "Limited to 1 per order!"
        else:
            quantity_info = f"Quantity: {quantity_str}"
        return f"{index}. {self.name}, Price: ${self.price}, {quantity_info}, Promotion: {promotion_names}"

    def get_promotions(self):
        """Returns the promotions for the product."""
        return self.promotions

    def clear_promotions(self):
        """Clears all the promotions for the product."""
        self.promotions = []


class NonStockedProduct(Product):
    """Class representing a non-stocked product."""

    def buy(self, quantity):
        """Buys a non-stocked product."""
        if self.promotions:
            min_price = min([promotion.apply_promotion(self, quantity) for promotion in self.promotions])
            return min_price * quantity
        else:
            return self.price * quantity

    def is_active(self):
        """Returns whether the product is active."""
        return True


class LimitedProduct(Product):
    """Class representing a limited product."""

    def __init__(self, name, price, quantity, max_quantity, promotions=None):
        super().__init__(name, price, quantity, promotions)
        if quantity < 0:
            raise Exception("Quantity can't be negative")
        self.max_quantity = max_quantity

    def buy(self, quantity):
        """Buys a stocked product."""
        if self.quantity >= quantity:
            self.quantity -= quantity
            total_price = 0
            if self.promotions:
                prices = [promotion.apply_promotion(self, quantity) for promotion in self.promotions]
                total_price = min(prices)
            else:
                total_price = self.price * quantity
            return total_price
        else:
            raise Exception("Not enough quantity in stock!")

    def is_active(self):
        """Returns whether the product is active."""
        return self.quantity > 0


class StockedProduct(Product):
    """Class representing a stocked product."""

    def __init__(self, name, price, quantity, max_quantity, promotions=None):
        super().__init__(name, price, quantity, promotions)
        if quantity < 0:
            raise Exception("Quantity can't be negative")
        self.max_quantity = max_quantity

    def buy(self, quantity):
        """Buys a stocked product."""
        if self.quantity >= quantity:
            self.quantity -= quantity
            total_price = 0
            if self.promotions:
                prices = [promotion.apply_promotion(self, quantity) for promotion in self.promotions]
                total_price = min(prices)
            else:
                total_price = self.price * quantity
            return total_price
        else:
            raise Exception("Not enough quantity in stock!")

    def is_active(self):
        """Returns whether the product is active."""
        return self.quantity > 0
