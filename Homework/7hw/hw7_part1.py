'''
Homework 7
Part 1
'''

# function declarations

'''
function dropCheck (w (word), d (dictionary)):
    --> will return all possible replacements from dropping
    
    for length of the word:
        create a substring of the first i characters (non inclusive)
        
        # drop portion
        append the rest of the characters of the string starting with character at index i + 1
        
        check if resulting substring combo is in dictionary:
            if in dictionary --> add to set of valid replacements
    
    return valid set of words
'''

def dropCheck(w, d):
    word = w.lower()
    valid = set() # holds replacements
    
    for i in range(len(word)):
        checkS = word[:i]
        if (i + 1 < len(word)):
            checkS += word[i+1:]
        if (checkS in d):
            valid.add(checkS)
            
    return valid
 
'''
function insertCheck (w (word), d (dictionary)):
    --> will return all possible replacements from inserting
    
    for length of the word + 1 (can insert one index before and after word):
        create a substring of the first i characters (non inclusive)
        
        for j in range(26): -->  0 - 25 for letters in alphabet
        
            # inserting portion
            append character 'a' + j # character a + j gives next alpha char to add to string --> (chr(ord('a' + j)))
            
            append rest of existing characters of string starting at index i to substring
            
        
        check if resulting substring combo is in dictionary:
            if in dictionary --> add to set of valid replacements
    
    return valid set of words
'''

def insertCheck(w, d):
    word = w.lower()
    valid = set() # holds replacements
    
    for i in range(0, len(word) + 1):
        stringAdd = word[:i]
        
        for j in range(26):
            perLetter = stringAdd
            perLetter += chr(ord('a') + j)
            perLetter += word[i:]
            if (perLetter in d):
                valid.add(perLetter)
    return valid

'''
function swapCheck (w (word), d (dictionary)):
    --> will return all possible replacements from swapping
    
    for length of the word - 1: (only switching up to second to last with last)
        create a substring of the first i characters (non inclusive)
        
        # swap portion 
        append the i + 1 character to the string
        append the i character to the string
        
        append rest of the string from index i + 2
        
        check if resulting substring combo is in dictionary:
            if in dictionary --> add to set of valid replacements
    
    return valid set of words
'''

        
def swapCheck(w, d):
    word = w.lower()
    valid = set() # to hold replacements
    
    for i in range(len(word) - 1):
        swapS = word[:i]
        swapS += word[i+1]
        swapS += word[i]
        if (i + 2 < len(word)):
            swapS += word[i+2:]
        
        if swapS in d:
            valid.add(swapS)
            
    return valid

'''
function replaceCheck (w (word), d (dictionary), fre (frequencies)):
    --> will return all possible words from replacing letters
    
    for length of the word:
        for each letter in the list of values corresponding to the key (word[i]) in frequency dictionary:
            create substring of first i characters (non-inclusive)
            
            # replace portion
            append letter from list of values
            
            append rest of the original word from index i + 1
            
            check if resulting substring combo is in dictionary:
                if in dictionary --> add to set of valid replacements
    
    return valid set of words
'''
            
def replaceCheck(w, d, fre):
    word = w.lower()
    valid = set() # to hold replacements
    
    for i in range(len(word)):
        for letter in fre[word[i]]:
            repString = word[:i]
            repString += letter
            if (i + 1 < len(word)):
                repString += word[i+1:]
                
            if repString in d:
                valid.add(repString)
    return valid

'''
function comboCheck(w (word), d (dictionary), fre (frequency))
    --> calls all four checks on a word
    --> returns combination of all valid 'replacements' from all four checks
'''

def comboCheck(w, d, fre):
    possCh = set() # set to add changes to
    
    # drop checking
    dropped = dropCheck(w, d)
    for word in dropped:
        possCh.add(word)
        
    # insert checking
    inserted = insertCheck(w, d)
    for word in inserted:
        possCh.add(word)
        
    # swap checking
    swapped = swapCheck(w, d)
    for word in swapped:
        possCh.add(word)
        
    # replace checking 
    repped = replaceCheck(w, d, fre)
    for word in repped:
        possCh.add(word)
        
    return possCh
        
'''
function wordCheck (w (word), d (dictionary), letterS (frequency)):
    --> will return (FOUND / NOT FOUND / possible replacements, # of replacements found))
    
    get lowercase version of the word
    if word is in the dictionary:
        return 'FOUND', 0
    
    run comboCheck to get all replacements
    
    if len(comboCheck) == 0: # means no replacements
        return 'NOT FOUND', 0  
    
    elif len(comboCheck < 3): # less than three replacements
        create a list of tuples with (frequency of replacement, replacement)
        sort list in reverse order to get most frequent first
        
        return list, len(list)
    
    else: # >= three replacements
        create a list of tuples with (frequency of replacement, replacement)
        sort list in reverse order to get most frequent first
        
        return first three values in the list, len(total number of possibilities found)
    
'''
def wordCheck(w, dictionary, letterS): # word to check, dictionary of words, letters for replacement
    word = w.lower()
    if word in dictionary:
        return 'FOUND', 0
    
    # all checks
    allCombos = comboCheck(w, dictionary, letterS)
    
    if len(allCombos) == 0:
        return 'NOT FOUND', 0
    elif (len(allCombos) < 3):
        possible = []
        for w in allCombos:
            tupleB = (dictionary[w], w)
            possible.append(tupleB)
            possible.sort(reverse=True)
        return possible, len(possible)
    else:
        possL = []
        for w in allCombos:
            tupleA = (dictionary[w], w)
            possL.append(tupleA)
        
        possL.sort(reverse=True)
        return (possL[:3], len(possL))

'''
function wPrint(word, freqD (dictionary), keyD (potential letter sub dictionary):
    --> returns nothing (print function)
    
    call wordCheck  --> store ('FOUND' / 'NOTFOUND' / most frequend possible replacements) and # of total possible replacements
    
    if # of possible replacements == 0
    print(corresponding found / not found message)
    
    else:
        calculate proper white spaces in output
        if # of replacements != double digits:
            print way one
        else:
            print way two
            
'''

def wPrint(inWord, freqD, keyD):
    vals, totalL = wordCheck(inWord, freqD, keyD)
    first = ' ' * (15 - len(inWord))
    arrow = '->'
    f = 'FOUND'
    
    if (vals == 'FOUND' or vals == 'NOT FOUND'):
        print('{}{} {} {}'.format(first, inWord, arrow, vals))
    else:
        length = len(vals)
        num = len(str(totalL))
        beg = ' ' * (2 - num)
        
        words = ''
        
        if length == 1:
            words = vals[0][1]
        elif length == 2:
            words += vals[0][1]
            words += ' '
            words += vals[1][1]
        else:
            for i in range(length):
                tup = vals[i]
                
                if (i < (length - 1)):
                    words += tup[1]
                    words += ' '
                else:
                    words += vals[i][1]
        
        if (beg == ''):
            print('{}{} {} {} {}:  {}'.format(first, inWord, arrow, f, totalL, words))
        else:                    
            print('{}{} {} {} {}{}:  {}'.format(first, inWord, arrow, f, beg, totalL, words))



if __name__ == '__main__':
    # get user input

    # word and frequency file
    freqF = input ('Dictionary file => ').strip()
    print(freqF)

    # to auto correct file
    inF = input('Input file => ').strip()
    print(inF)

    # potential letter substitution file
    keyF = input('Keyboard file => ').strip()
    print(keyF)
    
    # create dicionary with frequencies
    freqF = open(freqF, 'r')
    freqL = freqF.readlines() # returns list of lines in the file

    freqD = dict() # python dictionary to add word and frequencies to 
    for line in freqL:
        wordKey = line.strip().split(',')
        freqD[wordKey[0]] = wordKey[1]
        
    # create dictionary with potential letter switches
    keyF = open(keyF, 'r')
    keyL = keyF.readlines() # returns list of lines in the file

    keyD = dict() # python dictionary to add letters and possible substitutions to
    for line in keyL:
        letterSubs = line.strip().split()
        key = letterSubs[0]
        letterSubs.pop(0)
        keyD[key] = letterSubs
        
    # parse input and feed into computing functions
    inF = open(inF, 'r')
    inL = inF.read().strip().split() # get each word

    for word in inL:
        if (word == ' '):
            inL.remove(' ') # if don't remove spaces, errors are thrown

    # computation        
    for word in inL:
        wPrint(word, freqD, keyD) # wprint calls computational functions + handles printing
    