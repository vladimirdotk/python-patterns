from abc import ABC, abstractmethod


class Beverage(ABC):

    def get_description(self):
        return 'Unknown Beverage'

    @abstractmethod
    def get_cost(self):
        pass
