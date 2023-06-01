from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract class representing a promotion."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

    def __str__(self):
        return self.name


class PercentDiscount(Promotion):
    """Class representing a percentage discount promotion."""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = product.price * self.percent / 100
        return (product.price - discount) * quantity

    def __str__(self):
        return f"{self.percent}% off!"


class TwentyPercentOff(Promotion):
    """Class representing a promotion for a second item 20% off."""

    def __init__(self, name="Second 20% off!"):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity >= 2:
            discount = product.price * 0.2
            return product.price - discount
        return product.price


class ThirtyPercentOff(Promotion):
    """Class representing a promotion for a third item 30% off."""

    def __init__(self, name="Third one 30% off!"):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity >= 3:
            discount = product.price * 0.3
            return product.price - discount
        return product.price


class SecondHalfPrice(Promotion):
    """Class representing a second item half price promotion."""

    def __init__(self, name="Second one half price!"):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity < 2:
            return product.price * quantity
        full_price_quantity = (quantity + 1) // 2
        half_price_quantity = quantity // 2
        return product.price * full_price_quantity + (product.price / 2) * half_price_quantity


class ThirdOneFree(Promotion):
    """Class representing a third item free promotion."""

    def __init__(self, name="Third one free!"):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_quantity = 2 * (quantity // 3) + quantity % 3
        return product.price * full_price_quantity
