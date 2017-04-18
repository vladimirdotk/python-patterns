from abc import abstractmethod
from patterns.behavioral.decorator.beverage import Beverage


class CondimentDecorator(Beverage):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass
