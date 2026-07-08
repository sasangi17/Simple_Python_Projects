#Get User Input
weight = float(input("Enter Your Weight in kg:"))
height = float(input("Enter Your Weight in cm:"))

#Convert cm to m
height = height/100

#Calculate BMI 
bmi = weight / (height ** 2)

#Show BMI 
print(f"Your BMI is :{round(bmi,2)}")

#Show BMI category
if bmi < 18.5:
    print("Category:Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Category:Healthy weight")
elif 25 <= bmi <= 29.9:
    print("Category:Overweight")    
else:
    print("Category:Obese")