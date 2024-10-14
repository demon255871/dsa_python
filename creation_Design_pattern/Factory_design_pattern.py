"""
Summary:

    The abstract Product class defines a general interface for products.
    Concrete products like ConcreteProductA and ConcreteProductB implement the create() method.
    The abstract Creator class defines a general interface for creators, but concrete creators like ConcreteCreatorA and ConcreteCreatorB implement the factory method to determine which specific product to create.
    This pattern provides flexibility by decoupling the product creation process from the client code.

Advantages:

    The client code (in the Creator class) only knows about the abstract Product and does not need to know which specific product is being instantiated.
    This allows for easy expansion: adding new products and corresponding creators without modifying the existing code.
"""
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def create(self):
        pass

class ConcreteProductA(Product):
    def create(self):
        return "Product A"

class ConcreteProductB(Product):
    def create(self):
        return "Product B"

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create_product(self):
        product = self.factory_method()
        return product.create()

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Usage
creator = ConcreteCreatorA()
print(creator.create_product())  # Outputs: "Product A"
