class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._name = name
        self._orders = []  # To store orders

    @property
    def name(self):
        return self._name

    def create_order(self, coffee, price):
        from order import Order  # Local import to avoid circular dependency
        order = Order(self, coffee, price)
        self._orders.append(order)  # Store the order
        return order

    def coffees(self):
        return [order.coffee for order in self._orders]  # Return list of ordered coffees
