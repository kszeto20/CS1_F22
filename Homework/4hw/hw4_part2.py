'''
Homework 4
Part II: COVID-19 Quarantine States
'''

# imports
import hw4_util

# state index finder
def indFind(state, lists):
    stateInd = -1
    
    # find which index the state is
    for i in range(len(lists)):
        if (lists[i][0] == state):
            stateInd = i
    if(stateInd == -1):
        print("State {} not found".format(state))
        
    return stateInd

# daily checker 
def dailyF(state, lists):
    
    # get state index
    stateInd = indFind(state, lists)
    if (stateInd == -1):
        return -1
    # state list
    actS = lists[stateInd]
    
    # dailyAvg = all cases * (100000 / total population) / 7
    dAvg = 0
    for i in range(7):
        dAvg += actS[i + 2]
    dAvg *= (100000 / actS[1])
    dAvg /= 7
    
    return round(dAvg, 1)

# daily PCT
def dailyPCT(state, lists):
    
    # get state index
    stateInd = indFind(state, lists)
    if (stateInd == -1):
        return -1
    # state list
    sList = lists[stateInd]
    
    # following equation for daily PCT
    P = 0
    N = 0
    for i in range(7):
       P += sList[i+2]
       N += sList[i + 9]
    percent = P / (P + N) * 100
    
    return round(percent, 1)

# quarantine states
def quar(lists):
   
    # all contaminated states
    allS = []
    # check each state
    for i in range(52):
        stateC =  lists[i][0]
        dF = dailyF(stateC, lists)
        dPCT = dailyPCT(stateC, lists)
        # if either is larger than 10 == contaminated state
        if (dF > 10 or dPCT > 10):
            allS.append(stateC)
    hw4_util.print_abbreviations(allS)

# highest daily average
def highC(lists):
    highestAB = 'LOL'
    highestAvg = 0
    for i in range(52):
        stateC = lists[i][0]
        if (dailyF(stateC, lists) > highestAvg):
            highestAvg = dailyF(stateC, lists)
            highestAB = stateC
    print("State with highest infection rate is {}".format(highestAB))
    print("Rate is {:.1f} per 100,000 people".format(round(highestAvg, 1)))

while (1):
    # get user input
    print("...")
    week = input("Please enter the index for a week: ").strip('\r')
    print(week)
    week = int(week)
    
    if (week < 0):
        break
    elif (week > 29):
        print("No data for that week")
    else:
        lists = hw4_util.part2_get_week(week)
        req = input("Request (daily, pct, quar, high): ").strip('\r')
        print(req)
        req = req.lower()
        if (req == 'daily'):
            state = input("Enter the state: ").strip('\r')
            print(state)
            state = state.upper()
            dailyAvg = dailyF(state, lists)
            if not(dailyAvg == -1):
                print("Average daily positives per 100K population: {:.1f}".format(dailyAvg))
        elif (req == 'pct'):
            stateAB = input("Enter the state: ").strip('\r')
            print(stateAB)
            stateAB = stateAB.upper()
            dPCT = dailyPCT(stateAB, lists)
            if not(dPCT == -1):
                print("Average daily positive percent: {:.1f}".format(dPCT))
        elif (req == 'quar'):
            print("Quarantine states:")
            quar(lists)
        elif (req == 'high'):
            highC(lists)
        else:
            print("Unrecognized request")
            