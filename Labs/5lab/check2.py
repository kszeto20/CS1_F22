'''
Lab 5 'Yelp Data'
Check 2
'''

import lab05_util

restaurants = lab05_util.read_yelp('yelp.txt')

def print_info(rest):
    
    # name and type
    print("{} ({})".format(rest[0], rest[5]))
    
    # address
    address = rest[3].split('+')
    for i in range(len(address)):
        print("\t{}".format(address[i]))
    
    # average score
    scores = rest[6]
    total = 0 
    for score in scores:
        total += score    
        
    if (len(scores) > 3):
        total -= max(scores)
        total -= min(scores)
        length = len(scores) - 2
    else:
        length = len(scores)
    
    avg = total / length
    if (avg < 2):
        print("This restaurant is rated bad, based on {} reviews".format(length))
    elif (avg >= 2 and avg < 3):
        print("This restaurant is rated average, based on {} reviews".format(length))
    elif (avg >= 3 and avg < 4):
        print("This restaurant is rated above average, based on {} reviews".format(length))
    elif (avg >= 4 and avg < 5):
        print("This restaurant is rated very good, based on {} reviews".format(length))
    print()
    
    
i = input("Which restaurant id? => ").strip('\r')
print(i)
i = int(i)

if (i > len(restaurants) or i <= 0):
    print("There aren't that many restaurants in Troy")
else:
    print_info(restaurants[i - 1])
    