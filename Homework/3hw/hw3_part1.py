'''
Homework 03 
Part I: Text Complexity
'''
from syllables import find_num_syllables

# get input from user
inP = input("Enter a paragraph => ")
print(inP)

# Functions to calculate

# average sentence length
def asl_count(string):
    sentC = string.count('.')
    m = string.split()
    
    # return ratio
    return (len(m) / sentC)

# percent hard words
#PHW word list
hardW = []

def phw_count(string):
    totalC = 0              # total word count
    hardWC = 0              # hard word count 
    words = string.split()

    # check each word
    for word in words:
        totalC += 1
        # does it have hyphen
        if (word.count('-') == 0):
            # does it not end in 'es' or 'ed'
            if (word[-3:-1] != 'es' and word[-3:-1] != 'ed'):
                if (find_num_syllables(word) >= 3):
                    hardWC += 1
                    hardW.append(word)
    # return ratio
    return hardWC / totalC * 100

# average number of syllables
def asyl_count(string):
    wordC = 0
    sylCount = 0
    words = string.split()
    for word in words:
        # add total syllables of word
        sylCount += find_num_syllables(word)   
        # add to total word count
        wordC += 1                              
    
    # return ratio
    return (sylCount / wordC)

def gfri_count(asl, phw):
    return 0.4 * (asl + phw)

def fkri_count(asl, asyl):
    return 206.835-1.015*asl-86.4*asyl

# use functions
asl = asl_count(inP)
phw = phw_count(inP)
asyl = asyl_count(inP)
gfri = gfri_count(asl, phw)
fkri = fkri_count(asl, asyl)

# print statements
print('Here are the hard words in this paragraph: \n{}'.format(hardW))
print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(round(asl, 2), round(phw,2), round(asyl, 2)))
print('Readability index (GFRI): {:.2f}'.format(round(gfri, 2)))
print('Readability index (FKRI): {:.2f}'.format(round(fkri, 2)))