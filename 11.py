# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = weight / (height ** 2)
if bmi < 18.5:
    bmi = int(round(bmi, 0))
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    bmi = int(round(bmi, 0))
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    bmi = int(round(bmi, 0))
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    bmi = int(round(bmi, 0))
    print(f"Your BMI is {bmi}, you are obese.")
else:
    bmi = int(round(bmi, 0))
    print(f"Your BMI is {bmi}, you are clinically obese.")

