from patterns.behavioral.decorator.beverage import Beverage


class HouseBlend(Beverage):

    def get_description(self):
        return 'House Blend Coffee'

    def get_cost(self):
        return 0.99
