students = []

def show_menu():
    print("Student Manager")
    print("1. Add student")
    print("2. View students")
    print("3. Search students by number")
    print("4. All who passed")
    print("5. With mark over 70")
    print("6. Average mark")
    print("7. Update Mark")
    print("8. Delete by student num")
    print("9. Exit")

def create_student():
    student = {
        "name": input("Name: "),
        "student_number": int(input("Number-xxx: ")),
        "course": input("Course: "),
        "mark": int(input("Mark: "))
    }
    students.append(student)
    print("Student added") 

def view_students():
    if len(students) == 0:
        print("No students in the list")
    else:
        for student in students:
            print(student)

def search_student_number():
    if len(students) == 0:
        print("No students in the list")

    search_number = int(input("Search by student number:xxx "))
    for student in students:
        if search_number == student['student_number']:
            print(student)
            break
    else:
        print("No student with that number")

def all_who_passed():
    if len(students) == 0:
            print("No students in the list")
    pass_list = []        
    for student in students:
        if student['mark']>=40:
            pass_list.append(student)

    print(f"List of Students that passed") 
    for student in pass_list: 
            print((student["name"]))    

def all_over_70():
    if len(students) == 0:
        print("No students in the list")
    genius_list = []   
    for student in students:
        if student['mark']>70:
            genius_list.append(student)

    print(f"List of Students with a mark over 70") 
    for student in genius_list: 
        print((student["name"])) 

 
def average_mark():
    if len(students) == 0:
            print("No students in the list")
    total_mark = 0
    for student in students:
        total_mark = total_mark + student['mark']
        average = total_mark/len(students)
    
    print(f"Average mark for {len(students)} students: {average}")

def update_mark():
    search_student = int(input("Change the mark of which student number:xxx "))
    if len(students) == 0:
            print("No students in the list")
   
    for student in students:
        if search_student == student['student_number']:
            print(f"We found your student: {student['name']} has a mark of - {student['mark']}")
            new_mark = int(input(f"Enter your new mark for {student['name']}: "))
            student['mark'] = new_mark
            print(f"Student name: {student['name']} New mark - {student['mark']}")



def delete_by_student_num():
    search_student = int(input("Delete which student number:xxx "))
    if len(students) == 0:
            print("No students in the list")

    for student in students:
        if search_student == student['student_number']:
            print(f"We found your student: {student['name']}")

            confirm = input("Are you sure you want to delete this student? Y/N ").lower()
            if confirm == "y":
                students.remove(student)
                print(f"Students after delete: {students}")      
            else:
                break

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student_number()
    elif choice == "4":
        all_who_passed()
    elif choice == "5":
        all_over_70()
    elif choice == "6":
        average_mark()
    elif choice == "7":
        update_mark()
    elif choice == "8":
        delete_by_student_num()
    elif choice == "9":
        break
    else:
        print("Invalid choice")