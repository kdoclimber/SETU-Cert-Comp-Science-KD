numbers = [10, 20, 30, 40, 50, 60]

print(f"First three numbers [:3] {numbers[:3]}")
print(f"Everything except the first three numbers [3:] {numbers[3:]}")
print(f"Last Two numbers [-2:] {numbers[-2:]}")
print(f"20-40 [1:4] {numbers[1:4]}")

print(f"Second last number [-2] {numbers[-2]}")
print(f"Everything pu to the second last number [:-2] {numbers[:-2]}")


course = "PythonXProgramming"

print(f"First 6 letters- Course [:6] {course[:6]}")
print(f"Course [0:6] {course[0:6]}")
print(f"Course [1:6] {course[1:6]}")
print("\n")
print(f"Everything except the first 6, Course [6:] {course[6:]}")
print(f"The last six, Course [-6:] {course[-6:]}")
print(f"Everything except the first 7, course[7:] {course[7:]}")
print(f"Reverse print Course [::-1] {course[::-1]}")

#exercise
student_id = "SETU2026WD"
#SETU
print("\n")
print(f"First 4- SETU [:4]: {student_id[:4]}")
print(f"0,1,2,3 SETU [0:4]: {student_id[0:4]}")
print(f"Prints everything except the last six numbers, leaces SETU [:-6]: {student_id[:-6]}")
#2026
print("\n")
print(f"Prints 2026 [4:8]: {student_id[4:8]}")
#WD
print("\n")
print(f"WD [-2:]: {student_id[-2:]}")
print(f"WD [8:10]: {student_id[8:10]}")
