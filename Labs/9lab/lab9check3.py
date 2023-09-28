from Date import Date
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

birthF = open('birthdays.txt', 'r')

bDays = birthF.readlines()

bList = []

for line in bDays:
    bDay = line.strip().split()
    date = Date(bDay[0], bDay[1], bDay[2])
    bList.append(date)
    
earliest = bList[0]
for day in bList:
    if day < earliest:
        earliest = day

latest = bList[0]
for day in bList:
    if not (day < latest):
        latest = day

months = [0] * 13
for day in bList:
    months[int(day.month)] += 1
    

print('Earliest Birthday', str(earliest))
print('Latest Birthday', str(latest))
month = months.index(max(months))

print("The most popular month is: {}".format(month_names[month]))