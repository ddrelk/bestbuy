import pytest
from products import Product


def test_create_product():
    assert Product("MacBook Air M2", price=1450, quantity=100)


def test_create_product_invalid_details():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-5, quantity=100)


def test_prod_becomes_inactive():
    res = Product("MacBook Air M2", price=1450, quantity=10)
    res.buy(10)
    assert res.is_active() is False


def test_buy_modifies_quantity():
    res = Product("MacBook Air M2", price=1450, quantity=100)
    res.buy(50)
    assert res.quantity == 50


def test_buy_too_much():
    with pytest.raises(ValueError):
        res = Product("MacBook Air M2", price=1450, quantity=100)
        res.buy(150)


pytest.main()
