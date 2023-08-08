#BMI is calculated by dividing a person's weight in KG by the square of their height in meters.  

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height **2
bmi_as_int = int(bmi)

print(bmi_as_int)


