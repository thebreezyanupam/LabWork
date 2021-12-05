# The program should print two numbers: the number of hours (between 0 and 23) and the
# number of minutes (between 0 and 59).
# For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30
# am. So, the program should print 2 30.
a = int(input("enter a number" ))
hour = a // 60
min = a % 60
print(hour,min)