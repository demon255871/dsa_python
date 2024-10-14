"""
The State Pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. It involves defining state-specific behavior within individual state classes, and the context (the object whose behavior changes) delegates state-specific behavior to these state classes.
Example: Vending Machine using the State Pattern

In this example, we’ll implement a Vending Machine that can be in different states such as Idle, HasMoney, and SoldOut. The behavior of the vending machine will change depending on its current state. For instance, if the vending machine is in the SoldOut state, it won't accept money or dispense items.

Explanation:

    State Interface (VendingMachineState):
        The VendingMachineState is an abstract class that defines two methods: insert_money() and dispense(). These methods represent the actions that a vending machine can perform.

    Concrete States:
        IdleState: Represents the state where the vending machine is waiting for money to be inserted. If money is inserted, the machine transitions to the HasMoneyState.
        HasMoneyState: Represents the state where the vending machine has received money and is waiting to dispense the item. After dispensing, the machine either returns to IdleState or transitions to SoldOutState if there are no more items.
        SoldOutState: Represents the state where the vending machine has no items left to dispense. In this state, it will reject any money.

    Context (VendingMachine):
        The VendingMachine class represents the vending machine itself. It holds a reference to its current state and delegates the behavior to the current state's insert_money() and dispense() methods. It can transition between states by calling set_state().

    Client Code:
        The client code demonstrates the vending machine in action. Initially, the machine is in the IdleState. After inserting money, it moves to HasMoneyState and dispenses an item. Once the machine runs out of items, it transitions to SoldOutState and stops accepting money.
"""

from abc import ABC, abstractmethod

# State Interface
class VendingMachineState(ABC):
    @abstractmethod
    def insert_money(self, vending_machine):
        pass

    @abstractmethod
    def dispense(self, vending_machine):
        pass

# Concrete States
class IdleState(VendingMachineState):
    def insert_money(self, vending_machine):
        print("Money inserted. Waiting for selection.")
        vending_machine.set_state(vending_machine.has_money_state)

    def dispense(self, vending_machine):
        print("Please insert money first.")

class HasMoneyState(VendingMachineState):
    def insert_money(self, vending_machine):
        print("Money already inserted. Please select an item.")

    def dispense(self, vending_machine):
        if vending_machine.item_count > 0:
            print("Dispensing item...")
            vending_machine.item_count -= 1
            if vending_machine.item_count == 0:
                print("The machine is now sold out.")
                vending_machine.set_state(vending_machine.sold_out_state)
            else:
                vending_machine.set_state(vending_machine.idle_state)
        else:
            vending_machine.set_state(vending_machine.sold_out_state)

class SoldOutState(VendingMachineState):
    def insert_money(self, vending_machine):
        print("The machine is sold out. No items to dispense.")

    def dispense(self, vending_machine):
        print("Cannot dispense. The machine is sold out.")

# Context: VendingMachine
class VendingMachine:
    def __init__(self, item_count):
        self.item_count = item_count

        # Initialize states
        self.idle_state = IdleState()
        self.has_money_state = HasMoneyState()
        self.sold_out_state = SoldOutState()

        # Set initial state
        self.state = self.sold_out_state if item_count == 0 else self.idle_state

    def set_state(self, new_state):
        self.state = new_state

    # Delegate behavior to the current state
    def insert_money(self):
        self.state.insert_money(self)

    def dispense(self):
        self.state.dispense(self)

# Client Code
if __name__ == "__main__":
    # Create a vending machine with 2 items
    vending_machine = VendingMachine(2)

    # Perform actions on the vending machine
    print("\nCurrent State: Idle (Initial State)")
    vending_machine.insert_money()  # Money inserted, move to HasMoneyState
    vending_machine.dispense()      # Dispenses item, back to IdleState

    print("\nInsert Money again:")
    vending_machine.insert_money()  # Money inserted, move to HasMoneyState
    vending_machine.dispense()      # Dispenses item, becomes SoldOutState

    print("\nAttempt to insert money when sold out:")
    vending_machine.insert_money()  # Cannot insert money, sold out
