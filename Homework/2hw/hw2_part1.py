import math as m

# Part I: A Penny for a Gum Ball Mickey

# Step I: write find volume functions
def find_volume_sphere(radius):
    return (4/3) * m.pi * (radius ** 3)

def find_volume_cube(side):
    return side ** 3

# Step II: Get radius of the gum balls and the weekly sales from user

gRadius = input("Enter the gum ball radius (in.) => ").strip('\r')
print(gRadius)
rad = float(gRadius)

wSales = input("Enter the weekly sales => ").strip('\r')
print(wSales)

print('')

# Step IIIA: Calculate the total number of gumballs desired (1.25 * sales)
sales = m.ceil(int(wSales) * 1.25)
bPerRow = m.ceil(sales ** (1/3))

# Step IIIB: Calculate the length of the side of the machine
sideLen = (rad * 2) * bPerRow

# Step IVA: Calculate the max # of balls to fit
maxB = bPerRow ** 3

# Step IVB: Calculate vol of cube
cVol = find_volume_cube(sideLen)

# Step IVC: Calculate vol of gumball
gBVol = find_volume_sphere(rad)

# Step IVC: Wasted Space of
# i. num of needed balls in
needWasted = cVol - (sales * gBVol)
# ii. num of total possible balls in
totalWasted = cVol - (maxB * gBVol)

# Step V: Print these values out using .2f format if needed
print('The machine needs to hold {0} gum balls along each edge.'.format(bPerRow))
print('Total edge length is {0:.2f} inches.'.format(sideLen))
print('Target sales were {0}, but the machine will hold {1} extra gum balls.'.format(sales, maxB - sales))
print('Wasted space is {0:.2f} cubic inches with the target number of gum balls, \nor {1:.2f} cubic inches if you fill up the machine.'.format(needWasted, totalWasted))