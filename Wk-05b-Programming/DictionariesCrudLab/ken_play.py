students = [
    {"name":"Ken", "student_number":100, "course":"art", "mark":76},
    {"name":"Ken2", "student_number":200, "course":"2art", "mark":79}
]


def all_over_70():
    if len(students) == 0:
        print("No students in the list")
    genius_list = []   
    for student in students:
        if student['mark']>70:
            genius_list.append(student)
    print(f"List of Students with a mark over 70") 
    print(genius_list) 
    for student in genius_list: 
        print((student["name"]))  
#funxtion below not called trying different format at the end
def all_over_701():
    if len(students) == 0:
        print("No students in the list")
    genius_list = []   
    for student in students:
        if student['mark']>70:
            genius_list.append(student)
    print(f"List of Students with a mark over 70") 
    print(genius_list) 
    name_list=[]
    for student in genius_list: #cant access the names in one go? (need help) don't want to print seperate lines
        name_list.append(student["name"])
    print(name_list) 

all_over_70()
  