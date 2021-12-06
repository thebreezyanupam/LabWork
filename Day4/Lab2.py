#Write a Python program to sum three given integers. However, if two or more values are
#equal sum will be zero.
a= int(input("Enter 1st integer."))
b= int(input("Enter 2nd integer."))
c= int(input("Enter 3rd integer."))
sum= a+b+c
if a==b or b==c or a==c:
    print("The sum is zero")
else:
    print(f'The sum is {sum}.')
    