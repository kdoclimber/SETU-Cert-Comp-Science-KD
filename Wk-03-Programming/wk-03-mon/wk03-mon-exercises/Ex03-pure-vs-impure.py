import random

def add(a, b):#pure changes nothing, same in same out
    return a + b

def get_name():#impure need user input
    return input("Name: ")

def get_name2(name):#new
    return name
name = input("enter your name: ")
print(get_name2(name))

def to_uppercase(text):#impure changes the input but not sure if this can be avoided so maybe its pure same input same output
    return text.upper()


def random_greeting():#impure returns a random option
    options = ["Hi", "Hello", "Hey"]
    return random.choice(options)

def print_total(total):#impure, it prints something
    print(f"Total: {total}")