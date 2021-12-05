#CONVERT INTO DAY, HOURS AND MINUTES
time = int(input("enter time"))
minutes = time/60
hours = minutes/60
day = hours/24
seconds = time/86400
print(minutes)
print(hours)
print(day)
print(seconds)