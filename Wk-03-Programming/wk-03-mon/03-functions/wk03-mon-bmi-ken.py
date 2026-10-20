
def bmi_category(bmi_value):
    if bmi_value >= 30.00: bmi_result = "Obese"; return bmi_result
    if bmi_value >= 25 and bmi_value <= 29.99: bmi_result = "Overweight"; return bmi_result
    if bmi_value >= 18.5 and bmi_value <= 24.99: bmi_result = "Normal Weight"; return bmi_result
    if bmi_value < 18.5: bmi_result = "Under Weight"; return bmi_result
    
def bmi(weight_kg, height_m):
    bmi_num = weight_kg / (height_m**2)
    print(f'Your BMI is {bmi_num:.2f} which is ', end=" ")
    print(bmi_category(bmi_num))

weight_num = float(input('Weight kg '))
height_num = float(input('Height m '))

bmi(weight_num, height_num)