from patterns.behavioral.decorator.condiment_decorator import CondimentDecorator


class Chocolate(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return '{}, {}'.format(
            self.beverage.get_description(), self.__class__.__name__
        )

    def get_cost(self):
        return 0.50 + self.beverage.get_cost()
