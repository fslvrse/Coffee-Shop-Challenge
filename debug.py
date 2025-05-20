from customer import Customer
from coffee import Coffee

def main():
    # Create some customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create some coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    # Create some orders
    alice.create_order(espresso, 3.50)
    alice.create_order(latte, 4.25)
    bob.create_order(espresso, 4.00)

    # Test methods
    print("Alice's orders:", [order.coffee.name for order in alice.orders()])
    print("Alice's coffees:", [coffee.name for coffee in alice.coffees()])
    print("Espresso orders:", espresso.num_orders())
    print("Espresso average price:", espresso.average_price())

if __name__ == "__main__":
    main()
