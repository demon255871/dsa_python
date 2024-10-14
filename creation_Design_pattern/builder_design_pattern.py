"""
The Builder Pattern separates the construction of a complex object from its representation. A Director class oversees the construction process, while a Builder class defines the specific steps to build the object. This pattern is useful when the object creation process involves multiple steps or configurations.
Structure:

    Builder: Specifies an abstract interface for building parts of a product.
    ConcreteBuilder: Implements the Builder interface to create specific parts of the product.
    Product: The complex object being built.
    Director: Controls the construction process, using the Builder to assemble the product step by step.
"""


# Product class
class House:
    def __init__(self):
        self.has_walls = False
        self.has_roof = False
        self.has_windows = False
        self.has_doors = False

    def __str__(self):
        return f"House with walls: {self.has_walls}, roof: {self.has_roof}, windows: {self.has_windows}, doors: {self.has_doors}"

# Abstract Builder
class HouseBuilder:
    def build_walls(self):
        pass

    def build_roof(self):
        pass

    def build_windows(self):
        pass

    def build_doors(self):
        pass

    def get_result(self):
        pass

# Concrete Builder
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.has_walls = True

    def build_roof(self):
        self.house.has_roof = True

    def build_windows(self):
        self.house.has_windows = True

    def build_doors(self):
        self.house.has_doors = True

    def get_result(self):
        return self.house

# Director
class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_minimal_house(self):
        self.builder.build_walls()
        self.builder.build_doors()

    def construct_full_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_windows()
        self.builder.build_doors()

# Usage
builder = ConcreteHouseBuilder()
director = Director(builder)

# Build a minimal house
director.construct_minimal_house()
house = builder.get_result()
print(house)  # Outputs: House with walls: True, roof: False, windows: False, doors: True

# Build a full house
builder = ConcreteHouseBuilder()  # Reset builder
director = Director(builder)
director.construct_full_house()
house = builder.get_result()
print(house)  # Outputs: House with walls: True, roof: True, windows: True, doors: True
