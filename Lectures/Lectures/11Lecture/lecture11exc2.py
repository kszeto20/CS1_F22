dH = input("Enter Dale's height: ").strip('\r')
print(dH)
dH = int(dH)

eH = input("Enter Erin's height: ").strip('\r')
print(eH)
eH = int(eH)

sH = input("Enter Sam's height: ").strip('\r')
print(sH)
sH = int(sH)

if (max(dH, eH, sH) == dH):
    print('Dale')
    if (eH > sH):
        print('Erin')
        print('Sam')
    else:
        print('Sam')
        print('Erin')
elif(max(dH, eH, sH) == eH):
    print('Erin')
    if (dH > sH):
        print('Dale')
        print('Sam')
    else:
        print('Sam')
        print('Dale')
else:
    print('Sam')
    if (dH > eH):
        print('Dale')
        print('Erin')
    else:
        print('Erin')
        print('Dale')
        
        