"""

This code implements the Singleton design pattern in Python, which ensures that only one instance of a class can exist throughout the program. Let’s break it down step by step:
Key Concepts:

    Class Attribute: _instance
        The attribute _instance is a class variable (shared by all instances of the class). It holds the reference to the single instance of the class.
        Initially, _instance is set to None to indicate that no instance has been created yet.

    Overriding __new__(cls)
        __new__ is a special method responsible for creating a new instance of a class.
        It’s called before __init__ and is where the actual object creation happens (i.e., allocating memory for the new object).
        By overriding __new__, we can control how and when the object is created.

How the Singleton Pattern Works:

    Step 1: The first time you try to create an object of the Singleton class, _instance is None.
        The if condition is True, so super(Singleton, cls).__new__(cls) is called to create a new instance.
        This instance is stored in _instance so that next time it can be reused.
    Step 2: On subsequent attempts to create objects of Singleton, _instance will not be None (since it holds the reference to the first instance).
        The if condition is False, so it directly returns the existing _instance, preventing the creation of any new instances.
        """


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
