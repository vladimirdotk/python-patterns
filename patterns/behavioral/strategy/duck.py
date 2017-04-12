from abc import ABC, abstractmethod


class Duck(ABC):
    """
    Abstract duck class
    """

    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        return self.fly_behavior.fly()

    def perform_quack(self):
        return self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self):
        pass

    @staticmethod
    def swim():
        return 'All ducks can swim!'
