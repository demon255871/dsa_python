"""
This code implements the Abstract Factory design pattern, which is used to create families of related objects (in this case, Button and Checkbox) without specifying their concrete classes.
Key Components:

    Abstract Products:
        Button and Checkbox are abstract product interfaces that define the general methods paint() and render() respectively.

    Concrete Products:
        WindowsButton and MacOSButton are concrete implementations of the Button interface.
        WindowsCheckbox and MacOSCheckbox are concrete implementations of the Checkbox interface.

    Abstract Factory:
        GUIFactory is the abstract factory that declares methods to create abstract products, create_button() and create_checkbox().

    Concrete Factories:
        WindowsFactory creates Windows-specific products (WindowsButton and WindowsCheckbox).
        MacOSFactory creates MacOS-specific products (MacOSButton and MacOSCheckbox).

    Client Code:
        The client_code() function takes a GUIFactory object and uses it to create a button and a checkbox, then calls their respective methods (paint() and render()).

Usage:

    The client uses WindowsFactory to get Windows-specific UI elements.
    By changing the factory to MacOSFactory, the client would get MacOS-specific elements without changing its code.
"""
from abc import ABC, abstractmethod

# Abstract Product A
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

# Concrete Product A1
class WindowsButton(Button):
    def paint(self):
        return "Windows Button"

# Concrete Product A2
class MacOSButton(Button):
    def paint(self):
        return "MacOS Button"

# Abstract Product B
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Product B1
class WindowsCheckbox(Checkbox):
    def render(self):
        return "Windows Checkbox"

# Concrete Product B2
class MacOSCheckbox(Checkbox):
    def render(self):
        return "MacOS Checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factory 1
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Concrete Factory 2
class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

# Client Code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return button.paint(), checkbox.render()

# Usage
windows_gui = WindowsFactory()
print(client_code(windows_gui))  # Outputs: ("Windows Button", "Windows Checkbox")
