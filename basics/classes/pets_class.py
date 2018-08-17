#!/usr/bin/python

class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Pets:
    def CountDogs(*args):
        return len(args)

    def descDogs(*args):
        for i in args:
            print(f'{i.name} is {i.age}')
        return "And they're all mammals, of course."

first = Dog("Tom",6)
second = Dog("Fletcher", 7)
third = Dog("Larry", 9)

print(f'I have {Pets.CountDogs(first,second,third)} dogs.')
print(Pets.descDogs(first,second,third))


