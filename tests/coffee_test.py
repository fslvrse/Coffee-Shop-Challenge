import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 5.0)

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 1)
