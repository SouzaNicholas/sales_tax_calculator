from item import Item
import pytest
import main


def test_calculate_sum():
    items = [
        Item("Bananas", 1.30, "WIC Eligible Food"),
        Item("Strawberries", 2.99, "WIC Eligible Food"),
        Item("Sunglasses", 19.99, "Clothing"),
        Item("Blender", 27.99, "Everything Else")
    ]

    ma_sum = main.calculate_sum("MA", items)
    me_sum = main.calculate_sum("ME", items)
    nh_sum = main.calculate_sum("NH", items)

    assert ma_sum == 55.27
    assert me_sum == 54.91
    assert nh_sum == 52.27


def test_empty_cart():
    items = []

    assert main.calculate_sum("NH", items) == 0


def test_invalid_state():
    items = [
        Item("Bananas", 1.30, "WIC Eligible Food"),
        Item("Strawberries", 2.99, "WIC Eligible Food"),
        Item("Sunglasses", 19.99, "Clothing"),
        Item("Blender", 27.99, "Everything Else")
    ]

    with pytest.raises(KeyError):
        assert main.calculate_sum("RI", items) == 52.27
