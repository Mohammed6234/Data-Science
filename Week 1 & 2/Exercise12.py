class Animal:
    def __init__(self, species):
        self.species = species

    def habitat(self):
        print(f"{self.species} lives in various habitats.")


class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def bark(self):
        print(f"{self.species} ({self.breed}) barks.")

# Creating Animal and Dog objects
animal = Animal("Generic Animal")
dog = Dog("Dog", "Labrador")

# Calling the habitat method from Animal class
animal.habitat()

# Calling the habitat method from Dog class, inherited from Animal
dog.habitat()

# Calling the bark method specific to the Dog class
dog.bark()
