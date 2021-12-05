#Given three integers,
# print the smallest one. (Three integers should be user input) 

a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if a<b and a<c:
    print(a,"is the smallest")
elif b<a and b<c:
    print(b,"is the smallest")
else:
    print(c,"is the smallest")