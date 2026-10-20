names = ["Ava", "Ben", "Cara", "Dylan"]

for name in names:
    print(f"name in names list: {name}")
print("\n")

for i in names:
    print(f"i in names list: {i}")
print("\n")

print(f"len(names) : {len(names)}")#4
print("\n")
for i in range(len(names)):
    print(f"i in range(len(names)) : {i}")
    print(f"names[i] : {names[i]}")
print("\n")

for i in range(len(names)):
    print(f"i in range(len(names)) i, name[i]: {i, names[i]}")
print("\n")

for i, name in enumerate(names, start=1):
    print(f"enumerate i {i}")
    print(f"enumerate name {name}")
    print(f"enumerate(names, start=1) {i, name}")
print("\n")   

#exercise
grades = [55, 72, 81, 90, 66]

for i in grades:
    print(i)
print("\n")

for i in grades:
    if i >= 70:
     print(i)
     
print("\n")