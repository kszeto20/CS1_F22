'''
Part I: MadLibs
Write a Python program to construct the Mad Lib
'''

'''
Good morning <proper name>!
This will be a/an <adjective> <noun>! Are you <verb> forward to it?
You will <verb> a lot of <noun> and feel <emotion> when you do.
If you do not, you will <verb> this <noun>.
This <season> was <adjective>. Were you <emotion> when <team-name> won
the <noun>?
Have a/an <adjective> day!

'''

# grab the  user inputs

print("Let's play Mad Libs for Homework 1")
print("Type one word responses to the following:\n")

pName = input('proper_name ==> ').strip('\r')
print(pName)


adj = input('adjective ==> ').strip('\r')
print(adj)


noun = input('noun ==> ').strip('\r')
print(noun)


verb = input('verb ==> ').strip('\r')
print(verb)


verb2 = input('verb ==> ').strip('\r')
print(verb2)


noun2 = input('noun ==> ').strip('\r')
print(noun2)


emotion = input('emotion ==> ').strip('\r')
print(emotion)


verb3 = input('verb ==> ').strip('\r')
print(verb3)


noun3 = input('noun ==> ').strip('\r')
print(noun3)


season = input('season ==> ').strip('\r')
print(season)


adj2 = input('adjective ==> ').strip('\r')
print(adj2)


emotion2 = input('emotion ==> ').strip('\r')
print(emotion2)


teamN = input('team-name ==> ').strip('\r')
print(teamN)


noun4 = input('noun ==> ').strip('\r')
print(noun4)


adj3 = input('adjective ==> ').strip('\r')
print(adj3)


#populate the madlib story
print("\nHere is your Mad Lib...\n")


print("Good morning {0}!\n".format(pName))
print("  This will be a/an {0} {1}! Are you {2} forward to it?".format(adj, noun, verb))
print("  You will {0} a lot of {1} and feel {2} when you do.".format(verb2, noun2, emotion))
print("  If you do not, you will {0} this {1}.\n".format(verb3, noun3))
print("  This {0} was {1}. Were you {2} when {3} won\n  the {4}?\n".format(season, adj2, emotion2, teamN, noun4))
print("Have a/an {0} day!".format(adj3))
