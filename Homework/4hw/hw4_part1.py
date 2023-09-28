'''
Homework 4
Part I: Password Strength
'''
# imports
import hw4_util

#################################################
# checker functions

## length
def lenC(s):
    leng = len(s)
    
    # number to add to score
    toRet = 0
    
    # case checking
    if (leng == 6 or leng == 7):
        toRet = 1
    elif(leng >= 8 and leng <= 10):
        toRet = 2
    elif(leng > 10):
        toRet = 3
    
    # if toRet == 0; do not print; return 0
    if not(toRet):
        return 0
    # else print modification and return mod number
    else:
        print("Length: +{}".format(str(toRet)))
        return toRet

## case
def caseC(s):
    upper = 0
    lower = 0
    
    # loop through each character
    for i in range(len(s)):
        # character being looked at
        ch = s[i]
        # check for alphabetical -- number doesn't matter
        if(ch.isalpha()):
            # if upper
            if (ch.isupper()):
                upper += 1
            # if lower
            else:
                lower += 1
    
    # if 2+ upper and lower
    if (upper >= 2 and lower >= 2):
        print("Cases: +2")
        return 2
    # if 1+ upper and lower
    elif(upper >= 1 and lower >= 1):
        print("Cases: +1")
        return 1
    # if not, return 0
    else:
        return 0
    
## digits
def digitsC(s):
    numCount = 0
    
    # loop through each character
    for i in range(len(s)):
        ch = s[i]
        numCount += ch.isnumeric()
    # if 2+
    if (numCount >= 2):
        print("Digits: +2")
        return 2
    # if 1+
    elif(numCount == 1):
        print("Digits: +1")
        return 1
    # else return 0
    else:
        return 0

## punctuation
def puncC(s):
    #a = ['!', '@', '#', '$']
    #b = ['%', '^', '&', '*']
    # number of each category
    aC = 0
    bC = 0
    # number to add
    toRet = 0
    
    # check for a type
    aC += s.count('!')
    aC += s.count('@')
    aC += s.count('#')
    aC += s.count('$')
    
    # check for b type
    bC += s.count('%')
    bC += s.count('^')
    bC += s.count('&')
    bC += s.count('*')
    
    # if either is triggered; print corresponding message
    if (aC > 0):
        toRet += 1
        print("!@#$: +1")
    if (bC > 0):
        toRet += 1
        print("%^&*: +1")
    
    # return number to add
    return toRet

## NY License
def licenseC(s):
    # loop through each character up to 7 left
    for i in range(len(s) - 6):
        # check if first three are alphabet
        if (s[i].isalpha() and s[i+1].isalpha() and s[i+2].isalpha()):
            # check if next 4 are numbers
            if (s[i+3].isnumeric() and s[i+4].isnumeric() and s[i+5].isnumeric() and s[i+6].isnumeric()):
                print("License: -2")
                return -2
    return 0

## Common Password
def commonC(s):
    # if listed in the list
    listed = 0
    # grab from list
    a = hw4_util.part1_get_top()
    listed = a.count(s.lower())
    
    if (listed == 0):
        return 0
    else:
        print("Common: -3")
        return -3
    
###################################################################

#get user input

passW = input("Enter a password => ")
print(passW)

## check user input

combo = 0 
combo += lenC(passW)
combo += caseC(passW)
combo += digitsC(passW)
combo += puncC(passW)
combo += licenseC(passW)
combo += commonC(passW)

print("Combined score: {}".format(combo))

if (combo <= 0):
    print("Password is rejected")
elif (combo == 0 or combo == 2):
    print("Password is poor")
elif (combo == 3 or combo == 4):
    print("Password is fair")
elif (combo == 5 or combo == 6):
    print("Password is good")
else:
    print("Password is excellent")