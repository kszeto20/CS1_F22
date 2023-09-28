import math as m

# circle one
rOne = 5
aOne = (rOne ** 2) * m.pi
aOne = round(aOne, 2)
print("Area 1 =", aOne)


# circle two
rTwo = 32
aTwo = pow(rTwo, 2) * m.pi
aTwo = round(aTwo, 2)
toRet = "Area 2 = {a}".format(a = aTwo)
print(toRet)