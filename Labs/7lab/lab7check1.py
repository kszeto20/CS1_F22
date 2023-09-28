'''
Lab 07
Check I
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
    

print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line(" Here is some spaces 12/32/4"))

print(parse_line(" Again some spaces\n/12/12/12"))



