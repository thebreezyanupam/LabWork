#Write a program to find the factorial of a number.
num=int(input("enter the num"))
factorial=1
if num < 0:
    print("Wrong number")
elif num==0:
    print("The factorial is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print(f'The factorial of {num} is {factorial}')