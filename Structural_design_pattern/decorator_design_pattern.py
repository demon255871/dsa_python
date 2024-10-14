"""
The Decorator Pattern is a structural design pattern that allows you to dynamically add behavior or responsibilities to objects without modifying their code. Decorators provide a flexible alternative to subclassing for extending functionality.

The pattern involves a set of decorator classes that are used to wrap concrete components. Both the decorator and the component share a common interface, allowing the client to treat the decorated object the same way as the undecorated one.
Example: Coffee Shop

Imagine you have a coffee shop where you sell basic coffee, but customers can add additional ingredients like milk or sugar to their coffee. Instead of creating multiple subclasses for every combination of coffee and ingredients, the Decorator pattern can be used to dynamically add ingredients.

Explanation:

    Coffee (Component):
        This is the common interface that defines the structure of a coffee. It has two methods: cost() (to get the price) and description() (to describe the coffee).

    BasicCoffee (Concrete Component):
        This is the basic coffee, which implements the Coffee interface. It has a fixed cost of 5 and a simple description: "Basic Coffee".

    CoffeeDecorator (Abstract Decorator):
        This is the abstract decorator class that wraps a Coffee object. It implements the same interface and delegates the calls to the wrapped object. It is the base class for all concrete decorators.

    MilkDecorator and SugarDecorator (Concrete Decorators):
        These decorators extend the functionality of BasicCoffee by adding additional behavior (e.g., increasing the cost and updating the description) for adding milk or sugar.
        Each decorator modifies the behavior of the cost() and description() methods.

    Client Code:
        The client interacts with the Coffee interface and can combine multiple decorators to dynamically enhance the object’s behavior.
        The client doesn’t need to know if it’s dealing with a decorated coffee or a plain one; it treats all objects as Coffee.

"""

from abc import ABC, abstractmethod

# Component: Coffee interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete Component: Basic Coffee
class BasicCoffee(Coffee):
    def cost(self):
        return 5  # Cost of basic coffee

    def description(self):
        return "Basic Coffee"

# Abstract Decorator: CoffeeDecorator class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()

# Concrete Decorators: Add-ons for coffee
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Milk costs extra

    def description(self):
        return self._coffee.description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Sugar costs extra

    def description(self):
        return self._coffee.description() + ", Sugar"

# Client Code
def client_code(coffee: Coffee):
    print(f"Description: {coffee.description()}")
    print(f"Cost: {coffee.cost()}")

# Usage
basic_coffee = BasicCoffee()
print("Basic coffee:")
client_code(basic_coffee)

# Coffee with milk
coffee_with_milk = MilkDecorator(basic_coffee)
print("\nCoffee with milk:")
client_code(coffee_with_milk)

# Coffee with milk and sugar
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print("\nCoffee with milk and sugar:")
client_code(coffee_with_milk_and_sugar)
