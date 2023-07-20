# Custom Exception: AdultException
class AdultException(Exception):
    def __init__(self, message="The person is an adult."):
        super().__init__(message)


# Class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if self.age < 18:
            return self.age
        else:
            raise AdultException()

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Example usage:

# Creating a person with age below 18
person1 = Person("Alice", 17)
try:
    print(person1.get_minor_age())
except AdultException as e:
    print(e)

person1.display_person()

# Creating a person with age above 18
person2 = Person("Bob", 25)
try:
    print(person2.get_minor_age())
except AdultException as e:
    print(e)

person2.display_person()
