# A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks
# that can be purchased.
# The program should read three integers: the number of students in each of the three
# classes, a, b and c respectively.
# Suppose In the first test there are three groups. The first group has 20 students and thus needs 10
# desks. The second group has 21 students, so they can get by with no fewer than 11 desks.
# 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

a=int(input("Enter the number of students in 1st class "))
b=int(input("Enter the number of studnets in 2nd class "))
c=int(input("Enter the number of students in 3rd class "))
table1 = (a //2 + b //2 + c // 2)
table2=  (a % 2 + b % 2 + c % 2)
print("So,we need {} desks in total".format(table1+table2))