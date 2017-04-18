from patterns.behavioral.decorator.espresso import Espresso
from patterns.behavioral.decorator.house_blend import HouseBlend
from patterns.behavioral.decorator.chocolate import Chocolate
from patterns.behavioral.decorator.mocha import Mocha


def test_coffee_shop():
    espresso = Espresso()
    espresso = Mocha(espresso)
    espresso = Chocolate(espresso)

    assert espresso.get_cost() == 2.69
    assert all(name in espresso.get_description() for name in [
        'Espresso', 'Mocha', 'Chocolate'
    ])

    house_blend = HouseBlend()
    house_blend = Chocolate(house_blend)

    assert house_blend.get_cost() == 1.49
    assert all(name in house_blend.get_description() for name in [
        'House Blend Coffee', 'Chocolate'
    ])


