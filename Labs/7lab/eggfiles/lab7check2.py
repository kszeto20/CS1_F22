'''
Lab 07
Check II
'''
def parse_line(line):
    sLine = line.split('/')
    if(len(sLine) < 4):
        return None
    nums = [sLine[-3], sLine[-2], sLine[-1]]
    
    output = []
    
    for num in nums:
        if not (num.isdigit()):
            return None
        else:
            output.append(int(num))
            
    outs = ''
    num_str = len(sLine) - 3
    for s in range(num_str):
        if(s != num_str - 1):
            outs += sLine[s]
            outs += '/'
        else:
            outs += sLine[s]
    
    return (int(sLine[-3]), int(sLine[-2]), int(sLine[-1]), outs)
    
def get_line(fname,parno,lineno):
    file = open('{}.txt'.format(fname))
    pNum = 1
    lNum = 0
    inP = True
    
    for line in file:
        if (line.isspace() and inP == True):
            inP = False
            pNum += 1
            lNum = 0
        else:
            inP = True
            lNum += 1
            if pNum == parno and lNum == lineno:
                return line.rstrip()
        
fileName = input("Please enter the file number ==> ")
print(fileName)

paragraphNum = input("Please enter the paragraph number ==> ")
print(paragraphNum)
paragraphNum = int(paragraphNum)

lineNum = input("Please enter the line number ==> ")
print(lineNum)
lineNum = int(lineNum)

print(get_line(fileName, paragraphNum, lineNum))
