def skewer(name, t1, t2, t3, t4, t5):
    toRet = ''
    avg = (t1+t2+t3+t4+t5)/5
    var = (t1-avg)**2 + (t2-avg)**2 + (t3-avg)**2 + (t4-avg)**2 + (t5-avg)**2
    var /= 5
    skew = (t1-avg)**3 + (t2-avg)**3 + (t3-avg)**3 + (t4-avg)**3 + (t5-avg)**3
    skew /= 5
    skew = skew/var**3**0.5
    toRet = "{}'s running times have a skew of {:.2f}".format(name, skew)
    return toRet

def minMaxAvg(name, t1, t2, t3, t4, t5):
    sumT = t1 + t2 + t3 + t4 + t5
    
    maxNum = max(t1, t2, t3, t4 , t5)
    sumT -= maxNum
    
    minNum = min(t1, t2, t3, t4, t5)
    sumT -= minNum
    
    avg = round(sumT / 3, 1)
    
    print("{}'s stats-- min: {}, max: {}, avg: {:.1f}".format(name, minNum, maxNum, avg))
    
    

print(skewer("Stan", 34, 34, 35, 31, 29))
print(skewer("Kyle", 30, 31, 29, 29, 28))
print(skewer("Cartman", 36, 31, 32, 33, 33))
print(skewer("Kenny", 33, 32, 34, 31, 35))
print(skewer("Bebe", 27, 29, 29, 28, 30))

print()

minMaxAvg("Stan", 34, 34, 35, 31, 29)
minMaxAvg("Kyle", 30, 31, 29, 29, 28)
minMaxAvg("Cartman", 36, 31, 32, 33, 33)
minMaxAvg("Kenny", 33, 32, 34, 31, 35)
minMaxAvg("Bebe", 27, 29, 29, 28, 30)