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


fileN = input("File name please: ")
fileN = fileN + '.txt'

file = open(fileN, 'r')

cName = 'holder'
cDes = 'holder'
for line in file:
    parts = line.split('|')
    cName  = parts[0]
    cDes = parts[1]
file.close()

print(get_words(cDes))

