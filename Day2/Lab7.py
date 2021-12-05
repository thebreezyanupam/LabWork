# You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
# of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
# run to university. You jog the first mile at 7mph; then run the next two at15mph; before
# jogging the last at 7mph again. Will this be quicker or slower than the bus?

distance1 = 4
speed1 =25
#bus stops at 10 places and spent 2 minutes
Stop1= 10*2
timefor1distance = 1/Stop1
totaltime=Stop1+timefor1distance
print("the total time to reach university by bus {}".format(totaltime))
# jogging walla
speed2= 7
time1= 1/speed2
time_1=time1*60
speed3=15
time2 = 2/speed3
time_2 = time2*60
speed4 = 7
time3 = 1/speed4
time_3 = time3*60
total_time1=time_1+time_2+time_3
print("the total time for walking is {}".format(total_time1))
if(total_time1 > totaltime):
    print("so, jogging is faster dont use bus")
