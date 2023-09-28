'''
Part 2: Pikachu in the Wild!
'''
# move function
def move_pokemon(t, dire, num):
    yc = t[0]
    xc = t[1]
    if (direction == 'N'):
        yc -= num
    elif (direction == 'S'):
        yc += num
    elif (direction == 'W'):
        xc -= num
    elif (direction == 'E'):
        xc += num
    
    # bound checking
    if (xc < 0):
        xc = 0
    elif (yc < 0):
        yc = 0
    elif (xc > 150):
        xc = 150
    elif (yc > 150):
        yc = 150
    return (yc, xc)

# get user input
turns = input('How many turns? => ')
print(turns)
turns = int(turns)

name = input('What is the name of your pikachu? => ').strip('\r')
print(name)

often = input('How often do we see a Pokemon (turns)? => ')
print(often)
often = int(often)

# initializing original state
yc = 75
xc = 75
done = 1 # turn number
wR = [] # win record

# starting simulation
print('\nStarting simulation, turn 0 {} at (75, 75)'.format(name))

# run simulation
while (turns > 0):
    # ask user for direction
    direction = input('What direction does {} walk? => '.format(name))
    print(direction)
    direction = direction.strip('\r').upper()
    
    # update xy with correct movement
    xy = (yc, xc)
    xy = move_pokemon(xy, direction, 5)
    yc = xy[0]
    xc = xy[1]
    
    # check for running into pokemon
    if (done % often == 0):
        print("Turn {}, {} at ({}, {})".format(done, name, yc, xc))
        
        # ask user for pokemon encountered
        encountered = input("What type of pokemon do you meet (W)ater, (G)round? => ")
        print(encountered)
        encountered = encountered.strip('\r').upper()
        
        # water pokemon
        if (encountered == "W"):
            xy = (yc, xc)
            xy = move_pokemon(xy, direction, 1)
            yc = xy[0]
            xc = xy[1]
            print("{} wins and moves to ({}, {})".format(name, yc, xc))
            wR.append('Win') # update win record
        
        # ground pokemon
        elif (encountered == "G"):
            inty = -10
            xy = (yc, xc)
            xy = move_pokemon(xy, direction, inty)
            yc = xy[0]
            xc = xy[1]
            print("{} runs away to ({}, {})".format(name, yc, xc))
            wR.append('Lose') # update win record
        else:
            wR.append('No Pokemon') # update win record      
    turns -= 1
    done += 1
print("{} ends up at ({}, {}), Record: {}".format(name, yc, xc, wR))

