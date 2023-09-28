'''
Part II: Speed Calculations

write a program that asks the user for the minutes, seconds, miles run, 
and miles to target from an exercise event and outputs both 
the average pace and the average speed.
'''

#get user input

minu = input('Minutes ==> ')
print(minu)

sec = input('Seconds ==> ')
print(sec)

mi = input('Miles ==> ')
print(mi)

tMi = input('Target Miles ==> ')
print(tMi + "\n")

# convert input from string1

tmin = int(minu)
tsec = int(sec)
tmiles = float(mi)
targMi = float(tMi)

#find pace
#Pace = time / mi = (60 * min + sec) / mi // 60 for min or % 60 for sec

perMi = ((60 * tmin + tsec) / tmiles)
paceSec = perMi % 60
paceMin = (perMi - paceSec) // 60
print("Pace is {0} minutes and {1} seconds per mile.".format(int(paceMin), int(paceSec)))

#find speed
# 1 hr -> 60 min 1 min -> 60 seconds = 3600 seconds / hour

speed = (3600.0 / (paceMin * 60 + paceSec))
print("Speed is {:.2f} miles per hour.".format(speed))

#pace for target milage
# target mil * pace(in seconds) =-> convert into proper minutes and seconds

targTotal = targMi * (paceMin * 60 + paceSec)
targSec = targTotal % 60
targMin = (targTotal - targSec) // 60

targMi = round(targMi, 2)
print("Time to run the target distance of {:.2f} miles is {} minutes and {} seconds.".format(targMi, int(targMin),int(targSec)))