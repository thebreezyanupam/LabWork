#Write a Python program that accepts a string and calculate the number of digits and letters
a = input("enter the string")
d=l=0
for c in a:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print(f'Letters: {l}')
print(f'Digits: {d}')
    