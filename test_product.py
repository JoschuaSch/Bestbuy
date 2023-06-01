import pytest
from product import LimitedProduct, NonStockedProduct
from store import Store
import promotions


def test_create_product():
    """Test that creating a normal product works."""
    product = LimitedProduct('Test Product', 10.99, 5, 10)
    assert product.name == 'Test Product'
    assert product.price == 10.99
    assert product.quantity == 5
    assert product.is_active() == True


def test_create_invalid_product():
    """Test that creating a product with invalid elements."""
    with pytest.raises(Exception):
        LimitedProduct('', 10.99, 5, 10)
    with pytest.raises(Exception):
        LimitedProduct('Test Product', -10.99, 5, 10)
    with pytest.raises(Exception):
        LimitedProduct('Test Product', 10.99, -5, 10)


def test_product_becomes_inactive():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = LimitedProduct('Test Product', 10.99, 1, 10)
    product.buy(1)
    assert product.is_active() == False


def test_buy_product():
    """Test that product purchase modifies the quantity and returns the right output."""
    product = LimitedProduct('Test Product', 10.99, 5, 10)
    total_price = product.buy(3)
    assert product.quantity == 2
    assert total_price == 10.99 * 3


def test_buy_more_than_exists():
    """Test that buying a larger quantity than exists invokes exception."""
    product = LimitedProduct('Test Product', 10.99, 5, 10)
    with pytest.raises(Exception):
        product.buy(10)


def test_store_initialization():
    """Test the Store initialization with different products."""
    product_list = [
        LimitedProduct("MacBook Air M2", 1450, 100, 10),
        LimitedProduct("Bose QuietComfort Earbuds", 250, 500, 10),
        LimitedProduct("Google Pixel 7", 500, 250, 5),
        NonStockedProduct("Windows License", 125, float('inf')),
        LimitedProduct("Shipping", 10, 250, 1)
    ]
    best_buy = Store(product_list)
    assert len(best_buy.product_list) == 5


def test_non_stocked_product_purchase():
    """Test buying a non-stocked product."""
    product = NonStockedProduct("Windows License", 125, float('inf'))
    assert product.buy(1) == 125


def test_limited_product_purchase():
    """Test buying a limited product."""
    product = LimitedProduct("Shipping", 10, 1, 1)
    assert product.buy(1) == 10
    with pytest.raises(Exception):
        product.buy(2)


def test_create_promotions():
    """Test the creation and functionality of promotions."""
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    assert second_half_price.name == "Second Half price!"

    third_one_free = promotions.ThirdOneFree("Third One Free!")
    assert third_one_free.name == "Third One Free!"

    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    assert thirty_percent.name == "30% off!"

    product = LimitedProduct('Test Product', 10, 10, 10)
    product.set_promotions([second_half_price])
    assert product.buy(2) == 15

    product.set_promotions([third_one_free])
    assert product.buy(3) == 20

    product.set_promotions([thirty_percent])
    assert product.buy(1) == 7


def test_product_promotion():
    """Test adding and removing promotions from a product."""
    product = LimitedProduct('Test Product', 10.99, 10, 10)
    second_half_price = promotions.SecondHalfPrice("Second Half price!")

    product.set_promotions([second_half_price])
    assert product.get_promotions() == [second_half_price]

    product.clear_promotions()
    assert product.get_promotions() == []


if __name__ == '__main__':
    pytest.main(['-q', '--no-header', '--no-summary', 'test_product.py'])
