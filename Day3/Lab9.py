# Take username and password from user and check it again for the three times whether the user has entered the right
#username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
#for consecutive 3 times and if the limit exceeds than print "Attempt finished".

username=str(input("Enter the username"))
password=str(input("Enter the password"))

for i in range(0,3):
    x=input("Enter the username")
    y=input("Enter the password")
    if(x==username and y==password):
        print("login successful")
        break
    elif i<3:
        if (username != x and password != y and i<3):
            print("Invalid Credentials, Try again!!!")
else:
    print("Invalid credentials")
    

 