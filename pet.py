import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    # Let each group member add their methods here

    def eat(self):
        """Simulate feeding the pet."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has been fed!. Hunger level: {self.hunger}, Happiness: {self.happiness},")

    def sleep(self):
        """Simulate letting the pet sleep."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} has already slept. Energy level: {self.energy},")

    def play(self):
        """Simulate playing with the pet."""
        if self.energy > 0:
            self.happiness = min(10, self.happiness + 2)
            self.energy = max(0, self.energy - 2)
            self.hunger = max(0, self.hunger + 1)
            print(f"{self.name} is playing! Happiness: {self.happiness}, Energy: {self.energy}, hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        """Display the pet's current status."""
        print(f"Pet Name: {self.name}:")
        print(f"Hunger Level: {self.hunger}/10")
        print(f"Energy Level: {self.energy}/10")
        print(f"Happiness Level: {self.happiness}/10")
        print("Tricks Learned: " + ", ".join(self.tricks) if self.tricks else "No tricks learned yet.")
        print("==============================================")

    def train(self, trick):
        """Teach the pet a new trick."""
        if len(trick) < 3 or len(trick) > 20 or not trick.isalpha():
            print("Invalid trick name. Please enter a name between 3 and 20 characters, containing only letters.")
            return
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 2)
        print(f" ,{self.name} has learned the trick: {trick}! Happiness: {self.happiness},")

    def show_tricks(self):
        """Display all tricks the pet knows."""
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")                                            