def nextBP(bpop, fpop):
    nextBP = (10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop
    return int(nextBP)

def nextFP(bpop, fpop):
    nextFP = 0.4 * fpop + 0.02 * fpop * bpop
    return int(nextFP)

    
bpop = input("Number of Bunnies ==> ").strip('\r')
print(bpop)
bpop = int(bpop)

fpop = input("Number of Foxes ==> ").strip('\r')
print(fpop)
fpop = int(fpop)

i = 1
BPStore = bpop
FPStore = fpop
while (i < 6):
    print("Year {}: {} {}".format(i, str(BPStore), str(FPStore)))
    bS = nextBP(BPStore, FPStore)
    fS = nextFP(BPStore, FPStore)
    
    BPStore = bS
    FPStore = fS
    i += 1