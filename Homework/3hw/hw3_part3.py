'''
Part 3: Population Changes
'''
import math

#function to calculate tourists
def computing_tourists(bears):
    if(bears <= 15 and bears >= 4):
        if(bears > 10):
            return ((bears - 10) * 20000) + (10 * 10000)
        else:
            return bears * 10000
    return 0

# find next bears and berries
def find_next(bears, berries, tourists):
    bears_next = berries / (50 * (bears + 1)) + (bears * 0.60) - (math.log(1 + tourists, 10) * 0.1)
    berries_next = (berries * 1.5) - (bears + 1) * (berries / 14) - (math.log(1 + tourists, 10) * 0.05)
    return(max(int(bears_next), 0), max(berries_next, 0))

# print function dynamically
def print_and_store(year, bears, berries, tourists):
    
    berries = round(berries, 1)
    
    # spaces between next column
    year_spacing = ' ' * (10 - len(str(year)))
    bears_spacing = ' ' * (10 - len(str(bears)))
    berries_spacing = ' ' * (10 - len(str(berries)))
    tourists_spacing = ' ' * (10 - len(str(tourists)))
    
    print(year, year_spacing, bears, bears_spacing, berries, berries_spacing, tourists, tourists_spacing, sep = '')
    
    # compile all data points for min max later
    bear_list.append(bears)
    berry_list.append(berries)
    tourist_list.append(tourists)
    return 0

# get input from user 
bears = input("Number of bears => ")
print(bears)
bears = int(bears)

berries = input("Size of berry area => ")
print(berries)
berries = float(berries)

years = 10
current_year = 1
tourists = computing_tourists(bears)

berry_list = []
bear_list = []
tourist_list = []

while(years > 0):
    if(current_year == 1):
        print("Year      Bears     Berry     Tourists")
    print_and_store(current_year, bears, float(berries), tourists)
    bears, berries = find_next(bears, berries, tourists)
    tourists = computing_tourists(bears)
    current_year += 1
    years -= 1

print()
print("Min:      {}         {}".format(min(bear_list), min(berry_list)) + (' ' * 5) + str(min(tourist_list)))
print("Max:      {}         {}".format(max(bear_list), max(berry_list)) + (' ' * 5) + str(max(tourist_list)))
    





















