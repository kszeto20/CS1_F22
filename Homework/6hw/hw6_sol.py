'''
Homework VI - Files, Sets and Document Analysis
Part I
'''

''''
This opens the file 
    - reds lines
    - removes non alphas
    - closes file
'''
def open_files(fileName):
    file = open(fileName, encoding="utf-8")
    wholeFile = file.read()
    listFile = wholeFile.split()

    added = []
    for word in listFile:
        newWord = ''
        for i in range(len(word)):
            if (word[i].isalpha()):
                newWord += word[i]
        if not newWord == '':
            added.append(newWord.lower())
    file.close()
    return added

'''
Changes list into word
'''
def change_set(wordL):
    nSet = set()
    for word in wordL:
        nSet.add(word)
    return nSet

'''
Given list of words and a set of stop words
    - for each word: if not in stop:
        append to acceptable words list
'''
def check_stop(wordList, stopSet):
    notIn = []
    for word in wordList:
        
        if word in stopSet:
            continue
        else:
            notIn.append(word)
    return notIn

''' 
#1 function for average length
Calculate and output the average word length, accurate to two decimal places. The idea here
is that word length is a rough indicator of sophistication.
'''
def checkLen(wList):
    totalLens = 0
    for word in wList:
        totalLens += len(word)
        
    return round(totalLens / len(wList), 2)

'''
#2 function for distinct word ration
. Calculate and output, accurate to three decimal places, the ratio between the number of
distinct words and the total number of words. This is a measure of the variety of language
used (although it must be remembered that some authors use words and phrases repeatedly
to strengthen their message.)
'''
def checkDistinct(wList):
    sets = set(wList)
    return round((len(sets) / len(wList)), 3)
       
'''
HELPER FUNCTION FOR checkLens()
returns a list of words of a certain length 
'''    
def desLengths(length, wList):
    corrLengths = []
    
    wSet = set()
    
    for word in wList:
        wSet.add(word)
        
    for word in wSet:
        if len(word) == length:
            corrLengths.append(word)
    corrLengths.sort()
    
    return corrLengths

'''
HELPER FUNCTION FOR checkLens()
prints correct layout for when more than six words of that length
'''
def sixPrint(wList):
    print('{} {} {} ... {} {} {}'.format(wList[0], wList[1], wList[2], wList[-3], wList[-2], wList[-1]))
        

'''
#3 function for counting amount of words with length (x)
For each word length starting at 1, find the set of words having that length. Print the length,
the number of different words having that length, and at most six of these words. If for a
certain length, there are six or fewer words, then print all six, but if there are more than six
print the first three and the last three in alphabetical order. For example, suppose our simple
text example above were expanded to the list
'''
def checkLens(wList):
    maxLength = -1
    for word in wList:
        if len(word) > maxLength:
            maxLength = len(word)
            
    lengths = []
    for i in range(maxLength):
        lengths.append(0)

    words = set()
    for word in wList:
        words.add(word)
        
    for word in words:
        lengths[len(word) - 1] += 1
        
    for i in range(len(lengths)):
        first = ''
        lengs = desLengths(i+1, wList)
        
        beg = ' ' * (4 - len(str(i + 1)))
        sec = ' ' * (4 - len(str(lengths[i])))
        
        print('{}{}:{}{}:'.format(beg, i + 1, sec, lengths[i]), end = '')
        if (lengths[i] == 0):
            print()
        else:
            print(' ', end = '')
        
        if (len(lengs) <= 6):
            for i in range(len(lengs)):
                if i + 1 == len(lengs):
                    print(lengs[i])
                else:
                    print(lengs[i], end = ' ')
        else:
            sixPrint(lengs)
            
    return maxLength     
   
'''
#4 function to find pairs
for each word:
    get all possible pairs
    sort each pair
    add pairs to set (prevents duplicates)
    
Find the distinct word pairs for this document. A word pair is a two-tuple of words that
appear max_sep or fewer positions apart in the document list. For example, if the user input
resulted in max_sep == 2, then the first six word pairs generated will be:
('puppy', 'weather'), ('challenge', 'weather'),
('challenge', 'puppy'), ('house', 'puppy'),
('challenge', 'house'), ('challenge', 'whistle')
Your program should output the total number of distinct word pairs. (Note that ('puppy', 'weather')
and ('weather', 'puppy') should be considered the same word pair.) It should also output
the first 5 word pairs in alphabetical order (as opposed to the order they are formed, which
is what is written above) and the last 5 word pairs. You may assume, without checking, that
there are enough words to generate these pairs. 
'''
def pairs(wList, sep):
    pairCount = 0
    wSet = set()
    
    for i in range(len(wList)):
        for j in range(i + 1, i + sep  + 1):
            if j > len(wList) - 1:
                break
            tup = (wList[i], wList[j])
            pairCount += 1
            sTup = tuple(sorted(tup))
            wSet.add(sTup)
            
    
    lSet = []
    for s in wSet:
        lSet.append(s)
    
    lSet.sort()
    print('  {} distinct pairs'.format(len(lSet)))
    for i in range(5):
        x,y = lSet[i]
        print('  {} {}'.format(x, y))
    
    if len(lSet) > 5:
        print('  ...')
        i = -5
        while i != 0:
            x,y = lSet[i]
            print('  {} {}'.format(x, y))
            i += 1
            
    return (pairCount, len(wSet), lSet)

'''
#2 function to check word pair distinction

Calculate the Jaccard similarity in the overall word use in the two documents. This should
be accurate to three decimal places.
'''
def sim_check(oneList, twoList):
    oneSet = set()
    twoSet = set()
    
    for word in oneList:
        oneSet.add(word)
        
    for word in twoList:
        twoSet.add(word)
        
    return (round(len(oneSet.intersection(twoSet)) / (len(oneSet.union(twoSet))), 3))

'''
#3 function for similiarities per word length

Calculate the Jaccard similarity of word use for each word length. Each output should also
be accurate to three decimal places.

'''
def eachLength_sim(oneList, twoList, num):
    oneLW = desLengths(num, oneList)
    twoLW = desLengths(num, twoList)
        
    oneSet = set()
    for word in oneLW:
        oneSet.add(word)
    
    twoSet = set()
    for word in twoLW:
       twoSet.add(word)
       
    if (len(oneSet) == 0 or len(twoSet) == 0):
        return 0
       
    if len(oneSet.union(twoSet)) == 0:
        return 0
    else:
        return(len(oneSet.intersection(twoSet)) / len(oneSet.union(twoSet)))

'''
#4 pair similarities

Calculate the Jaccard similarity between the word pair sets. The output should be accurate
to four decimal places. The documents we study here will not have substantial similarity of
pairs, but in other cases this is a useful comparison measure.

'''
def pair_sim(onePair, twoPair):
    oneSet = set()
    twoSet = set()
    
    for word in onePair:
        oneSet.add(word)
    
    for word in twoPair:
       twoSet.add(word)
       
    if (len(oneSet) == 0 or len(twoSet) == 0):
         return 0
     
    return (len(oneSet.intersection(twoSet)) / len(oneSet.union(twoSet)))


# main portion of the code
if __name__ == '__main__':
    mStop = open_files('stop.txt')
    mStop = change_set(mStop)
    
    
    oneO = input("Enter the first file to analyze and compare ==> ").strip()
    print(oneO)
    
    twoO = input("Enter the second file to analyze and compare ==> ").strip()
    print(twoO)
    
    max_sep = input("Enter the maximum separation between words in a pair ==> ").strip()
    print(max_sep)
    max_sep = int(max_sep)
    
    
    print()
    
    getOne = open_files(oneO)
    wordsOne = check_stop(getOne, mStop)
    
    
    getTwo = open_files(twoO)
    wordsTwo = check_stop(getTwo, mStop)
    
    '''
    oneO = 'cat_in_the_hat.txt'
    twoO = 'pulse_morning.txt'
    '''
    docMax = 0
    
    print("Evaluating document {}".format(oneO))
    
    getOne = open_files(oneO)
    wordsOne = check_stop(getOne, mStop)
    
    oneLen = checkLen(wordsOne)
    print('1. Average word length: {:.2f}'.format(oneLen))
    
    oneD = checkDistinct(wordsOne)
    print('2. Ratio of distinct words to total words: {:.3f}'.format(oneD))
    
    print('3. Word sets for document {}:'.format(oneO))
    lengthOne = checkLens(wordsOne)
    
    docMax = lengthOne
    
    print('4. Word pairs for document {}'.format(oneO))
    x,y,z = pairs(wordsOne,max_sep)
    
    print('5. Ratio of distinct word pairs to total: {:.3f}'.format(y/x))
    
    print()
    
    print("Evaluating document {}".format(twoO))
    
    getTwo = open_files(twoO)
    wordsTwo = check_stop(getTwo, mStop)
    
    twoLen = checkLen(wordsTwo)
    print('1. Average word length: {}'.format(twoLen))
    
    twoD = checkDistinct(wordsTwo)
    print('2. Ratio of distinct words to total words: {}'.format(twoD))
    
    print('3. Word sets for document {}:'.format(twoO))
    lengthTwo = checkLens(wordsTwo)
    
    if docMax < lengthTwo:
        docMax = lengthTwo
    
    print('4. Word pairs for document {}'.format(twoO))
    a,b,c = pairs(wordsTwo,max_sep)
    
    print('5. Ratio of distinct word pairs to total: {:.3f}'.format(b/a))
    
    
    print('\nSummary comparison')
    
    if oneLen > twoLen:
        m = oneO
        n = twoO
    else:
        m = twoO
        n = oneO
    print('1. {} on average uses longer words than {}'.format(m,n))
    
    val = sim_check(wordsOne, wordsTwo)
    print('2. Overall word use similarity: {:.3f}'.format(val))
    
    print('3. Word use similarity by length:')
    
    for i in range(docMax):
        ratio = eachLength_sim(wordsOne, wordsTwo, i + 1)
        first = ' ' * (4 - len(str(i + 1)))
        
        print('{}{}: {:.4f}'.format(first, i + 1, ratio))
        
    over = pair_sim(z, c)
    print('4. Word pair similarity: {:.4f}'.format(over))