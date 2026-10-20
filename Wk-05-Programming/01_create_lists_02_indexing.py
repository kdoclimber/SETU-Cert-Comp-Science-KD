modules = ["Programming", "Maths", "Computer Systems", "Web Development"]
print(modules)
grades = [55, 72, 81, 90, 66]
print(grades)
""" lists a re better than individual variables because they are easier keep track of, alter, change, loop through, compare etc"""

animals = ["dog", "cat", "rabbit", "hamster"]

print(animals[0])
print(animals[2])
print(animals[-1])
print(animals[1])

"""Mini Exercise below"""

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
#first day
print(f"First Day: {days[0]}")
#last day
print(f"Last Day: {days[-1]}")
#last day
print(f"Last Day: {days[4]}")
#Number of days
print(f"Number of days: {len(days)}")
#Mon
print(f"-5 = Mon: {days[-5]}")
#Mon
print(f"-0 = Mon: {days[-0]}")
#Mon
print(f"0 = Mon: {days[0]}")
#error
print(f"Index Error [5]: {days[5]}")
