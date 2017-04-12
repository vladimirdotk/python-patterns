from patterns.behavioral.strategy.duck import Duck
from patterns.behavioral.strategy.fly_with_wings import FlyWithWings
from patterns.behavioral.strategy.mute_quack import MuteQuack
from patterns.behavioral.strategy.quack import Quack
from patterns.behavioral.strategy.fly_no_way import FlyNoWay


def test_duck():

    class ModelDuck(Duck):
        def __init__(self):
            super().__init__(FlyNoWay(), Quack())

        def display(self):
            return 'I\'m a model duck'

    duck = ModelDuck()

    assert isinstance(duck, Duck)
    assert duck.perform_fly() == 'I can\'t fly'
    assert duck.perform_quack() == "Quack!"
    assert duck.display() == 'I\'m a model duck'

    duck.set_fly_behavior(FlyWithWings())
    duck.set_quack_behavior(MuteQuack())

    assert duck.perform_fly() == 'I\'m flying!'
    assert duck.perform_quack() == '<<< Silence >>>'
    assert duck.swim() == 'All ducks can swim!'

