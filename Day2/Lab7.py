# You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
# of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
# run to university. You jog the first mile at 7mph; then run the next two at15mph; before
# jogging the last at 7mph again. Will this be quicker or slower than the bus?

distance1 = 4
speed1 =25
T1 =((distance1/ speed1) * 60)
#since the bus spends two minutes in each ten steps so 2*10
T2 = 20
Total1 = T1 + T2
print(f"total time taken by bus is {Total1}")
# when jogging
Jog1= 7
time1= 1/Jog1
time2=time1*60
Jog2=15
time2 = 2/Jog2
time3 = time2*60
Jog3 = 7
time3 = 1/Jog3
time4 = time3*60
TotalTime=time2+time3+time4
print("the total time for walking is {}".format(TotalTime))
if(TotalTime > Total1):
    print("so, jogging is faster dont use bus")
