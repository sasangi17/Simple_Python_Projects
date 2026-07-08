#Get User Age 
age = int(input("Enter Your Age :"))
def check_age(age):
    if age <=12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior Citizen"

#Display Category
category = check_age(age)
print("You are a:",category)