# Part III: How Do You Feel about Homework?

# program fuctions

def number_happy(sentence):
    sentence = sentence.lower()
    goodCount = 0
    goodCount += sentence.count('laugh')
    goodCount += sentence.count('happiness')
    goodCount += sentence.count('love')
    goodCount += sentence.count('excellent')
    goodCount += sentence.count('good')
    goodCount += sentence.count('smile')
    return goodCount

def number_sad(sentence):
    sentence = sentence.lower()
    badCount = 0
    badCount += sentence.count('bad')
    badCount += sentence.count('sad')
    badCount += sentence.count('terrible')
    badCount += sentence.count('horrible')
    badCount += sentence.count('problem')
    badCount += sentence.count('hate')
    return badCount
    
    
# Get input from user
inStr = input('Enter a sentence => ').strip('\r')
print(inStr)

# calculate happy
h = number_happy(inStr)

# calculate sad
s = number_sad(inStr)

print('Sentiment: ' + ('+' * h) + ('-' * s))

if (h > s):
    print('This is a happy sentence.')
elif (s > h):
    print('This is a sad sentence.')
else:
    print('This is a neutral sentence.')