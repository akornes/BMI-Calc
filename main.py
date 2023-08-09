#BMI is calculated by dividing a person's weight in KG by the square of their height in meters.  

#Under 18.5 underweight
#Over 18.5 but below 25 is normal weight 
#Over 25 but below 30 is overweight 
#Over 30 but below 35 is obese
#Above 35 is clinically obese 



height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height **2
bmi_as_int = int(bmi)

print(bmi_as_int)

if bmi_as_int > 35: 
  print("clinically obese. ")
elif bmi_as_int < 18.5:
  print("underweight. ")
elif bmi_as_int > 30: 
  print("obese")
elif bmi_as_int >25: 
  print ("normal.")


