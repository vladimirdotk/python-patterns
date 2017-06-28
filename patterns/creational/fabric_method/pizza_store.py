from patterns.creational.fabric_method.chicago_pizza import ChicagoPizza
from patterns.creational.fabric_method.new_york_pizza import NewYorkPizza

class PizzaStore:

    def make_pizza(self, pizza_type):
        if pizza_type == 'Chicago':
            return ChicagoPizza()
        elif pizza_type == 'NewYork':
            return NewYorkPizza()

    def deliver_pizza(self, pizza):
        return '{} has been delivered'.format(pizza.get_name())

    def get_pizza_cheese(self, pizza):
        return pizza.get_cheese()

    def get_pizza_smell(self, pizza):
        return pizza.get_smell()