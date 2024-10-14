"""
The Facade Pattern is a structural design pattern that provides a simplified, unified interface to a complex subsystem. It hides the complexity of the system and provides an easy way to interact with it, without exposing the underlying details.
Example: Facade Pattern in a Home Theater System

Imagine you have a home theater system with multiple components like a DVD player, Projector, Lights, Sound System, and more. The process of turning on all these devices for a movie night can be cumbersome. The Facade pattern helps by providing a simplified interface to control all these components with a single method.
Components:

    Subsystem classes (DVD player, Projector, Lights, Sound System, etc.)
    Facade (HomeTheaterFacade) simplifies the interaction with these components.

Explanation:

    Subsystem Classes:
        These are the various components of the home theater system, such as DVDPlayer, Projector, SoundSystem, Lights, and PopcornMaker. Each class has methods to turn on/off or perform specific actions.
    Facade (HomeTheaterFacade):
        The HomeTheaterFacade class provides a simple interface to interact with the entire system.
        It has two main methods:
            watch_movie(): Sets up all the subsystems for a movie (e.g., dims the lights, turns on the projector, plays the DVD, etc.).
            end_movie(): Shuts down all the systems (e.g., turns off the projector, sound, lights, etc.).
    Client Code:
        Instead of directly interacting with each subsystem class, the client interacts with the HomeTheaterFacade to perform a sequence of actions.
        This reduces complexity and makes the process much more user-friendly.    
"""

# Subsystem 1: DVD Player
class DVDPlayer:
    def on(self):
        return "DVD Player is on"
    
    def play(self, movie):
        return f"Playing '{movie}'"

    def off(self):
        return "DVD Player is off"

# Subsystem 2: Projector
class Projector:
    def on(self):
        return "Projector is on"
    
    def off(self):
        return "Projector is off"
    
    def wide_screen_mode(self):
        return "Projector is in widescreen mode"

# Subsystem 3: Surround Sound System
class SoundSystem:
    def on(self):
        return "Sound System is on"
    
    def set_volume(self, level):
        return f"Sound system volume set to {level}"

    def off(self):
        return "Sound System is off"

# Subsystem 4: Lights
class Lights:
    def dim(self):
        return "Lights are dimmed"

    def on(self):
        return "Lights are on"

# Subsystem 5: Popcorn Maker
class PopcornMaker:
    def on(self):
        return "Popcorn Maker is on"
    
    def pop(self):
        return "Popping popcorn!"

    def off(self):
        return "Popcorn Maker is off"

# Facade: Simplified interface to control all subsystems
class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, projector: Projector, sound: SoundSystem, lights: Lights, popcorn_maker: PopcornMaker):
        self.dvd = dvd
        self.projector = projector
        self.sound = sound
        self.lights = lights
        self.popcorn_maker = popcorn_maker

    def watch_movie(self, movie):
        steps = [
            self.popcorn_maker.on(),
            self.popcorn_maker.pop(),
            self.lights.dim(),
            self.projector.on(),
            self.projector.wide_screen_mode(),
            self.sound.on(),
            self.sound.set_volume(10),
            self.dvd.on(),
            self.dvd.play(movie)
        ]
        return "\n".join(steps)

    def end_movie(self):
        steps = [
            self.popcorn_maker.off(),
            self.lights.on(),
            self.projector.off(),
            self.sound.off(),
            self.dvd.off()
        ]
        return "\n".join(steps)

# Client code
def client_code():
    # Instantiate all subsystems
    dvd = DVDPlayer()
    projector = Projector()
    sound = SoundSystem()
    lights = Lights()
    popcorn_maker = PopcornMaker()

    # Use Facade to simplify interaction
    home_theater = HomeTheaterFacade(dvd, projector, sound, lights, popcorn_maker)

    # Watch movie
    print("Starting movie:")
    print(home_theater.watch_movie("The Matrix"))

    # End movie
    print("\nEnding movie:")
    print(home_theater.end_movie())

# Usage
client_code()
