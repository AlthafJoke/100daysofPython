print("Welcome to the BMI Calculator")

height = float(input("what is your height ? :"))
weight = float(input("what is your weight ? :"))


def bmi(height, weight):
    BMI = weight/ height ** 2
    BMI = round(BMI, 2)
    
    return BMI


BMI = bmi(height, weight)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")

elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
    
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are overweight")
    

elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese")

else:
    print(f"Your BMI is {BMI}, you are clinically obese")

    
    