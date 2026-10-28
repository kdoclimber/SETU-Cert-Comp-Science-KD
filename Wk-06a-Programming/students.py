students = [
    {"id": 101, "name": "Mary", "mark": 72},
    {"id": 102, "name": "John", "mark": 38},
    {"id": 103, "name": "Sarah", "mark": 55},
    {"id": 104, "name": "Adam", "mark": 81},
    {"id": 105, "name": "Niamh", "mark": 40}
]
for student in students:
    print(student["name"])
    print(student["name"], student ['mark'])
    print(f"Name: {student['name']}, Mark: {student ['mark']}, ID: {student['id']}")

def student_pass_fail():
    for student in students:
        if student['mark'] >= 40 and student['mark'] < 70:
            print(student['name'], "- Pass")
        elif student['mark'] >= 70:
            print(student['name'], "- Distinction")
        else:
            print(student['name'], "- Fail")

def count_records():
    passes = 0
    fails = 0
    for student in students:
        if student['mark'] >=40:
            passes = passes + 1
    fails = len(students)-passes
    print("Number of passes:", passes)
    print("Number of fails:", fails)

def total_and_average_mark():
    total = 0
    for student in students:
        total  = total + student['mark']
    average = total / len(students)
    print("Total mark: ", total)
    print("Average mark: ", average)

def find_highest_mark():
    highest_mark = students[0]['mark']
    for student in students:
        if student['mark'] > highest_mark:
            highest_mark = student['mark']
    print("Highest mark: ", highest_mark)

def searching_for_data():
    search_id = int(input('Search by student ID '))
    found = False # flag to test later
    for student in students:
        if student['id'] == search_id:
            print(f'Student found: Student Name: {student['name']}, Student Mark: {student['mark']}')
            found = True
    if found == False:
        print("No student with that ID exists")

def find_student(my_list, search_id):
    for student in my_list:
        if student['id'] == search_id:
            return student
    return None

def display_students(my_list):
    for student in my_list:
        print(student['id'], student['name'], student['mark'])

def calculate_average(my_list):
    if len(my_list) == 0:#checks to see if there is something in the list
        print("The list is empty")
    total = 0
    for student in my_list:
        total  = total + student['mark']
    average = total / len(students)
    return total, average

student_pass_fail()
count_records()
total_and_average_mark()
find_highest_mark()
searching_for_data()

#FIND STUDENTS BY ID
found_student = find_student(students, 102)
if found_student is not None:
    print(f"Student found: {found_student['name']}, {found_student['mark']}")
else:
    print("Student not found")

#DISPLAY STUDENTS
display_students(students)

#count_passes () already done above in student_pass_fail()

total, average = calculate_average(students)
print("Total mark from calculate_average: ", total)
print("Average mark from calculate_average: ", average)

#CRUD CHALLENGE BELOW

def find_student_by_name(my_list, search_name):
    if len(my_list) == 0:
        print("Nothing in the list")
        return None
    for student in my_list:
        if student['name'].lower() == search_name.lower():
            return student
        else:
            print("No student found")
            return None
        
found_student = find_student_by_name(students, "Mary")
print(f"Found Student: {found_student}")

def find_highest_student_mark(my_list):
    if len(my_list) == 0:
        print("Nothing in the list")
        return None
    highest_mark = my_list[0]['mark']
    for student in my_list:
        if student['mark'] > highest_mark:
            highest_mark = student['mark']
            return student        

student_wih_highest_mark = find_highest_student_mark(students)
print(f"student_wih_highest_mark: {student_wih_highest_mark}")

def display_summary(my_list):
    print("\n")
    print("Results from display summary()")
    display_students(my_list)
    count_records()
    total, average = calculate_average(my_list)
    print("Total mark: ", total)
    print("Average mark: ", average)
    student_wih_highest_mark = find_highest_student_mark(my_list)
    print(f"Student wih highest mark: {student_wih_highest_mark['name']}")
    print(f"Highest mark: {student_wih_highest_mark['mark']}")

display_summary(students)