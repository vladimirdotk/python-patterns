from patterns.creational.fabric_method.pizza_store import PizzaStore

def test_pizza_store():

    pizza_store = PizzaStore()
    chicago_pizza = pizza_store.make_pizza('Chicago')
    new_york_pizza = pizza_store.make_pizza('NewYork')

    assert pizza_store.deliver_pizza(chicago_pizza) == 'Chicago pizza has been delivered'
    assert pizza_store.deliver_pizza(new_york_pizza) == 'New York pizza has been delivered'

    assert pizza_store.get_pizza_cheese(chicago_pizza) == 'Mozzarella'
    assert pizza_store.get_pizza_cheese(new_york_pizza) == 'Gouda'

    assert pizza_store.get_pizza_smell(chicago_pizza) == 'Bitter'
    assert pizza_store.get_pizza_smell(new_york_pizza) == 'Sweet'
