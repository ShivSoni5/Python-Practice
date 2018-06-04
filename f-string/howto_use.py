#!/usr/bin/python3

# f-string takes the least execution time in string formatting

user_input = input("enter your message: ")

my_words = user_input.strip().split()

for i,word in enumerate(my_words):
    print(f'{i}: {word}')   #string formatting using f-string
