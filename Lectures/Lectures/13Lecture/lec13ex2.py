fRead = input("Enter the scores file: ").strip('\r')
print(fRead)

numList = []
for line in (open(fRead)):
    number = int(line)
    numList.append(number)
    
numList.sort()

fWrite = input("Enter the output file: ").strip('\r')
print(fWrite)

out = open(fWrite, 'w')

for i in range(len(numList)):
    out.write("{:2d}: {:3d}\n".format(i, numList[i]))