import random

def add(a, b):
    # PURE — same inputs always give same output, no side effects
    return a + b

def get_name():
    # IMPURE — depends on user input (external state)
    return input("Name: ")

# Pure equivalent: pass the name as a parameter
def process_name(name):
    # PURE — same input always gives same output
    return name.strip()

def to_uppercase(text):
    # PURE — same input always gives same output, no side effects
    return text.upper()

def random_greeting():
    # IMPURE — different result on each call (uses random)
    options = ["Hi", "Hello", "Hey"]
    return random.choice(options)

# Pure equivalent: accept the choice as a parameter
def format_greeting(greeting, name):
    # PURE — deterministic, no side effects
    return f"{greeting}, {name}!"

def print_total(total):
    # IMPURE — side effect (printing to screen)
    print(f"Total: {total}")

# Pure equivalent: return a formatted string instead
def format_total(total):
    # PURE — returns a value, no side effects
    return f"Total: {total}"