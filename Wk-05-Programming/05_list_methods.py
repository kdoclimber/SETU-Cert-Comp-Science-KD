shopping = []

shopping.append("milk")
shopping.append("bread")
shopping.append("eggs")

print(f"shopping: {shopping}")
print("\n")
shopping.remove("bread")
print(f"After shopping.remove bread: {shopping}")
print("\n")
print(f"REMOVES LAST ITEM shopping.pop(): {shopping.pop()}")
print(f"shopping: {shopping}")
print("\n")

last_item = shopping.pop()
print(f"last_item = shopping.pop(): {last_item}")
print("Removed last_item:", last_item)
print(f"shopping: {shopping}")
print("\n")

#exercise
tasks = []
tasks.append("sleep")
tasks.append("jump")
tasks.append("drive")
print(f"tasks: {tasks}")
tasks.remove("jump")
print(f"tasks: {tasks}")
tasks.append("new task")
print(f"tasks: {tasks}")
tasks.pop(2)
print(f"tasks: {tasks}")

""" pop() removes the last item by default but can take an argument to target specific index
remove() removes the item by value not index. removes the first matching value
https://www.geeksforgeeks.org/python/what-is-difference-between-del-remove-and-pop-on-python-lists/
"""
