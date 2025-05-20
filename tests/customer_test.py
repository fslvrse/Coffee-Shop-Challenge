import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_create_order(self):
        order = self.customer.create_order(self.coffee, 5.0)
        self.assertIsNotNone(order)

    def test_coffees(self):
        self.customer.create_order(self.coffee, 5.0)
        self.assertIn(self.coffee, self.customer.coffees())
