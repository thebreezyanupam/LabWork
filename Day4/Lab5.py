#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
a=int(input("Number of classes held"))
b=int(input("Number of classes attended."))
per= (b/a)*100
if per<75:
    print("You are not allowed for exam.")
else:
    print("You're allowed for exam.")