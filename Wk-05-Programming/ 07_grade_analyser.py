print("\n")
grades = [55, 72, 81, 90, 66]
total = 0
for grade in grades:
    total = total + grade
    grades_length = len(grades)
    average_grade = total/grades_length

#task 4
#count passes in grades
def count_passes(my_grades):
    count = 0
    for i in my_grades:
        if i >= 40:
            count = count + 1
    return count
#called later

print("TASK 1 Total:", total)
print("TASK 2 Average:", average_grade)
print("TASK 3 max(grades):", max(grades))
print("TASK 3  min(grades):", min(grades))
print("TASK 4  count_passes(grades):", count_passes(grades))
print("\n")

#task 5 functions below
#add user input
def create_grades():
    new_grades = []
    grade = int(input("Please enter your grades: -1 to exit "))

    while grade != -1:
        new_grades.append(grade)
        grade = int(input("Please enter your grades: -1 to exit "))

    if grade == -1:
        print("Goodbye")
        return new_grades

#get the average of a list of grades
def average_grades(my_grades):
    if len(my_grades)== 0:#error check
        print("The list is empty")
        return
    else:
        total = 0
        for grade in my_grades:
            total = total + grade
            grades_length = len(grades)
            grade_average = total/grades_length
        return grade_average


def get_max(my_grades):
    if len(my_grades)== 0:#error check
            print("The list is empty")
            return
    else:
        return max(my_grades)
    
def get_min(my_grades):
    if len(my_grades)== 0:#error check
            print("The list is empty")
            return
    else:
        return min(my_grades)


#create a new grades list 
new_grades = create_grades()
print(f"New Grades List = {new_grades}")
#average of new grades list
print(f"Average of New Grades List = {average_grades(new_grades)}")
#highest grade
print(f"Max of New Grades List = {get_max(new_grades)}")
#lowest grade
print(f"Min of New Grades List = {get_min(new_grades)}")
#number of passes- grades >= 40
print(f"Number of Passes in New Grades List = {count_passes(new_grades)}")
