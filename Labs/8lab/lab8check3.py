def get_words(desc):
    desc = desc.replace('.', ' ')
    desc = desc.replace(',', ' ')
    desc = desc.replace('(', ' ')
    desc = desc.replace(')', ' ')
    desc = desc.replace('"', ' ')
    desc = desc.lower()
    
    words = desc.split()
    
    vWords = set()
    for word in words:
        if len(word) >= 4:
            if word.isalpha():
                vWords.add(word)
                
    return vWords

# check wrpi and csa
fileW = input("File name please: ")
fileW = fileW + '.txt'

fileC = 'allclubs.txt'

fileW = open(fileW, 'r')
fileA = open(fileC, 'r')

# for all
aNames = []
aDes = []

lines = fileA.readlines()

for line in lines:
    parts = line.split('|')
    aNames.append(parts[0])
    aDes.append(parts[1])
    
fileA.close()

# for little
wName = 'holder'
wDes = 'holder'

for line in fileW:
    parts = line.split('|')
    wName  = parts[0]
    wDes = parts[1]
fileW.close()

# filter words for wrpi and all
dW = get_words(wDes)

nameCount = 0
mostC = []
for des in aDes:
    tCheck = get_words(des)
    mostC.append((len(tCheck.intersection(dW)), aNames[nameCount]))
    nameCount += 1
    
mostC.sort(reverse=True)
mostC.pop(0)

for i in range(5):
    print(mostC[i][1])
