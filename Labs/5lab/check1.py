'''
Lab 5 'Yelp Data'
Check 1
'''

import lab05_util

restaurants = lab05_util.read_yelp('yelp.txt')
print(restaurants[0])
print()

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
    avg = total / len(scores)
    print("Average score: {:.2f}".format(avg))
    print()
    
print_info(restaurants[0])
print_info(restaurants[4])
print_info(restaurants[42])