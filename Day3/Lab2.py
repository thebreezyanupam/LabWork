# WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
a= int(input("Enter the marks of 1st sub"))
b= int(input("Enter the marks of 2nd sub"))
c= int(input("Enter the marks of 3rd sub"))
d= int(input("Enter the marks of 4th sub"))
TotalMarks= (a+b+c+d)
TotalPercentage= (TotalMarks/400)*100
print(f"Total Marks is {TotalMarks}")
print(f"Total Percentage is {TotalPercentage}")
if(TotalPercentage>=70):
    print("Distinction")
elif(TotalPercentage>=60):
    print("First Division")
elif(TotalPercentage>=40):
    print("Pass")
else:
    ("Fail")