students = [ 
    {"id": 101, "name": "Mary", "mark": 72}, 
    {"id": 102, "name": "John", "mark": 38}, 
    {"id": 103, "name": "Sarah", "mark": 55} 
]
"""
for student in students: 
    print(student["name"], student["mark"])

for student in students: 
    if student["mark"] >= 40: 
        print(student["name"], "Pass") 
    else: 
        print(student["name"], "Fail")

passes = 0 
for student in students: 
    if student["mark"] >= 40: 
        passes = passes + 1 
print("Number of passes:", passes)

search_id = int(input("Student ID: ")) 
found = False 
for student in students: 
    if student["id"] == search_id: 
        print(f"Student from if: {student}") 
        found = True 
    if found == False:
        print("Student not found")
"""

def find_student(students, search_id): 
    for student in students:
        if student["id"] == search_id: 
            return student 
    return None 

def find_student2(students, search_id): 
    for student in students:
        if student["id"] == search_id: 
            print(f"Student from inside function: {student}")
            #return student 
    return None 

student = find_student(students, 102)
print(f"Student from function: {student}")

find_student2(students, 102)
