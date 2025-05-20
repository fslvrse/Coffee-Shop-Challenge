class Order:
    def __init__(self, customer: 'Customer', coffee: 'Coffee', price: float):
        from customer import Customer  # Local import to avoid circular dependency
        from coffee import Coffee      # Local import to avoid circular dependency
        
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        
        coffee.add_order(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
