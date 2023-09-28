'''
Part III: Framed Box
Write a program that asks the user for a frame character, and then the height 
and width of a framed box. Then output a box of the given size, framed by the
given character. Also, output the dimentions of the box centered  horizontally
and vertically inside the box.

If centering is not possible, one line more under, one line more to the right
'''

# get info from the user
fChar = input("Enter frame character ==> ").strip('\r')
print(fChar)


height = input("Height of box ==> ").strip('\r')
print(height)
h = int(height)

width = input("Width of box ==> ").strip('\r')
print(width)
w = int(width)

# create top and bottom border

top = (fChar * w) + '\n'
bottom = fChar * w

# create non dimension line

regLine = fChar + (' ' * (w - 2)) + fChar + '\n'

# create dimension line

dimStr = width + 'x' + height
dStrLen = len(dimStr)

left = ((w - 2 - dStrLen) // 2)
right = (w - 2 - dStrLen - left)

tDimStr = fChar +  (' ' * left) + dimStr + (' ' * right) + fChar + '\n'

# calculate rows

vertTop = (h - 3) // 2
vertBottom = (h - 3 - vertTop) 

# assemble
totalStr = top + (vertTop * regLine) + tDimStr + (vertBottom * regLine) + bottom

print("\nBox:")
print(totalStr) 