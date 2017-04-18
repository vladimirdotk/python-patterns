from patterns.behavioral.decorator.beverage import Beverage


class Espresso(Beverage):

    def get_description(self):
        return 'Espresso'

    def get_cost(self):
        return 1.99
