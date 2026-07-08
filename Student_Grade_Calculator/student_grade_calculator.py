print("Student Grade Calculator")
name =input("Enter Your Name :")

#Total no of subjects
sub =int(input("Enter Number of Subjects:"))

#Maximum marks of one subject and get the Total marks of all subjects
max_marks = float(input("Enter Maximum marks of each subject:"))
Total = sub * max_marks
obt=0

#Get marks of each subject.
for i in range(sub):
    marks = float(input(f"Enter marks of Subject {i+1}:"))
    obt =obt + marks

#Calculate Percentage
percent =(obt * 100)/Total

#Determine Grade
if(percent >= 75):
    grade = "A"
elif(percent >= 65):
    grade = "B"    
elif(percent >= 55):
    grade = "C"   
elif(percent >= 33):
    grade = "F"      

#Display the Result
print("")
print ("Result")
print("")
print(f"Student Name: {name}")
print(f"Total Marks: {Total}")
print(f"Obtained Marks: {obt}")
print(f"Percentage:{percent}")
print(f"Grade:{grade}")

