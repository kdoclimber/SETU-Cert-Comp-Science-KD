"""
for i in range (5):
    print (i)

for i in range (1, 11):
    print(i)

for i in range (2, 12, 3):
    print(i)
  
for i in range(1, 21):
    print(i)
    
for i in range(10, 0, -1):
    print(i)

for i in range(5, 51, 5):
    print(i)

for i in range(1, 21, 2):
    print(i)

total = 0
for i in range(5):
    print(i)
    mark = int(input("Enter mark: "))
    total += mark
    print("mark ", mark)
    print(f"total = {total}")

average = total / 5
print("Average: ", average)

"""
def count_space():
    space_count = 0
    sentence = input("type a sentence " )
    for i in sentence:
        print(i)
        if i == " ":
            space_count += 1
            print ("Number of spaces", space_count)

    print("Total number of spaces is", space_count)
    
#count_space()

#marks = [75, 60, 80, 90] 
#for mark in marks: print(mark)


#for y in range(1, 10): 
    #print("*" * y)

for table in range(1, 11): 
    print("Table", table) 
    for i in range(1, 11): 
        print(i, "x", table, "=", i * table) 
        
    print()