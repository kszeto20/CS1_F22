def get_words(desc):
    desc = desc.replace('.', ' ')
    desc = desc.replace(',', ' ')
    desc = desc.replace('(', ' ')
    desc = desc.replace(')', ' ')
    desc = desc.replace('"', ' ')
    desc = desc.lower()
    
    words = desc.split(' ')
    
    vWords = set()
    for word in words:
        if len(word) >= 4:
            if word.isalpha():
                vWords.add(word)
                
    return vWords

# check wrpi and csa
fileW = 'wrpi.txt'
fileC = 'csa.txt'

fileW = open(fileW, 'r')
fileC = open(fileC, 'r')


# for wrpi
wName = 'holder'
wDes = 'holder'

for line in fileW:
    parts = line.split('|')
    wName  = parts[0]
    wDes = parts[1]
fileW.close()

# for csa
cName = 'holder'
cDes = 'holder'

for line in fileC:
    parts = line.split('|')
    cName  = parts[0]
    cDes = parts[1]
fileC.close()

# filter words for wrpi and csa
dW = get_words(wDes)
dC = get_words(cDes)

print("Comparing wrpi and csa:")

uW = set() # unique to wrpi
uC = set() # unique to csa
for dubs in dW:
    uW.add(dubs)
        
for cees in dC:
    uC.add(cees)
        
print("Same words: {}".format(uW.intersection(uC)))
print("Unique to wrpi: {}".format(uW.difference(uC)))
print("Unique to csa: {}".format(uC.difference(uW)))

        
