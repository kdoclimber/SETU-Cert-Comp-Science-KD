
sentence = "the quick brown fox"
words = sentence.split()
print(words)
print(len(words))

csv_line2 = "Alice,25,Dublin,Engineer"
parts = csv_line2.split(",")
print(parts)

name, age, city, job = parts
print(f"{name} is {age} and works as a {job} in {city}")

full_name = "alice mary smith"
parts = full_name.split()

first = parts[0].title()
last = parts[1].title()
print(f"{last}, {first}")

csv_line = "Dublin,Cork,Galway,Limerick"
cities = csv_line.split(",")
print(cities)# , are printed between items and some space
print(" | ".join(cities))
print(cities[0])
print (len(cities)) #4
#for i in len(cities): 
    #print (i)
for i in cities:
    print (f"i = {i}")

print(f"cities[0] = {cities[0]}")
print(f"cities[1] = {cities[1]}")
print(f"cities[2] = {cities[2]}")
print(f"cities[3] = {cities[3]}")
#print(f"cities[4] = {cities[4]}") # index error

print(f"cities[-1] = {cities[-1]}")
print(f"cities[-2] = {cities[-2]}")
print(f"cities[-3] = {cities[-3]}")
print(f"cities[-4] = {cities[-4]}")
#print(f"cities[-5] = {cities[-5]}") # index error

