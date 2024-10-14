"""
The Command Pattern is a behavioral design pattern that encapsulates requests (commands) as objects, allowing you to parameterize clients with different requests, queue requests, and support undoable operations. This is particularly useful in scenarios like a remote control system where actions can be executed or undone, such as turning an air conditioner (AC) on or off.
Example: Air Conditioner Remote Control with Undo

In this example, we’ll implement a simple remote control system for an Air Conditioner (AC) that can execute commands like turning the AC on or off. We will also implement an undo feature to reverse the last command.

Explanation:

    Command Interface:
        The Command class defines two methods: execute() and undo(). Each concrete command must implement these methods to perform the action and reverse it, respectively.

    AirConditioner (Receiver):
        This class represents the actual Air Conditioner (AC) that will perform actions such as turning on, turning off, and setting the temperature.

    Concrete Commands:
        ACOnCommand: Encapsulates the action of turning the AC on. The undo() method turns the AC off.
        ACOffCommand: Encapsulates the action of turning the AC off. The undo() method turns the AC back on.
        SetACTemperatureCommand: Encapsulates setting the AC temperature. The undo() method restores the previous temperature by remembering it before executing the temperature change.

    RemoteControl (Invoker):
        The RemoteControl class is the invoker that sends the commands. It holds the last command executed, which allows it to call the undo() method to reverse the action.

    Client Code:
        The client creates the AirConditioner and the concrete command objects. It submits commands to the RemoteControl, which executes them. The undo() feature reverses the last action.

"""
from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver: Air Conditioner
class AirConditioner:
    def __init__(self):
        self._is_on = False
        self._temperature = 24  # Default temperature

    def turn_on(self):
        self._is_on = True
        print(f"Air Conditioner is ON. Temperature is set to {self._temperature}°C.")

    def turn_off(self):
        self._is_on = False
        print("Air Conditioner is OFF.")

    def set_temperature(self, temperature):
        self._temperature = temperature
        if self._is_on:
            print(f"Temperature set to {self._temperature}°C.")

# Concrete Command: Turn AC On
class ACOnCommand(Command):
    def __init__(self, ac: AirConditioner):
        self._ac = ac

    def execute(self):
        self._ac.turn_on()

    def undo(self):
        self._ac.turn_off()

# Concrete Command: Turn AC Off
class ACOffCommand(Command):
    def __init__(self, ac: AirConditioner):
        self._ac = ac

    def execute(self):
        self._ac.turn_off()

    def undo(self):
        self._ac.turn_on()

# Concrete Command: Set Temperature
class SetACTemperatureCommand(Command):
    def __init__(self, ac: AirConditioner, temperature):
        self._ac = ac
        self._temperature = temperature
        self._previous_temperature = ac._temperature

    def execute(self):
        self._previous_temperature = self._ac._temperature
        self._ac.set_temperature(self._temperature)

    def undo(self):
        self._ac.set_temperature(self._previous_temperature)

# Invoker: Remote Control
class RemoteControl:
    def __init__(self):
        self._last_command = None

    def submit(self, command: Command):
        command.execute()
        self._last_command = command

    def undo(self):
        if self._last_command:
            self._last_command.undo()
        else:
            print("Nothing to undo.")

# Client Code
def client_code():
    # Create an air conditioner (receiver)
    ac = AirConditioner()

    # Create concrete commands
    ac_on = ACOnCommand(ac)
    ac_off = ACOffCommand(ac)
    set_temp = SetACTemperatureCommand(ac, 18)

    # Create a remote control (invoker)
    remote = RemoteControl()

    # Turn the AC on
    print("\nTurning AC ON:")
    remote.submit(ac_on)

    # Set the temperature
    print("\nSetting temperature to 18°C:")
    remote.submit(set_temp)

    # Undo temperature change
    print("\nUndo setting temperature:")
    remote.undo()

    # Turn the AC off
    print("\nTurning AC OFF:")
    remote.submit(ac_off)

    # Undo turning AC off
    print("\nUndo turning AC OFF:")
    remote.undo()

# Usage
client_code()
