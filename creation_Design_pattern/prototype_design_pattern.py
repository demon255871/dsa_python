"""
Creates new objects by copying an existing object, known as a prototype.

    Use case: When the cost of creating a new object is more expensive than cloning an existing one.
"""
class Prototype:
    def __init__(self, name, data):
        self.name = name
        self.data = data  # Assume this is a mutable object like a list

    def clone(self):
        # Creates a shallow copy (not deep)
        return Prototype(self.name, self.data)


# Usage
original = Prototype("Original", [1, 2, 3])
clone = original.clone()

# Modify the cloned object's mutable attribute
clone.data.append(4)

# Checking results
print("Original:", original.data)  # Outputs: [1, 2, 3, 4]
print("Clone:", clone.data)        # Outputs: [1, 2, 3, 4]

