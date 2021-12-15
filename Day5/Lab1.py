#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
for i in range(1500,2701):
    if i%7==0:
        print(f"It is divisible by 7, {i}")
    elif i%5==0:
        print(f"multiple of 5, {i}")
    