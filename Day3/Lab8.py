#Given a n-digit number. Find the sum of its digits.
a=int(input("Enter a number"))
first_digit = a//10
second_digit=a%10
total=first_digit + second_digit
print("The sum of digits of the number entered is", total)