# Given the integer N - the number of minutes that is passed since midnight - how many
#hours and minutes are displayed on the 24h digital clock?
N = int(input("Enter minutes"))
hours = N//60
minutes= N % 60
print(f"Hours and Minutes displayed in 24h digital clock is {hours,minutes}")
