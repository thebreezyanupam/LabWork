
# N students take K apples and distribute them among each other evenly. The remaining
# (the indivisible) part remains in the basket. How many apples will each single student
# get? How many apples will remain in the basket? The program reads the numbers N and
# K. It should print the two answers for the questions above.

student = int(input("enter the number of students"))
apple = int(input("enter the number of apples"))
print(apple // student)
print(apple % student)

