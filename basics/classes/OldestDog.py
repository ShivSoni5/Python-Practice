#!/usr/bin/python3

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

first = Dog("first",5)
second = Dog("second",4)
third = Dog("third",9)

def OldestAge(*args):
    return max(args)

print('The oldest dog is {} years old.'.format(OldestAge(first.age, second.age, third.age)))
