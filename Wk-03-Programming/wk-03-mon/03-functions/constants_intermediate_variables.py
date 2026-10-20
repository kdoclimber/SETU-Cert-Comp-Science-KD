def calculate_statistics(numbers):
    """Return mean, minimum, and maximum for a list of numbers."""
    """len returns the number of items in an object, if it's a string it returns the number of letters
    if its a list it returns the number of items in a list"""
    print (type(numbers))
    if not numbers:#why this error check. It's not checking if it's a number? just if there is something there in the argument
           print("NONE")
           return None, None, None
    count   = len(numbers)      # intermediate. 
    total   = sum(numbers)      # intermediate
    mean    = total / count     # intermediate — reuses total and count
    minimum = min(numbers)      # intermediate
    maximum = max(numbers)      # intermediate
    return mean, minimum, maximum

data = [23, 45, 12, 67, 34, 89, 56]
avg, lo, hi = calculate_statistics(data)
print (hi)
print (lo)
print (avg)
print(f"Mean:  {avg:.1f}")
print(f"Range: {lo} to {hi}")